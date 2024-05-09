import pygame
from classes.card import Card
from classes.board import Board
from classes.boat import Boat
from classes.player import Player
from classes.destination import Card_bateau
from classes.menu import Menu
from classes.package import Package
from classes.package_destination import Package_Destination


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
        
        self.destination_pioche=Package_Destination()
        self.boat=Boat()
        self.liste=[]

    def init_cards(self):
        pass
    
    def init_pygame(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN) #(1280, 720))
        pygame.display.set_caption("Knarr")
        self.clock = pygame.time.Clock()
        self.step = "Menu"
        pygame.mixer.music.load(".\\musique\\Dragonborn.mp3")
        pygame.mixer.music.play()
        self.musique=True
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        #Fermeture
        self.fermeture_size=30
        self.fermeture_load = pygame.image.load(".\\images\\gui\\stop.png").convert_alpha()
        self.fermeture= pygame.transform.scale(self.fermeture_load, (self.fermeture_size,self.fermeture_size))
        self.fermeture_rect=self.fermeture.get_rect()

    def afficher(self,screen,joueur_name):
        screen.blit(self.background,(0,0))

        #afficher board
        self.board.print(screen)
        self.board.update_renome_pos(screen,self.players)
        self.board.update_score_pos(screen,self.players)
        for player in range(self.players):
            if player.name == joueur_name :
                player.boat.print(screen)
                player.print_equipage(screen)
        
        self.boat.print(screen)
        self.boat.print_object(screen,self.liste)

    def event_handler(self,screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        self.destination_pioche.print_pioche_dest(screen)
        self.destination_pioche.dragndrop(screen,event) # type: ignore


