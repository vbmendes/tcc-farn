from multiprocessing import Pool
from sys import argv
import urllib
import datetime
from server.soap_client import CurrencyClient
from server.currencies import currencies
from server.models import Currency
from server.db import Session

session = Session()

def mymethod(currency):
    c = Currency(code=currency, rate=CurrencyClient().get_rate(currency))
    session.add(c)
    print '%s OK!' % currency

if __name__ == '__main__':
    inicio = datetime.datetime.now()
    p = Pool(int(argv[1]))
    if len(argv) >= 3:
        currencies = currencies[:int(argv[2])]
    p.map(mymethod, currencies)
    print datetime.datetime.now() - inicio
