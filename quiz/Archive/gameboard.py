BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'


class GameBoard:
    def __init__(self, width=5, height=5):
        grid = []
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append(BLANK)
            grid.append(new_row)
        self.grid = grid
