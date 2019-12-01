from numpy import sqrt, array, append
class Tank:
    def __init__(self, height=0., inflow=0., valve_coef=1., outlet_area=1.):
        self.height = height
        self.inflow = inflow
        self.valve_coef = valve_coef
        self.outlet_area = outlet_area
        self.time = 0
        self.history = array([self.time, self.height])

    def update_level(self):
        outflow = self.valve_coef*sqrt(9.81*self.height)
        self.height = height  + (1/self.outlet_area)*(self.inflow - outflow)
        self.time += 1
        self.history.append([self.time, self.height])

