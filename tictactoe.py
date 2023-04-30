import numpy as np


class TicTacToe:
    def __init__(self, grid_size=3, win_size=3):
        self.grid_size = grid_size
        self.win_size = win_size
        self.grid = np.array([str(x) for x in range(9)]).reshape((grid_size, grid_size))

        self.players = ["x", "o"]
        self.turn = 0

    def print(self):
        out_string = ""
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                out_string += str(col)
                if x < self.grid_size - 1:
                    out_string += "|"
            out_string += "\n"
        print(out_string)

    def play(self, move: int):
        x, y = int(move % self.grid_size), int(move / self.grid_size)
        self.grid[y, x] = self.players[self.turn]
        self.turn = (self.turn + 1) % len(self.players)

    def evaluate(self):
        # Using masks is the fun \ unique way, and we are all about learning having fun!
        y, x = np.ogrid[:self.grid_size, :self.grid_size]

        rows = [self.grid[((y == row) & (x >= 0))] for row in range(self.grid_size)]
        cols = [self.grid[((y >= 0) & (x == col))] for col in range(self.grid_size)]

        diag_mask = (x == y)
        diag = self.grid[diag_mask]

        anti_diag_mask = (x + y == self.grid_size - 1)
        anti_diag = self.grid[anti_diag_mask]

        threes = rows+cols+[diag]+[anti_diag]
        print(threes)
