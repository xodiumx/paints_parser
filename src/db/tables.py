from datetime import datetime

from sqlalchemy import (JSON, Column, Date, Integer, Numeric,
                        String, Table, )

from db.connect import metadata

ordernn_products = Table(
    'ordernn_products',
    metadata,
    Column('id', Integer, primary_key=True, index=True, autoincrement=True),
    Column('name', String(512), nullable=True, ),
    Column(
        'price',
        Numeric(asdecimal=True, decimal_return_scale=1),
        nullable=True
    ),
    Column(
        'description',
        String(512),
        nullable=True
    ),
    Column('characteristics', JSON, nullable=True, ),
    Column('url', String(512), nullable=True, ),
    Column(
        'created_at',
        Date,
        default=datetime.now,
    ),
)