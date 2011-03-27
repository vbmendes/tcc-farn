import cherrypy
import time

class HelloWorld(object):
    def index(self, seconds):
        time.sleep(int(seconds))
        return "%s seconds slept.\n" % seconds
    index.exposed = True

cherrypy.quickstart(HelloWorld())
