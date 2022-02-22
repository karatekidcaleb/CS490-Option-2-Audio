import pygame
import random
import time
from tuning import Tuning
import usb.core
import usb.util
import time
import math

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
Mic_tuning = Tuning(dev)
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    bgd_image = pygame.image.load("bgd_image.png")
     
    screen_width = 480
    screen_height = 480
    # create a surface on screen that has the size of 240 x 240
    screen = pygame.display.set_mode((screen_width,screen_height))
    image = [pygame.image.load("logo32x32.png"), pygame.image.load("logo32x32.png")]
    font = pygame.font.SysFont("monospace", 20)
    label = font.render("Dog", 1, (36, 36, 0))
    labels = [label, label]
    
     
    # define a variable to control the main loop
    running = True
    posx = [50, 175]
    posy = [150, 76]
    trackedEntityNum=2
    # main loop
    while running:
        time.sleep(0.1)
        #print (Mic_tuning.direction)
        image[0].set_colorkey((255,255,255))
        screen.blit(bgd_image, (0,0))
        for N in range(0, trackedEntityNum):
            posx[N] = posx[N] + random.randint(-3, 3)#(math.cos(Mic_tuning.direction) * screen_width/2) + screen_width/2 - 16
            posy[N] = posy[N] #(math.sin(Mic_tuning.direction) * screen_height/2) + screen_height/2 - 16
            screen.blit(image[N], (posx[N],posy[N]))
            screen.blit(labels[N], (posx[N]-10,posy[N]-20))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.flip()
        
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()