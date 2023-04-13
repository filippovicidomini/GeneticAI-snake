# using the snake.py in this reposotory i want to create a genetic algorithm to train the snake to play the game
# the fitness function is the score of the snake
# the mutation rate is the rate at which the snake changes direction

import random


def fitness(snake):
    return snake.score


def mutate(snake):
    snake.direction = random.randint(0, 3)


def crossover(snake1, snake2):
    snake = snake1
    snake.direction = snake2.direction
    return snake


def selection(population):
    population.sort(key=fitness, reverse=True)
    return population[:len(population) // 2]


def generate(population):
    new_population = []
    for i in range(len(population)):
        snake1 = random.choice(population)
        snake2 = random.choice(population)
        child = crossover(snake1, snake2)
        mutate(child)
        new_population.append(child)
    return new_population


def main():
    population = []
    for i in range(100):
        snake = snake.Snake()
        population.append(snake)
    for i in range(1000):
        for snake in population:
            snake.update()
        population = selection(population)
        population = generate(population)
        print(fitness(population[0]))


if __name__ == "__main__":
    main()
