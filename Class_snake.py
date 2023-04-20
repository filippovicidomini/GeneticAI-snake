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

    def put_snake_on_grid(self):
        self.position_of_snake = [[randint(0, 9), randint(0, 9)]]
        self.grid[self.position_of_snake[0][0]][self.position_of_snake[0][1]] = 1

    def put_food_on_grid(self):
        self.position_of_food = [randint(0, 9), randint(0, 9)]
        self.grid[self.position_of_food[0]][self.position_of_food[1]] = 2

    def create_grid(self):
        self.grid = [[0 for i in range(10)] for j in range(10)]
        self.put_snake_on_grid()
        self.put_food_on_grid()
    def position_of_snake(self):
        return self.position_of_snake

    def position_of_food(self):
        return self.position_of_food

    def update_grid(self):
        position_of_snake = self.position_of_snake
        position_of_food = self.position_of_food
        grid = [[0 for i in range(10)] for j in range(10)]
        grid[position_of_snake[0][0]][position_of_snake[0][1]] = 1
        grid[position_of_food[0]][position_of_food[1]] = 2
        self.grid = grid


    def get_distance_from_food(self): # distance from food in the four directions (up, down, left, right)
        distance_from_food = [0, 0, 0, 0]
        position_of_food = self.position_of_food
        position_of_snake = self.position_of_snake
        distance_from_food[0] = position_of_food[0] - position_of_snake[0][0]
        distance_from_food[1] = position_of_snake[0][0] - position_of_food[0]
        distance_from_food[2] = position_of_food[1] - position_of_snake[0][1]
        distance_from_food[3] = position_of_snake[0][1] - position_of_food[1]

        return distance_from_food

    def get_distance_from_wall(self): # distance from wall in the four directions (up, down, left, right)
        distance_from_wall = [0, 0, 0, 0]
        position_of_snake = self.position_of_snake
        distance_from_wall[0] = position_of_snake[0][0]
        distance_from_wall[1] = 9 - position_of_snake[0][0]
        distance_from_wall[2] = position_of_snake[0][1]
        distance_from_wall[3] = 9 - position_of_snake[0][1]
        return distance_from_wall

    def get_distance_from_body(self): # distance from body in the four directions (up, down, left, right)
        distance_from_body = [0, 0, 0, 0]
        position_of_snake = self.position_of_snake
        for i in range(self.score-1):
            if position_of_snake[0] == self.snake_body[i][0]:
                if position_of_snake[1] > self.snake_body[i][1]:
                    distance_from_body[2] = position_of_snake[1] - self.snake_body[i][1]
                else:
                    distance_from_body[3] = self.snake_body[i][1] - position_of_snake[1]
            elif position_of_snake[1] == self.snake_body[i][1]:
                if position_of_snake[0] > self.snake_body[i][0]:
                    distance_from_body[0] = position_of_snake[0] - self.snake_body[i][0]
                else:
                    distance_from_body[1] = self.snake_body[i][0] - position_of_snake[0]
        return distance_from_body

    def output(self):
        grid = self.grid
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 0:
                    print("_", end="  ")
                elif grid[i][j] == 1:
                    print("S", end="  ")
                elif grid[i][j] == 2:
                    print("F", end="  ")
            print()
        print('\n')

    def move(self, direction):
        position_of_snake = self.position_of_snake
        position_of_food = self.position_of_food
        distance_from_food = self.get_distance_from_food()
        distance_from_wall = self.get_distance_from_wall()
        if direction == 0:
            if distance_from_wall[0] == 0:
                breakpoint()
                print('You hit the wall')
            elif distance_from_food[0] == 0:
                self.score += 1
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][0] -= 1
                self.put_food_on_grid()
                self.update_grid()
            else:
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][0] -= 1
                self.update_grid()
        elif direction == 1:
            if distance_from_wall[1] == 0:
                print('You hit the wall')
            elif distance_from_food[1] == 0:
                self.score += 1
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][0] += 1
                self.put_food_on_grid()
                self.update_grid()
            else:
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][0] += 1
                self.update_grid()
        elif direction == 2:
            if distance_from_wall[2] == 0:
                print('You hit the wall')
            elif distance_from_food[2] == 0:
                self.score += 1
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][1] -= 1
                self.put_food_on_grid()
                self.update_grid()
            else:
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][1] -= 1
                self.update_grid()
        elif direction == 3:
            if distance_from_wall[3] == 0:
                print('You hit the wall')
            elif distance_from_food[3] == 0:
                self.score += 1
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][1] += 1
                self.put_food_on_grid()
                self.update_grid()
            else:
                self.snake_body.append([position_of_snake[0][0], position_of_snake[0][1]])
                position_of_snake[0][1] += 1
                self.update_grid()
        else:
            print('Invalid direction')


if __name__ == "__main__":
    snake = Snake()
    snake.create_grid()
    snake.output()
    snake.get_distance_from_food()
    snake.get_distance_from_wall()
    snake.get_distance_from_body()
    print(snake.get_distance_from_food())
    print(snake.get_distance_from_wall())
    print(snake.position_of_snake)


    for i in range(10):

        snake.move(choose_direction())
        snake.output()
    print(snake.position_of_snake)