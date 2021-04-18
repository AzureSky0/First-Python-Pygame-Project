import pygame
import sys
from pygame import mixer

clock=pygame.time.Clock()

pygame.init()
mixer.init()
mixer.music.load("Sounds/combatbg.wav")
mixer.music.play(-1)

pygame.display.set_caption("{[[[{   Level 2   }]]]}")
icon=pygame.image.load("Images/001-swords.png")
pygame.display.set_icon(icon)
screen=pygame.display.set_mode((800,700))



#background images
bgImg1=pygame.image.load("Images/forest_05.png")

Tree1Img=pygame.image.load("Images/003-tree-1.png")
Tree2Img=pygame.image.load("Images/002-tree.png")
Tree3Img=pygame.image.load("Images/001-tree-2.png")
wood1Img=pygame.image.load("Images/003-wood1.png")
wood2Img=pygame.image.load("Images/004-firewood1.png")
wood3Img=pygame.image.load("Images/005-logs1.png")
naturebg1Img=pygame.image.load("Images/001-pine-tree.png")
naturebg2Img=pygame.image.load("Images/002-mountains.png")
Thunder1Img= pygame.image.load("Images/002-lightning(1).png")
Thunder2Img= pygame.image.load("Images/001-lighting(1).png")






#clouds  and birds
cloudImg=pygame.image.load("Images/cloud1.png")
def cloud(x,y):
    screen.blit(cloudImg,(x,y))

cloudImg2=pygame.image.load("Images/cloud2.png")
cloudImg2=pygame.transform.scale2x(cloudImg2)
def cloud2(x,y):
    screen.blit(cloudImg2,(x,y))

cloudImg3=pygame.image.load("Images/cloud3.png")
cloudImg3=pygame.transform.scale2x(cloudImg3)
def cloud3(x,y):
    screen.blit(cloudImg3,(x,y)) 

birdImg1=pygame.image.load("Images/bird1.png")
birdImg2=pygame.image.load("Images/bird2.png")    
def bird1(x,y):
    screen.blit(birdImg1,(x,y))
def  bird2(x,y):
    screen.blit(birdImg2,(x,y))

#animals
animalImg1=pygame.image.load("Images/rabbit.png")
animalImg1=pygame.transform.scale2x(animalImg1)
animalImg2=pygame.image.load("Images/owl.png")
animalImg2=pygame.transform.scale2x(animalImg2)
def animal1(x,y):
    screen.blit(animalImg1,(x,y))
def animal2(x,y):
    screen.blit(animalImg2,(x,y))




#enemy Image

enemyImg="Images/character_1.png"
enemyImage=pygame.image.load(enemyImg)
enemy_rect=enemyImage.get_rect(topleft=(200,200))



#player Image
playerImg="Images/character_2.png"
playerImg2="Images/character_2_facing_left.png"
playerImage=pygame.image.load(playerImg)
playerImage2=pygame.image.load(playerImg2)
player_rect=playerImage.get_rect(topleft=(600,200))




#fireball Image
fireballImg=pygame.image.load("Images/001-fire.png")
fireballX=400
fireballY=400
fireball_position=0
fireball_positionY=0
fireballX_changed=0
fireballY_changed=0
fireball_state="ready"






# backgroind objects definitions:
def Tree1(x,y):
    screen.blit(Tree1Img,(x, y))

def Tree2(x,y):
    screen.blit(Tree2Img,(x, y))
def Tree3(x,y):
    screen.blit(Tree3Img,(x, y))

def wood1(x,y):
    screen.blit(wood1Img,(x, y))
def wood2(x,y):
    screen.blit(wood2Img,(x, y))
def wood3(x,y):
    screen.blit(wood3Img,(x, y))
def naturebg1(x,y):
    screen.blit(naturebg1Img,(x, y))
def naturebg2(x,y):
    screen.blit(naturebg2Img,(x, y))
def bgImage1(x,y):
    screen.blit(bgImg1,(x,y))







# game characters:
   
