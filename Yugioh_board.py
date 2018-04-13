import pygame
import time
import yugioh


x = pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
tan = (210,150,90)
 
display_width = 1250
display_height = 950
box_size1 = 110
box_size2 = 140

FPS = 60
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('YUGIOH')

font = pygame.font.SysFont(None,50)
                
def message_to_screen(msg,color,x_cor,y_cor):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[x_cor,y_cor])

class box_draw():

    def __init__(self,color,locx,locy,size1,size2,gd):
        self.locx = locx
        self.locy = locy
        self.color = color
        self.size1 = size1
        self.size2 = size2
        self.filled = False
        self.loc = (locx,locy)
        self.gd = gd
        self.internal = None
        pygame.draw.rect(self.gd, self.color, [self.locx,self.locy,self.size1,self.size2],2)

    def redraw(self):
        
        if self.internal == None:
            pygame.draw.rect(self.gd, self.color, [self.locx,self.locy,self.size1,self.size2],2) 
        else:
            pygame.draw.rect(self.gd, self.color, [self.locx,self.locy,self.size1,self.size2],2)
            self.internal.draw_itself(self.loc,self.gd)
        

class hand_card():

    def __init__(self,locx,locy,gd):
        self.locx = locx
        self.locy = locy
        self.loc = (locx,locy)
        gd.blit(bImg,self.loc)

def hand_deck_shuffle(list1,list2,gd1):

    if len(list2)>=5:
        for i in range(len(list1)):
            if list1[i].filled==True:
                pass
            else:
                list1[i].internal = list2[i]
                list1[i].filled = True
                list1[i].internal.draw_itself(list1[i].loc,gd1)
            print(i)
            print(list1[i].loc)
            
    elif len(list2)<5 and len(list2)>0:
        for j in range(len(list2)):
            for i in range(len(list1)):
                if list1[i].filled==True:
                    pass
                else:
                    list1[i].filled = True
                    list1[i].internal = list2[j]
                    list1[i].internal.draw_itself(list1[i].loc,gd1)
                    


Yugi_box=[]
Kaiba_box=[]


b1 = box_draw(tan,445,160,box_size1,box_size2,gameDisplay)
b2 = box_draw(tan,575,160,box_size1,box_size2,gameDisplay)
b3 = box_draw(tan,705,160,box_size1,box_size2,gameDisplay)
b4 = box_draw(tan,445,310,box_size1,box_size2,gameDisplay)
b5 = box_draw(tan,575,310,box_size1,box_size2,gameDisplay)
b6 = box_draw(tan,705,310,box_size1,box_size2,gameDisplay)

b7 = box_draw(tan,445,500,box_size1,box_size2,gameDisplay)
b8 = box_draw(tan,575,500,box_size1,box_size2,gameDisplay)
b9 = box_draw(tan,705,500,box_size1,box_size2,gameDisplay)
b10 = box_draw(tan,445,650,box_size1,box_size2,gameDisplay)
b11 = box_draw(tan,575,650,box_size1,box_size2,gameDisplay)
b12 = box_draw(tan,705,650,box_size1,box_size2,gameDisplay)

h1 = box_draw(red,315,10,box_size1,box_size2,gameDisplay)
h2 = box_draw(red,445,10,box_size1,box_size2,gameDisplay)
h3 = box_draw(red,575,10,box_size1,box_size2,gameDisplay)
h4 = box_draw(red,705,10,box_size1,box_size2,gameDisplay)
h5 = box_draw(red,835,10,box_size1,box_size2,gameDisplay)

Yugi_bf=[b1,b2,b3,b4,b5,b6]
Kaiba_bf=[b7,b8,b9,b10,b11,b12]

