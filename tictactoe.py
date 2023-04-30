class TicTacToe:
    def __init__(self, grid_size=3, win_size=3):
        self.grid_size = grid_size
        self.win_size = win_size
        self.grid = [[x+grid_size*y for x in range(grid_size)] for y in range(grid_size)]

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
        x, y = int(move / self.grid_size), int(move % self.grid_size)
        self.grid[x][y] = self.players[self.turn]
        self.turn = (self.turn + 1) % len(self.players)
