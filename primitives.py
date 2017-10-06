#!/usr/bin/env python

from typing import List
import itertools
import enum
import math

import numpy


class Point(list):
    def __init__(self, pos: List[int]):
        super(Point, self).__init__(pos)
        assert(len(self) == 2 or len(self) == 3)

    def __sub__(self, p: "Point"):
        res = []
        for i in range(len(self)):
            res.append(self[i] - p[i])
        assert(len(res) == len(self))
        return res

    def distance_to(self, p: "Point"):
        return math.sqrt(sum(p - self))


class GridBox:
    def __init__(self, pos: Point):
        self.pos = pos
        # Denotes that this will be occupied next turn
        self.will_occupy = False
        self.occupant = None

    def __repr__(self):
        return 'Box@{}'.format(self.pos)


class Unit:
    def __init__(self, gridbox: GridBox, grid: "Grid"):
        self.grid = grid
        self.gridbox = gridbox

    def adjacent(self):
        '''
        Returns a list of adjacent units
        '''
        adj_gridboxes = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    box = self.grid[Point(i, j, k)]
                    # We could check before adding, but leaving the Nones in
                    # preserves the position of the occupied boxes
                    adj_gridboxes.append(box.occupant)
        return adj_gridboxes


class Bot(Unit):
    block = None

    def plan_move(self, point: Point) -> Point:
        '''
        Plans a move to happen next 'turn'. Move should be no more than
        1 unit in any direction
        '''
        # Make sure movement is only 1 unit
        assert(self.pos.distance(point) <= 1)

        self.next_move = point - self.pos
        occupant = self.grid[point].will_occupy
        if occupant:
            raise Exception(
                'Invalid move by bot {}, {} occupied by {}'
                .format(self, point, occupant)
            )

    def is_planar(self, point: Point):
        '''
        Determine if the point is in the same xy plane as the bot
        '''
        return (self.pos - block.pos)[2] == 0


    def carry_block(self, block: "Block"):
        # Can only pick up blocks adjacent on the same xy plane
        assert(self.pos.distance(block.pos) <= 1)
        assert(self.is_planar(block.pos))

        self.block = block
        self.block.gridbox.occupant = None

    def place_block(self, point: Point): 
        assert(self.pos.distance(point) <= 1)
        assert(self.is_planar(block.pos))

        self.grid[point].occupant = self.block
        self.block = None

        
class Color(enum.Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


class Block(Unit):
    def __init__(self, *args, color: Color):
        self.color = color
        super(self, Block).__init__(*args)


class Grid(dict):
    def __init__(self, size):
        grid = itertools.product(range(size), range(size), range(size))
        for point in grid:
            self[point] = GridBox(point)