def intro():

    img = pygame.image.load("Yugi1.png")
    img = pygame.transform.scale(img, (display_width, display_height))

    bImg = pygame.image.load("yugioh_back.jpg")
    bImg = pygame.transform.scale(bImg, (box_size1, box_size2))

    gImg = pygame.image.load("graveyard.jpg")
    gImg = pygame.transform.scale(gImg, (box_size1+50, box_size2+50))
    gImg = pygame.transform.rotate(gImg,180)

    dImg = pygame.image.load("yugioh_back.jpg")
    dImg = pygame.transform.scale(dImg, (box_size1+50, box_size2+50))

    yugiImg = pygame.image.load("yugimoto.jpg")
    yugiImg = pygame.transform.scale(yugiImg, (box_size1*2, box_size2*2))

    kaibaImg = pygame.image.load("setokaiba.png")
    kaibaImg = pygame.transform.scale(kaibaImg, (box_size1*2, box_size2*2))
       
    gameDisplay.blit(img,(0,0))

    gameDisplay.blit(gImg,(240,550))
    gameDisplay.blit(pygame.transform.rotate(gImg,180),(240,200))

    gameDisplay.blit(dImg,(50,200))
    gameDisplay.blit(dImg,(50,550))

    gameDisplay.blit(yugiImg,(970,130))
    gameDisplay.blit(kaibaImg,(970,510))



    b1 = box_draw(tan,445,160,box_size1,box_size2,gameDisplay)
    b2 = box_draw(tan,575,160,box_size1,box_size2,gameDisplay)
    b3 = box_draw(tan,705,160,box_size1,box_size2,gameDisplay)
    b4 = box_draw(tan,445,310,box_size1,box_size2,gameDisplay)
    b5 = box_draw(tan,575,310,box_size1,box_size2,gameDisplay)
    b6 = box_draw(tan,705,310,box_size1,box_size2,gameDisplay)

    b7 = box_draw(tan,445,500,box_size1,box_size2,gameDisplay)
    b8 = box_draw(tan,575,500,box_size1,box_size2,gameDisplay)
    b9 = box_draw(tan,705,500,box_size1,box_size2,gameDisplay)
    b10 = box_draw(tan,445,650,box_size1,box_size2,gameDisplay)
    b11 = box_draw(tan,575,650,box_size1,box_size2,gameDisplay)
    b12 = box_draw(tan,705,650,box_size1,box_size2,gameDisplay)

    h1 = box_draw(red,315,10,box_size1,box_size2,gameDisplay)
    h2 = box_draw(red,445,10,box_size1,box_size2,gameDisplay)
    h3 = box_draw(red,575,10,box_size1,box_size2,gameDisplay)
    h4 = box_draw(red,705,10,box_size1,box_size2,gameDisplay)
    h5 = box_draw(red,835,10,box_size1,box_size2,gameDisplay)

    if len(Yugi_box)==0:
        Yugi_box.append(h1)
        Yugi_box.append(h2)
        Yugi_box.append(h3)
        Yugi_box.append(h4)
        Yugi_box.append(h5)
    
    h6 = box_draw(red,315,800,box_size1,box_size2,gameDisplay)
    h7 = box_draw(red,445,800,box_size1,box_size2,gameDisplay)
    h8 = box_draw(red,575,800,box_size1,box_size2,gameDisplay)
    h9 = box_draw(red,705,800,box_size1,box_size2,gameDisplay)
    h10 = box_draw(red,835,800,box_size1,box_size2,gameDisplay)

    if len(Kaiba_box)==0:
        Kaiba_box.append(h6)
        Kaiba_box.append(h7)
        Kaiba_box.append(h8)
        Kaiba_box.append(h9)
        Kaiba_box.append(h10)
    
    b23 = box_draw(tan,970,130,box_size1*2,box_size2*2,gameDisplay)
    b24 = box_draw(tan,970,510,box_size1*2,box_size2*2,gameDisplay)

    b25 = box_draw(white,970,410,box_size1*2,50,gameDisplay)
    b26 = box_draw(white,970,790,box_size1*2,50,gameDisplay)

    ##b27 = hand_card(315,10,gameDisplay)
    ##b28 = hand_card(445,10,gameDisplay)
    ##b29 = hand_card(575,10,gameDisplay)
    ##b30 = hand_card(705,10,gameDisplay)
    ##b31 = hand_card(835,10,gameDisplay)
    ##
    ##b32 = hand_card(315,800,gameDisplay)
    ##b33 = hand_card(445,800,gameDisplay)
    ##b34 = hand_card(575,800,gameDisplay)
    ##b35 = hand_card(705,800,gameDisplay)
    ##b36 = hand_card(835,800,gameDisplay)

    message_to_screen("points:" + str(yugioh.Yugi_life),black,980,420)
    message_to_screen("points:" + str(yugioh.Kaiba_life),black,980,800)

    

    pygame.display.update()


def update_game():

    intro()
    
    for k in range(len(Yugi_box)):
        Yugi_box[k].redraw()
    for k in range(len(Kaiba_box)):
        Kaiba_box[k].redraw()
    for k in range(len(Yugi_bf)):
        Yugi_bf[k].redraw()
    for k in range(len(Kaiba_bf)):
        Kaiba_bf[k].redraw()
        
def gameloop():
    YugiTurn = True
    intro()
    pygame.mixer.music.load('score1.mp3')
    pygame.mixer.music.play(15)
    gameExit = False
    
    while not gameExit:

        update_game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hand_deck_shuffle(Yugi_box,yugioh.Yugi,gameDisplay)

                if event.key == pygame.K_k:
                    hand_deck_shuffle(Kaiba_box,yugioh.Kaiba,gameDisplay)
                    YugiTurn = True
                        
                if event.key == pygame.K_1:
                    Yugi_box[0].internal.draw_itself(Yugi_bf[0].loc, gameDisplay)
                    Yugi_bf[0].internal = Yugi_box[0].internal
                    Yugi_box[0].internal = None 
                    

        clock.tick(FPS)
        pygame.display.update()
        
    pygame.quit()
    quit()

gameloop()

