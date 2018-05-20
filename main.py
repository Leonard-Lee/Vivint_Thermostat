import json
import web
from RESTfulCtrlr import RESTfulCtrlr
from Thermostat import Thermostat
from Unity import Unity

urls = (
    r'/thermostat(?:/(?P<resource_id>[0-9]+))?',
    # r'/thermostat/(?P<resource_id>[0-9]+))?',
    'ThermoCtrlr',
)

class ThermoCtrlr(RESTfulCtrlr):
#   "update", "deleteAll"
    def __init__(self):
        super(ThermoCtrlr, self).__init__()

    def get(self, id):
        if not id in web.dict_id_thermostat:
            raise web.notfound
        return json.dumps(web.dict_id_thermostat(id).json())

    def getAll(self):
        if not web.dict_id_thermostat:
            raise web.notfound
        list = []
        for key, val in web.dict_id_thermostat:
            list.append(val.json())
        return json.dumps(list)

    # create whole thermostat
    def create(self):
        data = json.loads(web.data())
        thermostat = Thermostat(data['name'], web)
        web.dict_id_thermostat[thermostat.id] = thermostat
        return json.dumps(thermostat.json())

    def delete(self, id):
        thermostat = web.dict_id_thermostat.get(id, None)
        if thermostat is None:
            raise web.notfound
        else:
            web.dict_id_thermostat.pop(id)
            raise web.nocontent

    def deleteAll(self):
        if len(web.dict_id_thermostat) == 0:
            raise web.notfound
        else:
            web.dict_id_thermostat.clear()
            raise web.nocontent

    def update(self):
        data = json.loads(web.data())
        if not 'id' in data:
            raise web.notfound

        id = data.get('id')
        thermostat = web.dict_id_thermostat.get(id)
        for key in data.keys():
            if hasattr(thermostat, key):
                setattr(thermostat, key, data.get(key))
            else:
                raise web.notfound

        web.dict_id_thermostat[id] = thermostat

    def updateAll(self):
        data = json.loads(web.data())
        for id, thermostat in web.dict_id_thermostat:
            for data_key in data.keys():
                if hasattr(thermostat, data_key):
                    setattr(thermostat, data_key, data.get(data_key))
                else:
                    raise web.notfound
            web.dict_id_thermostat[id] = thermostat

    # GET / tickets / 12 / messages - Retrieves list of messages for ticket  # 12
    # PUT / tickets / 12 / messages / 5 - Updates message  # 5 for ticket #12

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.dict_id_thermostat = {}
    web.last_id = 0
    app.run()