import pygame
import sys
from pygame import *
import time;

tan_health = 100;
has_health = 100;

# Initialize Pygame
pygame.init()
pygame.display.set_caption('GameBox')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
# assigning values to X and Y variable
X = 200
Y = 200
# tan_health = 100;
# has_health = 100;
##############  TEXT  Starts from here #######################
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render(f'Tanjim : {tan_health}', True, green, blue)
textRect = text.get_rect()
textRect.center = (100, 20)

text2 = font.render(f'Hassan : {has_health}', True, green, blue)
text2Rect = text2.get_rect()
text2Rect.center = (600, 20)


# pygame.mixer.music.load("music/bg.mp3")
# pygame.mixer.music.load("effects/has-punch.mp3")
# pygame.mixer.music.load("effects/tan-punch.mp3")

# pygame.mixer.music.play()
first_char = True;
second_char = True;

# res VARS
screen_width = 700
screen_height = 399
char1_x,char1_y = 400,200;
char2_x,char2_y = 200,200;


# Load the background image
bg_img_path = "bg.png"
background_image = pygame.image.load(bg_img_path)

################# char1 starts here 
char = pygame.image.load("char1/img-3.png")
# punch image
char_punch = pygame.image.load("char1/img-1.png")
################# char1 end here 

char2 = pygame.image.load("char1/img-tan-1.png")
window = pygame.display.set_mode((screen_width, screen_height))





# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      # ################## logic for the first character ##################
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            first_char=True;
            if char1_x <15:
               char1_x -=0
            else:
               char1_x -=15;
          elif event.key == pygame.K_RIGHT:
             first_char=True;
             if char1_x>600:
                char1_x +=0
             else:
                char1_x +=15;
          elif event.key == pygame.K_UP:
             tan_health -=0;
             first_char=False;
               
        
      
      # ################## logic for the first character  ENDS HERE ##################   
         #  if first_char==False:
               
            # char_punch = pygame.image.load("char1/img-1.png")
            # char1_punch= pygame.transform.scale(char_punch, (100, 167))
            # window.blit(char1_punch,(char1_x,char1_y))
              
        
        ################# login for the second characters  ###################
        if event.type == pygame.KEYDOWN:
           if pygame.key.name(event.key) =="a":
              if char2_x <15:
                 char2_x -=0
              else:
                 char2_x -=15;
           elif pygame.key.name(event.key) =="d":
              if char2_x >600:
                 char2_x +=0
              else:
                 char2_x +=15;
           elif pygame.key.name(event.key) =="w":
              second_char=False;
              
    
              
    


      #   if event.type == pygame.KEYDOWN:
      #       if event.key == pygame.K_SPACE:
      #           jumping = True
         

    # Update the sprite

    # Draw the game
    scaled_bg_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    char1 = pygame.transform.scale(char, (100, 167))
    char2 = pygame.transform.scale(char2, (50, 180))


    
   #  flipping tanjim
    char2_flip = pygame.transform.flip(char2, True, False)
    window.blit(scaled_bg_image, (0, 0))

   ############# First character blitting #################
    if first_char==True:
      window.blit(char1,(char1_x,char1_y))
    else: 
      char_punch = pygame.image.load("char1/img-1.png")
      char1_punch= pygame.transform.scale(char_punch, (100, 167))
      window.blit(char1_punch,(char1_x,char1_y))
      # playing the sound effect.
      pygame.mixer.music.load("effects/has-punch.mp3")
      pygame.mixer.music.play()
      font = pygame.font.Font('freesansbold.ttf', 20)
      text = font.render(f'Tanjim : {tan_health}', True, green, blue)
      tan_health-=10;
      textRect = text.get_rect()
      textRect.center = (100, 20)
      # time.sleep(0.5);
      first_char=True;



   ############# Second character blitting #################
    if second_char==True:
      window.blit(char2_flip,(char2_x,char2_y))
    else: 
      char2_punch = pygame.image.load("char1/img-tan-4.png")
      char2_flip = pygame.transform.flip(char2_punch, True, False)
      char2_punch= pygame.transform.scale(char2_flip, (100, 180))
      window.blit(char2_punch,(char2_x,char2_y))
      # playing the sound effect.
      pygame.mixer.music.load("effects/tan-punch.mp3")
      pygame.mixer.music.play()
      second_char=True;
    ##############  TEXT  Starts from here #######################
   #  font = pygame.font.Font('freesansbold.ttf', 20)
   #  text = font.render(f'Tanjim : {tan_health}', True, green, blue)
   #  textRect = text.get_rect()
   #  textRect.center = (100, 20)

    text2 = font.render(f'Hassan : {has_health}', True, green, blue)
    text2Rect = text2.get_rect()
    text2Rect.center = (600, 20)
    window.blit(text, textRect)
    window.blit(text2, text2Rect)
    


    # Update the display
    pygame.display.flip()

