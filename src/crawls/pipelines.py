from core.db_utils import create_db_objects
from crawls.spiders.ordernn import OrdernnSpider
from db.connect import get_session
from db.tables import ordernn_products

AMOUNT_TO_CREATE = 100


class OrdernnPipeline:

    def __init__(self) -> None:
        self.db_session = next(get_session())

    def open_spider(self, spider: OrdernnSpider) -> None:
        """Создаем список для сохранения товаров."""
        self.data = []

    def process_item(self, item: dict, spider: OrdernnSpider) -> dict:
        """
        - Добавляем полученные объекты товаров в список
        - Если в списке AMOUNT_TO_CREATE объктов, создаем объекты в db и
          обнуляем список объектов.
        """
        self.data.append(item)

        if len(self.data) == AMOUNT_TO_CREATE:
            create_db_objects(ordernn_products, self.data, self.db_session)
            self.data = []
        return item

    def close_spider(self, spider: OrdernnSpider) -> None:
        """Добавляем оставшиеся объекты в db."""
        if self.data:
            create_db_objects(ordernn_products, self.data, self.db_session)
