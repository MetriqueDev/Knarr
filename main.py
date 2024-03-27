import pygame
from  fichiers.card import Card

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,500)) #(1280, 720))
clock = pygame.time.Clock()
running = True

#initialisation des cartes
cards=[]
card_types=["bleu1","bleu2","bleu3","bleu4"]
for card_type in card_types:
    card=Card(card_type)
    card.init_image()
    cards.append(card)

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")

    # RENDER YOUR GAME HERE

    #afficher les cartes
    for i in range(len(cards)):
        cards[i].print(screen,(i*125,0))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) # limits FPS to 60

pygame.quit()