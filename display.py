from primitives import Grid

#import visual
#import vpython
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Display:
    def __init__(self, grid: Grid):
        self.grid = grid

        self.fig = plt.figure()
        self.fig.add_subplot(111, projection='3d')

    def draw(self):
        pass
        #for point, obj in self.grid()
