from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

from models import Currency

engine = create_engine('sqlite:///tcc-farn.db', echo=True)

metadata = MetaData()
currencies_table = Table('currencies', metadata,
    Column('id', Integer, primary_key=True),
    Column('code', String),
    Column('rate', Float)
)
metadata.create_all(engine)

mapper(Currency, currencies_table)

Session = sessionmaker(bind=engine)

