import pygame

#for initialization of pygame
pygame.init()

 
#creating a screen 

screen2= pygame.display.set_mode((600,400))          #adding an another window
pygame.display.set_caption("Selected Charactor info")
icon=pygame.image.load("Images/001-swords.png")
pygame.display.set_icon(icon) 

bgImg3=pygame.image.load("Images/island1280.png")
bgImg4=pygame.image.load("Images/001-thank-you.png")
bgImg5=pygame.image.load("Images/001-boy.png")
bgImg6=pygame.image.load("Images/002-girl.png")


def bgImage3(x,y):
    screen2.blit(bgImg3,(x,y))
def bgImage4(x,y):
    screen2.blit(bgImg4,(x,y))
def bgImage5(x,y):
    screen2.blit(bgImg5,(x,y))
def bgImage6(x,y):
    screen2.blit(bgImg6,(x,y))

running2=True




while running2:
    screen2.fill((0,191,255))      #second window screen colour  
    bgImage3(-30,-50)
    bgImage4(360,180)
    bgImage5(220,100)
    bgImage6(280,100)
    for event1 in pygame.event.get():
                    
        if event1.type==pygame.QUIT:
            pygame.display.quit()
            running2=False
            print("player exited the game2")

    pygame.display.update()           
            
