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
from classes.menu_test import Button

#PyGame setup
pygame.init()
screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE) #(1280, 720))
players=['Tristonks']
pygame.display.set_caption("Knarr")
jeu=game.Game(players)
jeu.init_game()
jeu.init_cards()
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
main_menu_bgload=pygame.image.load(".\\images\\Menu\\background.png").convert()
main_menu_bg = pygame.transform.scale(main_menu_bgload,(1920,1080))

#Fermeture
fermeture_size=30
fermeture_load = pygame.image.load(".\\images\\gui\\stop.png").convert_alpha()
fermeture= pygame.transform.scale(fermeture_load, (fermeture_size,fermeture_size))
fermeture_rect=fermeture.get_rect()

connexion_image_load=pygame.image.load(f".\\images\\MENU\\connexion.png").convert_alpha() 
connexion_boutton= Button(200,200,connexion_image_load,0.5)
inscription_image_load=pygame.image.load(f".\\images\\MENU\\inscrire.png").convert_alpha()
inscription_button= Button(200,350,inscription_image_load,0.5)
option_image_load=pygame.image.load(f".\\images\\MENU\\option.png").convert_alpha() 
option_boutton= Button(200,500,option_image_load,0.5)
retour_image_load=pygame.image.load(f".\\images\\MENU\\empty.png").convert_alpha() 
retour_boutton= Button(750,200,retour_image_load,0.5)

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

package=Package(4)
package.shuffle()

board = Board()
boat = Boat()
players=[]
for i in range(nbr_player):
    players.append(Player("Vladimir Ilitch",50))
    players[i].game_init()
    players[i].info()
    for el in range(3):
     package.pioche_hand(players[i].hand)


for card in cards2:
    players[0].add_equipage(card)

#focntion de jeu
def game_process(players):
    for player in players:
        player.add_renome_to_score()

destination=Package_Destination()
liste=[]


active_card=None
mouse_pos=[0,0]

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
        if inscription_button.draw(screen):
            step="inscription"
        if option_boutton.draw(screen):
            step="option"
    if step == "play":
        screen.blit(background, (0,0))
        boat.print(screen)
        boat.print_object(screen,liste)
        destination.print_pioche_dest(screen)
        board.print(screen)
        board.update_renome_pos(screen,players)
        board.update_score_pos(screen,players)
        boat.print_object(screen,liste)
        if retour_boutton.draw(screen):
            print(step)
            step="main"
    if step == "inscription":
        screen.blit(main_menu_bg,(0,0))
        img = font.render("Menu inscription",True,TEXT_COL)
        screen.blit(img,(400,500))
    if step == "option":
        screen.blit(main_menu_bg,(0,0))
        img = font.render("Menu d'option",True,TEXT_COL)
        screen.blit(img,(400,500))
        print(step)
        if retour_boutton.draw(screen):
            print(step)
            step="main"


    fermeture_rect.x=int(screen.get_width()-fermeture_size-10)
    fermeture_rect.y=10
    #screen.blit(fermeture,(fermeture_rect.x,fermeture_rect.y))

    for event in pygame.event.get():
            background= pygame.transform.scale(background_load, (screen.get_width(),screen.get_height()))
            if event.type == pygame.QUIT:
                running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()