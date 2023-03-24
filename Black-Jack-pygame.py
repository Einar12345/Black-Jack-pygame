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
bg_img = pygame.image.load('BlackJack-table5.png').convert()
bg_img = pygame.transform.scale(bg_img,(width,height))

# kort = pygame.image.load(kortlek_map["c2"]).convert()
blank = pygame.image.load(kortlek_map["blank"]).convert_alpha()
redchip = pygame.image.load('redchip.png').convert_alpha()
redchip = pygame.transform.scale(redchip, (200, 200)) 
bluechip = pygame.image.load('bluechip.png').convert_alpha()
bluechip = pygame.transform.scale(bluechip, (200, 200)) 

pygame.display.set_caption("Black Jack")

clock = pygame.time.Clock()


color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont("arial",65)
textfont = pygame.font.SysFont("arial",40)

text = smallfont.render('Hit' , True , color)
text2 = smallfont.render('Stand' , True , color)
text3 = smallfont.render('Double' , True , color)
text4 = smallfont.render('Next' , True , color)
text5 = smallfont.render('Bid +10' , True , color)
text55 = smallfont.render('Lock Bid' , True , color)
text555 = smallfont.render('Bid -10' , True , color)
text6 = bigfont.render('Money:' , True , color)
text7 = bigfont.render('Bid:' , True , color)
text8 = textfont.render('Player:' , True , color)
text9 = textfont.render('Dealer:' , True , color)


skort=""
skort2=""
skort3=""
skort4=""
skort5=""
skort6=""
dkort=""
dkort2=""
dkort3=""
dkort4=""
dkort5=""
dkort6=""

spelare = 0
dealer = 0

sy=100
dy=450
sx=100
dx=100

hit=-1
stand=-1

reset=0
reset1=0
reset2=0
reset3=0

skortD=0
skort2D=0
skort3D=0
skort4D=0
skort5D=0
skort6D=0
dkortD=0
dkort2D=0
dkort3D=0
dkort4D=0
dkort5D=0
dkort6D=0

pengar=100
bid=0

runda=1


kortlek =  ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13",
            "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"]

