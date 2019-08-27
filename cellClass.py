class Cell:
    def __init__(self, value=None):
        if value <= 0:
            raise ValueError
        self.value = value
        self.possible_vals = []
    
    def set_value(self, val):
        self.value = val
        if val in self.possible_vals:
            self.possible_vals.remove(val)
    
    def add_possible_value(self, val):
        if val not in self.possible_vals:
            self.possible_vals.append(val)