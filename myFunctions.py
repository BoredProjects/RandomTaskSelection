import pygame
import math
import textwrap

pygame.init()

def getTask():#Gets all task for array then returns array and the end points for each line that will be drawn

    taskArr = []
    points = []
    loop = True

    while loop:

        task = str(input("What would do you have to do today? Leave it blank to exit."))

        if task != "":
            taskArr.append(task)
        else:
            loop = False

    angle = 360/len(taskArr)

    for count in range(len(taskArr)):

        xPoint = (math.cos(math.radians(angle))*200) + 400
        yPoint = (math.sin(math.radians(angle))*200) + 400
        points.append([xPoint,yPoint])

        if(angle != 360):
            angle = angle + (angle / (count + 1))
        
    return points, taskArr


def makeMyCircle(display,endPoints,task):#Draws the circle

    white = (255,255,255)

    pygame.draw.circle(display,white,(400,400),200,1)

    for count in range(len(endPoints)):
        pygame.draw.line(display,white,(400,400),(endPoints[count]),1)


def spinMySpinner(display,color,degree):#Spins the spinner around my circle and returns the last angle

    x = (math.cos(math.radians(degree)) * 200) + 400
    y = (math.sin(math.radians(degree)) * 200) + 400
    spinner = pygame.draw.line(display,color,(400,400),(x,y),5)
    degree += 3

    if degree > 360:
        degree = 0

    return degree

def findMyTask(degree,task,display):#Finds which task to display by determining where the spinner was pointing when it stopped. Then prints out text on new window.

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    sliceSize = 360/len(task)
    currentAngle = 0
    luckyWinner = ''

    for slice in range(len(task)):
        currentAngle = sliceSize + currentAngle
        if degree < currentAngle:
            luckyWinner = task[slice]
            break

    wrappedText = textwrap.wrap(staggerText(luckyWinner),50)

    textYPos = 200
    for newLine in range(len(wrappedText)):
        textsurface = myfont.render(wrappedText[newLine], False, (255, 0, 0))
        display.blit(textsurface, (50, textYPos))
        textYPos = textYPos + 50

def staggerText(myTask):#Splits my text into a string
    myWords = ['Congratulations','you','now','have','to','do']
    newWords = myTask.split()

    myWords = myWords + newWords

    return ' '.join(myWords)


