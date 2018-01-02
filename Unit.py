
class Unit:
    __slots__ = 'entity', 'properties'
    def __init__(self, entity, properties):
        self.entity = entity + ''
        self.load( properties or {} )

    def load(self, properties):
        p = Unit(None, None)
        for property in properties:
            p[property] = properties[property]
        self.properties = p
        return self

    def set(self, property, value):
        self.properties[property] = value
        return self.properties

    def unset(self, property):
        return self.properties.pop(property)

    def has(self, property):
        if property in self.properties:
            return self.properties[property]

    def get(self, property):
        return self.properties[property]