def enemy():
    global x_speed,y_speed,playerHealth,enemyHealth,enemyDamage
    screen.blit(enemyImage,enemy_rect)
    
    #enemy movement
    
    enemy_rect.right+=x_speed
    enemy_rect.top-=y_speed

    #collision with borders:
    if enemy_rect.right >=800 or enemy_rect.left <=0:
        x_speed*=-1
         
    if enemy_rect.bottom >= 700 or enemy_rect.top <=60:
        y_speed*=-1
    
    #collision with rect:
    collision_tolerance=180
    if enemy_rect.colliderect(player_rect):
        if abs(player_rect.top - enemy_rect.bottom) < collision_tolerance or abs(player_rect.bottom - enemy_rect.top) < collision_tolerance:
            y_speed*=-1
            sword_sound= mixer.Sound("Sounds/sword.wav")
            sword_sound.play()
            #Attack status
            if attacked==True:
                print("player attacked")
                playerDamage=30
                sword_sound= mixer.Sound("Sounds/sword.wav")
                sword_sound.play()
                #damage done
                enemyHealth-=playerDamage
            if defended==True:
                sheald_sound= mixer.Sound("Sounds/shield.wav")
                sheald_sound.play()
                print("player defended")
                playerHealth+=4
            enemyDamage=10    
            playerHealth-=enemyDamage            

        if abs(player_rect.left-enemy_rect.right) < collision_tolerance or abs(player_rect.right-enemy_rect.left) < collision_tolerance:
            x_speed*=-1
            
            sword_sound= mixer.Sound("Sounds/sword.wav")
            sword_sound.play()
            
            #Attack status
            if attacked==True:
                print("player attacked")
                playerDamage=20            
                sword_sound= mixer.Sound("Sounds/sword.wav")
                sword_sound.play()
                #damage done
                playerHealth-=enemyDamage
                enemyHealth-=playerDamage
            if defended==True:
                print("player defended")
                playerHealth+=5
        
    if abs(enemy_rect.left-fireball_position)<40 and abs(enemy_rect.bottom-fireball_positionY)<40 or abs(enemy_rect.right-fireball_position)<40 and abs(enemy_rect.top-fireball_positionY)<40  :
        
        if M_attacked==True:
            print("Fire attacked")
            playerM_Damage=50            
            sword_sound= mixer.Sound("Sounds/fire-burning.wav")
            sword_sound.play()
            enemyHealth-=playerM_Damage 
        
        
            



def player():
    global playerX_speed,playerY_speed
    screen.blit(playerImage,player_rect)

    #player movement
    player_rect.x+=playerX_speed
    player_rect.y+=playerY_speed
    if player_rect.right>=800 or player_rect.left <=0:
        playerX_speed *=-1
    if player_rect.bottom >= 700 or player_rect.top <=60:
        playerY_speed*=-1
    
def fireball(x,y):
    global fireball_state
    fireball_state="fire"
    screen.blit(fireballImg,(x,y))

    




#Health
enemyDamage=0
playerDamage=0 
playerHealth=500
enemyHealth=600

   

#Speeds
x_speed=5
y_speed=5
playerX_speed=0
playerY_speed=0



#main_loop
Rightfacing=True
Leftfacing=True
attacked=False
defended=False
M_attacked=False

#Score

font=pygame.font.Font("freesansbold.ttf",18)
textX=10
textY=10





def show_score(x,y):
    playerHealth_stats= "|"*int(playerHealth/10)
    enemyHealth_stats= "|"*int(enemyHealth/10)
    score =font.render(f"""P.Health : {playerHealth_stats}""",True,(225,225,225),(100,100,225))
    score2 =font.render(f"""E.Health: {enemyHealth_stats}""",True,(225,225,225),(100,100,225))
    screen.blit(score,(x,y)),screen.blit(score2,(x+380,y))





#for cloud and other animations
x1=100      #cloud
x2=600      #cloud
x3=10       #bird
x4=600      #bird
x5=10       #cloud
x6,y6=0,710 #rabbit
x7,y7=500,800 #owl





