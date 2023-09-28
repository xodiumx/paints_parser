from sqlalchemy import insert
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.schema import Table


def create_db_objects(
        table: Table,
        data: dict,
        db_session: Session) -> None:
    """функция создания объектов в базе данных."""
    statement = insert(table).values(data)

    db_session.execute(statement)
    db_session.commit()

    print(f'{len(data)} объектов созданы в таблице {table}')
