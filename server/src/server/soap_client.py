from suds.client import Client


class SOAPClient(object):

    @classmethod
    def get_client(cls):
        if not hasattr(cls, '_client'):
            cls._client = Client(cls.wsdl)
        return cls._client
    
    @property
    def client(self):
        return self.__class__.get_client()


class CurrencyClient(SOAPClient):
    
    wsdl = 'http://www.restfulwebservices.net/wcf/CurrencyService.svc?wsdl'    
    
    def get_rate(self, from_currency, to_currency=None):
        to_currency = to_currency or 'USD'
        response = self.client.service.GetConversionRate(
            from_currency,
            to_currency)
        return response.Rate

