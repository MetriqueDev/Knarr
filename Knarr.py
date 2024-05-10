import pygame
from classes.card import Card
from classes.board import Board
from classes.boat import Boat
from classes.player import Player
from classes.destination import Card_bateau
from classes.menu import Menu
from classes.package import Package
from classes.hand import Hand
from classes.package_destination import Package_Destination
import classes.game as game
from classes.input import Button , Input

#PyGame setup
pygame.init()
screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE) #(1280, 720))
players=['Tristonks']
pygame.display.set_caption("Knarr")

running=True
clock = pygame.time.Clock()
step="main"
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)


#Musique
#pygame.mixer.music.load(".\\musique\\Dragonborn.mp3")
#pygame.mixer.music.play()
#musique=True

#Background
background_load = pygame.image.load(".\\images\\fond.jpg").convert()
background= pygame.transform.scale(background_load, (1920,1080))
main_menu_bgload=pygame.image.load(".\\images\\gui\\background.png").convert()
main_menu_bg = pygame.transform.scale(main_menu_bgload,(1920,1080))

#Fermeture
fermeture_size=30
fermeture_load = pygame.image.load(".\\images\\gui\\stop.png").convert_alpha()
fermeture= pygame.transform.scale(fermeture_load, (fermeture_size,fermeture_size))
fermeture_boutton= Button(screen.get_width()-40,10,fermeture,1)


connexion_image_load=pygame.image.load(f".\\images\\gui\\connexion.png").convert_alpha() 
connexion_boutton= Button(200,200,connexion_image_load,0.5)
inscription_image_load=pygame.image.load(f".\\images\\gui\\inscrire.png").convert_alpha()
inscription_button= Button(200,350,inscription_image_load,0.5)
option_image_load=pygame.image.load(f".\\images\\gui\\option.png").convert_alpha() 
option_boutton= Button(200,500,option_image_load,0.5)

retour_image_load=pygame.image.load(f".\\images\\gui\\empty.png").convert_alpha() 
retour_boutton= Button(750,500,retour_image_load,0.2)



#Initialisation propre
nbr_player=1



destination=Package_Destination()
liste=[]


active_card=None
mouse_pos=[0,0]


#focntion de jeu
def game_process(players):
    for player in players:
        player.add_renome_to_score()


while running:
    screen.blit(background, (0,0))

    #for i in range(len(cards)):
    #    cards[i].print(screen,(int(screen.get_width()/2-len(cards)*125/2)+i*125, 310))

    #for player in players:
        #   player.print_equipage(screen)
            #  Hand.afficher_main(screen)

    #Afficher board
    #board.print(screen)

    ##Afficher points bateau
    #board.update_renome_pos(screen,players)
    #board.update_score_pos(screen,players)

    #Afficher bateau
    #boat.print(screen)
    #boat.print_object(screen,liste)
    #destination.print_pioche_dest(screen)
    #package.print_package(screen)

    #boat.print_object(screen,liste)

    if step == "main":
        screen.blit(main_menu_bg,(0,0))
        if connexion_boutton.draw(screen):
            step="play"
            jeu=game.Game(players)
            jeu.init_game()
            jeu.init_cards()
            package=Package(4)
            package.shuffle()
            board = Board()
            boat = Boat()
            destination.liste=[]
            players=[]
            for i in range(nbr_player):
                players.append(Player("Vladimir Ilitch",50))
                players[i].game_init()
                players[i].info()
                for el in range(3):
                    card= package.pioche_hand(players[i].hand)
        if inscription_button.draw(screen):
            step="inscription"
            inscription_title=font.render("Menu inscription",True,TEXT_COL)
            name_label=font.render("Votre nom:",True,TEXT_COL)
            input_name_image_load=pygame.image.load(f".\\images\\gui\\input.png").convert_alpha() 
            input_name_boutton= Input(400,250,input_name_image_load,2,font,TEXT_COL)
            mdp_label=font.render("Votre mot de passe:",True,TEXT_COL)
            input_mdp_image_load=pygame.image.load(f".\\images\\gui\\input.png").convert_alpha() 
            input_mdp_boutton= Input(400,450,input_name_image_load,2,font,TEXT_COL)


        if option_boutton.draw(screen):
            step="option"
    if step == "play":
        screen.blit(background, (0,0))
        boat.print(screen)
        boat.print_object(screen,destination.liste)
        destination.print_pioche_dest(screen)
        board.print(screen)
        board.update_renome_pos(screen,players)
        board.update_score_pos(screen,players)
        boat.print_object(screen,liste)
        for event in pygame.event.get():
            destination.dragndrop_echange(screen,event,boat)
            destination.dragndrop_influence(screen,event,boat)
            destination.Ajout_boat_echange(screen,event,boat)
        
        if retour_boutton.draw(screen):
            print(step)
            step="main"
        if destination.active_card_e != None:
            destination.echange[destination.active_card_e].print(screen,(event.pos[0]-destination.offset_x,event.pos[1]-destination.offset_y))
        if destination.active_card_i != None:
            destination.influence[destination.active_card_i].print(screen,(event.pos[0]-destination.offset_x,event.pos[1]-destination.offset_y))
    if step == "inscription":
        screen.blit(main_menu_bg,(0,0))

        screen.blit(inscription_title,(400,100))
        screen.blit(name_label,(400,200))
        input_name_boutton.draw(screen)

        screen.blit(mdp_label,(400,400))
        input_mdp_boutton.draw(screen)

    if step == "option":
        screen.blit(main_menu_bg,(0,0))
        img = font.render("Menu d'option",True,TEXT_COL)
        screen.blit(img,(400,500))
        print(step)
        if retour_boutton.draw(screen):
            print(step)
            step="main"


    if fermeture_boutton.draw(screen):
        break

    for event in pygame.event.get():
        if step == "inscription":
            input_name_boutton.write(event)
            input_mdp_boutton.write(event)


        background= pygame.transform.scale(background_load, (screen.get_width(),screen.get_height()))
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()