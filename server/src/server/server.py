import cherrypy
import time
import json
from server.soap_client import CurrencyClient
from server.currencies import currencies
from server.db import Session
from server.models import Currency


class CurrencyService(object):
    def index(self, currency):
        return json.dumps({'rate': CurrencyClient().get_rate(currency)})
    index.exposed = True

    def from_local(self, currency):
        session = Session()
        return json.dumps({'rate': session.query(Currency).filter_by(code=currency).first().rate})
    from_local.exposed = True

cherrypy.quickstart(CurrencyService())

