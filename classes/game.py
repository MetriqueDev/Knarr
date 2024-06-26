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
import time


class Game():
    def __init__(self,players):
        self.nbr_player=len(players)
        self.players=players
        self.package=Package(self.nbr_player)
        self.package.shuffle()
        self.board=Board()
        self.turn=0
        self.v_wait=0
        self.start=0


    def wait(self,v):
        self.v_wait=v
        self.start=time.time()
    
    def wait_finish(self):
        if time.time()-self.start>self.v_wait:
            self.v_wait=0
            return True
        return False

    def init_image(self,screen):
        #Background
        self.background_load = pygame.image.load(".\\images\\fond.jpg").convert()
        self.background= pygame.transform.scale(self.background_load, (screen.get_width(),screen.get_height()))

    def init_game(self,screen):
        self.liste=[]

        self.board.init_cartes(self.package)
        self.destination=Package_Destination()
        for player in self.players:
            player.init_boat()
            for i in range(3):
                self.package.pioche_hand(player.hand)


        btn_unselect_image_load=pygame.image.load(f".\\images\\gui\\skip.png").convert_alpha() 
        btn_select_image_load=pygame.image.load(f".\\images\\gui\\skip_select.png").convert_alpha() 
        
        self.skip_boutton= Button(10,screen.get_height()-32*5-5,[btn_unselect_image_load,btn_select_image_load],5)
        
    
    
    #fonction qui update le jeu
    def update(self,screen,font,pioche_number,name):

        text_turn="Tour de "+self.players[self.turn%len(self.players)].name

        self.turn_name=font.render(text_turn,True,(200,200,210))
        
        screen.blit(self.background, (0,0))
        self.destination.print_pioche_dest(screen)
        
        self.board.print(screen)
        self.board.recrutement_print(screen)
        self.board.update_renome_pos(screen,self.players)
        self.board.update_score_pos(screen,self.players)
        for player in self.players:
            if player.name ==name and pioche_number==0 and player.asplay :
                if player.name == self.players[self.turn%len(self.players)].name:
                    if player.ia==False:
                        if self.skip_boutton.draw(screen):
                            self.wait(1)
                            #condition si il peut ou non skip
                            self.new_turn()
                        


        screen.blit(self.turn_name, (10,screen.get_height()-75))

    def new_turn(self):
        self.turn+=1
        if self.turn%len(self.players) ==0:
            #Nouveau tour
            for player in self.players:

                player.Explore=False#destination et influence
                player.recrute=False#pioche et main 
                player.pioche=False#recrue 


                player.asplay=False

                player.couleur=None
                player.add_renome_to_score()

                #print(player.name," -> ",player.get_score())

            return self.check_win()
        return False

    #fonction qui gere les evenements
    def event_handler(self,event,screen,pioche_number):
        if self.players[self.turn%len(self.players)].Explore==False and self.players[self.turn%len(self.players)].recrute==False:  
            d=self.players[self.turn%len(self.players)].dragndrop_hand(screen, event)
            if d==True:
                self.players[self.turn%len(self.players)].recrute=True
            a, p_pioche_a=self.destination.dragndrop_echange(screen,event,self.players[self.turn%len(self.players)].boat,self.players[self.turn%len(self.players)].equipage,self.players[self.turn%len(self.players)])
            b, p_pioche_b=self.destination.dragndrop_influence(screen,event,self.players[self.turn%len(self.players)].boat,self.players[self.turn%len(self.players)].equipage,self.players[self.turn%len(self.players)])
            if a or b:
                self.players[self.turn%len(self.players)].Explore=True
            if p_pioche_a or p_pioche_b:
                return pioche_number+1

        else:
            if self.players[self.turn%len(self.players)].pioche==False and self.players[self.turn%len(self.players)].recrute==True:
                c=self.board.dragndrop_recrutement(screen,event,self.players[self.turn%len(self.players)].hand,self.package,self.players[self.turn%len(self.players)])

                if c:
                    self.players[self.turn%len(self.players)].pioche=True#la partie pioche est fini

        if pioche_number!=0:
            if self.board.dragndrop_recrue_to_equipage(screen,event,self.players[self.turn%len(self.players)],self.package):
                return pioche_number-1
            else: 
                return pioche_number
        return 0


    #sert a ajouter les valeurs des cartes 
    def liste_valeurs_to_game(self,player,liste_valeurs):
        # Ajoute le nombre de recrues à la main du joueur
        player.add_recrue(liste_valeurs.count("recrue"))
        # Ajoute le nombre de points de victoire au score du joueur
        player.add_score(liste_valeurs.count("victoire"))
        # Ajoute le nombre de points de renommée au total de renommée du joueur
        player.add_renome(liste_valeurs.count("renommee"))
        # Retourne le nombre de cartes "pioche" dans la liste de valeurs
        return liste_valeurs.count("pioche")
    
    #verifie si un joueur a gagné
    def check_win(self):
        for player in self.players:
            if player.get_score()>=40:
                return player.name
        return False