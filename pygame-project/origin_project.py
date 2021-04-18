Selected1=False
Selected2=False


import pygame
from pygame import mixer
mixer.init()
#Adding background music
mixer.music.load("Sounds/skyloft.wav")
mixer.music.play(0)

#for initialization of pygame
pygame.init()

#create the screen
screen= pygame.display.set_mode((700,500))


#Title and icon

pygame.display.set_caption("Charactor INFO")
icon=pygame.image.load("Images/001-swords.png")
pygame.display.set_icon(icon)

#background image
bgImg=pygame.image.load("Images/forest_02.png")

#charactor 1

charactor1Img= pygame.image.load("Images/character_1.png")
charactor1X=40
charactor1Y=100
charactor1X_changed=0

charactor2Img= pygame.image.load("Images/character_2_facing_left.png")
charactor2X=380
charactor2Y=100
charactor2X_changed=0

def charactor1(x, y):
    screen.blit(charactor1Img,(x, y))                       #blit-to drawing something in the screen  
                                                            #screen also known as surface 
def charactor2(x1,y1):
    screen.blit(charactor2Img,(x1,y1))

def bgImage(x,y):
    screen.blit(bgImg,(x,y))



    





#Game loops \\Important\\

running=True
while running:
    
    
    
    # screen colour
    screen.fill((0,0,200))
    bgImage(-90,-90)
    #Charactor movement
    for event in pygame.event.get():
        charactor2X+=charactor2X_changed
        charactor1X+=charactor1X_changed
        if event.type==pygame.KEYDOWN:
            print(event.type)
            if event.key== pygame.K_LEFT:
                print("Left Arrow is pressed")
                print(charactor1X)
                charactor1Img=pygame.image.load("Images/001-knight1.png")
                Selected1=True
                Selected2=False
                selectedsound=mixer.Sound("Sounds/selection.wav")
                selectedsound.play()

                pygame.display.update()    
                   
                    


            if event.key== pygame.K_RIGHT:
                print("Right Arrow is pressed")
                print(charactor2X)
                charactor2Img=pygame.image.load("Images/002-helmet1.png")
                
                Selected2=True
                Selected1=False   
                selectedsound=mixer.Sound("Sounds/selection.wav")
                selectedsound.play()
                pygame.display.update()

            
            if event.key== pygame.K_KP_ENTER:
                print("enter is pressed")
                
            if event.key== pygame.K_SPACE and Selected1 and Selected2 is False:    
                print("SpaceBar is pressed with left")
                pygame.display.quit()
                running=False
                import Game_Trial_Rect_imag_1_part_4
                Selected1=False
                


            if event.key== pygame.K_SPACE and Selected2 and Selected1 is False:    
                print("SpaceBar is pressed with right ") 
                pygame.display.quit()
                running=False
                
                import Game_Trial_Rect_imag_1_part_4
                Selected2=False
                
                

        if event.type== pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT :
                charactor1Img=pygame.image.load("Images/character_1.png")   
                charactor2Img=pygame.image.load("Images/character_2_facing_left.png")   

                pygame.display.update()

            
            
        
        if event.type==pygame.QUIT:
            print(event)
            print("player exited the game")
            
            running=False
            import origin_project_Charactor_stats_info
            

    #print(charactor1X)
    
    charactor1(charactor1X,charactor1Y)
    charactor2(charactor2X,charactor2Y) 
    pygame.display.update()            
        


    
        
        
        
    

