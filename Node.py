from Unit import Unit

class Node(Unit):
    __slots__ = 'entity', 'properties', 'edges', 'inputEdges', 'outputEdges'

    def __init__(self, entity, properties, edges = [], inputEdges = [], outputEdges = []):
        Unit.__init__(self, entity, properties)

    def unlink(self):
        edges = self.edges

        for i in range(len(edges)):
            edges[i].unlink()

        return True

