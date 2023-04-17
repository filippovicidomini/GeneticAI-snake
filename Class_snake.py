# now i want code snake but withouth the pygame and with a neural network that will control the snake and try to get the highest score possible

from random import randint

import numpy as np


def choose_direction():
    direction = np.random.randint(0, 4)
    return direction


class Snake:
    def __init__(self):
        self.grid: list  = []
        self.position_of_snake: list = []
        self.position_of_food: list = []
        self.score = 1  # one because the snake start with one point
        self.snake_body: list = []  # is a tuple with the coordinates of the snake head
