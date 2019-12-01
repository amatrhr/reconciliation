from numpy import sqrt, array, append


class Tank:
    """A model of a water tank with unit bottom area and an outflow valve in the bottom."""
    def __init__(self, height=1.0, inflow=0.05, valve_coef=1.0, outlet_area=0.01):
        self.height = height
        self.inflow = inflow
        self.valve_coef = valve_coef
        self.outlet_area = outlet_area
        self.time = 0
        self.outflow = self.valve_coef * sqrt(9.81 * self.height)
        self.history = array([self.time, self.height, self.inflow, self.outflow]).reshape(1,4)

    def update_level(self):
        self.outflow = self.valve_coef * sqrt(9.81 * self.height)
        self.height = self.height + (self.outlet_area) * (self.inflow - self.outflow)
        if self.height <= 0:
            self.height = 0
        self.time += 1
        self.history = append(self.history, [self.time, self.height, self.inflow, self.outflow])

    def update_history(self, n_obs):
        start_shape = self.history.shape[0]
        for i in range(n_obs):
            self.update_level()
        # breakpoint()
        self.history = self.history.reshape((n_obs + start_shape),4)

    def set_inflow(self, new_inflow):
        self.inflow = new_inflow

    def measure_inflow(self, gross_error=False):
        return self.inflow + gross_error

    def measure_outflow(self, gross_error=False):
        return self.outflow + gross_error

    def measure_height(self, gross_error=False):
        return self.height + gross_error

    def measure_history(self, gross_in, gross_out, gross_height):
        measured_history = self.history.copy()
        # add measurement error functions
        return measured_history
