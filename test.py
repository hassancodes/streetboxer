# Importing the pygame module
import pygame
from pygame.locals import *
import sys

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((1080, 720))


# Create a list of different sprites
# that you want to use in the animation
idlesprite = [pygame.image.load("png/Idle (1).png"),
				pygame.image.load("png/Idle (2).png"),
                pygame.image.load("png/Idle (3).png"),
                pygame.image.load("png/Idle (4).png"),
                pygame.image.load("png/Idle (5).png"),        
                pygame.image.load("png/Idle (6).png"),    
                pygame.image.load("png/Idle (7).png"),
                pygame.image.load("png/Idle (8).png"), 
                pygame.image.load("png/Idle (9).png"), 
                pygame.image.load("png/Idle (10).png"),
                ]

image_sprite = idlesprite
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Creating a new variable
# We will use this variable to
# iterate over the sprite list
value = 0

# Creating a boolean variable that
# we will use to run the while loop
run = True

# Creating an infinite loop
# to run our game
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.quit();
            
        # Setting 0 in value variable if its
        # value is greater than the length
        # of our sprite list
        if value >= len(image_sprite):
            value = 0

        # Storing the sprite image in an
        # image variable
        image = image_sprite[value]

        # Creating a variable to store the starting
        # x and y coordinate
        x = 150

        # Changing the y coordinate
        # according the value stored
        # in our value variable
        if value == 0:
            y = 200
        else:
            y = 200

        # Displaying the image in our game window
        window.blit(image, (x, y))

        # Updating the display surface
        pygame.display.update()

        # Filling the window with black color
        window.fill((0, 0, 0))

        # Increasing the value of value variable by 1
        # after every iteration
        value += 1













# import pygame
# from pygame import *

# pygame.init()
# window = pygame.display.set_mode((400, 400))
# clock = pygame.time.Clock()

# class Player(pygame.sprite.Sprite):
    
#     def __init__(self, center_pos, image):
#         super().__init__() 
#         self.image = image
#         self.rect = self.image[].get_rect(center = center_pos)
    
#     def update(self, surf):
#         keys = pygame.key.get_pressed()
#         self.rect.x += (keys[pygame.K_d]-keys[pygame.K_a]) * 5
#         self.rect.y += (keys[pygame.K_s]-keys[pygame.K_w]) * 5
#         self.rect.clamp_ip(surf.get_rect())


# mainlist = []
# player_surf = pygame.image.load("characters/hassan/hassan-1.png").get_alpha();
# player = Player(window.get_rect().center, player_surf)
# all_sprites = pygame.sprite.Group([player])

# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     all_sprites.update(window)

#     window.fill(0)
#     all_sprites.draw(window)
#     pygame.display.flip()

# pygame.quit()
# exit()