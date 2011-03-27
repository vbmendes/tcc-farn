from multiprocessing import Pool
from sys import argv
import urllib

def mymethod(seconds):
    response = urllib.urlopen('http://localhost:8080/index/%s/' % seconds)
    print response.read()

if __name__ == '__main__':
    p = Pool(int(argv[1]))
    p.map(mymethod,[3,3,3])

