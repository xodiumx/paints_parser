# =================== Sync connection =================== #

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from crawls.settings import DATABASE

DB_USER = DATABASE['DB_USER']
DB_PASS = DATABASE['DB_PASS']
DB_HOST = DATABASE['DB_HOST']
DB_PORT = DATABASE['DB_PORT']
DB_NAME = DATABASE['DB_NAME']

metadata = MetaData()


DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(engine, expire_on_commit=True)


def get_session():
    """Getting a new session to connect to the database."""
    with Session() as session:
        yield session