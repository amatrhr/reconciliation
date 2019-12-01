from numpy import sqrt, array, append
class Tank:
    def __init__(self, height=0., inflow=0., valve_coef=1., outlet_area=1.):
        self.height = height
        self.inflow = inflow
        self.valve_coef = valve_coef
        self.outlet_area = outlet_area
        self.time = 0
        self.history = array([self.time, self.height])
        self.outflow = self.valve_coef * sqrt(9.81 * self.height)

    def update_level(self):
        self.outflow = self.valve_coef*sqrt(9.81*self.height)
        self.height = height  + (1/self.outlet_area)*(self.inflow - self.outflow)
        self.time += 1
        self.history.append([self.time, self.inflow, self.outflow, self.height])

    def set_inflow(self, new_inflow):
        self.inflow = new_inflow

    def measure_inflow(self, gross_error = False):
        return self.inflow + gross_error

    def measure_outflow(self, gross_error = False):
        return self.outflow + gross_error

    def measure_height(self, gross_error = False):
        return self.height + gross_error

    def measure_history(self, gross_in, gross_out, gross_height):
        measured_history = self.history.copy()
        # add measurement error functions
        return measured_history
