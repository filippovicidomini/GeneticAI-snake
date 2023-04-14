# now i want code snake but withouth the pygame and with a neural network that will control the snake and try to get the highest score possible

import numpy as np
import random
import math


class Snake:
    def __init__(self):
        self.score = 0
        self.brain = np.random.normal(0, 1, (5, 4))

    def workspace(self, num):
        self.grid = np.zeros((num, num))

    def put_snake(self, random=True):
        if random:
            self.grid[random.randomint(0, len(self.grid)), random.randomint(0, len(self.grid))] = 1
        else:
            self.grid[0, 0] = 1     # parte dal angolo in alto a sinistra

    def put_food(self, random=True):
        if random:
            self.grid[random.randomint(0, len(self.grid)), random.randomint(0, len(self.grid))] = 2
        else:
            self.grid[-1, -1] = 2   # parte dal angolo in basso a destra

    def get_distance_from_food(self):
        self.position_of_snake = np.where(self.grid == 1)
        self.position_of_food = np.where(self.grid == 2)
        # devo trovare la distanza di manhattan tra il serpente e il cibo
        self.distance_from food = abs(self.position_of_snake[0] - self.position_of_food[0]) + abs(self.position_of_snake[1] - self.position_of_food[1])
        return self.distance_from_food

    def get_distance_from_wall(self):   # distanza tra le 4 mura
        self.position_of_snake = np.where(self.grid == 1)
        self.distance_wall = [self.position_of_snake[0], len(self.grid) - self.position_of_snake[0], self.position_of_snake[1], len(self.grid) - self.position_of_snake[1]]
        return self.distance_wall

    def game_over(self):
        self.position_of_snake = np.where(self.grid == 1)
        if self.position_of_snake[0] == 0 or self.position_of_snake[0] == len(self.grid) - 1 or self.position_of_snake[1] == 0 or self.position_of_snake[1] == len(self.grid) - 1:
            return True
        else:
            return False


    def move(self, direction):
        if direction == 0:
            self.grid[self.position_of_snake[0], self.position_of_snake[1] + 1] = 1

        elif direction == 1:
            self.grid[self.position_of_snake[0], self.position_of_snake[1] - 1] = 1
        elif direction == 2:
            self.grid[self.position_of_snake[0] + 1, self.position_of_snake[1]] = 1
        elif direction == 3:
            self.grid[self.position_of_snake[0] - 1, self.position_of_snake[1]] = 1


    def play(self):
        self.workspace(10)
        self.put_snake()
        self.put_food()
        while True:
            self.move()