while True:

    screen.fill((70,70,250))
    
    bgImage1(1,268)
    bgImage1(200,268)
    bgImage1(1,50)
    bgImage1(200,50)
    bgImage1(200,-138)
    bgImage1(1,-138)


    #for movement in background of cloud.etc
    if x1 <=805 :           #cloud
        x1+=0.5
        if x1>=800:
            x1=10
    if x2 >=0 :             #cloud
        x2-=3
        if x2<=5:
            x2=800
    if x3 <=860:            #bird
        x3+=5
        if x3>=850:
            x3=0
    if x4 >=0 :             #bird
        x4-=2
        if x4<=5:
            x4=810
    if x5 <=805 :           #cloud
        x5+=1.5
        if x5>=800:
            x5=10
    if x6 <=100:            #rabbit
        x6+=1
        y6-=1
        if x6 >=70:
            x6+=2.5
            y6+=1
            if x6 >=98:
                x6=0
                y6=730
    if y7 >= 600:
        y7-=2
        x7+=0.5
        if y7 <= 680:
            y7+=1
            if y7<= 640:
                y7=790
                x7=500




    for event in pygame.event.get():
        
        #Health
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_speed=-6
                playerImg="Images/character_2_facing_left.png"
                playerImage=pygame.image.load(playerImg)
                Rightfacing=False
                Leftfacing=True

            if event.key==pygame.K_RIGHT:
                playerX_speed=6
                playerImg="Images/character_2.png"
                playerImage=pygame.image.load(playerImg)
                Leftfacing=False
                Rightfacing=True                

            if event.key==pygame.K_UP:
                playerY_speed=-6
            if event.key==pygame.K_DOWN:
                playerY_speed=6
            
            #command keys Down
            if event.key==pygame.K_a:
                if Rightfacing==True:
                    playerImg="Images/spartan sword.png"
                    playerImage=pygame.image.load(playerImg)
                    attacked=True
                if Leftfacing==True:
                    playerImg="Images/spartan sword_left.png"
                    playerImage=pygame.image.load(playerImg)
                    attacked=True
            if event.key==pygame.K_s:
                playerImg="Images/002-shield.png"
                playerImage=pygame.image.load(playerImg)
                defended=True
            if event.key==pygame.K_d:
                if Leftfacing==True:
                    playerImg="Images/001-lighting(1)_left.png"
                    playerImage=pygame.image.load(playerImg)
                    fireball_position=player_rect.x-50
                    M_attacked=True
                if Rightfacing==True:
                    playerImg="Images/001-lighting(1).png"
                    playerImage=pygame.image.load(playerImg)
                    fireball_position=player_rect.x+50
                    M_attacked=True
                fireball_positionY=player_rect.y
                fireball(fireball_position,fireball_positionY)
                
                
            if event.key==pygame.K_c:
                print(f"player: {player_rect.right}")
                print(f"enemy: {enemy_rect.right}")
                print(f"fire x: {fireballX} , fire y: {fireballY} ")

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                playerX_speed=0
            if event.key==pygame.K_RIGHT:
                playerX_speed=0
            if event.key==pygame.K_UP:
                playerY_speed=0
            if event.key==pygame.K_DOWN:
                playerY_speed=0
        
            #command keys Up
            if event.key==pygame.K_a:
                if Rightfacing==True:
                    playerImg="Images/character_2.png"
                    playerImage=pygame.image.load(playerImg)
                    attacked=False

                if Leftfacing==True:
                    playerImg="Images/character_2_facing_left.png"
                    playerImage=pygame.image.load(playerImg)
                    attacked=False
            if event.key==pygame.K_s:
                if Rightfacing==True:
                    playerImg="Images/character_2.png"
                    playerImage=pygame.image.load(playerImg)
                    defended=False
                if Leftfacing==True:
                    playerImg="Images/character_2_facing_left.png"
                    playerImage=pygame.image.load(playerImg)
                    defended=False
            if event.key==pygame.K_d:
                if Rightfacing==True:
                    playerImg="Images/character_2.png"
                    playerImage=pygame.image.load(playerImg)
                    M_attacked=False
                    fireball_state=""
                if Leftfacing==True:
                    playerImg="Images/character_2_facing_left.png"
                    playerImage=pygame.image.load(playerImg)
                    M_attacked=False
                    fireball_state=""
        
        if event.type==pygame.QUIT :
            import origin_project_Thankyou
            pygame.quit()
            
        #gameover
        if enemyHealth<1:
            print("Game over You Won....'>-<'")
            pygame.quit()
            import you_won
            sys.exit()
            
        if playerHealth<0:
            print("Game over You Lost...>..<")
            pygame.quit()
            import you_lost
            sys.exit()
            

    
    print(f"player health: {playerHealth}   enemy health: {enemyHealth}")    
    
    if enemy_rect.right<=450:
        print("left")
        enemyImg="Images/character_1.png"
        enemyImage=pygame.image.load(enemyImg)
        

    if enemy_rect.right>450:
        print("right")
        enemyImg="Images/character_1_facing_left.png"
        enemyImage=pygame.image.load(enemyImg)

    #player movement    
    player_rect.x+=playerX_speed
    player_rect.y+=playerY_speed
     
    #fire movement
    if fireball_state is "fire" and Leftfacing==True and fireball_state != "":
        fireball_positionY=player_rect.y
        fireball(fireball_position,fireball_positionY)
        
        fireball_position-=20
    if fireball_state is "fire" and Rightfacing==True and fireball_state != "" :
        fireball(fireball_position,player_rect.y)
        fireball_position+=20    
    
