import pygame
import random
import math
pygame.init()

screenHeight = 500
screenWidth  = 500
gameWindow = pygame.display.set_mode([screenWidth,screenHeight])

gameOver = False

x = 45
y = 45
score = 0
font = pygame.font.SysFont(None, 25)
img = font.render('score = '+str(score), True, (0,0,255))
gameWindow.blit(img, (0, 0))
xVelocity = 0
yVelocity = 0

snakeHeight = 20
snakeWidth = 20
snake = pygame.draw.rect(gameWindow,(0,0,255),[x,y,snakeWidth,snakeHeight])

foodX = random.randint(0, screenWidth-snakeWidth)
foodY = random.randint(0, screenHeight-snakeHeight)
foodHeight = 10
foodWidth = 10
snakeList = []
snake_length= 1
food = pygame.draw.rect(gameWindow,(255,0,0),[foodX,foodY,foodWidth,foodHeight])
pygame.display.update()

clk = pygame.time.Clock()

while not gameOver:
    if x>= screenWidth-(snakeWidth//2) or x < 0 or y < 0 or y>=screenHeight-(snakeHeight//2):
        break
    if snake.colliderect(food):
        print('collison at ', math.sqrt((x - foodX)**2 + (y-foodY)**2))

        foodX = random.randint(0, screenWidth-snakeWidth)
        foodY = random.randint(0, screenHeight-snakeHeight)
        snake_length += 10
        score += 10
        print(score)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:

                xVelocity = 0
                yVelocity = 2

            if event.key == pygame.K_UP:

                xVelocity = 0
                yVelocity = -2
            if event.key == pygame.K_LEFT:

                yVelocity = 0
                xVelocity = -2
            if event.key == pygame.K_RIGHT:

                yVelocity = 0
                xVelocity = 2
        elif event.type == pygame.QUIT:
            gameOver = True

    x += xVelocity
    y += yVelocity
    head = []
    head.append(x)
    head.append(y)
    snakeList.append(head)
    gameWindow.fill((255,255,255))
    if len(snakeList) > snake_length:
        del snakeList[0]
    if [x,y] in snakeList[:-1]:
        break
    for i,j in snakeList:
        snake = pygame.draw.rect(gameWindow,(0,0,255),[i,j,snakeWidth,snakeHeight])

    img = font.render('score = ' + str(score), True, (0, 0, 255))
    gameWindow.blit(img, (0, 0))
    food = pygame.draw.rect(gameWindow, (255, 0, 0), [foodX, foodY, foodWidth, foodHeight])
    pygame.display.update()
    clk.tick(100)

pygame.quit()
