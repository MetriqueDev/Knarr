import pygame
from classes.card import Card
from classes.board import Board
from classes.boat import Boat
from classes.player import Player
from classes.destination import Card_bateau
from classes.menu import Menu
from classes.package import Package



class Game():
    def __init__(self,players):
        self.nbr_player=len(players)
        self.players=players
        self.package=Package(self.nbr_player)
        self.package.shuffle()
        self.board=Board()
        self.turn=0
  
    def init_image(self):
        #Background
        self.background_load = pygame.image.load(".\\images\\fond.jpg").convert()
        self.background= pygame.transform.scale(self.background_load, (1600,900))

    def init_game(self):
        for player in range(self.players):
            self.player.init_boat()

    def afficher(self,screen,joueur_name):
        screen.blit(background,(0,0))

        #afficher board
        board.print(screen)
        board.update_renome_pos(screen,players)
        board.update_score_pos(screen,players)
        for player in range(self.players):

            if player.name == joueur_name :
                player.boat.print(screen)
                player.print_equipage(screen)


