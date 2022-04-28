import py
import pygame
import math
import time
import LocalizationProject.Localization
 
# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo70x70.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    bgd_image = pygame.image.load("bgd_image.png")
     
    screen_width = 720
    screen_height = 720
    bgd_image = pygame.transform.scale(bgd_image, (screen_width, screen_height))
    # create a surface on screen that has the size of 240 x 240
    screen = pygame.display.set_mode((screen_width,screen_height))
    image = pygame.image.load("logo70x70.png")
    stockfoto = pygame.image.load("stockMic.png")
    stockfoto.set_colorkey((255,255,255))
    
     
    # define a variable to control the main loop
    running = True
    pos = [0,0]
    
        
    # main loop
    while running:
        image.set_colorkey((255,255,255))
        screen.blit(bgd_image, (0,0))
        time.sleep(0.1)
        
        myfont = pygame.font.SysFont("monospace", 15)

        # render text
        label = myfont.render("Air Conditioning", 1, (255,255,0))
        
        '''
        try:
            file1 = open('CoordinateOutputs.txt', 'r')
        except IOError:
            print("File has opened already.")
        Lines = file1.readlines()
        file1.close()
 
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            pos[count-1] = line.strip()
            
            
        '''
        
        pos = localization()
        print(pos[0])
        print(int(float(pos[0])*50))
        pos[0] = int(float(pos[0])*50)
        pos[1] = int(float(pos[1])*50)
        #posx = (int(lines[0])*0.01745329) * screen_width/2 + screen_width/2 - 16
        #posy = (math.sin(int(lines[1]*0.01745329)) * screen_height/2) + screen_height/2 - 16
        screen.blit(image, (pos[0]+(screen_width/2),pos[1]+(screen_height/2)))
        screen.blit(label, (pos[0]+(screen_width/2),pos[1]+(screen_height/2)))
        screen.blit(stockfoto, ((screen_width/2)-60, (screen_height/2)-57))
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