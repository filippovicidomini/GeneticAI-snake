# now i want code snake but withouth the pygame and with a neural network that will control the snake and try to get the highest score possible

from random import randint

import numpy as np


def choose_direction():
    direction = np.random.randint(0, 4)
    return direction


class Snake:
    def __init__(self):
        self.grid = None
        self.position_of_snake = None
        self.position_of_food = None
        self.score = 1  # one because the snake start with one point
        self.snake_head = None  # is a tuple with the coordinates of the snake head
        snake_body = None  # is a list with the coordinates of the snake
        self.brain = np.random.normal(0, 1, (5, 4))

    def workspace(self, num):
        self.grid = np.zeros((num, num))

    def put_snake(self, random=True, x=None, y=None):
        if random:
            self.grid[randint(0, len(self.grid) - 1), randint(0, len(self.grid) - 1)] = 1
        else:
            self.grid[x, y] = 1  # parte dal angolo in alto a sinistra
        self.snake_head = np.where(self.grid == 1)

    def put_food(self, random=True, x=None, y=None):
        if random:
            self.grid[randint(0, len(self.grid) - 1), randint(0, len(self.grid) - 1)] = 2
        else:
            self.grid[x, y] = 2   # parte dal angolo in basso a destra

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
        print('\n')

    def play(self):
        self.workspace(10)
        self.put_snake()
        self.put_food()

    def get_score(self):
        return self.score

    def free_position(self, direction):
        # check that the snake is not going to hit the wall or itself uso la direzione per capire dove andare e get_distance_from_wall per capire se c'è un muro
        if direction == 0:
            if self.get_distance_from_wall()[0] == 1:
                return False
            else:
                return True
        elif direction == 1:
            if self.get_distance_from_wall()[1] == 1:
                return False
            else:
                return True
        elif direction == 2:
            if self.get_distance_from_wall()[2] == 1:
                return False
            else:
                return True
        elif direction == 3:
            if self.get_distance_from_wall()[3] == 1:
                return False
            else:
                return True


    def move_snake(self, direction):
        if direction == 0:
            if not self.free_position(direction):
                breakpoint()
                return self.game_over()

            # se incontra il cibo allora aumenta di 1 la lunghezza del serpente e mette un nuovo cibo in una posizione random e non elimina la coda
            if self.grid[self.snake_head[0], self.snake_head[1] + 1] == 2:
                self.grid[self.snake_head[0], self.snake_head[1] + 1] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)
                self.put_food()
            else:
                self.grid[self.snake_head[0], self.snake_head[1] + 1] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)
        elif direction == 1:
            if self.grid[self.snake_head[0], self.snake_head[1] - 1] == 2:
                self.grid[self.snake_head[0], self.snake_head[1] - 1] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)
                self.put_food()
            else:
                self.grid[self.snake_head[0], self.snake_head[1] - 1] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)
        elif direction == 2:
            if self.grid[self.snake_head[0] + 1, self.snake_head[1]] == 2:
                self.grid[self.snake_head[0] + 1, self.snake_head[1]] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)
                self.put_food()
            else:
                self.grid[self.snake_head[0] + 1, self.snake_head[1]] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)
        elif direction == 3:
            if self.grid[self.snake_head[0] - 1, self.snake_head[1]] == 2:
                self.grid[self.snake_head[0] - 1, self.snake_head[1]] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)
                self.put_food()
            else:
                self.grid[self.snake_head[0] - 1, self.snake_head[1]] = 1
                self.grid[self.snake_head[0], self.snake_head[1]] = 0
                self.snake_head = np.where(self.grid == 1)

    def game_over(self):
        print("GAME OVER")


if __name__ == "__main__":
    game = Snake()

    game.play()
    game.output()
    print(game.get_distance_from_food())
    for i in range(10):
        game.move_snake(choose_direction())
        game.output()
