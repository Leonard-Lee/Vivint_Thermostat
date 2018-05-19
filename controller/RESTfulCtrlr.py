import web

class RESTfulCtrlr(object):
    methods = ("get", "create", "update", "delete", "getAll", "updateAll", "deleteAll")

    def __getattr__(self, name):
        if name in self.methods and "headers" in web.ctx:
            raise web.badrequest()
        else:
            raise web.notfound()

    # read one or all objects
    def GET(self, resource_id=None):
        if resource_id is None:
            return self.getAll()
        else:
            return self.get(resource_id)

    # create one object
    def POST(self, resource_id=None):
        if resource_id is None:
            return self.create()
        else:
            raise web.badrequest()

    # update one or all objects
    def PUT(self, resource_id=None):
        if resource_id is None:
            return self.updateAll()
        else:
            return self.update(resource_id)

    # delete one or all objects
    def DELETE(self, resource_id=None):
        if resource_id is None:
            return self.deleteAll()
        else:
            return self.delete(resource_id)
