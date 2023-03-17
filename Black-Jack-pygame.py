import pygame
import sys
import time
import random
from kortlek import * 

pygame.init()

# width = 1299
# height = 711
width = 1920
height = 1080
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('BlackJack-table3.png').convert()
bg_img = pygame.transform.scale(bg_img,(width,height))

# kort = pygame.image.load(kortlek_map["c2"]).convert()
blank = pygame.image.load(kortlek_map["blank"]).convert_alpha()
redchip = pygame.image.load('redchip.png').convert_alpha()
redchip = pygame.transform.scale(redchip, (200, 200)) 
bluechip = pygame.image.load('bluechip.png').convert_alpha()
bluechip = pygame.transform.scale(bluechip, (200, 200)) 

pygame.display.set_caption("Black Jack")

clock = pygame.time.Clock()


# white color
color = (255,255,255)
# light shade of the button
color_light = (170,170,170)
# dark shade of the button
color_dark = (100,100,100)

smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont("arial",65)
text = smallfont.render('Hit' , True , color)
text2 = smallfont.render('Stand' , True , color)
text3 = smallfont.render('Double' , True , color)


skort=""
skort2=""
skort3=""
skort4=""
skort5=""
dkort=""
dkort2=""
dkort3=""
dkort4=""
dkort5=""
spelare = 0
dealer = 0
sy=100
dy=450
sx=100
dx=100
hit=0
stand=0
double=0

skortD=0
skort2D=0
skort3D=0
skort4D=0
skort5D=0
dkortD=0
dkort2D=0
dkort3D=0
dkort4D=0
dkort5D=0


kortlek =  ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13",
            "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"]

