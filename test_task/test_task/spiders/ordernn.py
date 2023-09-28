import scrapy


class OrdernnSpider(scrapy.Spider):
    name = "ordernn"
    allowed_domains = ["order-nn.ru"]
    start_urls = ["https://order-nn.ru/"]

    def parse(self, response):
        pass
