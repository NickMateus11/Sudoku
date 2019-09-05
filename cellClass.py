class Cell:
    def __init__(self, value=None):
        if value is not None and value <= 0:
            raise ValueError
        self.val = value
        self.possible_vals = []