import pygame
import sys
from pygame import * 
import time
import mediapipe as mp
import cv2



pygame.display.set_caption('RT Boxer')
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
class Player:
    def __init__(self,name,cord_x, cord_y,health:int):
        self.name = name
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.health = health
        print(f"{self.name} initiated")
        
    def current_health(self):
        if self.health <=0:
            pass
        else:
            self.health = self.health -10
            
    def health_update(self ,health_x:int, health_y:int):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(f'{self.name} : {self.health}', True,green,blue)
        textRect = text.get_rect()
        textRect.center = (health_x, health_y)
        return (text,textRect)
        
         
        
character1 = Player("Hassan", cord_x=800,cord_y=200, health=100)
character2 = Player("Soham", cord_x=300,cord_y=200,health=100)
# print(character1.cord_x)    
        
 
 
def collision(x,y):
    if abs(x-y) < 150:
        return True
    else:
        return False
    
        
# all the images are loaded in this function
def load_image(): 
    
    # ######## Raw Images 
    bg_raw = pygame.image.load("bg.png");
    char1_raw = pygame.transform.flip(pygame.image.load("characters/hassan/hassan-1.png"), True,False);
    char1_raw_punch =pygame.transform.flip(pygame.image.load("characters/hassan/hassan-2.png"), True,False);

    char2_raw =pygame.image.load("characters/soham/soham-1.png")
    char2_raw_punch = pygame.image.load("characters/soham/soham-2.png")

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
    
    
    
def init_func():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock();
    first_character_punch = False
    second_character_punch = False
    
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

    char1_x,char1_y = 1000,200;
    char2_x,char2_y = 1000,200;
    # cap = cv2.VideoCapture(0)

    # Start the game loop
    cap = cv2.VideoCapture()
    img_dictionary = load_image()
    while True:
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
                first_character_punch=True
                
            
            if distBetween(R_elbow,R_shoul, 0, 40):
                first_character_punch=True

            
            pos = abs(distance(L_shoul, R_shoul) - 50) * 5.5
            print(pos)

            counter= counter +1
            
            # still working on this
            if counter%30 == 0 and abs(character1.cord_x-character2.cord_x)>45:
                if pos > 1200 and character1.cord_x > 35 :
                    character1.cord_x -= 35
                elif pos > 1000 and pos < 1100 and character1.cord_x > 25:
                    character1.cord_x -= 25
                elif pos > 900 and pos < 1000 and character1.cord_x > 20:
                    character1.cord_x -= 20
                elif pos > 850 and pos < 900 and character1.cord_x < 1280:
                    character1.cord_x += 0
                elif pos > 700 and pos < 750 and character1.cord_x <1280:
                    character1.cord_x += 25
                elif pos > 500 and pos < 700 and character1.cord_x < 1280:
                    character1.cord_x += 30
                elif pos > 500 and pos < 600 and character1.cord_x < 1280:
                    character1.cord_x += 35

            # draw skeleton on the frame
            # mp_drawing.draw_landmarks(frame_rgb, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            # display the frame
            cv2.imshow('RealTime', frame_rgb)
            
        except error as e:
            print(e);
        if cv2.waitKey(1) == ord('q'):
            print("Terminating the Program")
            break


    
    # while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    first_character_punch = True
                
                
                    
                if event.key==pygame.K_LEFT:
                    if character2.cord_x >15:
                        if not collision(character1.cord_x,character2.cord_x):
                            character1.cord_x -=25
                    character1.cord_x;

                        
                        
                if event.key==pygame.K_DOWN:
                    pass
                if event.key==pygame.K_RIGHT:
                    if character1.cord_x <1150:
                        character1.cord_x += 25;
                    else:
                        character1.cord_x;
                
                
                # second character
                
                if event.key==pygame.K_w:
                    second_character_punch = True
                    
                if event.key==pygame.K_s:
                    pass
                if event.key==pygame.K_a:
                    if character2.cord_x >15:
                        character2.cord_x -=25
                    character2.cord_x;
                    
                if event.key==pygame.K_d:
                    if character2.cord_x <1150:
                        if not collision(character2.cord_x,character1.cord_x):
                            character2.cord_x +=25;
                        else:
                            character2.cord_x;
                           
                    
            
        
        
            
        
        #within for loop   
        screen.blit(img_dictionary["bg"],(0,0))
        if first_character_punch:
            screen.blit(img_dictionary["character1_punch"], (character1.cord_x,character1.cord_y))
            first_character_punch=False;
            if collision(character2.cord_x,character1.cord_x):
                character2.current_health();
                # print(character2.health)
                
        else:    
            screen.blit(img_dictionary["character1"], (character1.cord_x,character1.cord_y))

        # second player logic
        if second_character_punch:
            screen.blit(img_dictionary["character2_punch"], (character2.cord_x-100,character2.cord_y))
            second_character_punch=False;
            if collision(character2.cord_x,character1.cord_x):
                character1.current_health();
                # print(character1.health)
                
        else:    
            screen.blit(img_dictionary["character2"], (character2.cord_x,character2.cord_y))

        # screen.blit(img_dictionary["bg"],(0,0))
        char1_health = character1.health_update(320,20)
        char2_health = character2.health_update(960,20)
        # print(char1_health)
        screen.blit(char1_health[0],(char1_health[1]))
        screen.blit(char2_health[0],(char2_health[1]))
        pygame.display.update();
    
    cap.release()
    cv2.destroyAllWindows()

init_func();

    

    
