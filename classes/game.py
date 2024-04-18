import pygame
from card import Card
from board import Board
from boat import Boat
from player import Player
from destination import Card_bateau
from menu import Menu
from package import Package

class Game():
    def __init__(self,players):
        self.nbr_player=len(players)
        self.players=players
        self.package=Package(self.nbr_player).shuffle()
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


