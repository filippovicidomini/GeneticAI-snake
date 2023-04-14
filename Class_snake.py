# now i want code snake but withouth the pygame and with a neural network that will control the snake and try to get the highest score possible

from random import randint

import numpy as np


class Snake:
    def __init__(self):
        self.score = 1 # one because the snake start with one point
        self.brain = np.random.normal(0, 1, (5, 4))

    def workspace(self, num):
        self.grid = np.zeros((num, num))

    def put_snake(self, random=True):
        if random:
            self.grid[randint(0, len(self.grid) - 1), randint(0, len(self.grid) - 1)] = 1
        else:
            self.grid[0, 0] = 1     # parte dal angolo in alto a sinistra

    def put_food(self, random=True):
        if random:
            self.grid[randint(0, len(self.grid) - 1), randint(0, len(self.grid) - 1)] = 2
        else:
            self.grid[-1, -1] = 2   # parte dal angolo in basso a destra

    def get_distance_from_food(self):
        self.position_of_snake = np.where(self.grid == 1)
        self.position_of_food = np.where(self.grid == 2)
        # devo trovare la distanza di manhattan tra il serpente e il cibo
        self.distance_from_food = abs(self.position_of_snake[0] - self.position_of_food[0]) + abs(
            self.position_of_snake[1] - self.position_of_food[1])
        return self.distance_from_food[0]

    def get_distance_from_wall(self):  # distanza tra le 4 mura
        # sinistra, destra, sotto, sopra
        self.position_of_snake = np.where(self.grid == 1)
        self.distance_wall = [int(self.position_of_snake[0]), int(len(self.grid) - self.position_of_snake[0]),
                              int(self.position_of_snake[1]), int(len(self.grid) - self.position_of_snake[1])]
        return list(self.distance_wall[:])

    def move(self, direction):
        if direction == 0:
            self.grid[self.position_of_snake[0], self.position_of_snake[1] + 1] = 1
        elif direction == 1:
            self.grid[self.position_of_snake[0], self.position_of_snake[1] - 1] = 1
        elif direction == 2:
            self.grid[self.position_of_snake[0] + 1, self.position_of_snake[1]] = 1
        elif direction == 3:
            self.grid[self.position_of_snake[0] - 1, self.position_of_snake[1]] = 1

    def output(self):
        # i want to display the grid S if is the snake, F if is the food and . if is nothing
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i, j] == 0:
                    print("_", end="  ")
                elif self.grid[i, j] == 1:
                    print("S", end="  ")
                elif self.grid[i, j] == 2:
                    print("F", end="  ")
            print()

    def play(self):
        self.workspace(10)
        self.put_snake()
        self.put_food()

    def move_snake(self, direction):
        if direction == 0:
            self.grid[self.position_of_snake[0], self.position_of_snake[1] + 1] = 1
            if self.grid[self.position_of_snake[0], self.position_of_snake[1] + 1] == 2:
                self.score += 1
                self.put_food()
        elif direction == 1:
            self.grid[self.position_of_snake[0], self.position_of_snake[1] - 1] = 1
            if self.grid[self.position_of_snake[0], self.position_of_snake[1] - 1] == 2:
                self.score += 1
                self.put_food()
        elif direction == 2:
            self.grid[self.position_of_snake[0] + 1, self.position_of_snake[1]] = 1
            if self.grid[self.position_of_snake[0] + 1, self.position_of_snake[1]] == 2:
                self.score += 1
                self.put_food()
        elif direction == 3:
            self.grid[self.position_of_snake[0] - 1, self.position_of_snake[1]] = 1
            if self.grid[self.position_of_snake[0] - 1, self.position_of_snake[1]] == 2:
                self.score += 1
                self.put_food()

if __name__ == "__main__":
    game = Snake()
    game.play()
    game.output()
    print(game.get_distance_from_food())
    game.move_snake(0)
    game.output()
