import pygame
from random import choice  # choice a random item from a data structure

pygame.init()  # Initialize the pygame library

fps = 30  # frame per second
width = 800
height = 600
x_feed = choice(list(range(200, 800, 15)))
y_feed = choice(list(range(0, 600, 15)))
points = 0  # score

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
lightBlue = (76, 231, 255)

img = pygame.image.load('snake_image.png')  # load the main menu image
pygame.display.set_caption("Snake")
gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def score_texts(score):
    global points
    '''Print the score to the screen.'''
    font = pygame.font.SysFont('comicsansms', 23)
    scoretext = font.render("score: " + str(score), 1, (0, 0, 0))
    gameDisplay.blit(scoretext, (50, 100))

    points = score


def text(texts, size, x, y, font_color):
    '''Print text to the screen.'''

    font = pygame.font.SysFont('comicsansms', size)
    txt = font.render(texts, 1, font_color)
    gameDisplay.blit(txt, (x, y))


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action == 'play':

            points = 0

            snake1.MOVE = 'UP'

            game(x_feed, y_feed, points)

        if click[0] == 1 and action == 'quit':
            pygame.quit()
            quit()

    else:

        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    font = pygame.font.SysFont('comicsansms', 20)
    textSurf = font.render(msg, True, black)
    textRect = textSurf.get_rect()
    textRect.center = ((x + w / 2), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def game(x_feed, y_feed, points):
    '''The game progress'''

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP and snake1.MOVE != 'DOWN':
                    snake1.MOVE = 'UP'

                    break

                elif event.key == pygame.K_DOWN and snake1.MOVE != 'UP':
                    snake1.MOVE = 'DOWN'

                    break

                elif event.key == pygame.K_RIGHT and snake1.MOVE != 'LEFT':
                    snake1.MOVE = 'RIGHT'

                    break

                elif event.key == pygame.K_LEFT and snake1.MOVE != 'RIGHT':
                    snake1.MOVE = 'LEFT'

                    break


        while (x_feed, y_feed) in zip(list(snake1.x_var.values()), list(snake1.y_var.values())):

            x_feed = choice(list(range(200, 800, 15)))

            y_feed = choice(list(range(0, 600, 15)))

            points += 1

            snake1.grow()

        gameDisplay.fill(white)

        pygame.draw.line(gameDisplay, black, (200, 0), (200, 600))

        pygame.draw.rect(gameDisplay, lightBlue, (x_feed, y_feed, snake1.snake_height, snake1.snake_height))

        snake1.show_snake(snake1.snake_height)

        snake1.movement()

        snake1.kill()

        score_texts(points)

        pygame.display.update()

        clock.tick(fps)


def game_over():
    '''The game over menu'''

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        font = pygame.font.SysFont('comicsansms', 23)

        scoretext = font.render("score: " + str(points), 1, (0, 0, 0))

        gameDisplay.blit(scoretext, (50, 100))

        text('Game Over', 50, 350, 250, (250, 0, 0))

        button('Play again', 400, 400, 100, 50, (0, 200, 0), (0, 255, 0,), 'play')

        button('Quit', 600, 400, 100, 50, (0, 200, 0), (255, 0, 0,), 'quit')

        pygame.display.update()

        clock.tick(fps)


class snake:
    '''This is the snake class'''

    def __init__(self):

        self.x_var = {
            'x0': 305,
            'x1': 305,
            'x2': 305,
            'x3': 305,
            'x4': 305}

        self.y_var = {
            'y0': 405,
            'y1': 420,
            'y2': 435,
            'y3': 450,
            'y4': 465}

        # x_var and y_var is position of snake, xo and y0 is the head position.

        self.MOVE = 'UP'

        self.snake_height = 15

    def show_snake(self, height):
        '''Drawing the snake'''

        for i in range(len(self.x_var)):

            if i == 0:
                pygame.draw.rect(gameDisplay, red, (self.x_var['x{}'.format(i)], self.y_var['y{}'.format(i)], height, height))

            else:
                pygame.draw.rect(gameDisplay, green, (self.x_var['x{}'.format(i)], self.y_var['y{}'.format(i)], height, height))

    def movement(self):
        '''Move the snake.'''

        for n in reversed(range(1, len(self.x_var))):

            self.x_var['x{}'.format(n)] = self.x_var['x{}'.format(n - 1)]

            self.y_var['y{}'.format(n)] = self.y_var['y{}'.format(n - 1)]

        if self.MOVE == 'UP':

            self.y_var['y0'] -= self.snake_height

        elif self.MOVE == 'RIGHT':

            self.x_var['x0'] += self.snake_height

        elif self.MOVE == 'DOWN':

            self.y_var['y0'] += self.snake_height

        elif self.MOVE == 'LEFT':

            self.x_var['x0'] -= self.snake_height

        if self.x_var['x0'] < 200:
            self.x_var['x0'] = 785

        elif self.x_var['x0'] > 785:
            self.x_var['x0'] = 200

        if self.y_var['y0'] < 0:
            self.y_var['y0'] = 585

        elif self.y_var['y0'] > 585:
            self.y_var['y0'] = 0

    def grow(self):
        '''This method is called when snake eat food and growing'''

        if (list(self.x_var.values())[-1] == list(self.x_var.values())[-2] and
                list(self.y_var.values())[-1] > list(self.y_var.values())[-2]):

                    self.x_var['x{}'.format(len(self.x_var))] = list(self.x_var.values())[-1]
                    self.y_var['y{}'.format(len(self.y_var))] = list(self.y_var.values())[-1] + self.snake_height

        elif (list(self.x_var.values())[-1] == list(self.x_var.values())[-2] and
                list(self.y_var.values())[-1] < list(self.y_var.values())[-2]):

                    self.x_var['x{}'.format(len(self.x_var))] = list(self.x_var.values())[-1]
                    self.y_var['y{}'.format(len(self.y_var))] = list(self.y_var.values())[-1] - self.snake_height

        elif (list(self.y_var.values())[-1] == list(self.y_var.values())[-2] and
                list(self.x_var.values())[-1] > list(self.x_var.values())[-2]):

                    self.y_var['y{}'.format(len(self.y_var))] = list(self.y_var.values())[-1]
                    self.x_var['x{}'.format(len(self.x_var))] = list(self.x_var.values())[-1] + self.snake_height

        elif (list(self.y_var.values())[-1] == list(self.y_var.values())[-2] and
                list(self.x_var.values())[-1] < list(self.x_var.values())[-2]):

                    self.y_var['y{}'.format(len(self.y_var))] = list(self.y_var.values())[-1]
                    self.x_var['x{}'.format(len(self.x_var))] = list(self.x_var.values())[-1] - self.snake_height

    def kill(self):
        '''This method is called if the snake eat himself.'''

        for i in range(1, len(self.x_var) - 1):

            if (self.x_var['x0'], self.y_var['y0']) == (self.x_var['x{}'.format(i)], self.y_var['y{}'.format(i)]):
                game_over()


snake1 = snake()  # create the snake instance


while True:
    '''Main loop'''

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.blit(img, (0, 0))

    button('Play', 50, 400, 100, 50, (0, 200, 0), (0, 255, 0), 'play')
    button('Quit', 250, 400, 100, 50, (0, 200, 0), (255, 0, 0,), 'quit')

    pygame.display.update()

    clock.tick(fps)
