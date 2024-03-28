import pygame
from  classes.card import Card
from  classes.board import Board
from  classes.boat import Boat
from  classes.player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1600,900)) #(1280, 720))
clock = pygame.time.Clock()
running = True

#pygame.mixer.music.load()
#pygame.mixer.music.play()
background_load = pygame.image.load(f".\images\\fond.jpg").convert_alpha()
background= pygame.transform.scale(background_load, (1600,900))

#initialisation des cartes
cards=[]
card_types=["bleu1","bleu2","bleu3","bleu4"]
for card_type in card_types:
    card=Card(card_type)
    card.init_image()
    cards.append(card)


board = Board()
board.init_image()
boat = Boat()
boat.init_image()



players=[Player("Vladimir Ilitch",50)]
players[0].game_init()
players[0].info()



while running:
    screen.blit(background,(0,0))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                players[0].add_renome(1)
            elif event.key == pygame.K_DOWN:
                players[0].add_renome(-1)
            print(players[0].get_renome())

    # fill the screen with a color to wipe away anything from last frame


    # RENDER YOUR GAME HERE

    #afficher les cartes
    for i in range(len(cards)):
        cards[i].print(screen,(int(1600/2-len(cards)*125/2)+i*125,500))



    board.print(screen, (200,70))
    board.update_renome_pos(screen,players)
    boat.print(screen, (600,700))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) # limits FPS to 60

pygame.quit()