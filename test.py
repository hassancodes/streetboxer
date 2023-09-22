# # Importing the pygame module
# import pygame
# from pygame.locals import *
# import sys

# # Initiate pygame and give permission
# # to use pygame's functionality
# pygame.init()

# # Create a display surface object
# # of specific dimension
# window = pygame.display.set_mode((1080, 720))


# # Create a list of different sprites
# # that you want to use in the animation
# idlesprite = [pygame.image.load("png/Idle (1).png"),
# 				pygame.image.load("png/Idle (2).png"),
#                 pygame.image.load("png/Idle (3).png"),
#                 pygame.image.load("png/Idle (4).png"),
#                 pygame.image.load("png/Idle (5).png"),        
#                 pygame.image.load("png/Idle (6).png"),    
#                 pygame.image.load("png/Idle (7).png"),
#                 pygame.image.load("png/Idle (8).png"), 
#                 pygame.image.load("png/Idle (9).png"), 
#                 pygame.image.load("png/Idle (10).png"),
#                 ]

# image_sprite = idlesprite
# # Creating a new clock object to
# # track the amount of time
# clock = pygame.time.Clock()

# # Creating a new variable
# # We will use this variable to
# # iterate over the sprite list
# value = 0

# # Creating a boolean variable that
# # we will use to run the while loop
# run = True

# # Creating an infinite loop
# # to run our game
# while run:
#     clock.tick(10)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.quit();
            
#         # Setting 0 in value variable if its
#         # value is greater than the length
#         # of our sprite list
#         if value >= len(image_sprite):
#             value = 0

#         # Storing the sprite image in an
#         # image variable
#         image = image_sprite[value]

#         # Creating a variable to store the starting
#         # x and y coordinate
#         x = 150

#         # Changing the y coordinate
#         # according the value stored
#         # in our value variable
#         if value == 0:
#             y = 200
#         else:
#             y = 200

#         # Displaying the image in our game window
#         window.blit(image, (x, y))

#         # Updating the display surface
#         pygame.display.update()

#         # Filling the window with black color
#         window.fill((0, 0, 0))

#         # Increasing the value of value variable by 1
#         # after every iteration
#         value += 1


# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
28
29
30
31
32
33
import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('char1/test.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    print(frame)
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()






