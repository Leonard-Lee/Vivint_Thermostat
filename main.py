import json
import web
from RESTfulCtrlr import RESTfulCtrlr
from Thermostat import Thermostat

class ThermoCtrlr(RESTfulCtrlr):
#   "update", "deleteAll"
    def __init__(self):
        super(ThermoCtrlr, self).__init__()
        session = web.config.session
        self.dict_id_thermostat = session['dict_id_thermostat']


    def get(self, id):
        id = int(id)
        if not id in self.dict_id_thermostat.keys():
            raise web.notfound()
        return json.dumps(self.dict_id_thermostat.get(id).json())

    def getAll(self):
        if not self.dict_id_thermostat:
            raise web.notfound()
        return self.jsonfyDict()

    # create whole thermostat
    def create(self):
        data = json.loads(web.data())
        thermostat = Thermostat(data['name'])
        self.dict_id_thermostat[thermostat.id] = thermostat
        return json.dumps(thermostat.json())

    def delete(self, id):
        id = int(id)
        thermostat = self.dict_id_thermostat.get(id)
        if thermostat is None:
            raise web.notfound()
        else:
            self.dict_id_thermostat.pop(id)
            raise web.nocontent

    def deleteAll(self):
        if self.dict_id_thermostat:
            self.dict_id_thermostat.clear()
            raise web.nocontent
        else:
            raise web.notfound()

    def update(self, id):
        data = json.loads(web.data())
        id = int(id)
        thermostat = self.dict_id_thermostat.get(id)
        # not found the thermostat
        if not thermostat:
            raise web.notfound()

        for key in data.keys():
            if hasattr(thermostat, key):
                setattr(thermostat, key, data.get(key))
            else:
                raise web.notfound()

        self.dict_id_thermostat[id] = thermostat
        return json.dumps(thermostat.json())

    def updateAll(self):
        if not self.dict_id_thermostat:
            raise web.notfound()

        data = json.loads(web.data())
        for id, thermostat in self.dict_id_thermostat.items():
            for data_key in data.keys():
                if hasattr(thermostat, data_key):
                    setattr(thermostat, data_key, data.get(data_key))
                else:
                    raise web.notfound
            self.dict_id_thermostat[id] = thermostat
        return self.jsonfyDict()

    # for return all items in dict in memory
    def jsonfyDict(self):
        list = []
        for key, val in self.dict_id_thermostat.items():
            list.append(val.json())
        return json.dumps(list)

    # GET / tickets / 12 / messages - Retrieves list of messages for ticket  # 12
    # PUT / tickets / 12 / messages / 5 - Updates message  # 5 for ticket #12

if __name__ == '__main__':
    # define router, application and session
    urls = (
        r'/thermostat(?:/(?P<resource_id>[0-9]+))?',
        'ThermoCtrlr',
    )
    app = web.application(urls, globals())
    # customize notfound error message
    def notfound():
        err = 'Sorry, the item you were searching or updating was not found.'
        return web.notfound(json.dumps({'result': err}))

    app.notfound = notfound

    if not web.config.get('session'):
        init = {'count': 1, 'dict_id_thermostat': {}}
        ### Store the data in the directory './sessions'
        store = web.session.DiskStore('./sessions')
        session = web.session.Session(app, store, initializer=init)

        ### Store it somewhere we can access
        web.config.session = session
    else:
        ### If it is already created, just use the old one
        session = web.config.session

    app.run()