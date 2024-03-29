import pygame
import sys
import time
import random
from kortlek import * 

pygame.init()

# bakgrund
width = 1920
height = 1080
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('BlackJack-table5.png').convert()
bg_img = pygame.transform.scale(bg_img,(width,height))

# Laddar in några bilder
blank = pygame.image.load(kortlek_map["blank"]).convert_alpha()
redchip = pygame.image.load('redchip.png').convert_alpha()
redchip = pygame.transform.scale(redchip, (200, 200)) 
bluechip = pygame.image.load('bluechip.png').convert_alpha()
bluechip = pygame.transform.scale(bluechip, (200, 200)) 

pygame_icon = pygame.image.load('redchip.png')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("Black Jack")

clock = pygame.time.Clock()

# Färger
black = (0,0,0)
white = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
bg_color = (211, 211, 211)

# Font
smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont("arial",65)
textfont = pygame.font.SysFont("arial",40)
font1 = pygame.font.SysFont("arial",20)

# Laddar in all text
text = smallfont.render('Hit' , True , white)
text2 = smallfont.render('Stand' , True , white)
text3 = smallfont.render('Double' , True , white)
text4 = smallfont.render('Next' , True , white)
text5 = smallfont.render('Bid +10' , True , white)
text55 = smallfont.render('Lock Bid' , True , white)
text555 = smallfont.render('Bid -10' , True , white)
text6 = bigfont.render('Money:' , True , white)
text7 = bigfont.render('Bid:' , True , white)
text8 = textfont.render('Player:' , True , white)
text9 = textfont.render('Dealer:' , True , white)
text10 = smallfont.render('Classic' , True , white)
text11 = bigfont.render('BLACKJACK' , True , black)
text12 = font1.render(' Made by: Einar' , True , black)
text13 = smallfont.render('Rules' , True , white)
text14 = smallfont.render('Push 22' , True , white)


sy=100 # Y koordinaten för spelaren kort
dy=450 # Y koordinaten för dealerns kort

blackjack = 0


