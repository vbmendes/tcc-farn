import cherrypy
import json
from server.soap_client import CurrencyClient
from server.db import Session
from server.models import Currency


class CurrencyService(object):
    def index(self, currency):
        rate = CurrencyClient().get_rate(currency)
        return json.dumps({'rate': rate})
    index.exposed = True

    def from_local(self, currency):
        session = Session()
        rate = session.query(Currency).filter_by(code=currency).first().rate
        return json.dumps({'rate': rate})
    from_local.exposed = True

cherrypy.quickstart(CurrencyService())
