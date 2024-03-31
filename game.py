import random
import pygame
import pygame.freetype

pygame.init()  # initializer, checks the installation

# colors
white = (255, 255, 255)  
black = (0, 0, 0) 

# initializes font
font = pygame.font.Font('opensans.ttf', 40)

# recyclebin object
recyclebin = pygame.image.load('images/recyclebin.png')
recyclebin_rect = recyclebin.get_rect()
vel = 3
recyclebin_rect.bottom = 800
recyclebin_rect.centerx = 250

# class dedicated to the falling pieces of trash
class FallingObjects:
    def __init__(self, image_path, speed, position, num):
        self.recycleable = bool(num)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.top = self.rect.top
        self.speed = speed
        self.position = position
      
    def randomSpeed(self):
        self.speed = random.uniform(2, 4.5)

    def randomPosition(self):
        self.position = random.uniform(0, 800)

# individual Falling Objects, using hand-drawn images
plasticBottle = FallingObjects("images/plasticbottle.png", 2, (300, 125), True)
chipBag = FallingObjects("images/chipbag.png", 2, (300, 125), True)
cigarette = FallingObjects("images/cigarette.png", 2, (300, 125), False) #not recycle
plasticBag = FallingObjects("images/plasticbag.png", 2, (300, 125), False )
bananaPeel = FallingObjects("images/bananapeel.png", 2, (300, 125), False)
can = FallingObjects("images/can.png", 2, (300, 125), True)

# canvas/background of homescreen
canvas = pygame.display.set_mode((800, 800))
background = pygame.image.load("images/titlescreen.jpeg")

# score counter
score = 0
score_change = 10

# Running game
runningscreen = True
running = True

# list to randomize what trash object falls from sky
list = [plasticBottle, chipBag, cigarette, plasticBag, bananaPeel, can]

# assigns initial random piece of trash, and initial random values of trash 
fallingtrash = list[int (random.uniform(0, 6))]
fallingtrash.randomSpeed()
fallingtrash.randomPosition()


# menu screen
def menu() :
    pygame.display.set_caption("Menu")
    while runningscreen : 
         canvas.blit(background, 0, 0)
             
         menu_text = font.render(menu_text, True, (0, 0, 0))
         canvas.blit(menu_text, (10, 10))
         
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningscreen = False

# the game utilizes a while loop to continously update the positions of 
# the objects on screen, both those controlled by player and not controlled
# by player   
def play() :
    # title of game window
    pygame.display.set_caption("Play")

while running:

    canvas.fill(white)
    
    # creates time delay 
    pygame.time.delay(10)

    # checks if recyclable trash is collected
    if pygame.Rect.colliderect(recyclebin_rect, fallingtrash.rect) and fallingtrash.recycleable == True:
        score = score + score_change
        fallingtrash = list[int (random.uniform(0, 6))]
        fallingtrash.randomSpeed()
        fallingtrash.randomPosition()
        fallingtrash.rect.top = -320
        fallingtrash.rect.centerx = random.uniform(150, 450)
    
    # checks if non-recyclable trash is collected
    if pygame.Rect.colliderect(recyclebin_rect, fallingtrash.rect) and fallingtrash.recycleable == False:
        score = score - score_change
        fallingtrash = list[int (random.uniform(0, 6))]
        fallingtrash.randomSpeed()
        fallingtrash.randomPosition()
        fallingtrash.rect.top = -320
        fallingtrash.rect.centerx = random.uniform(150, 450)

    # checks if player has missed trash
    if fallingtrash.rect.top > 800: 
        fallingtrash = list[int (random.uniform(0, 6))]
        fallingtrash.randomSpeed()
        fallingtrash.randomPosition()
        fallingtrash.rect.top = -320
        fallingtrash.rect.centerx = random.uniform(150, 450)

    # this is what updates the position of trash
    else:
        fallingtrash.rect.y += fallingtrash.speed
		
    # ends program if player clicks out of screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player input controls
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and recyclebin_rect.left > 0:
        # decrement in x co-ordinate, move trashbin left 
        recyclebin_rect.x -= vel

    # if right arrow key is pressed, move trashbin right
    if keys[pygame.K_RIGHT] and recyclebin_rect.right < 800:
        # increment in x co-ordinate
        recyclebin_rect.x += vel

    # draws updated position of objects on screen
    canvas.blit(recyclebin, recyclebin_rect)  
    canvas.blit(fallingtrash.image, fallingtrash.rect)
    
    # score is incremented here
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    canvas.blit(score_text, (10, 10))

    # updates display
    pygame.display.update()

pygame.quit()