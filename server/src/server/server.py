import cherrypy
import time
import json
from server.soap_client import CurrencyClient


class HelloWorld(object):
    def index(self, currency):
        return json.dumps({'rate': CurrencyClient().get_rate(currency)})
    index.exposed = True

cherrypy.quickstart(HelloWorld())

