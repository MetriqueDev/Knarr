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
        self.destination_pioche=Package_Destination()
        self.boat=Boat()
        self.liste=[]
        #for player in self.players:
        #    player.boat.init_boat()

    def init_cards(self):
        pass
    
#    def init_pygame(self):
#        pygame.display.set_caption("Knarr")
#        self.clock = pygame.time.Clock()
#        pygame.mixer.music.load(".\\musique\\Dragonborn.mp3")
#        pygame.mixer.music.play()
#        self.musique=True
#        pygame.mouse.set_cursor(*pygame.cursors.diamond)
#        #Fermeture
#        self.fermeture_size=30
#        self.fermeture_load = pygame.image.load(".\\images\\gui\\stop.png").convert_alpha()
#        self.fermeture= pygame.transform.scale(self.fermeture_load, (self.fermeture_size,self.fermeture_size))
#        self.fermeture_rect=self.fermeture.get_rect()
#
    def event_handler(self,screen,background_load,players,menu,fermeture_rect):
        for event in pygame.event.get():
            self.background= pygame.transform.scale(background_load, (screen.get_width(),screen.get_height()))
            if event.type == pygame.QUIT:
                running = False
            self.destination_pioche.print_pioche_dest(screen)
            self.destination_pioche.dragndrop(screen,event) # type: ignore
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


