import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]]
                )

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    def __init__(game, Size):
        game.board = np.zeros((Size, Size))

    def play(self):
        """Initialise game."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Calculate next step."""
        STENCIL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        NeighbourCount = convolve2d(self.board, STENCIL, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (NeighbourCount[i, j] == 3
                                         or (NeighbourCount[i, j] == 2
                                             and self.board[i, j])) else 0

    def __setitem__(self, key, value):
        self.board[key] = value

    def show(self):
        """Show new move on screen."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, p, loc):
        if not isinstance(p, Pattern):
            return NotImplemented
        game = self.board
        size = np.array(p.grid.shape)
        centre = size // 2
        tl = np.array(loc) - centre
        gamec = game.copy()
        try:
            gamec[tl[0]:tl[0]+size[0], tl[1]:tl[1]+size[1]] = p.grid
        except IndexError:
            print("invalid placement")
            raise IndexError
        self.board = gamec


class Pattern:
    def __init__(self, grid: np.ndarray):
        self.grid = grid

    def flip_vertical(self):
        return Pattern(np.flipud(self.grid))

    def flip_horizontal(self):
        return Pattern(np.fliplr(self.grid))

    def flip_diag(self):
        return Pattern(self.grid.T)

    def rotate(self, n: int):
        grid = self.grid
        for i in range(n):
            grid = np.rot90(grid)
        return Pattern(grid)


grid_size = 9
coordinates = [4, 5]
g = Game(grid_size)
g.insert(Pattern(glider), coordinates)
