import sys

import pygame

from pygame.locals import *
import time
file1 = open("output.txt","w") 
timeout = time.time() + 60 * 5   # 5 minutes from now

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())
    file1.write(joystick.get_name()+'\n')

my_square = pygame.Rect(50, 50, 50, 50)
my_square_color = 0
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
motion = [0, 0]
firsttime=True
min_axis_0=0
max_axis_0=0
min_axis_1=0
max_axis_1=0
min_axis_2=0
max_axis_2=0
min_axis_3=0
max_axis_3=0
while True:
    """
    if time.time() > timeout:
        file1.close()
        break
    """
    

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, colors[my_square_color], my_square)
    if abs(motion[0]) < 0.1: # if the object moves without touch the joystick increases this number
        motion[0] = 0
    if abs(motion[1]) < 0.1: # if the object moves without touch the joystick increases this number
        motion[1] = 0
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)
            file1.write(str(event)+'\n')
            if event.button == 0:
                my_square_color = (my_square_color + 1) % len(colors)
        if event.type == JOYBUTTONUP:
            print(event)
            file1.write(str(event)+'\n')
        if event.type == JOYAXISMOTION:
            print(event)
            file1.write(str(event)+'\n')
            if event.axis == 0:
                if firsttime == True:
                    min_axis_0 = event.value
                    max_axis_0 = event.value
                if firsttime == False:
                    if event.value < min_axis_0:
                        min_axis_0 = event.value
                    if event.value > max_axis_0:
                        max_axis_0 = event.value
            if event.axis == 1:
                if firsttime == True:
                    min_axis_1 = event.value
                    max_axis_1 = event.value
                if firsttime == False:
                    if event.value < min_axis_1:
                        min_axis_1 = event.value
                    if event.value > max_axis_1:
                        max_axis_1 = event.value
            if event.axis == 2:
                if firsttime == True:
                    min_axis_2 = event.value
                    max_axis_2 = event.value
                if firsttime == False:
                    if event.value < min_axis_2:
                        min_axis_2 = event.value
                    if event.value > max_axis_2:
                        max_axis_2 = event.value
            if event.axis == 3:
                if firsttime == True:
                    min_axis_3 = event.value
                    max_axis_3 = event.value
                if firsttime == False:
                    if event.value < min_axis_3:
                        min_axis_3 = event.value
                    if event.value > max_axis_3:
                        max_axis_3 = event.value
            if event.axis == 4:
                if firsttime == True:
                    min_axis_4 = event.value
                    max_axis_4 = event.value
                if firsttime == False:
                    if event.value < min_axis_4:
                        min_axis_4 = event.value
                    if event.value > max_axis_4:
                        max_axis_4 = event.value


            if event.axis < 2:
                motion[event.axis] = event.value
            
            if event.axis >= 2:
                #motion[event.axis-2] = event.value
                if abs(event.value)>0.5:
                    my_square_color = (my_square_color + 1) % len(colors)
        if event.type == JOYHATMOTION:
            if event.value==(0,1):
                my_square_color = (my_square_color + 1) % len(colors)
            print(event)
            file1.write(str(event)+'\n')
        if event.type == JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
                file1.write(joystick.get_name()+'\n')
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        if firsttime == True:
            firsttime = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: #escape 
                print("min_axis_0",min_axis_0)
                print("max_axis_0",max_axis_0)
                print("min_axis_1",min_axis_1)
                print("max_axis_1",max_axis_1)
                print("min_axis_2",min_axis_2)
                print("max_axis_2",max_axis_2)
                print("min_axis_3",min_axis_3)
                print("max_axis_3",max_axis_3)
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)
