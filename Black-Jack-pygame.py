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
text2 = smallfont.render('Stand' , True , color)
text3 = smallfont.render('Double' , True , color)

val=""
skort=""
skort2=""
skort3=""
skort4=""
skort5=""
spelare = []
x = -250
hit=0
stand=0
double=0
dkort=""
dkort2=""
dkort3=""
dkort4=""
dkort5=""

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
            if width/2 <= mouse[0] <= width/2+140 and height-50 <= mouse[1] <= height-10:
                hit+=1
                x+=250

            if width/3 <= mouse[0] <= width/3+140 and height-50 <= mouse[1] <= height-10:
            	stand=1

            if width/3*2 <= mouse[0] <= width/3*2+140 and height-50 <= mouse[1] <= height-10:
            	double=1

    # Do logical updates here.
    # ...

    window.blit(bg_img, [0, 0])
    # window.blit(kort, [0, 0])
    # window.blit(blank, [250, 0])
	# screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height-50 <= mouse[1] <= height-10:
        pygame.draw.rect(window,color_light,[width/2,height-50,140,40])
          
    else:
        pygame.draw.rect(window,color_dark,[width/2,height-50,140,40])

    window.blit(text , (width/2+50,height-50))


    if width/3 <= mouse[0] <= width/3+140 and height-50 <= mouse[1] <= height-10:
        pygame.draw.rect(window,color_light,[width/3,height-50,140,40])
          
    else:
        pygame.draw.rect(window,color_dark,[width/3,height-50,140,40])

    window.blit(text2 , (width/3+30,height-50))


    if width/3*2 <= mouse[0] <= width/3*2+140 and height-50 <= mouse[1] <= height-10:
        pygame.draw.rect(window,color_light,[width/3*2,height-50,140,40])
          
    else:
        pygame.draw.rect(window,color_dark,[width/3*2,height-50,140,40])

    window.blit(text3 , (width/3*2+20,height-50))


    kortlek =  ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
				"c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
				"d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13",
				"s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"]


    while skort == "":
    	skort = random.choice(kortlek)
    	kortlek.remove(skort)
    	skort = pygame.image.load(kortlek_map[skort]).convert()

    while skort2 == "":
    	skort2 = random.choice(kortlek)
    	kortlek.remove(skort2)
    	skort2 = pygame.image.load(kortlek_map[skort2]).convert()

    while skort3 == "":
    	skort3 = random.choice(kortlek)
    	kortlek.remove(skort3)
    	skort3 = pygame.image.load(kortlek_map[skort3]).convert()

    while skort4 == "":
    	skort4 = random.choice(kortlek)
    	kortlek.remove(skort4)
    	skort4 = pygame.image.load(kortlek_map[skort4]).convert()

    while skort5 == "":
    	skort5 = random.choice(kortlek)
    	kortlek.remove(skort5)
    	skort5 = pygame.image.load(kortlek_map[skort5]).convert()


    if hit == 0:
    	window.blit(skort, [0, 0])
    	window.blit(skort2, [250, 0])
    if hit == 1:
    	window.blit(skort, [0, 0])
    	window.blit(skort2, [250, 0])
    	window.blit(skort3, [500, 0])
    if hit == 2:
    	window.blit(skort, [0, 0])
    	window.blit(skort2, [250, 0])
    	window.blit(skort3, [500, 0])
    	window.blit(skort4, [750, 0])
    if hit == 3:
    	window.blit(skort, [0, 0])
    	window.blit(skort2, [250, 0])
    	window.blit(skort3, [500, 0])
    	window.blit(skort4, [750, 0])
    	window.blit(skort5, [1000, 0])


    while dkort == "":
    	dkort = random.choice(kortlek)
    	kortlek.remove(dkort)
    	dkort = pygame.image.load(kortlek_map[dkort]).convert()

    while dkort2 == "":
    	dkort2 = random.choice(kortlek)
    	kortlek.remove(dkort2)
    	dkort2 = pygame.image.load(kortlek_map[dkort2]).convert()

    while dkort3 == "":
    	dkort3 = random.choice(kortlek)
    	kortlek.remove(dkort3)
    	dkort3 = pygame.image.load(kortlek_map[dkort3]).convert()

    while dkort4 == "":
    	dkort4 = random.choice(kortlek)
    	kortlek.remove(dkort4)
    	dkort4 = pygame.image.load(kortlek_map[dkort4]).convert()

    while dkort5 == "":
    	dkort5 = random.choice(kortlek)
    	kortlek.remove(dkort5)
    	dkort5 = pygame.image.load(kortlek_map[dkort5]).convert()

    if stand == 0:
    	window.blit(dkort, [0, 250])
    	window.blit(blank, [250, 250])

    if stand == 1:
    	window.blit(dkort, [0, 250])
    	window.blit(dkort2, [250, 250])
    	stand=2
    	pygame.display.update()
    	time.sleep(1)
    if stand == 2:
    	window.blit(dkort, [0, 250])
    	window.blit(dkort2, [250, 250])
    	window.blit(dkort3, [500, 250])
    	stand=3
    	pygame.display.update()
    	time.sleep(1)
    if stand == 3:
    	window.blit(dkort, [0, 250])
    	window.blit(dkort2, [250, 250])
    	window.blit(dkort3, [500, 250])
    	window.blit(dkort4, [750, 250])
    	stand=4
    	pygame.display.update()
    	time.sleep(1)
    if stand == 4:
    	window.blit(dkort, [0, 250])
    	window.blit(dkort2, [250, 250])
    	window.blit(dkort3, [500, 250])
    	window.blit(dkort4, [750, 250])
    	window.blit(dkort5, [1000, 250])


    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)