while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print(skort)
                print(skort2)
                print(skort3)
                print(skort4)
                print(skort5)
                print(dkort)
                print(dkort2)
                print(dkort3)
                print(dkort4)
                print(dkort5)
                print(kortlek, len(kortlek))
                pygame.quit()
                raise SystemExit

        if event.type == pygame.MOUSEBUTTONDOWN:
              
            if width/2 <= mouse[0] <= width/2+140 and height-45 <= mouse[1] <= height-5:
                if hit < 3:
                    if stand == 0:
                        hit+=1

            if width/3 <= mouse[0] <= width/3+140 and height-45 <= mouse[1] <= height-5:
            	if stand == 0:
                    stand=1

            if width/3*2 <= mouse[0] <= width/3*2+140 and height-45 <= mouse[1] <= height-5:
            	if double == 0:
                    double=1

    # Do logical updates here.
    # ...

    window.blit(bg_img, [0, 0])
    # window.blit(kort, [0, 0])
    # window.blit(blank, [250, 0])
	# screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    window.blit(bluechip, [1632, 132])
    spoints = bigfont.render(str(spelare), True, color)
    window.blit(spoints, [1700, 200])
    # dpoints = bigfont.render(str(dealer), True, color)
    # window.blit(dpoints, [1700, 600])

    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height-45 <= mouse[1] <= height-5:
        pygame.draw.rect(window,color_light,[width/2,height-45,140,40])
          
    else:
        pygame.draw.rect(window,color_dark,[width/2,height-45,140,40])

    window.blit(text , (width/2+50,height-45))


    if width/3 <= mouse[0] <= width/3+140 and height-45 <= mouse[1] <= height-5:
        pygame.draw.rect(window,color_light,[width/3,height-45,140,40])
          
    else:
        pygame.draw.rect(window,color_dark,[width/3,height-45,140,40])

    window.blit(text2 , (width/3+30,height-45))


    if width/3*2 <= mouse[0] <= width/3*2+140 and height-45 <= mouse[1] <= height-5:
        pygame.draw.rect(window,color_light,[width/3*2,height-45,140,40])
          
    else:
        pygame.draw.rect(window,color_dark,[width/3*2,height-45,140,40])

    window.blit(text3 , (width/3*2+20,height-45))


    while skort == "":
    	skort = random.choice(kortlek)
    	kortlek.remove(skort)
    	skort_ = pygame.image.load(kortlek_map[skort]).convert_alpha()

    while skort2 == "":
    	skort2 = random.choice(kortlek)
    	kortlek.remove(skort2)
    	skort2_ = pygame.image.load(kortlek_map[skort2]).convert_alpha()

    while skort3 == "":
    	skort3 = random.choice(kortlek)
    	kortlek.remove(skort3)
    	skort3_ = pygame.image.load(kortlek_map[skort3]).convert_alpha()

    while skort4 == "":
    	skort4 = random.choice(kortlek)
    	kortlek.remove(skort4)
    	skort4_ = pygame.image.load(kortlek_map[skort4]).convert_alpha()

    while skort5 == "":
    	skort5 = random.choice(kortlek)
    	kortlek.remove(skort5)
    	skort5_ = pygame.image.load(kortlek_map[skort5]).convert_alpha()


    if hit == 0:
        sx=100
        window.blit(skort_, [sx, sy])
        if skortD == 0:
            spelare += int(skort[1:])
            if skort[1:] == "11":
                spelare += -1
            if skort[1:] == "12":
                spelare += -2
            if skort[1:] == "13":
                spelare += -3
            skortD=1
        sx+=250
        window.blit(skort2_, [sx, sy])
        if skort2D == 0:
            spelare += int(skort2[1:])
            if skort2[1:] == "11":
                spelare += -1
            if skort2[1:] == "12":
                spelare += -2
            if skort2[1:] == "13":
                spelare += -3
            skort2D=1
    if hit == 1:
        sx=100
        window.blit(skort_, [sx, sy])
        sx+=250
        window.blit(skort2_, [sx, sy])
        sx+=250
        window.blit(skort3_, [sx, sy])
        if skort3D == 0:
            spelare += int(skort3[1:])
            if skort3[1:] == "11":
                spelare += -1
            if skort3[1:] == "12":
                spelare += -2
            if skort3[1:] == "13":
                spelare += -3
            skort3D=1
    if hit == 2:
        sx=100
        window.blit(skort_, [sx, sy])
        sx+=250
        window.blit(skort2_, [sx, sy])
        sx+=250
        window.blit(skort3_, [sx, sy])
        sx+=250
        window.blit(skort4_, [sx, sy])
        if skort4D == 0:
            spelare += int(skort4[1:])
            if skort4[1:] == "11":
                spelare += -1
            if skort4[1:] == "12":
                spelare += -2
            if skort4[1:] == "13":
                spelare += -3
            skort4D=1
    if hit == 3:
        sx=100
        window.blit(skort_, [sx, sy])
        sx+=250
        window.blit(skort2_, [sx, sy])
        sx+=250
        window.blit(skort3_, [sx, sy])
        sx+=250
        window.blit(skort4_, [sx, sy])
        sx+=250
        window.blit(skort5_, [sx, sy])
        if skort5D == 0:
            spelare += int(skort5[1:])
            if skort5[1:] == "11":
                spelare += -1
            if skort5[1:] == "12":
                spelare += -2
            if skort5[1:] == "13":
                spelare += -3
            skort5D=1


    while dkort == "":
    	dkort = random.choice(kortlek)
    	kortlek.remove(dkort)
    	dkort_ = pygame.image.load(kortlek_map[dkort]).convert_alpha()

    while dkort2 == "":
    	dkort2 = random.choice(kortlek)
    	kortlek.remove(dkort2)
    	dkort2_ = pygame.image.load(kortlek_map[dkort2]).convert_alpha()

    while dkort3 == "":
    	dkort3 = random.choice(kortlek)
    	kortlek.remove(dkort3)
    	dkort3_ = pygame.image.load(kortlek_map[dkort3]).convert_alpha()

    while dkort4 == "":
    	dkort4 = random.choice(kortlek)
    	kortlek.remove(dkort4)
    	dkort4_ = pygame.image.load(kortlek_map[dkort4]).convert_alpha()

    while dkort5 == "":
    	dkort5 = random.choice(kortlek)
    	kortlek.remove(dkort5)
    	dkort5_ = pygame.image.load(kortlek_map[dkort5]).convert_alpha()

    if stand == 0:
        dx=100
        window.blit(dkort_, [dx, dy])
        if dkortD == 0:
            dealer += int(dkort[1:])
            if dkort[1:] == "11":
                dealer += -1
            if dkort[1:] == "12":
                dealer += -2
            if dkort[1:] == "13":
                dealer += -3
            dkortD=1
        dx+=250
        window.blit(blank, [dx, dy])
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 532])
        window.blit(dpoints, [1700, 600])

    if stand == 1:
        dx=100
        window.blit(dkort_, [dx, dy])
        dx+=250
        window.blit(dkort2_, [dx, dy])
        if dkort2D == 0:
            dealer += int(dkort2[1:])
            if dkort2[1:] == "11":
                dealer += -1
            if dkort2[1:] == "12":
                dealer += -2
            if dkort2[1:] == "13":
                dealer += -3
            dkort2D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 532])
        window.blit(dpoints, [1700, 600])
        pygame.display.update()
        time.sleep(1)
        stand=2
    if stand == 2:
        pygame.display.update()
        dx=100
        window.blit(dkort_, [dx, dy])
        dx+=250
        window.blit(dkort2_, [dx, dy])
        dx+=250
        window.blit(dkort3_, [dx, dy])
        if dkort3D == 0:
            dealer += int(dkort3[1:])
            if dkort3[1:] == "11":
                dealer += -1
            if dkort3[1:] == "12":
                dealer += -2
            if dkort3[1:] == "13":
                dealer += -3
            dkort3D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 532])
        window.blit(dpoints, [1700, 600])
        pygame.display.update()
        time.sleep(1)
        stand=3
    if stand == 3:
        dx=100
        window.blit(dkort_, [dx, dy])
        dx+=250
        window.blit(dkort2_, [dx, dy])
        dx+=250
        window.blit(dkort3_, [dx, dy])
        dx+=250
        window.blit(dkort4_, [dx, dy])
        if dkort4D == 0:
            dealer += int(dkort4[1:])
            if dkort4[1:] == "11":
                dealer += -1
            if dkort4[1:] == "12":
                dealer += -2
            if dkort4[1:] == "13":
                dealer += -3
            dkort4D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 532])
        window.blit(dpoints, [1700, 600])
        pygame.display.update()
        time.sleep(1)
        stand=4
    if stand == 4:
        dx=100
        window.blit(dkort_, [dx, dy])
        dx+=250
        window.blit(dkort2_, [dx, dy])
        dx+=250
        window.blit(dkort3_, [dx, dy])
        dx+=250
        window.blit(dkort4_, [dx, dy])
        dx+=250
        window.blit(dkort5_, [dx, dy])
        if dkort5D == 0:
            dealer += int(dkort5[1:])
            if dkort5[1:] == "11":
                dealer += -1
            if dkort5[1:] == "12":
                dealer += -2
            if dkort5[1:] == "13":
                dealer += -3
            dkort5D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 532])
        window.blit(dpoints, [1700, 600])


    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)