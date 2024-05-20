from classes.boat import Boat
from classes.hand import Hand
from classes.package import Package
from classes.card import Card
import pygame
import random
import time

class Player():

    def __init__(self,name,niveau,ia=False):
        self.name=name
        self.ia=ia
        self.niveau=niveau
        self.nombre_de_vicoire=0
        self.nombre_de_defaite=0

        self.hand=Hand()
        self.active_card_h=None
        self.active_card_p=None

        self.equipage={"rouge":[],"jaune":[],"vert":[],"bleu":[],"violet":[]}
    def init_boat(self):
        self.boat=Boat()

    def info(self):
        print("name:",self.name)
        print("niveau:",self.niveau)

    def game_init(self):
        self.score = 0
        self.renome = 0


        self.asplay = False
        self.Explore=False#destination et influence
        self.recrute=False#pioche et main 
        self.pioche=False#recrue 



        self.couleur=None

    def add_renome(self,add):
        if ((self.renome + add)<15) and ((self.renome+add)>(-1)):
            self.renome+=add
        else:
            self.renome=14

    def add_score(self,add):
        #le score ne doit pas dépasser 40 points et ne peut pas être négatif sinon on le met à 0 ou au max
        if ((self.score + add)<=40):
            self.score+=add

    def get_renome(self):
        return self.renome

    def add_renome_to_score(self):
        if self.renome<3:
            self.score+=0
        elif self.renome<6:
            self.score+=1
        elif self.renome<10:
            self.score+=2
        elif self.renome<14:
            self.score+=3
        if self.renome==14:
            self.score+=5

    def get_score(self):
        return self.score

    def get_recrue(self):
        return self.boat.recrue
    
    def get_bracelet(self):
        return self.boat.bracelet
    
    def add_recrue(self,add):
        if ((self.boat.recrue + add)<=3):
            self.boat.recrue+=add
            if self.boat.recrue<0:
                self.boat.recrue=0
    
    def add_bracelet(self,add):
        if ((self.boat.bracelet + add)<=3):
            self.boat.bracelet+=add



    def add_equipage(self,card):
        self.equipage[card.couleur].append(card)

    def print_equipage(self,screen):
        
        self.taille=30
        pygame.draw.rect(screen, (100, 30, 22),  (1280-10, -410-200+int(screen.get_height() )-self.taille   ,125*5+20 ,220  ))
        x=0
        for couleur in self.equipage.keys():
            for i in range(len(self.equipage[couleur])):
                self.equipage[couleur][i].print(screen,(1280+125*x,-400+int(screen.get_height()-self.taille*len(self.equipage[couleur])+i*self.taille-self.equipage[couleur][i].size[1])))
            x+=1
    
    def dragndrop_hand(self,screen,event):#main to equipage
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, card in enumerate(self.hand.main):
                    print(num,card,card.front_rect.collidepoint(event.pos),card.front_rect.x,self.hand.main[num].front_rect.x,card.front_rect.y,self.hand.main[num].front_rect.y)
                    if card.front_rect.collidepoint(event.pos):
                        self.active_card_h=num
                        mouse_x, mouse_y = event.pos
                        #position de la souris sur l'image
                        self.offset_x=mouse_x-self.hand.main[self.active_card_h].pos[0]
                        self.offset_y=mouse_y-self.hand.main[self.active_card_h].pos[1]


        if event.type == pygame.MOUSEBUTTONUP:
            
            if event.button==1:

                if ((1280-10)<event.pos[0]<(1280-10+125*5+20)) and ((-410-200+int(screen.get_height() ))-self.taille )<event.pos[1]<((-410-200+int(screen.get_height() ))-self.taille +220) and self.active_card_h != None: #position à adapter à l'equipage

                    self.add_equipage(self.hand.main[self.active_card_h]) 
                    self.couleur=self.hand.main[self.active_card_h].couleur
                    for card in self.equipage[self.hand.main[self.active_card_h].couleur]:
                        if card.gain == "renommee":
                            self.add_renome(1)
                        elif card.gain == "recrue":
                            self.add_recrue(1)
                        elif card.gain =="victoire":
                            self.add_score(1)
                        elif card.gain == "bracelet":
                            self.add_bracelet(1)
                    del self.hand.main[self.active_card_h]
                    self.active_card_h= None
                    return True
                else:
                    self.active_card_h=None
                self.active_card_h=None
            self.active_card_h=None
        

        #afficher l'image à la souris pendant le drag and drop si on bouge pas
        if self.active_card_h !=None:
            self.hand.main[self.active_card_h].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

        return False
    
    def play_ai(self,package_destination,board,jeu):
        # Choix de l'IA si elle explore ou recrute
        asplay = False
        p_pioche = False
        
        # Explore
        if asplay == False:
            for i in range(len(package_destination.echange)):
                can = package_destination.Compter_cartes(self.equipage, i, package_destination.echange)
                if can:
                    for gain in package_destination.echange[i].gain:
                        if gain == "pioche":
                            p_pioche = True
                        if gain == "recrue":
                            self.add_recrue(1)
                        if gain == "bracelet":
                            self.add_bracelet(1)
                        if gain == "renommee":
                            self.add_renome(1)
                        if gain == "victoire":
                            self.add_score(1)
                    self.boat.Cartes_desti(package_destination.echange[i])
                    del package_destination.echange[i]
                    asplay = True
        
        # Recrute
        if asplay == False:
            for i in range(len(package_destination.influence)):
                can = package_destination.Compter_cartes(self.equipage, i, package_destination.influence)
                if can:
                    for gain in package_destination.influence[i].gain:
                        if gain == "pioche":
                            p_pioche = True
                        if gain == "recrue":
                            self.add_recrue(1)
                        if gain == "bracelet":
                            self.add_bracelet(1)
                        if gain == "renommee":
                            self.add_renome(1)
                        if gain == "victoire":
                            self.add_score(1)
                    self.boat.Cartes_desti(package_destination.influence[i])
                    del package_destination.influence[i]
                    asplay = True

        # Pioche
        if p_pioche == True:
            # Choisir une couleur de board.recrue au hasard
            couleur_choice = random.choice(list(board.recrues.keys()))
            self.add_equipage(board.recrues[couleur_choice])
            board.recrues[couleur_choice] = None
            board.recrues[couleur_choice] = jeu.package.package[0]
            del jeu.package.package[0]
            p_pioche = False

        # Si aucune action n'a été effectuée, on recrute
        if asplay == False:
            # Je prends une carte de la main et je la mets dans l'équipage et je retire la carte de la main
            self.add_equipage(self.hand.main[0])
            self.couleur = self.hand.main[0].couleur
            for card in self.equipage[self.hand.main[0].couleur]:
                if card.gain == "renommee":
                    self.add_renome(1)
                elif card.gain == "recrue":
                    self.add_recrue(1)
                elif card.gain == "victoire":
                    self.add_score(1)
                elif card.gain == "bracelet":
                    self.add_bracelet(1)
            del self.hand.main[0]

            # Je pioche pour mettre une carte dans ma main de la couleur de la carte que j'ai mise dans l'équipage
            couleur = str("p_" + self.couleur)
            self.hand.main.append(board.recrues[couleur])
            board.recrues[couleur] = None
            board.recrues[couleur] = jeu.package.package[0]
            del jeu.package.package[0]
            asplay = True

        # Commerce
        choice = 0
        if self.boat.liste != []:
            if self.boat.bracelet == 3:
                choice = random.randint(0, 3)
            elif self.boat.bracelet == 2:
                choice = random.randint(0, 2)
            elif self.boat.bracelet == 1:
                choice = random.randint(0, 1)
            else:
                choice = 0
        if choice != 0:
            liste_valeurs = self.boat.Commerce(choice)
            n = jeu.liste_valeurs_to_game(self, liste_valeurs)
            for i in range(n):
                couleur_choice = random.choice(list(board.recrues.keys()))
                self.add_equipage(board.recrues[couleur_choice])
                board.recrues[couleur_choice] = None
                board.recrues[couleur_choice] = jeu.package.package[0]
                del jeu.package.package[0]
                p_pioche = False

        # Fini le tour