while True:

    # Run loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        # Stänger av spelet om man trycker escape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

        # knappar
        if event.type == pygame.MOUSEBUTTONDOWN:

            if width/2-70 <= mouse[0] <= width/2-70+140 and height-400 <= mouse[1] <= height-360: # Classic
                blackjack = 1
                spelare = 0
                spelare_lista = []
                dealer = 0
                dealer_lista = []
                hit=-1
                stand=-1
                reset=0
                reset1=0
                reset2=0
                reset3=0
                reset4=0
                pengar=100
                bid=0
                runda=1
                ess = 0
                ess2 = 0
                kortlek =  ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
                            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
                            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13",
                            "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"] * 8

                  
            if blackjack == 1:

                if width/2 <= mouse[0] <= width/2+140 and height-45 <= mouse[1] <= height-5: # Hit
                    if bid > 1:
                        if hit < 4:
                            if stand == 0:
                                kort = random.choice(kortlek)
                                kortlek.remove(kort)
                                spelare_lista.append(kort)
                                spelare += int(kort[1:])
                                if kort[1:] == "11":
                                    spelare += -1
                                if kort[1:] == "12":
                                    spelare += -2
                                if kort[1:] == "13":
                                    spelare += -3
                                if kort[1:] == "1":
                                    if spelare < 12:
                                        spelare += 10

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
                                    kort = random.choice(kortlek)
                                    kortlek.remove(kort)
                                    spelare_lista.append(kort)
                                    spelare += int(kort[1:])
                                    if kort[1:] == "11":
                                        spelare += -1
                                    if kort[1:] == "12":
                                        spelare += -2
                                    if kort[1:] == "13":
                                        spelare += -3
                                    if kort[1:] == "1":
                                        if spelare < 12:
                                            spelare += 10
                                    stand=1

                if reset == 1:
                    if width/2 <= mouse[0] <= width/2+140 and height-245 <= mouse[1] <= height-205: # Next
                        if pengar > 0:
                            spelare = 0
                            dealer = 0
                            hit=-1
                            stand=-1
                            bid=0
                            runda+=1
                            reset=0
                            reset1=0
                            reset2=0
                            reset3=0
                            reset4=0
                            spelare_lista=[]
                            dealer_lista=[]
                            ess = 0
                            ess2 = 0
                        else:
                            blackjack = 0

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



    # Visar bakgrund
    window.blit(bg_img, [0, 0])

    mouse = pygame.mouse.get_pos()

    if blackjack == 0:

        # Start meny

        pygame.draw.rect(window,bg_color,[500,300,920,480])

        if width/2-70 <= mouse[0] <= width/2-70+140 and height-400 <= mouse[1] <= height-360: # Classic
            pygame.draw.rect(window,color_light,[width/2-70,height-400,140,40]) 
        else:
            pygame.draw.rect(window,color_dark,[width/2-70,height-400,140,40])
        window.blit(text10 , (width/2-70+22,height-400))

        if width/2-70+300 <= mouse[0] <= width/2-70+300+140 and height-400 <= mouse[1] <= height-360: # Push 22
            pygame.draw.rect(window,color_light,[width/2-70+300,height-400,140,40]) 
        else:
            pygame.draw.rect(window,color_dark,[width/2-70+300,height-400,140,40])
        window.blit(text14 , (width/2-70+300+17,height-400))

        if width/2-70-300 <= mouse[0] <= width/2-70-300+140 and height-400 <= mouse[1] <= height-360: # Rules
            pygame.draw.rect(window,color_light,[width/2-70-300,height-400,140,40]) 
        else:
            pygame.draw.rect(window,color_dark,[width/2-70-300,height-400,140,40])
        window.blit(text13 , (width/2-70-300+35,height-400))

        window.blit(text11 , (width/2-180,height-600)) # BLACKJACK
        window.blit(text12 , (500,750)) # Made by


    if blackjack == 1:

        # Visa kortens värde
        if stand >= 0:
            window.blit(bluechip, [1632, 125])
            spoints = bigfont.render(str(spelare), True, white)
            window.blit(spoints, [1700, 193])
            window.blit(redchip, [1632, 475])
            dpoints = bigfont.render(str(dealer), True, white)
            window.blit(dpoints, [1700, 543])

        # Visa pengar och bid
        window.blit(text6, [100, 750]) # Money:
        window.blit(text7, [400, 750]) # Bid:
        pengarD = bigfont.render(str(pengar), True, white)
        window.blit(pengarD, [100, 850])
        bidD = bigfont.render(str(bid), True, white)
        window.blit(bidD, [400, 850])

        if hit >= 0:
            window.blit(text8, [100, 50]) # Player:
            window.blit(text9, [100, 400]) # Dealer:

        # Visa antal rundor
        rundortext = textfont.render("Runda:", True, white)
        window.blit(rundortext, [1680, 75])
        rundor = textfont.render(str(runda), True, white)
        window.blit(rundor, [1815, 75])


        # Knappar
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


        # Spelarens 2 startkort
        if reset2 == 0:
            for startkort in range(2):
                kort = random.choice(kortlek)
                kortlek.remove(kort)
                spelare_lista.append(kort)
                spelare += int(kort[1:])
                if kort[1:] == "11":
                    spelare += -1
                if kort[1:] == "12":
                    spelare += -2
                if kort[1:] == "13":
                    spelare += -3
                if kort[1:] == "1":
                    if spelare < 12:
                        spelare += 10
                        ess += 1
            reset2=1

        # Printar spelarens kort
        if hit >= 0:
            for index in range(len(spelare_lista)):
                kort_load = pygame.image.load(kortlek_map[spelare_lista[index]]).convert_alpha()
                window.blit(kort_load, [100 + 250*index, sy])
                
                # Gör att ess är värt 1 om handen är över 21
                if spelare > 21:
                    if spelare_lista[index][1:] == "1":
                        if ess > 0:
                            spelare += -10
                            ess += -1



        # Dealer startkort
        if stand == 0:
            if reset4 == 0:
                kort2 = random.choice(kortlek)
                kortlek.remove(kort2)
                dealer_lista.append(kort2)
                dealer += int(kort2[1:])
                if kort2[1:] == "11":
                    dealer += -1
                if kort2[1:] == "12":
                    dealer += -2
                if kort2[1:] == "13":
                    dealer += -3
                if kort2[1:] == "1":
                    if dealer < 12:
                        dealer += 10
                reset4=1
            kort2_ = pygame.image.load(kortlek_map[kort2]).convert_alpha()
            window.blit(kort2_, [100, dy])
            window.blit(blank, [350, dy])

        # Dealer dra kort
        if (stand == 1) or (reset1 == 1):
            if dealer < 17:
                kort2 = random.choice(kortlek)
                kortlek.remove(kort2)
                dealer_lista.append(kort2)
                dealer += int(kort2[1:])
                if kort2[1:] == "11":
                    dealer += -1
                if kort2[1:] == "12":
                    dealer += -2
                if kort2[1:] == "13":
                    dealer += -3
                if kort2[1:] == "1":
                    if dealer < 12:
                        dealer += 10

            # Printar dealerns kort
            for index in range(len(dealer_lista)):
                kort_load2 = pygame.image.load(kortlek_map[dealer_lista[index]]).convert_alpha()
                window.blit(kort_load2, [100 + 250*index, dy])

                # Gör att ess är värt 1 om handen är över 21
                if dealer > 21:
                    if dealer_lista[index][1:] == "1":
                        if ess2 > 0:
                            dealer += -10
                            ess2 += -1


        # Avslutar spelat när dealern har tagigt sina kort
        if (stand == 1) or (reset1 == 1):
            if dealer > spelare:
                reset=1
            elif dealer > 16:
                reset=1

        # Skapar ny kortlek om kortleken är tom
        if len(kortlek) < 13:
            kortlek =  ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
                        "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
                        "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13",
                        "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"] * 8

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
                    if len(spelare_lista) == 2:
                        if (spelare_lista[0][1:] == "1") or (spelare_lista[1][1:] == "1"):
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