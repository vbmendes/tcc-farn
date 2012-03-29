from multiprocessing import Pool
from sys import argv
import datetime
from server.soap_client import CurrencyClient
from server.currencies import currencies
from server.models import Currency
from server.db import Session

session = Session()


def update_currency(currency):
    c = Currency(code=currency, rate=CurrencyClient().get_rate(currency))
    session.add(c)
    print session.query(Currency).filter_by(code=currency).first().rate
    print '%s OK!' % currency

if __name__ == '__main__':
    inicio = datetime.datetime.now()
    p = Pool(int(argv[1]))
    if len(argv) >= 3:
        currencies = currencies[:int(argv[2])]
    p.map(update_currency, currencies)
    print datetime.datetime.now() - inicio
