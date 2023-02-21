import pygame
from kortlek import * 

pygame.init()

width = 1200
height = 661
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('blackjack.jpg').convert()
bg_img = pygame.transform.scale(bg_img,(width,height))

kort = pygame.image.load(kortlek_map["c2"]).convert()
blank = pygame.image.load(kortlek_map["blank"]).convert()

pygame.display.set_caption("Black Jack")

clock = pygame.time.Clock()

while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    window.blit(bg_img, [0, 0])
    window.blit(kort, [0, 0])
    window.blit(blank, [250, 0])
	# screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)