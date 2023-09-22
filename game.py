import pygame
import sys
from pygame import * 
import time


class Player:
    def __init__(self,name,cord_x, cord_y):
        self.name = name
        self.cord_x = cord_x
        self.cord_y = cord_y
        print(f"{self.name} initiated")
        
        
character1 = Player("Hassan", cord_x=300,cord_y=200)
character2 = Player("Soham", cord_x=800,cord_y=200)
print(character1.cord_x)    
        
 
 
def collision(x,y):
    if abs(x-y) < 150:
        return True
    else:
        return False
    
        
# all the images are loaded in this function
def load_image(): 
    
    # ######## Raw Images 
    bg_raw = pygame.image.load("bg.png");
    char1_raw = pygame.image.load("characters/hassan/hassan-1.png");
    char1_raw_punch = pygame.image.load("characters/hassan/hassan-2.png");

    char2_raw = pygame.transform.flip(pygame.image.load("characters/soham/soham-1.png"),True,False);
    char2_raw_punch = pygame.transform.flip(pygame.image.load("characters/soham/soham-2.png"), True,False);

    # ######## Raw Images 
    bg = pygame.transform.scale(bg_raw,(1280,720))
    char1 = pygame.transform.scale(char1_raw,(112,400))
    char1_punch = pygame.transform.scale(char1_raw_punch,(237,400))
    
    char2 = pygame.transform.scale(char2_raw,(137,400))
    char2_punch = pygame.transform.scale(char2_raw_punch,(281,400))
    
    image_dictionary = {
        "bg": bg,
        "character1" : char1,
        "character1_punch" : char1_punch,
        "character2" : char2,
        "character2_punch" : char2_punch,
    }
    return image_dictionary
    
    
    
    
def init():
    pygame.init();
    pygame.font.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock();
    first_character_punch = False
    second_character_punch = False

    while True:

        img_dictionary = load_image()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    first_character_punch = True
                
                
                    
                if event.key==pygame.K_LEFT:
                    if character1.cord_x >15:
                        character1.cord_x -=25;
                    character1.cord_x;
                        
                        
                if event.key==pygame.K_DOWN:
                    pass
                if event.key==pygame.K_RIGHT:
                    if character1.cord_x >1150 or collision(character2.cord_x,character1.cord_x):
                        pass
                    else:
                        character1.cord_x += 25;
                
                
                # second character
                
                if event.key==pygame.K_w:
                    second_character_punch = True
                if event.key==pygame.K_s:
                    pass
                if event.key==pygame.K_a:
                    if character2.cord_x >15:
                        if not collision(character2.cord_x,character1.cord_x):
                            character2.cord_x -=25
                    character2.cord_x;
                    
                if event.key==pygame.K_d:
                    if character2.cord_x >1150:
                        pass
                    else:
                        character2.cord_x += 25;
                    character2.cord_x;            
                    
            
        
        
            
        
        #within for loop   
        
        screen.blit(img_dictionary["bg"],(0,0))
        if first_character_punch:
            screen.blit(img_dictionary["character1_punch"], (character1.cord_x,character1.cord_y))
            first_character_punch=False;
        else:    
            screen.blit(img_dictionary["character1"], (character1.cord_x,character1.cord_y))

        # second player logic
        if second_character_punch:
            screen.blit(img_dictionary["character2_punch"], (character2.cord_x-45,character2.cord_y))
            second_character_punch=False;
        else:    
            screen.blit(img_dictionary["character2"], (character2.cord_x,character2.cord_y))
            
        
        

        pygame.display.flip()
 
        
            
init()