while True:

    # Run loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # print("End", kortlek, len(kortlek))
                pygame.quit()
                raise SystemExit

        # knappar
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            if width/2 <= mouse[0] <= width/2+140 and height-45 <= mouse[1] <= height-5: # Hit
                if bid > 1:
                    if hit < 4:
                        if stand == 0:
                            hit+=1

            if width/3 <= mouse[0] <= width/3+140 and height-45 <= mouse[1] <= height-5: # Stand
                if bid > 1:
                	if stand == 0:
                            stand=1

            if width/3*2 <= mouse[0] <= width/3*2+140 and height-45 <= mouse[1] <= height-5: # Double
                if bid > 1:
                    if hit == 0:
                    	if stand == 0:
                                pengar-=bid
                                bid=bid*2
                                hit=1
                                stand=1

            if reset == 1:
                if width/2 <= mouse[0] <= width/2+140 and height-245 <= mouse[1] <= height-205: # Next
                    spelare = 0
                    dealer = 0
                    hit=-1
                    stand=-1
                    reset=0
                    reset1=0
                    skort=""
                    skort2=""
                    skort3=""
                    skort4=""
                    skort5=""
                    skort6=""
                    dkort=""
                    dkort2=""
                    dkort3=""
                    dkort4=""
                    dkort5=""
                    dkort6=""
                    skortD=0
                    skort2D=0
                    skort3D=0
                    skort4D=0
                    skort5D=0
                    skort6D=0
                    dkortD=0
                    dkort2D=0
                    dkort3D=0
                    dkort4D=0
                    dkort5D=0
                    dkort6D=0
                    bid=0
                    runda+=1
                    reset2=0
                    reset3=0
                    # print("Reset", kortlek, len(kortlek))

            if hit == -1:
                if stand == -1:
                    if width/3*2 <= mouse[0] <= width/3*2+140 and height-245 <= mouse[1] <= height-205: # Bid +10
                        if pengar > 0:
                            if bid < 100:
                                bid+=10
                                pengar-=10
                    if width/2 <= mouse[0] <= width/2+140 and height-245 <= mouse[1] <= height-205: # Lock Bid
                        if bid > 1:
                            hit=0
                            stand=0
                    if width/3 <= mouse[0] <= width/3+140 and height-245 <= mouse[1] <= height-205: # Bid -10
                        if bid > 0:
                            bid-=10
                            pengar+=10



    window.blit(bg_img, [0, 0])

    # All text
    if stand >= 0:
        window.blit(bluechip, [1632, 125])
        spoints = bigfont.render(str(spelare), True, color)
        window.blit(spoints, [1700, 193])
    # dpoints = bigfont.render(str(dealer), True, color)
    # window.blit(dpoints, [1700, 600])
    window.blit(text6, [100, 750])
    window.blit(text7, [400, 750])
    pengarD = bigfont.render(str(pengar), True, color)
    window.blit(pengarD, [100, 850])
    bidD = bigfont.render(str(bid), True, color)
    window.blit(bidD, [400, 850])
    if hit >= 0:
        window.blit(text8, [100, 50])
        window.blit(text9, [100, 400])
    rundortext = textfont.render("Runda:", True, color)
    window.blit(rundortext, [1700, 75])
    rundor = textfont.render(str(runda), True, color)
    window.blit(rundor, [1815, 75])


    # Knappar
    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height-45 <= mouse[1] <= height-5: # Hit
        pygame.draw.rect(window,color_light,[width/2,height-45,140,40])
    else:
        pygame.draw.rect(window,color_dark,[width/2,height-45,140,40])
    window.blit(text , (width/2+50,height-45))


    if width/3 <= mouse[0] <= width/3+140 and height-45 <= mouse[1] <= height-5: # Stand
        pygame.draw.rect(window,color_light,[width/3,height-45,140,40]) 
    else:
        pygame.draw.rect(window,color_dark,[width/3,height-45,140,40])
    window.blit(text2 , (width/3+30,height-45))


    if width/3*2 <= mouse[0] <= width/3*2+140 and height-45 <= mouse[1] <= height-5: # Double
        pygame.draw.rect(window,color_light,[width/3*2,height-45,140,40])
    else:
        pygame.draw.rect(window,color_dark,[width/3*2,height-45,140,40])
    window.blit(text3 , (width/3*2+20,height-45))


    if reset == 1:
        if width/2 <= mouse[0] <= width/2+140 and height-245 <= mouse[1] <= height-205: # Next
            pygame.draw.rect(window,color_light,[width/2,height-245,140,40]) 
        else:
            pygame.draw.rect(window,color_dark,[width/2,height-245,140,40])
        window.blit(text4 , (width/2+40,height-245))

    if hit == -1:
        if stand == -1: 
            if width/3*2 <= mouse[0] <= width/3*2+140 and height-245 <= mouse[1] <= height-205: # +10
                pygame.draw.rect(window,color_light,[width/3*2,height-245,140,40])
            else:
                pygame.draw.rect(window,color_dark,[width/3*2,height-245,140,40])
            window.blit(text5 , (width/3*2+20,height-245))


            if width/2 <= mouse[0] <= width/2+140 and height-245 <= mouse[1] <= height-205: # Lock
                pygame.draw.rect(window,color_light,[width/2,height-245,140,40])
            else:
                pygame.draw.rect(window,color_dark,[width/2,height-245,140,40])
            window.blit(text55 , (width/2+10,height-245))


            if width/3 <= mouse[0] <= width/3+140 and height-245 <= mouse[1] <= height-205: # -10
                pygame.draw.rect(window,color_light,[width/3,height-245,140,40])
            else:
                pygame.draw.rect(window,color_dark,[width/3,height-245,140,40])
            window.blit(text555 , (width/3+20,height-245))


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

    while skort6 == "":
        skort6 = random.choice(kortlek)
        kortlek.remove(skort6)
        skort6_ = pygame.image.load(kortlek_map[skort6]).convert_alpha()


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
            if skort[1:] == "1":
                spelare += 10
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
            if skort2[1:] == "1":
                if spelare < 12:
                    spelare += 10
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
            if skort3[1:] == "1":
                if spelare < 12:
                    spelare += 10
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
            if skort4[1:] == "1":
                if spelare < 12:
                    spelare += 10
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
            if skort5[1:] == "1":
                if spelare < 12:
                    spelare += 10
            skort5D=1
    if hit == 4:
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
        sx+=250
        window.blit(skort6_, [sx, sy])
        if skort6D == 0:
            spelare += int(skort6[1:])
            if skort6[1:] == "11":
                spelare += -1
            if skort6[1:] == "12":
                spelare += -2
            if skort6[1:] == "13":
                spelare += -3
            if skort6[1:] == "1":
                if spelare < 12:
                    spelare += 10
            skort6D=1


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

    while dkort6 == "":
        dkort6 = random.choice(kortlek)
        kortlek.remove(dkort6)
        dkort6_ = pygame.image.load(kortlek_map[dkort6]).convert_alpha()

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
            if dkort[1:] == "1":
                dealer += 10
            dkortD=1
        dx+=250
        window.blit(blank, [dx, dy])
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 475])
        window.blit(dpoints, [1700, 543])

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
            if dkort2[1:] == "1":
                if dealer < 12:
                    dealer += 10
            dkort2D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 475])
        window.blit(dpoints, [1700, 543])
        pygame.display.update()
        if  dealer > spelare:
            stand=1
            reset=1
        elif dealer > 16:
            stand=1
            reset=1
        else:
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
            if dkort3[1:] == "1":
                if dealer < 12:
                    dealer += 10
            dkort3D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 475])
        window.blit(dpoints, [1700, 543])
        pygame.display.update()
        if  dealer > spelare:
            stand=2
            reset=1
        elif dealer > 16:
            stand=2
            reset=1
        else:
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
            if dkort4[1:] == "1":
                if dealer < 12:
                    dealer += 10
            dkort4D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 475])
        window.blit(dpoints, [1700, 543])
        pygame.display.update()
        if  dealer > spelare:
            stand=3
            reset=1
        elif dealer > 16:
            stand=3
            reset=1
        else:
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
            if dkort5[1:] == "1":
                if dealer < 12:
                    dealer += 10
            dkort5D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 475])
        window.blit(dpoints, [1700, 543])
        pygame.display.update()
        if  dealer > spelare:
            stand=4
            reset=1
        elif dealer > 16:
            stand=4
            reset=1
        else:
            time.sleep(1)
            stand=5
    if stand == 5:
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
        dx+=250
        window.blit(dkort6_, [dx, dy])
        if dkort6D == 0:
            dealer += int(dkort6[1:])
            if dkort6[1:] == "11":
                dealer += -1
            if dkort6[1:] == "12":
                dealer += -2
            if dkort6[1:] == "13":
                dealer += -3
            if dkort6[1:] == "1":
                if dealer < 12:
                    dealer += 10
            dkort6D=1
        dpoints = bigfont.render(str(dealer), True, color)
        window.blit(redchip, [1632, 475])
        window.blit(dpoints, [1700, 543])
        reset=1


    # Skapar ny kortlek om kortleken är tom
    if len(kortlek) < 13:
        kortlek =  ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
                    "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
                    "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13",
                    "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"]

    # Avslutar spelet om spelaren är tjock
    if spelare > 20:
        if stand == 0:
            if reset1 == 0:
                stand=1
                reset1=1

    # Vinstodds
    if reset == 1:
        if reset3 == 0:
            if spelare == 21 and dealer != 21:
                if hit == 0:
                    if (skort[1:] == "1") or (skort2[1:] == "1"):
                        pengar+=bid
                        bid=bid*2
                        pengar+=bid
                        reset3=1
                else:
                    bid=bid*2
                    pengar+=bid
                    reset3=1
            elif spelare > 21:
                reset3=1
            elif (spelare == dealer):
                pengar+=bid
                reset3=1
            elif (dealer > 21):
                bid=bid*2
                pengar+=bid
                reset3=1
            elif (spelare > dealer) and spelare <= 21:
                bid=bid*2
                pengar+=bid
                reset3=1
            bid=0

    pygame.display.flip()
    clock.tick(30)