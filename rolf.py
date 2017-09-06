import pygame
import time
from random import randint

black = (0,0,0)
white = (255,255,255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500
imageHeight = 40
imageWidth = 40

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Rolfcopter')
clock = pygame.time.Clock()

img = pygame.image.load('rolf.png')

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text, [0,0])

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, white, [x_block, y_block + block_height + gap, block_width, surface_height])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
	if event.type == pygame.QUIT:
	   pygame.quit()
	   quit()

	elif event.type == pygame.KEYDOWN:
	   continue

	return event.key

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurface, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.bilt(titleTextSurface, titleTextRect)

    typTextSurface, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight/ 2) +  100)
    surface.bilt(typTextSurface, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit == None:
    	clock.tick()

    main()


def gameOver():
    msgSurface('Ded')

def rolfcopter(x, y, image):
    surface.blit(img, (x,y))

def main():
    x = 150
    y = 200
    y_move = 2
    current_score = 0

    x_block = surfaceWidth
    y_block = 0
    block_width = 75
    block_height = randint(0, (surfaceHeight / 2))
    gap = imageHeight * 2.5
    block_move = 4

    game_over = False

    while not game_over:

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        game_over = True
	    if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_UP:
	           y_move = -5
	    if event.type == pygame.KEYUP:
	        if event.key == pygame.K_UP:
	           y_move = 5

	    y += y_move

	    surface.fill(black)
	    rolfcopter(x, y, img)
	    score(current_score)

	    blocks(x_block, y_block, block_width, block_height, gap)
            x_block -= block_move

	    if y > surfaceHeight - imageHeight or y < 0:
	    	gameOver()
        
            if x_block < (-1 * block_width):
        	x_block = surfaceWidth
        	block_height = randint(0, (surfaceHeight / 2))
        
            # earlier if statemets to test the logic
            if x + imageHeight > x_block:
        	if x < x_block + block_width:
        	    if y < block_height:
        		if x - imageWidth < block_width + x_block:
        		   gameOver()
        			   
           # earlier if statemets to test the logic
           if x + imageWidth > x_block:
               if y + imageHeight > block_height + gap:
        	   if x < block_width + x_block:
        	      gameOver()

           if x < x_block and x > x_block - block_move:
               current_score += 1


	    pygame.display.update()
	    clock.tick(60)

main()
pygame.quit()
quit()
