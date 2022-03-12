import random
from xxlimited import foo
import pygame
import time
pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
pygame.display.set_caption('Snake Game')

#prevents window from closing abruptly 
gameOver = False

green = (0,100,0)
crimson = (220,20,60)
background = (191,239,255)
food = (128,0,128)
lostScreen = (238,154,73)
pink = (255,20,147)


snake_block = 10
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 50)
scoreFont = pygame.font.SysFont("comicsansms", 35)

#display score
def setScore(score):
    result = scoreFont.render("Score: " + str(score), True, pink)
    display.blit(result, [0, 0])

#create snake
def snake(snakeBlock, snakeList):
    for s in snakeList:
        pygame.draw.rect(display, green, [s[0], s[1], snake_block, snake_block])        

#function to display message
def message(text, colour):
    msg = font_style.render(text, True, colour)
    display.blit(msg, [display_width / 10, display_height / 2])

#adding the food
def gameLoop():
    gameOver = False
    closeGame = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snakeList = []
    snakeLength = 1

    foodx = round(random.randrange(0, display_width - snake_block)/ 10.0) * 10.0
    foody = round(random.randrange(0, display_width - snake_block)/ 10.0) * 10.0

    while not gameOver:
        while closeGame == True:
            display.fill(lostScreen)
            message("You Lost! Press Q-Quit or P-Play Again", crimson)
            setScore(snakeLength - 1)
            pygame.display.update()

#user quits or restarts the game
            for screen in pygame.event.get():
                if screen.type == pygame.KEYDOWN:
                    if screen.key == pygame.K_q:
                        gameOver = True
                        closeGame = False
                    if screen.key == pygame.K_p:
                        gameLoop()    

        for screen in pygame.event.get():
            if screen.type == pygame.QUIT:
                gameOver = True
            if screen.type == pygame.KEYDOWN:
                if screen.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif screen.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif screen.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif screen.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change =  snake_block

        if x1 >= display_width or y1 >= display_height or y1 < 0 or x1 < 0:
            closeGame = True

        x1 += x1_change
        y1 += y1_change
        display.fill(background)
        pygame.draw.rect(display, food, [foodx, foody, snake_block, snake_block])

        #extend size of the snake
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for s in snakeList[:-1]:
            if s == snakeHead:
                closeGame = True

        snake(snake_block, snakeList)            
        setScore(snakeLength - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            snakeLength += 1

        clock.tick(snake_speed)                                                    

    pygame.quit()
    quit() 

gameLoop()       