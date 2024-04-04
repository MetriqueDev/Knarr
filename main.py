import pygame
from  classes.card import Card
from  classes.board import Board
from  classes.boat import Boat
from  classes.player import Player
from  classes.destination import Card_bateau
from  classes.destination import liste
from  classes.menu import Menu

pygame.init()

# pygame setup
screen = pygame.display.set_mode((1600,900),pygame.RESIZABLE) #(1280, 720))
pygame.display.set_caption("Knarr")
clock = pygame.time.Clock()
running = True
step = "Menu"

#Musique
pygame.mixer.music.load(".\\musique\\Dragonborn.mp3")
#pygame.mixer.music.play()
musique = True

#Background
background_load = pygame.image.load(".\\images\\fond.jpg").convert()
background= pygame.transform.scale(background_load, (1600,900))

#Curseur
pygame.mouse.set_cursor(*pygame.cursors.diamond)

#-------------------------------------------------------------------------------------


menu = Menu("a")



#initialisation des cartes (impropre)
cards=[]
card_types=["bleu1","bleu2","bleu3","bleu4",    "jaune1","jaune2","jaune3","jaune4",    "rouge1","rouge2","rouge3","rouge4",    "vert1","vert2","vert3","vert4",    "violet1","violet2","violet3","violet4"]
card_num=[0,0,3,3,3,0,4,0,3,0,0,0,0,0,4,0,0,3,0,4]
for i in range(5):
    card=Card(card_types[i],card_num[i])
    cards.append(card)




e,i=[],[]
liste(e,i)
for element in e:
    Card_bateau(element,True)
for element in i:
    Card_bateau(element,False)

#Initialisation propre
nbr_player=1

board = Board()
boat = Boat()
players=[]
for i in range(nbr_player):
    players.append(Player("Vladimir Ilitch",50))
    players[i].game_init()
    players[i].info()


#focntion de jeu
def game_process(players):
    for player in players:
        player.add_renome_to_score()




while running:
    
    #Gestion des events
    for event in pygame.event.get():
        background= pygame.transform.scale(background_load, (screen.get_width(),screen.get_height()))#Mise à jour de la taille du fond ecran a chaque action
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            #Gestion pointq
            if event.key == pygame.K_UP:
                players[0].add_score(1)
            elif event.key == pygame.K_DOWN:
                players[0].add_score(-1)

            #Gestion musique (Temporaire)
            elif event.key == pygame.K_SPACE:
                if musique == True:
                    musique = False
                    pygame.mixer.music.pause()
                elif musique == False:
                    musique = True
                    pygame.mixer.music.play()

        if event.type == pygame.MOUSEBUTTONDOWN:
            clic=menu.menu_interaction(event.pos)
            if clic :
                step="other"
        

    # RENDER YOUR GAME HERE
    screen.blit(background,(0,0))

    
    #Afficher les cartes
    for i in range(len(cards)):
        cards[i].print(screen,(int(screen.get_width()/2-len(cards)*125/2)+i*125,screen.get_height()-400))



    #Afficher board
    board.print(screen)
    ##Afficher points bateau
    board.update_renome_pos(screen,players)
    board.update_score_pos(screen,players)

    #Afficher bateau
    boat.print(screen)
    boat.print_object(screen)


    #Afficher carte échange et influence

    #menu
    if step == "Menu":
        menu.print(screen)

    pygame.display.flip()

    clock.tick(60) # limits FPS to 60

    
pygame.quit()