import pygame
from classes.card import Card
from classes.board import Board
from classes.boat import Boat
from classes.player import Player
from classes.destination import Card_bateau
from classes.menu import Menu
from classes.package import Package
from classes.hand import Hand

pygame.init()

# pygame setup

screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN) #(1280, 720))
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


#fermeture
fermeture_size=30
fermeture_load = pygame.image.load(".\\images\\stop.png").convert()
fermeture= pygame.transform.scale(fermeture_load, (fermeture_size,fermeture_size))
fermeture_rect=fermeture.get_rect()

#Curseur
pygame.mouse.set_cursor(*pygame.cursors.diamond)

#-------------------------------------------------------------------------------------


menu = Menu("a")



#initialisation des cartes (impropre)
cards=[]
cards2=[]
card_types=["bleu1","bleu2","bleu3","bleu4",    "jaune1","jaune2","jaune3","jaune4",    "rouge1","rouge2","rouge3","rouge4",    "vert1","vert2","vert3","vert4",    "violet1","violet2","violet3","violet4"]
card_gains=["renommee","recrue","victoire","bracelet","recrue","victoire","bracelet","renommee","renommee","bracelet","recrue","victoire","victoire","renommee","bracelet","recrue","bracelet","renommee","recrue","victoire"]
card_num=[0,0,3,3,3,0,4,0,3,0,0,0,0,0,4,0,0,3,0,4]
for i in range(len(card_num)):
    card=Card(card_types[i],card_gains[i],card_num[i])
    card.init_image()
    if i <5:
        cards.append(card)
    cards2.append(card)



#Initialisation propre
nbr_player=1

board = Board()
boat = Boat()
players=[]
for i in range(nbr_player):
    players.append(Player("Vladimir Ilitch",50))
    players[i].game_init()
    players[i].info()


for card in cards2:
    players[0].add_equipage(card)

#focntion de jeu
def game_process(players):
    for player in players:
        player.add_renome_to_score()

#initialisation cartes destinations
card_e=[]
card_id=['1','2','3','4','5','6']
card_cout=[('violet', 'violet'),('vert', 'vert'),('rouge', 'rouge'),
('different', 'different', 'different'),('different', 'different', 'different'),('vert', 'vert')]
card_gain=[('pioche'),('recrue','recrue'),('recrue'),('bracelet'),('bracelet','recrue','pioche'),('bracelet','recrue')]
card_gain_col=['raf','raf','raf','raf','raf','raf']
card_ech=[True,True,True,False,False,False]
liste=[]

for i in range(6):
    card=Card_bateau(card_id[i], card_cout[i], card_gain[i], card_gain_col[i], echange=card_ech[i])
    card.init_image()
    card_e.append(card)


verso=[]
verso.append(Card_bateau(1, "rien", "rien", "rien", echange=True))
verso.append(Card_bateau(1, "rien", "rien", "rien", echange=False))
verso[0].face="V"
verso[1].face="V"

package=Package(4)
package.shuffle()


active_card=None
mouse_pos=[0,0]
while running:

    # RENDER YOUR GAME HERE
    screen.blit(background,(0,0))

    
    #Afficher les cartes
    for i in range(len(cards)):
        cards[i].print(screen,(int(screen.get_width()/2-len(cards)*125/2)+i*125, 310))

    for player in players:
        player.print_equipage(screen)

    #Afficher board
    board.print(screen)
    ##Afficher points bateau
    board.update_renome_pos(screen,players)
    board.update_score_pos(screen,players)

    #Afficher bateau
    boat.print(screen)
    boat.print_object(screen,liste)


    #Afficher carte échange et influence
    #+315
    verso[0].print(screen, (5,5))
    verso[1].print(screen, (5,155))

    for i in range(3):
        card_e[i].print(screen, (int(i*300+305),5))
    for i in range(3):
        card_e[i+3].print(screen, (int(i*300+305),155))

    package.print_package(screen)

    #afficher la main
      #hand à initialiser "Hand.afficher_main(self, screen)""


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
            if fermeture_rect.collidepoint(event.pos):
                print("stop")
                pygame.quit()
                exit()

            if step =="Menu":
                step=menu.menu_interaction(event.pos)
                #if step!="Menu":
                    #step="other"
                if step=="inscription":
                    step="other"
            else:
                if event.button == 1:
                    for num, card in enumerate(card_e):
                        if card.front_rect.collidepoint(event.pos):
                            active_card=num
                            mouse_x, mouse_y = event.pos

                            #position de la souris sur l'image
                            offset_x=mouse_x-card_e[active_card].pos[0]
                            offset_y=mouse_y-card_e[active_card].pos[1]
        
        elif event.type == pygame.MOUSEBUTTONUP:            
            if event.button==1:
                if screen.get_width()/2-100<event.pos[0]<screen.get_width()/2+100 and event.pos[1]>screen.get_height()-200 and active_card != None:
                    boat.Cartes_desti(card_e[active_card], liste)
                    active_card=None
                else:
                    active_card=None

        elif event.type == pygame.MOUSEMOTION:
            if active_card != None:
                card_e[active_card].print(screen,(event.pos[0]-offset_x,event.pos[1]-offset_y))
                print((event.pos[0]-offset_x,event.pos[1]-offset_y))
                print((screen.get_width()/2-100,screen.get_width()/2+100))
                print((screen.get_height()/2+100,screen.get_height()/2-100))
                
    #afficher l'image à la souris pendant le drag and drop si on bouge pas
    if active_card !=None:
        card_e[active_card].print(screen,(event.pos[0]-offset_x,event.pos[1]-offset_y)) 

    #menu
    if step == "Menu":
        menu.print(screen)


    fermeture_rect.x=int(screen.get_width()-fermeture_size-10)
    fermeture_rect.y=10
    screen.blit(fermeture,(fermeture_rect.x,fermeture_rect.y))

    pygame.display.flip()

    clock.tick(60) # limits FPS to 60



    
pygame.quit()