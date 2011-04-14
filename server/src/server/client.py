from multiprocessing import Pool
from sys import argv
import urllib
import datetime

from server.currencies import currencies

def mymethod(currency):
    response = urllib.urlopen('http://localhost:8080/index/%s/' % currency)
    print response.read()

if __name__ == '__main__':
    inicio = datetime.datetime.now()
    p = Pool(int(argv[1]))
    if len(argv) >= 3:
        currencies = currencies[:int(argv[2])]
    p.map(mymethod, currencies)
    print datetime.datetime.now() - inicio

