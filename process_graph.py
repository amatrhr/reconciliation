from tank import Tank

class ProcessGraph:
    """Class for process graphs, generates tanks and flows"""
    def __init__(self, adjacency_matrix=array([])):
        self.n_tanks = adjacency_matrix.shape[0]
        self.n_flows = adjacency_matrix.shape[1]
        # set up all tanks as default
        self.tanks = {}
        self.arcs = {}


        # set up all arcs
    def measure_system(self, time):
        return 0
