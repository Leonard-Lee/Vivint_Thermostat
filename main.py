import json
import web
from RESTfulCtrlr import RESTfulCtrlr
from Thermostat import Thermostat

urls = (
    r'/thermostat(?:/(?P<resource_id>[0-9]+))?',
    'ThermoCtrlr',
)

class ThermoCtrlr(RESTfulCtrlr):
#   "update", "deleteAll"
    def __init__(self):
        super(ThermoCtrlr, self).__init__()

    def get(self, id):
        id = int(id)
        if not id in web.dict_id_thermostat.keys():
            raise web.notfound
        return json.dumps(web.dict_id_thermostat.get(id).json())

    def getAll(self):
        if not web.dict_id_thermostat:
            raise web.notfound
        return self.jsonfyDict()

    # create whole thermostat
    def create(self):
        data = json.loads(web.data())
        thermostat = Thermostat(data['name'])
        web.dict_id_thermostat[thermostat.id] = thermostat
        return json.dumps(thermostat.json())

    def delete(self, id):
        id = int(id)
        thermostat = web.dict_id_thermostat.get(id)
        if thermostat is None:
            raise web.notfound
        else:
            web.dict_id_thermostat.pop(id)
            raise web.nocontent

    def deleteAll(self):
        if web.dict_id_thermostat:
            web.dict_id_thermostat.clear()
            raise web.nocontent
        else:
            raise Exception(web.notfound)

    def update(self, id):
        data = json.loads(web.data())
        id = int(id)
        thermostat = web.dict_id_thermostat.get(id)
        for key in data.keys():
            if hasattr(thermostat, key):
                setattr(thermostat, key, data.get(key))
            else:
                raise web.notfound

        web.dict_id_thermostat[id] = thermostat
        return json.dumps(thermostat.json())

    def updateAll(self):
        data = json.loads(web.data())
        for id, thermostat in web.dict_id_thermostat.items():
            for data_key in data.keys():
                if hasattr(thermostat, data_key):
                    setattr(thermostat, data_key, data.get(data_key))
                else:
                    raise web.notfound
            web.dict_id_thermostat[id] = thermostat
        return self.jsonfyDict()

    # for return all items in dict in memory
    def jsonfyDict(self):
        list = []
        for key, val in web.dict_id_thermostat.items():
            list.append(val.json())
        return json.dumps(list)

    # GET / tickets / 12 / messages - Retrieves list of messages for ticket  # 12
    # PUT / tickets / 12 / messages / 5 - Updates message  # 5 for ticket #12

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.dict_id_thermostat = {}
    web.last_id = 1
    app.run()