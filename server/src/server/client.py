from multiprocessing import Pool
from sys import argv
import urllib
import datetime

from server.currencies import currencies


def index(currency):
    response = urllib.urlopen('http://localhost:8080/index/%s/' % currency)
    print response.read()


def from_local(currency):
    response = urllib.urlopen('http://localhost:8080/from_local/%s/' % currency)
    print response.read()

if __name__ == '__main__':
    inicio = datetime.datetime.now()
    method = globals()[argv[1]]
    p = Pool(int(argv[2]))
    if len(argv) >= 4:
        currencies = currencies[:int(argv[3])]
    p.map(method, currencies)
    print datetime.datetime.now() - inicio
