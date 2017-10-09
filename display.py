from primitives import Grid

#import visual
#import vpython
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Display:
    def __init__(self, grid: Grid):
        self.grid = grid

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def draw(self):
        gridboxes = self.grid.values()
        occupants = [g.occupant for g in gridboxes]
        print(occupants)
        #print([o.pos if o else None for o in occupants])
        self.ax.scatter(xs, ys, zs)
        plt.show()
