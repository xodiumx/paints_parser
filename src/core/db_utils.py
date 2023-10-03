from sqlalchemy import insert, select
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

    print(f'{len(data)} объектов создано в таблице {table}')


def get_db_objects(
        table: Table,
        db_session: Session) -> list[tuple]:
    """Функция получения всех объектов в таблице."""
    query = select(table)
    return db_session.execute(query).all()