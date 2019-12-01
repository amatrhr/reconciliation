from tank import Tank
from flow import Flow
import numpy as np

class ProcessGraph:
    """Class for process graphs, generates tanks and flows"""
    def __init__(self, adjacency_matrix=np.array([[0,0]]), env_outflow=1):
        self.adjacency_matrix = adjacency_matrix
        self.n_tanks = adjacency_matrix.shape[0]
        self.n_flows = adjacency_matrix.shape[1]
        self.environment = Tank(height=np.Inf)
        self.environment.outflow = env_outflow
        # set up all tanks as default
        self.tanks = {}
        for i in range(self.n_tanks):
            self.tanks.update({i:Tank()})
        self.flows = {}
        # Todo: edit this to force a balanced system
        for _, row in enumerate(adjacency_matrix):
            if any(row == 1) & any(row == -1):
                self.flows.update({_:Flow(from_node=self.tanks[int(np.argmax(row == 1))], to_node=self.tanks[int(np.argmax(row == -1))])})
            elif any(row == -1) & (not any(row == 1)): # a leak
                self.flows.update({_: Flow(from_node=self.environment,
                                           to_node=self.tanks[int(np.argmax(row == -1))])})
            elif any(row == 1) & (not any(row == -1)): # also a leak
                self.flows.update({_: Flow(from_node=self.tanks[int(np.argmax(row == 1))], to_node=self.environment)})
            elif all(row == 0):
                self.flows.update({_: Flow(from_node=self.environment,
                                           to_node=self.tanks[int(np.argmax(row == -1))])})
                _ += 1
                self.flows.update({_: Flow(from_node=self.tanks[int(np.argmax(row == 1))], to_node=self.environment)})

        # set up all arcs
    def run_system(self, n_iterations=10):
        return(0)
    def measure_system(self):
        return 0
