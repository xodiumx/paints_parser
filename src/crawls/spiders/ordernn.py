from math import ceil

import requests
from bs4 import BeautifulSoup
from scrapy import Request, Spider
from scrapy.http.response.html import HtmlResponse

from core.utils import get_price
from crawls.settings import ORDERNN_CONST, USER_AGENT
from db.connect import get_session


class OrdernnSpider(Spider):
    name = 'ordernn'
    allowed_domains = ['order-nn.ru']
    main_url = 'https://order-nn.ru'
    start_urls = ['https://order-nn.ru/kmo/catalog/']

    db_session = next(get_session())

    def __get_categories_urls(self, response: HtmlResponse) -> list[str]:
        """
        Метод получения урлов, категорий.
        url: https://order-nn.ru/kmo/catalog/
        """
        return set(response.xpath(ORDERNN_CONST['xpath_categories']).getall())
    
    def __get_pagination(self, response: HtmlResponse) -> int:
        """
        Метод получения пагинации, категорий.
        url: https://order-nn.ru/kmo/catalog/
        """
        pagination = ceil(int(response.xpath(
            ORDERNN_CONST['xpath_pagination']
        ).getall()[0].split('\xa0')[0]) / ORDERNN_CONST['count_items'])
        return pagination

    def __get_items_urls(self, response: HtmlResponse) -> list[str]:
        """
        Получение спика урлов товаров
        url: https://order-nn.ru/kmo/catalog/
        """
        return response.xpath(ORDERNN_CONST['xpath_item_urls']).getall()
    
    def start_requests(self) -> None:
        """Начало запросов."""
        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.parse,
                headers={'User-Agent': USER_AGENT})
    
    def parse(self, response: HtmlResponse) -> None:
        """Парсинг всех категорий на стартовой странице."""
        categories_urls = self.__get_categories_urls(response)

        for url in categories_urls:
            yield Request(
                url=f'{self.main_url}{url}',
                callback=self.parse_categories,
                headers={'Connection': 'keep-alive'}
            )

    def parse_categories(self, response: HtmlResponse) -> None:
        """Парсинг всех категорий на стартовой странице."""
        pagination = self.__get_pagination(response)

        for page in range(1, pagination + 1):
            yield Request(
                url=f'{response.url}/?PAGEN_1={page}',
                callback=self.parse_pages,
                headers={'Connection': 'keep-alive'}
            )

    def parse_pages(self, response: HtmlResponse) -> None:
        """Парсинг страниц товаров."""
        item_urls = self.__get_items_urls(response)

        for url in item_urls:
            yield Request(
                url=f'{self.main_url}{url}',
                callback=self.parse_items,
                headers={'Connection': 'keep-alive'}
            )

    def parse_items(self, response: HtmlResponse) -> None:
        """
        Парсинг страницы товарв:
        attributes:
            - item_id: id товара
            - name: наименование товара
            - description: описание товара
            - price: цена
            - characteristics_json: словарь с характеристиками товара
        """
        item_id = response.url.split('/')[-1]

        name = response.xpath(ORDERNN_CONST['xpath_name']).get()

        price = get_price(
            response.xpath(ORDERNN_CONST['xpath_price']).get())

        description = response.xpath(
            ORDERNN_CONST['xpath_description']).getall()
        description = '\n'.join(text.strip() for text in description)

        characteristics = requests.post(
            f'{ORDERNN_CONST["endpoint_characterstics"]}{item_id}')
        soup = BeautifulSoup(characteristics.text, 'html.parser')
        characteristics = soup.find_all('tr')
        characteristics_json = dict()

        for element in characteristics:

            key, value = element.find_all('td')
            key, value = key.text, value.text

            characteristics_json[key] = value

        product = {
            'name': name,
            'price': price,
            'description': description,
            'url': response.url,
            'characteristics': characteristics_json,
        }

        yield product
