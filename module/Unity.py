import random

class Unity(object):
    def __init__(self):
        # users could search the thermostat by name
        self.dict_name_thermostat = {}
        # users could search the thermostat by id
        self.dict_id_thermostat = {}

        self.last_id = 0

    # provide UUID for thermostat ID
    def getLastID(self):
        id = self.last_id
        self.last_id += 1
        return id

    # provide temperature degree(gF)
    def getTemperature(self):
        return random.randint(30, 120)
