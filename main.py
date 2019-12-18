import pygame
import random
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

tails = []
size = (600, 600)
tile_size = size[0]/12
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

dx = 1
dy = 0
x = 0
y = 0
length = 3
food = [random.randint(0,11)*tile_size,random.randint(0,11)*tile_size]

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
i = 0 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop 
    screen.fill(WHITE)
    tails.append([x,y,0])
    for tail in tails:
        if tail[2] < length:
            pygame.draw.rect(screen, RED, [tail[0], tail[1], tile_size, tile_size],0)
            if (tail[0] == x and tail[1] == y and tail[2] != 0):
                carryOn = False 
            tail[2] += 1
        else:
            tails.remove(tail)
            
    pygame.draw.rect(screen, BLACK, [x, y, tile_size, tile_size],0)
    pygame.draw.rect(screen, GREEN, [food[0], food[1], tile_size, tile_size],0)
    x += dx*tile_size
    y += dy*tile_size
    direction = [pygame.key.get_pressed()[pygame.K_w],pygame.key.get_pressed()[pygame.K_a],pygame.key.get_pressed()[pygame.K_s],pygame.key.get_pressed()[pygame.K_d]]
    if (direction[0] and dy != 1):
        dx = 0
        dy = -1
    elif (direction[1] and dx != 1):
        dx = -1
        dy = 0
    elif (direction[2] and dy != -1):
        dx = 0
        dy = 1
    elif (direction[3] and dx != -1):
        dx = 1
        dy = 0

    if (pygame.key.get_pressed()[pygame.K_g]):
        length += 1
    
    if (pygame.key.get_pressed()[pygame.K_h]):
        length -= 1

    if (x > 600 - tile_size):
        x = 0
    elif (x < 0):
        x = size[0] - tile_size
    if (y > size[0] - tile_size):
        y = 0
    elif (y < 0):
        y = size[0] - tile_size
    
    if (x == food[0] and y == food[1]):
        food = [random.randint(0,11)*tile_size,random.randint(0,11)*tile_size]
        print(food[0],food[1])
        length += 1
    
     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(10)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()