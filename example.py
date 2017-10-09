#!/usr/bin/env python

import random

import primitives
import display


SIZE = 5

def rpoint():
    return primitives.Point((
        random.randint(0, SIZE-1),
        random.randint(0, SIZE-1),
        random.randint(0, SIZE-1))
    )

g = primitives.Grid(SIZE)
bots = primitives.Bot(g, rpoint())

display.Display(g).draw()
