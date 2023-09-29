from datetime import datetime

from pandas.core.frame import DataFrame
from sqlalchemy.sql.schema import Table

from core.db_utils import get_db_objects
from db.connect import get_session
from db.tables import ordernn_products


def get_csv_data(table: Table) -> None:
    """Функция создания отчета в формате csv."""

    db_session = next(get_session())
    data = get_db_objects(table, db_session)

    csv_file_name = f'src/analytics/examples/{table}_{datetime.now()}.csv'
    df = DataFrame(data)
    df.to_csv(csv_file_name, index=False, sep=';')


get_csv_data(ordernn_products)
