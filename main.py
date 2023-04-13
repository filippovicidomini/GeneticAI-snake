# i want to try to code a snake game in python using pygame
# and a genetic algorithm to train the snake to play the game
# i want to use a neural network to control the snake
# i want to use pygame to display the game
# i want to use pygame to display the genetic algorithm

import pygame
import random
import time
import math
import numpy as np
import os
import sys

# initialize pygame
pygame.init()

# create the screen

screen = pygame.display.set_mode((800, 600))


# title and icon
pygame.display.set_caption("Snake")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# snake
snakeImg = pygame.image.load('snake.png')
# reformating the image
snakeImg = pygame.transform.scale(snakeImg, (32, 32))
snakeX = 370
snakeY = 480
snakeX_change = 0
snakeY_change = 0

# food
foodImg = pygame.image.load('food.png')
# reformating the image
foodImg = pygame.transform.scale(foodImg, (32, 32))
foodX = random.randint(0, 735)
foodY = random.randint(50, 535)

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def snake(x, y):
    screen.blit(snakeImg, (x, y))

def food(x, y):
    screen.blit(foodImg, (x, y))

# game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakeX_change = -5
                snakeY_change = 0
            if event.key == pygame.K_RIGHT:
                snakeX_change = 5
                snakeY_change = 0
            if event.key == pygame.K_UP:
                snakeY_change = -5
                snakeX_change = 0
            if event.key == pygame.K_DOWN:
                snakeY_change = 5
                snakeX_change = 0

    snakeX += snakeX_change
    snakeY += snakeY_change

    if snakeX <= 0:
        snakeX = 0
    elif snakeX >= 736:
        snakeX = 736

    if snakeY <= 50:
        snakeY = 50
    elif snakeY >= 536:
        snakeY = 536

    snake(snakeX, snakeY)
    food(foodX, foodY)
    show_score(textX, textY)
    pygame.display.update()

pygame.quit()
