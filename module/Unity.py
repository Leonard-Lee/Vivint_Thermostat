import random
import web

class Unity(object):
    # provide UUID for thermostat ID

    @classmethod
    def getLastID(cls):
        id = web.last_id
        web.last_id += 1
        return id

    # provide temperature degree(F)
    @classmethod
    def getTemperature(cls):
        return random.randint(30, 120)