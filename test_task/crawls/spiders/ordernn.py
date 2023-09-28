from crawls.settings import ORDERNN_CONST, USER_AGENT

from scrapy import Spider
from scrapy import Request
from scrapy.http.response.html import HtmlResponse


class OrdernnSpider(Spider):
    name = 'ordernn'
    allowed_domains = ['order-nn.ru']
    start_urls = ['https://order-nn.ru/kmo/catalog/']

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
        return
    
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
                url=f'{response.url}{url}',
                callback=self.parse_categories,
                headers={'Connection': 'keep-alive'}
            )
        

    def parse_items(self, response: HtmlResponse) -> None:
        """Парсинг всех категорий на стартовой странице."""
        categories_urls = self.__get_pagination(response)

        # for url in categories_urls:
        #     yield Request(
        #         url=f'{response.url}{url}',
        #         callback=self.parse_categories,
        #         headers={'Connection': 'keep-alive'}
        #     )
        