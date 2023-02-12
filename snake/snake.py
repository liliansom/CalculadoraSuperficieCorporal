import pygame
import random
from pygame.font import Font
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x // 10 * 10, y // 10 * 10

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

font = pygame.font.init()
font_1 = pygame.font.SysFont('Arial', 20, True, True)
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

snake = [(200, 200), (210, 200), (220, 200)]
my_direction = LEFT
snake_skin = pygame.Surface((10, 10))
snake_skin.fill(color='white')

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill(color='red')

clock = pygame.time.Clock()
pontos = 0

while True:
    clock.tick(15)
    message = 'Pontuação: {}'.format(pontos)
    text = Font.render(font_1, message, False,'green' )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    # COLISÕES
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append(0)
        pontos += 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        pygame.quit()
        exit()

    for i in range(2, (len(snake) - 1)):
        if collision(snake[0], snake[i]):
            pygame.quit()
            exit()

    if my_direction == UP:
        snake[0] = snake[0][0], snake[0][1] - 10

    if my_direction == DOWN:
        snake[0] = snake[0][0], snake[0][1] + 10

    if my_direction == RIGHT:
        snake[0] = snake[0][0] + 10, snake[0][1]

    if my_direction == LEFT:
        snake[0] = snake[0][0] - 10, snake[0][1]

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    screen.blit(text, (350,550))

    for pos in snake:
        screen.blit(snake_skin, pos)


    pygame.display.update()
