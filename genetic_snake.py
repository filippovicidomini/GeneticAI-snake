# using the snake.py in this reposotory i want to create a neural network that will control the snake and try to get the highest score possible


# Path: genetic_snake.py
# Compare this snippet from snake.py:

import random
import snake
import pygame
import math
import numpy as np
def fitness(snake):
    return snake.score

def crossover(parent1, parent2):
    child = snake.Snake()
    child.brain = parent1.brain + parent2.brain
    return child

def mutate(child):
    child.brain = child.brain + np.random.normal(0, 0.1, child.brain.shape)
    return child

def selection(population):
    fitnesses = [fitness(snake) for snake in population]
    total_fitness = sum(fitnesses)
    probs = [f/total_fitness for f in fitnesses]
    parents = np.random.choice(population, 2, p=probs, replace=False)
    return parents

def next_generation(population):
    new_population = []
    for i in range(len(population)):
        parents = selection(population)
        child = crossover(parents[0], parents[1])
        child = mutate(child)
        new_population.append(child)
    return new_population

def main():
    population = [snake.Snake() for i in range(100)]
    for generation in range(100):
        for snake in population:
            snake.play()
        population = next_generation(population)
        print(fitness(population[0]))

if __name__ == "__main__":
    main()

