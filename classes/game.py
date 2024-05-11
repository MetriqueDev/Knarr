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


class Game():
    def __init__(self,players):
        self.nbr_player=len(players)
        self.players=players
        self.package=Package(self.nbr_player)
        print(self.package.package)
        self.package.shuffle()
        self.board=Board()
        self.turn=0

    def init_image(self):
        #Background
        self.background_load = pygame.image.load(".\\images\\fond.jpg").convert()
        self.background= pygame.transform.scale(self.background_load, (1600,900))

    def init_game(self):
        self.liste=[]
        print(self.package.package)
        self.board.init_cartes(self.package)
        self.destination=Package_Destination()
        self.boat = Boat()
        for player in self.players:
            for i in range(3):
                e=self.package.pioche_hand(player.hand)
                if e== False:
                    print("plus de cartes dans package")
        
        

    
    def afficher(self,screen,liste):
        screen.blit(self.background, (0,0))

        self.boat.print(screen)
        self.boat.print_object(screen,liste)
        self.boat.print_object(screen,destination.liste)
        
        self.destination.print_pioche_dest(screen)
        
        self.board.print(screen)
        self.board.recrutement_print(screen)
        self.board.update_renome_pos(screen,self.players)
        self.board.update_score_pos(screen,self.players)

    def update(self):

        for player in self.players:
            player.add_renome_to_score()

        

    def event_handler(self,event):
        self.destination.dragndrop_echange(screen,event,boat)
        self.destination.dragndrop_influence(screen,event,boat)
        self.board.dragndrop_recrutement(screen,event,hand,jeu.package)