#calling background image before charactor
    naturebg1(-17,28),naturebg1(1,34),naturebg2(25,34),naturebg1(49,34),naturebg2(73,34),naturebg1(95,34),naturebg2(120,34),naturebg1(145,34),naturebg2(175,34),naturebg1(200,34),naturebg2(225,34),naturebg1(250,34),naturebg2(275,34),naturebg1(300,34),naturebg2(325,34),naturebg1(350,34),naturebg2(375,34),naturebg1(400,34),naturebg2(425,34),naturebg1(450,34),naturebg2(475,34),naturebg1(500,34),naturebg2(525,34),naturebg1(550,34),naturebg2(575,34),naturebg1(600,34),naturebg2(625,48),naturebg1(650,48),naturebg2(675,48),naturebg1(700,48),naturebg2(725,48),naturebg1(750,48),naturebg2(775,48),naturebg1(800,48),naturebg2(825,48),naturebg1(850,48),naturebg2(875,48),naturebg1(900,48),naturebg2(925,48),naturebg1(950,48),naturebg2(975,48),naturebg1(1000,48),naturebg2(1025,48)

    naturebg1(-17,48),naturebg1(1,48),naturebg2(25,48),naturebg1(49,48),naturebg2(73,48),naturebg1(95,48),naturebg2(120,48),naturebg1(145,48),naturebg2(175,48),naturebg1(200,48),naturebg2(225,48),naturebg1(250,48),naturebg2(275,48),naturebg1(300,48),naturebg2(325,48),naturebg1(350,48),naturebg2(375,48),naturebg1(400,48),naturebg2(425,48),naturebg1(450,48),naturebg2(475,48),naturebg1(500,48),naturebg2(525,48),naturebg1(550,48),naturebg2(575,48),naturebg1(600,48),naturebg2(625,48),naturebg1(650,48),naturebg2(675,48),naturebg1(700,48),naturebg2(725,48),naturebg1(750,48),naturebg2(775,48),naturebg1(800,48),naturebg2(825,48),naturebg1(850,48),naturebg2(875,48),naturebg1(900,48),naturebg2(925,48),naturebg1(950,48),naturebg2(975,48),naturebg1(1000,48),naturebg2(1025,48)

    Tree1(-10,70),Tree1(-30,60),Tree1(0,70),Tree1(30,68),Tree1(60,60),Tree1(70,55),Tree1(90,70),Tree1(100,73),Tree1(110,70),Tree1(130,68),Tree1(160,60),Tree1(180,60),Tree1(190,70),Tree1(210,55),Tree1(240,55),Tree1(230,70),Tree1(260,70),Tree1(270,55),Tree1(290,60),Tree1(300,55),wood3(50,110),Tree1(310,70),Tree1(330,70),Tree1(360,70),Tree1(380,55),Tree1(390,60),Tree1(410,55),Tree1(440,60),Tree1(460,70),wood2(480,68),Tree1(480,70),Tree1(500,55),Tree1(520,60),Tree1(560,55),Tree1(580,70),   
    cloud(x1,20)
    bird2(x4,20)
    cloud2(x2,30)
    bird1(x3,40)
    cloud3(x5,43)

    #calling the charactor function
    enemy()
    player()


#calling background image after charactor
    Tree3(-30,580),Tree3(-25,600),Tree3(-15,620),Tree3(-20,640),Tree2(-15,600),Tree3(-15,630),Tree3(-10,620),Tree3(-5,620),Tree2(0,650),Tree3(30,650),Tree2(35,650),Tree3(60,650),Tree3(70,650),Tree3(90,650),Tree2(120,650),Tree3(150,650),Tree3(190,650),Tree2(220,650),Tree3(250,650),Tree3(290,650),animal2(x7-300,y7),Tree2(320,650),Tree3(350,650),Tree3(390,650),Tree2(420,650),Tree3(450,650),Tree2(250,650),Tree3(490,650),Tree2(420,650),Tree3(450,650),Tree3(490,650),Tree2(420,650),Tree3(450,650),Tree3(490,650),Tree2(520,650),animal2(x7,y7),Tree2(570,625),Tree3(550,650),Tree3(590,650),Tree2(620,650),Tree3(650,650),Tree3(690,650),Tree2(720,650),Tree2(770,625),Tree3(750,650)
    animal1(x6,y6),animal1(x6+300,y6),animal1(x6+600,y6)
    
    show_score(textX,textY)
    pygame.display.flip()
    clock.tick(60)