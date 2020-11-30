import pygame
import myFunctions
import random
import time

pygame.init()
pygame.font.init()

gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption(("My Spinner"))

clock = pygame.time.Clock()
gameLoop = True
degree = 0
endTime = random.randint(1,20)

endPoints, taskArr = myFunctions.getTask()
myFunctions.makeMyCircle(gameDisplay,endPoints,taskArr)

currentTime = time.time()
while gameLoop:


    if not (time.time() - currentTime) > endTime:
        gameDisplay.fill([0, 0, 0])
        degree = myFunctions.spinMySpinner(gameDisplay,(255,0,0),degree)
        myFunctions.makeMyCircle(gameDisplay,endPoints,taskArr)
    else:
        gameDisplay.fill([0, 0, 0])
        myFunctions.findMyTask(degree,taskArr,gameDisplay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
