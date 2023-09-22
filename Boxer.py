import pygame
import sys
from pygame import *
import time;
import cv2 
import mediapipe as mp

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


## mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
height = 350
length = 600
def distBetween(pointA, pointB, distA, distB):
    x = length * (pointA.x - pointB.x)
    y = height * (pointA.y - pointB.y)
    dist = x**2 + y**2
    dist = dist**(0.5)
    if dist > distA and dist < distB:
        return True
    return False
def distance(pointA, pointB):
    x = length * (pointA.x - pointB.x)
    y = height * (pointA.y - pointB.y)
    dist = x**2 + y**2
    dist = dist**(0.5)
    return dist

jab = False
cross = False
counter = 0
cap = cv2.VideoCapture("char1/test.mp4")
# cap = cv2.VideoCapture(0)

# Start the game loop
while cap.isOpened():
    # Handle events
    _, frame = cap.read()
    try:
         # resize the frame for portrait video
         # frame = cv2.resize(frame, (350, 600))
         # convert to RGB
         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         
         # process the frame for pose detection
         pose_results = pose.process(frame_rgb)
         R_shoul = pose_results.pose_landmarks.landmark[12]
         L_shoul = pose_results.pose_landmarks.landmark[11]
         R_elbow = pose_results.pose_landmarks.landmark[14]
         L_elbow = pose_results.pose_landmarks.landmark[13]

         if distBetween(L_elbow,L_shoul, 0, 40):
              jab = True
         elif jab:
              first_char=False;
              jab = False
         if distBetween(R_elbow,R_shoul, 0, 40):
              cross = True
         elif cross:
              first_char=False;
              cross = False
         
         pos = abs(distance(L_shoul, R_shoul) - 50) * 5.5

         counter= counter +1
         if counter%30 == 0 and abs(char1_x-char2_x)>45:
            if pos > 600 and pos < 700 and char1_x > 35 :
                char1_x -= 35
            elif pos > 500 and pos < 600 and char1_x > 25:
                char1_x -= 25
            elif pos > 450 and pos < 500 and char1_x > 20:
                char1_x -= 20
            elif pos > 350 and pos < 450 and char1_x < 650:
                char1_x += 0
            elif pos > 300 and pos < 350 and char1_x < 650:
                char1_x += 25
            elif pos > 200 and pos < 300 and char1_x < 650:
                char1_x += 30
            elif pos > 100 and pos < 200 and char1_x < 650:
                char1_x += 35

         # draw skeleton on the frame
         mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
         # display the frame
         cv2.imshow('RealTime', frame)
         
    except error as e:
         print(e);
    if cv2.waitKey(1) == ord('q'):
        print("Terminating the Program")
        break
          
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
            if event.key == pygame.K_a:
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
      font = pygame.font.Font("freesansbold.ttf",20)
      text = font.render(f"Tanjim : {tan_health}", True,green,blue)
      if (abs(char1_x-char2_x)<50):
          if tan_health<=-10:
              tan_health=0
              time.sleep(3);
              break
          tan_health-=10;
    #   tan_health;ad
      textRect = text.get_rect();
      textRect.center = (100,20)
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
      font = pygame.font.Font("freesansbold.ttf",20)
      text = font.render(f"Hassan : {has_health}", True,green,blue)
      if (abs(char1_x-char2_x)<50):
          if has_health<=-10:
              has_health=0
              time.sleep(3);
              break
          has_health-=10;
      has_health;
      text2Rect = text2.get_rect();
      text2Rect.center = (600,20)
      window.blit(text,textRect)
      window.blit(text2,text2Rect)
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

cap.release()
cv2.destroyAllWindows()