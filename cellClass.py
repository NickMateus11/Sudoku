class Cell:
    def __init__(self, value=None):
        if value is not None and value <= 0:
            raise ValueError
        self.val = value
        self.possible_vals = [] # Values that CAN fit
        self.black_listed_vals = [] # Values that MAY fit but have already been tried (and failed) so black list them