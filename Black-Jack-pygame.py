import pygame
import sys
import time
import random
from kortlek import * 

pygame.init()

width = 1200
height = 661
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('blackjack.jpg').convert()
bg_img = pygame.transform.scale(bg_img,(width,height))

# kort = pygame.image.load(kortlek_map["c2"]).convert()
blank = pygame.image.load(kortlek_map["blank"]).convert()

pygame.display.set_caption("Black Jack")

clock = pygame.time.Clock()


# white color
color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)


smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('Hit' , True , color)

val=""
kort=""
spelare = []
x = -250

while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                val="h"
                x+=250

    # Do logical updates here.
    # ...

    window.blit(bg_img, [0, 0])
    # window.blit(kort, [0, 0])
    # window.blit(blank, [250, 0])
	# screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(window,color_light,[width/2,height/2,140,40])
          
    else:
        pygame.draw.rect(window,color_dark,[width/2,height/2,140,40])

    window.blit(text , (width/2+50,height/2))


    for i in range(1):
    	kortlek =  ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
					"c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
					"d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13",
					"s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"]

    	kort = random.choice(kortlek)
    	kortlek.remove(kort)
    	spelare.append(kort)
    	kort = pygame.image.load(kortlek_map[kort]).convert()


    if val == "h":
    	window.blit(kort, [x, 0])


    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)