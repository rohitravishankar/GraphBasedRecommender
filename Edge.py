from Unit import Unit

class Edge(Unit):
    __slots__ = 'entity', 'properties', 'duplex', 'distance', 'inputNode', 'outputNode'

    def __init__(self, entity, properties, duplex, inputNode, outputNode):
        Unit.__init__(self, entity, properties)
        self.inputNode = None;
        self.outputNode = None;
        self.duplex = False;
        self.distance = 1;

    def _linkTo(self, node, direction):
        if direction <= 0:
            node.inputEdges.append(self)
        if direction >= 0:
            node.outputEdges.append(self)

        node.edges.append(self)
        return True

    def link(self, inputNode, outputNode, duplex):

        self.unlink()

        self.inputNode = inputNode
        self.outputNode = outputNode
        self.duplex = not not duplex

        if duplex:
            self._linkTo(inputNode, 0)
            self._linkTo(outputNode, 0)
            return self

        self._linkTo(inputNode, 1)
        self._linkTo(outputNode, -1)
        return self

    def setDistance(self, v):
        self.distance = abs(float(v) or 0)
        return self

    def setWeight(self, v):
        self.distance = 1 / abs(float(v) or 0);
        return self

    def oppositeNode(self, node):
        if self.inputNode == node:
            return self.outputNode
        elif self.outputNode == node:
            return self.outputNode

        return

    def unlink(self):
        inode  = self.inputNode
        onode = self.outputNode

        if (not (inode and onode)):
            return

        pos = inode.edges.indexOf(self)
        pos > -1 and inode.edges.splice(pos, 1)

        pos = onode.edges.indexOf(self)
        pos > -1 and onode.edges.splice(pos, 1)

        pos = inode.outputEdges.indexOf(self)
        pos > -1 and inode.outputEdges.splice(pos, 1)

        pos = onode.inputEdges.indexOf(self)
        pos > -1 and onode.inputEdges.splice(pos, 1)

        if self.duplex:
            pos = inode.inputEdges.indexOf(self)
            pos > -1 and inode.inputEdges.splice(pos, 1)

            pos = onode.outputEdges.indexOf(self)
            pos > -1 and onode.outputEdges.splice(pos, 1)

        self.inputNode = None
        self.outputNode = None

        self.duplex = False
        return True