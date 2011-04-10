from multiprocessing import Pool
from sys import argv
import urllib
import datetime

def mymethod(seconds):
    response = urllib.urlopen('http://localhost:8080/index/%s/' % seconds)
    print response.read()

if __name__ == '__main__':
    inicio = datetime.datetime.now()
    p = Pool(int(argv[1]))
    p.map(mymethod,['BRL','AUD','EUR', 'MXN', 'CAD'])
    print datetime.datetime.now() - inicio

