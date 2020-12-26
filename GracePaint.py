""" Painter | Grace Li
March 30, 2018. Ms Paint knockoff."""

"""Assignment 1 - Drawing with Pygame, Grace Li
This program will create a cyan background and draw four
squares with yellow circles as specified in the assignment"""

import pygame #import and initialize necessary values
pygame.init()
done = False
clock = pygame.time.Clock()

#initialize variables
window = pygame.display.set_mode((600,400)) #set up basic display and background
pygame.display.set_caption("Paint!!")
mdown,drawing = False,False
font = pygame.font.Font(None, 24)
brush_options = font.render("Brush Settings", True, (30,30,30))
brush_size = font.render("SIZE:", True, (255,255,255))
brush_shape = font.render("SHAPE:", True, (255,255,255))
bSize,bColor,co = 2, (0,0,0),9
coList = [(255,0,0),(255,128,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),\
          (128,0,128),(255,0,255),(128,128,128),(0,0,0),(240,245,255)] #0-10

#set up unchanging screen
window.fill((255,255,255))
pygame.draw.rect(window,(0,200,240),[15,15,570,370],5) #blue frame
pygame.draw.rect(window,(200,200,200),[35,115,120,250]) #grey settings box
pygame.draw.rect(window,(240,245,255),[175,90,385,275]) #drawing window

window.blit(brush_options,(35,90))
window.blit(brush_size,(45,125))
window.blit(brush_shape,(45,260))

pygame.draw.rect(window,(0,200,240),[45,150,45,45])
pygame.draw.rect(window,(0,200,240),[100,150,45,45])
pygame.draw.rect(window,(0,200,240),[45,205,45,45])
pygame.draw.rect(window,(0,200,240),[100,205,45,45])

pygame.draw.circle(window,(0,0,0),(68,173),2)
pygame.draw.circle(window,(0,0,0),(123,173),6)
pygame.draw.circle(window,(0,0,0),(68,228),9)
pygame.draw.circle(window,(0,0,0),(123,228),15)

for box in range (10): #set color boxes
    pygame.draw.rect(window,coList[box],[30+50*box,30,45,45])
pygame.draw.rect(window,(240,245,255),[530,30,45,45])

#functions here
def brushDraw(bColor,bSize,x,y):
    if x > 175+bSize and x < 560-bSize: #if in light blue box
        if y > 90+bSize and y < 365-bSize:
            #pygame.draw.rect(window,bColor,(x,y,bSize,bSize))
            pygame.draw.circle(window,bColor,(x,y),bSize)

def updateColor(x,y,co):
    if x >= 30 and x <= 580:
        if y >= 30 and y <= 75:
            x -= 30
            return int(x//50)
        else:
            return (co)
    else:
        return (co)

def updateSize(bSize,x,y):
    if x >= 45 and x <= 90 and y >= 150 and y <= 195: #small
        return 2
    elif x >= 100 and x <= 145 and y >= 150 and y <= 195: #med-small
        return 6
    elif x >= 45 and x <= 90 and y >= 205 and y <= 250: #med-big
        return 9
    elif x >= 100 and x <= 145 and y >= 205 and y <= 250: #big
        return 15
    else:
        return bSize
            
#Here is the actual program which will call the function       
while not done:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            
        elif event.type == pygame.QUIT:
            done = True

    if drawing:
        mouseX, mouseY = pygame.mouse.get_pos()
        
        brushDraw(bColor,bSize,mouseX,mouseY)
        
        co = updateColor(mouseX,mouseY,co)
        bColor = coList[co]

        bSize = updateSize(bSize,mouseX,mouseY)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
