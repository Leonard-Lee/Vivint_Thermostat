class Thermostat(object):
    def __init__(self, name):
        # private variables
        self._id = Unity.getID()
        self._tmp = Unity.getTemp()

        # public variables
        self.name = name
        # "cool", "heat", "off"
        self.operation_mode = "off"
        # 30 - 100 degrees fahrenheit
        self.cool_set_point = 70
        self.hot_set_point = 70
        # "off", "auto"
        self.fan_mode = "off"

    def setCoolPoint(self, point):
        if point > 100:
            self.cool_set_point = 100;
        elif point < 70:
            self.cool_set_point = 70

    def setHotPoint(self, point):
        if point > 100:
            self.hot_set_point = 100;
        elif point < 70:
            self.hot_set_point = 70

    def json(self):
        return {
            'id': self._id,
            'temp': self._tmp,
            'name': self.name,
            'operation_mode': self.operation_mode,
            'cool_set_point': self.cool_set_point,
            'hot_set_point': self.hot_set_point,
            'fan_mode': self.fan_mode
        }