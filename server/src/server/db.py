from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

from models import Currency

engine = create_engine('mysql://root@localhost/tcc_farn')

metadata = MetaData()
currencies_table = Table('currencies', metadata,
    Column('id', Integer, primary_key=True),
    Column('code', String(5)),
    Column('rate', Float)
)
metadata.create_all(engine)

mapper(Currency, currencies_table)

Session = sessionmaker(bind=engine)
