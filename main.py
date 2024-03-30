import pygame
from  classes.card import Card
from  classes.board import Board
from  classes.boat import Boat
from  classes.player import Player
from  classes.card_bateau import Card_bateau

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1600,900),pygame.RESIZABLE) #(1280, 720))
pygame.display.set_caption("Knarr")
clock = pygame.time.Clock()
running = True

pygame.mixer.music.load(".\musique\\Dragonborn.mp3")
#pygame.mixer.music.play()

#icone
icon_load = pygame.image.load(".\images\\icon.png").convert_alpha()
icon = pygame.transform.scale(icon_load, (200,200))
pygame.display.set_icon(icon)


#Background
background_load = pygame.image.load(".\images\\fond.jpg").convert()
background= pygame.transform.scale(background_load, (1600,900))


pygame.mouse.set_cursor(*pygame.cursors.diamond)

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


card_echange=Card_bateau("echange_1")
card_echange.init_image()



players=[Player("Vladimir Ilitch",50)]
players[0].game_init()
players[0].info()





musique = True

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        background= pygame.transform.scale(background_load, (screen.get_width(),screen.get_height()))
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                players[0].add_score(1)
            elif event.key == pygame.K_DOWN:
                players[0].add_score(-1)
            elif event.key == pygame.K_SPACE:
                if musique == True:
                    musique = False
                    pygame.mixer.music.pause()
                elif musique == False:
                    musique = True
                    pygame.mixer.music.play()


    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE

    #afficher les cartes
    for i in range(len(cards)):
        cards[i].print(screen,(int(screen.get_width()/2-len(cards)*125/2)+i*125,screen.get_height()-400))



    board.print(screen)
    board.update_renome_pos(screen,players)
    board.update_score_pos(screen,players)
    boat.print(screen)


    card_echange.print(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) # limits FPS to 60

pygame.quit()