import random
import pygame

Yugi=[]
Kaiba=[]
Yugi_graveyard=[]
Yugi_graveyard=[]
Yugi_hand=[]
Kaiba_hand=[]

Yugi_life=2000
Kaiba_life=2000

class yugi_cards:

    def __init__(self,name,category,attack,defense,loc):
        self.category=category
        self.name = name
        self.attack = attack
        self.defense = defense        
        self.img = pygame.image.load(loc)
        self.imgB = pygame.image.load("yugioh_back.jpg")
        self.img = pygame.transform.scale(self.img, (110, 140))
        self.imgB = pygame.transform.scale(self.imgB, (110, 140))
        Yugi.append(self)

    def draw_itself(self,loc1,gd):
        self.loc1 = loc1
        gd.blit(self.img,loc1)
        
        
        
##    def spell(self):
##        if category=="s":
        


class kaiba_cards:

    def __init__(self,name,category,attack,defense,loc):
        self.category=category
        self.name=name
        self.attack=attack
        self.defense=defense
        self.img = pygame.image.load(loc)
        self.imgB = pygame.image.load("yugioh_back.jpg")
        self.img = pygame.transform.scale(self.img, (110, 140))
        self.imgB = pygame.transform.scale(self.imgB, (110, 140))
        self.filled = False
        Kaiba.append(self)

    def draw_itself(self,loc1,gd):
        self.loc1 = loc1
        gd.blit(self.img,loc1)

##    def spell(self):
##        if category=="s":
    

#Yugi's Deck
Dark_Magician = yugi_cards("Dark Magician","m",2500,2100,"darkmagician.jpg")

Summoned_Skull = yugi_cards("Summoned Skull","m",2500,1200,"summonedskull.jpg")

Gaia_The_Fierce_knight = yugi_cards("Gaia the fierce knight","m",2300,2100,"gaiaknight.jpg")

Curse_Of_Dragon = yugi_cards("Curse of Dragon","m",2000,1500,"curseofdrag.jpg")

Celtic_Guardian = yugi_cards("Celtic Guardian","m",1400,1200,"celticguardian.jpg")

Beaver_Warrior = yugi_cards("Beaver Warrior","m",1200,1500,"beaver.jpg")

Mystical_Elf = yugi_cards("Mystical Elf","m",800,2000,"mysticalelf.jpg")

Koumori_Dragon = yugi_cards("Koumori Dragon","m",1500,1200,"koumori.jpg")

Great_White = yugi_cards("Great White","m",1600,800,"greatwhite.jpg")
                    
Blue_Eyes_White_Dragon = yugi_cards("Blue Eyes White Dragon","m",3000,2500,"blueeyes.jpg")

##Kaiba's Deck.

Blue_Eyes_White_Dragon_1 = kaiba_cards("Blue Eyes White Dragon","m",3000,2500,"blueeyes.jpg")

Blue_Eyes_White_Dragon_2 = kaiba_cards("Blue Eyes White Dragon","m",3000,2500,"blueeyes.jpg")

Grappler = kaiba_cards("Grappler","m",1300,1200,"grappler.jpg")

Dark_Zorla = kaiba_cards("Dark Zorla","m",2050,1000, "dark_zorla.jpg")

Gremlin = kaiba_cards("Gremlin","m",2000,1000, "gremlin.jpg")

Hitotsu_Me_Giant = kaiba_cards("Hitotsu-Me Giant","m",1200,1000, "HitotsuMeGiant.png")

Ryu_Kishin = kaiba_cards("Ryu-Kishin","m",1600,1200, "ryu-kishin.jpg")

Saggi_the_Dark_Clown = kaiba_cards("Saggi the Dark Clown","m",600,1500,"saggi.png")

Battle_Ox = kaiba_cards("Battle Ox","m",1700,1000,"BattleOx.png")

Giant_Soldier_Of_Stone = kaiba_cards("Giant Soldier Of Stone","m",1300,2000,"soldierstone.jpg")



random.shuffle(Yugi)
random.shuffle(Kaiba)

##
##for i in range(5):
##    y=Yugi.pop(0)
##    Yugi_hand.append(y)
##for i in range(5):
##    y=Kaiba.pop(0)
##    Kaiba_hand.append(y)

