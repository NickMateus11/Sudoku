class Cell:
    def __init__(self, value=None):
        if value is not None and value <= 0:
            raise ValueError
        self.val = value
        self.possible_vals = [self.val] if self.val is not None else []
    
    def set_value(self, val):
        self.val = val
        if val in self.possible_vals:
            self.possible_vals.remove(val)