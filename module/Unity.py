import random
import web

class Unity(object):
    # provide UUID for thermostat ID

    @classmethod
    def getLastID(cls):
        session = web.config.session
        id = session['count']
        session['count'] += 1
        return id

    # provide temperature degree(F)
    @classmethod
    def getTemperature(cls):
        return random.randint(30, 120)