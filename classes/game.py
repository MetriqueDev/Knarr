import pygame
from classes.card import Card
from classes.board import Board
from classes.boat import Boat
from classes.player import Player
from classes.destination import Card_bateau
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


    def init_image(self,screen):
        #Background
        self.background_load = pygame.image.load(".\\images\\fond.jpg").convert()
        self.background= pygame.transform.scale(self.background_load, (screen.get_width(),screen.get_height()))

    def init_game(self,screen):
        self.liste=[]
        print(self.package.package)
        self.board.init_cartes(self.package)
        self.destination=Package_Destination()
        for player in self.players:
            player.init_boat()
            for i in range(3):
                e=self.package.pioche_hand(player.hand)
                if e== False:
                    print("plus de cartes dans package")

        btn_unselect_image_load=pygame.image.load(f".\\images\\gui\\skip.png").convert_alpha() 
        btn_select_image_load=pygame.image.load(f".\\images\\gui\\skip_select.png").convert_alpha() 
        
        self.skip_boutton= Button(10,screen.get_height()-32*5-5,[btn_unselect_image_load,btn_select_image_load],5)
        
        
    

    def update(self,screen,liste,font,instance_name):

        text_turn="Tour de "+self.players[self.turn%len(self.players)].name
        self.turn_name=font.render(text_turn,True,(200,200,210))
        
        screen.blit(self.background, (0,0))
        self.destination.print_pioche_dest(screen)
        
        self.board.print(screen)
        self.board.recrutement_print(screen)
        self.board.update_renome_pos(screen,self.players)
        self.board.update_score_pos(screen,self.players)

        if self.skip_boutton.draw(screen):
            #condition si il peut ou non skip
            self.turn+=1
            if self.turn%len(self.players) ==0:
                #Nouveau tour
                for player in self.players:
                    player.asExploreOrRecrute=False
                    player.asplay=False
                    player.add_renome_to_score()


        screen.blit(self.turn_name, (10,screen.get_height()-75))



    def event_handler(self,event,screen):
        
        print(self.players[self.turn%len(self.players)].name,self.players[self.turn%len(self.players)].asExploreOrRecrute)
        if self.players[self.turn%len(self.players)].asExploreOrRecrute==False:
            a=self.destination.dragndrop_echange(screen,event,self.players[self.turn%len(self.players)].boat)
            b=self.destination.dragndrop_influence(screen,event,self.players[self.turn%len(self.players)].boat)
            c=self.board.dragndrop_recrutement(screen,event,self.players[self.turn%len(self.players)].hand,self.package)
            d=self.players[self.turn%len(self.players)].dragndrop_hand(screen, event)
            #e=self.players[self.turn%len(self.players)].dragndrop_pioche(screen, event)
            if a or b or c or d:
                self.players[self.turn%len(self.players)].asExploreOrRecrute=True