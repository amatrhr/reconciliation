from numpy import sqrt, array, append
from tank import Tank

class Flow:
    def __init__(self, from_node: Tank, to_node: Tank):
        assert isinstance(from_node, Tank)
        assert isinstance(to_node, Tank)
        self.from_node = from_node
        self.to_node = to_node
        self.to_node.inflow = self.to_node.inflow + self.from_node.outflow
        self.flow = from_node.outflow

    def update_flow(self):
        self.to_node.inflow = self.to_node.inflow + self.from_node.outflow
        self.flow = from_node.outflow
