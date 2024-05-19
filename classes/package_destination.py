import random
from classes.destination import Card_bateau
import pygame
from boat import Boat
class Package_Destination():
    def __init__(self):
        self.echange=[]
        self.influence=[]
        self.verso=[]
        self.liste=[]
        self.active_card_e=None
        self.active_card_i=None

        #INITIALISATION DES CARTES ÉCHANGE ET INFLUENCE (échange en premier)
        self.card_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.card_cout=[('violet','violet'),('vert','vert'),('rouge','rouge'),('different','different','different'),('different','different','different'),('vert','vert'),
        ('rouge','rouge'),('violet','violet'),('jaune','jaune'),('different','different','different'),('different','different','different'),('bleu','bleu'),
        ('violet','violet'),('bleu','bleu'),('different','different','different'),('rouge','rouge'),('vert','vert'),('jaune','jaune'),('bleu','bleu'),('jaune','jaune'),
        ('egal','egal','egal','egal'),('violet','violet','violet','rouge','rouge'),('violet','violet','jaune','jaune'),
        ('egal','egal','egal','egal'),('vert','vert','violet','violet'),('bleu','bleu','bleu','violet','violet'),
        ('jaune','jaune','bleu','bleu'),('rouge','jaune','vert','bleu','violet'),('vert','vert','vert','bleu','bleu'),
        ('rouge','rouge','vert','vert'),('jaune','jaune','jaune','vert','vert'),('bleu','bleu','rouge','rouge'),('rouge','jaune','vert','bleu','violet'),
        ('rouge','rouge','rouge','jaune','jaune'),('egal','egal','egal','egal')]
        self.card_gain=[('pioche'),('recrue','recrue'),('bracelet','renommee'),('bracelet'),('bracelet','recrue','pioche'),
        ('bracelet','recrue'),('bracelet'),('pioche'),('renommee'),('bracelet','renommee','pioche'),('bracelet'),('renommee','renommee'),
        ('bracelet','pioche'),('bracelet','renommee'),('recrue','renommee','pioche'),('bracelet','pioche'),('recrue'),('recrue'),
        ('recrue','renommee'),(''),('victoire','victoire','victoire','victoire','victoire','recrue'),('victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire','pioche'),
        ('victoire','victoire','victoire','victoire','victoire','victoire'),('victoire','victoire','victoire','victoire','victoire','bracelet'),('victoire','victoire','victoire','victoire','victoire','victoire'),
        ('victoire','victoire','victoire','victoire','victoire','victoire','victoire','renommee','renommee'),('victoire','victoire','victoire','victoire','victoire','victoire'),
        ('victoire','victoire','victoire','victoire','bracelet','recrue','renommee','pioche'),('victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire','recrue'),
        ('victoire','victoire','victoire','victoire','victoire','victoire'),('victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire'),
        ('victoire','victoire','victoire','victoire','victoire','victoire'),('victoire','victoire','victoire','victoire','bracelet','recrue','renommee','pioche'),
        ('victoire','victoire','victoire','victoire','victoire','victoire','victoire','bracelet'),('victoire','victoire','victoire','victoire','victoire','renommee')]
        self.card_gain_col=[('pioche','rien','victoire'),('rien','recrue','rien'),('victoire','rien','victoire'),('victoire','renommee','recrue'),('rien','victoire','rien'),('victoire','rien','recrue'),
        ('victoire','victoire','rien'),('victoire','pioche','rien'),('victoire','victoire','rien'),('rien','victoire','rien'),('victoire','renommee','recrue'),('rien','victoire','renommee'),('rien','victoire','pioche'),
        ('rien','renommee','victoire'),('rien','victoire','rien'),('victoire','rien','victoire'),('recrue','victoire','rien'),('victoire','victoire','rien'),
        ('renommee','rien','victoire'),('victoire','victoire','victoire'),('rien','rien','victoire'),('rien','rien','victoire'),('rien','victoire','rien'),('rien','rien','victoire'),
        ('rien','victoire','rien'),('rien','rien','victoire'),('rien','victoire','rien'),('rien','rien','victoire'),('rien','rien','victoire'),('rien','victoire','rien'),
        ('rien','rien','victoire'),('rien','victoire','rien'),('rien','rien','victoire'),('rien','rien','victoire'),('rien','rien','victoire')]
        self.echangetype=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        for i in range(20):
            self.echange.append(Card_bateau(self.card_id[i], self.card_cout[i], self.card_gain[i], self.card_gain_col[i], echange=self.echangetype[i]))
        for i in range(15):
            self.influence.append(Card_bateau(self.card_id[i+20], self.card_cout[i+20], self.card_gain[i+20], self.card_gain_col[i+20], self.echangetype[i+20]))



        #CRÉATION DES VERSO
        self.verso.append(Card_bateau(1, "rien", "rien", "rien", echange=True))
        self.verso.append(Card_bateau(1, "rien", "rien", "rien", echange=False))
        self.verso[0].face="V"
        self.verso[1].face="V"

        #MÉLANGE DES CARTES
        random.shuffle(self.echange)
        random.shuffle(self.influence)

    def print_pioche_dest(self,screen):
        #print(self.echange)
        #print(self.influence)
        for i in range(3):
            self.echange[i].print(screen, (int(i*300+305),5))
        for i in range(3):
            self.influence[i].print(screen,(int(i*300+305),155))
        self.verso[0].print(screen, (5,5))
        self.verso[1].print(screen, (5,155))

    def Compter_cartes(self,equipage,active_card,liste):
        cpt=0
        for cost in liste[active_card].cout_coul:
            if cost != "egal" and cost != "different":
                if liste[active_card].cout_coul.count(cost) <= len(equipage[cost]):
                    cpt+=liste[active_card].cout_coul.count(cost)
            if cost == "egal":
                for couleur in equipage:
                    if len(equipage[couleur])>=len(liste[active_card].cout_coul):
                        cpt+=len(liste[active_card].cout_coul)
            if cost == "different":
                for couleur in equipage:
                    if len(equipage[couleur])!=0:
                        cpt+=1

            if cpt == len(liste[active_card].cout_coul):
                return True


    def dragndrop_echange(self,screen,event,boat,equipage,player):
        #self.echange = self.echange+self.influence
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, card in enumerate(self.echange):
                    if card.front_rect.collidepoint(event.pos):
                        print("ok")
                        self.active_card_e=num
                        mouse_x, mouse_y = event.pos
                        #position de la souris sur l'image
                        self.offset_x=mouse_x-self.echange[self.active_card_e].pos[0]
                        self.offset_y=mouse_y-self.echange[self.active_card_e].pos[1]
                        print(self.offset_x,self.offset_y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                if screen.get_width()/2-100<event.pos[0]<screen.get_width()/2+100 and event.pos[1]>screen.get_height()-200 and self.active_card_e != None:
                    print("echange")
                    if len(boat.liste)<1000:
                        print(self.Compter_cartes(equipage,self.active_card_e,self.echange))
                        if self.Compter_cartes(equipage,self.active_card_e,self.echange):
                            a=0
                            for cout in self.echange[self.active_card_e].cout_coul:
                                print(self.echange[self.active_card_e].cout_coul)
                                if cout == "egal":
                                    print('egal')
                                    for couleur in equipage:
                                        if len(equipage[couleur])>=len(self.echange[self.active_card_e].cout_coul):
                                            active_card=couleur
                                    del equipage[active_card][0]
                                    a+=1

                                if cout == "different":
                                    print('different')
                                    for couleur in equipage:
                                        if len(equipage[couleur])!=0:
                                            del equipage[couleur][0]
                                            break
                                    a+=1

                                if cout != "egal" and cout != "different":
                                    print('normal')
                                    del equipage[cout][0]
                                    a+=1
                                if a == len(self.echange[self.active_card_e].cout_coul):
                                    boat.Cartes_desti(self.echange[self.active_card_e])

                                    for gain in self.echange[self.active_card_e].gain:
                                        if gain == "pioche":
                                            print("pioche")
                                        if gain == "recrue":
                                            player.add_recrue(1)
                                        if gain == "bracelet":
                                            player.add_bracelet(1)
                                        if gain == "renommee":
                                            player.add_renome(1)
                                        if gain == "victoire":
                                            player.add_score(1)
                                    del self.echange[self.active_card_e]
                                    self.active_card_e=None
                                    return True
                        else:
                            print("pas assez de cartes")
                    self.active_card_e=None
                else:
                    self.active_card_e=None
            self.active_card_e=None

        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_e != None:
                #print("bouge")
                self.echange[self.active_card_e].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))
                #print((event.pos[0]-offset_x,event.pos[1]-offset_y))
                #print((screen.get_width()/2-100,screen.get_width()/2+100))
                #print((screen.get_height()/2+100,screen.get_height()/2-100))
            
        #afficher l'image à la souris pendant le drag and drop si on bouge pas
        if self.active_card_e != None:
            self.echange[self.active_card_e].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

        return False
        
    def dragndrop_influence(self,screen,event,boat,equipage,player):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, card in enumerate(self.influence):
                    if card.front_rect.collidepoint(event.pos):
                        self.active_card_i=num
                        mouse_x, mouse_y = event.pos
                        #position de la souris sur l'image
                        self.offset_x=mouse_x-self.influence[self.active_card_i].pos[0]
                        self.offset_y=mouse_y-self.influence[self.active_card_i].pos[1]
                        print(self.offset_x,self.offset_y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                if screen.get_width()/2-100<event.pos[0]<screen.get_width()/2+100 and event.pos[1]>screen.get_height()-200 and self.active_card_i != None:
                    print("influence")
                    if len(boat.liste)<1000:
                        if self.Compter_cartes(equipage,self.active_card_i,self.influence):
                            a=0
                            for cout in self.influence[self.active_card_i].cout_coul:
                                print(self.influence[self.active_card_i].cout_coul)
                                if cout == "egal":
                                    print('egal')
                                    for card in equipage:
                                        if len(equipage[card])>=len(self.influence[self.active_card_i].cout_coul):
                                            active_card=card
                                    del equipage[active_card][0]
                                    a+=1

                                if cout == "different":
                                    print('different')
                                    for couleur in equipage:
                                        if len(equipage[couleur])!=0:
                                            del equipage[couleur][0]
                                    a+=1

                                if cout != "egal" and cout != "different":
                                    print('normal')
                                    del equipage[cout][0]
                                    a+=1
                                if a == len(self.influence[self.active_card_i].cout_coul):
                                    boat.Cartes_desti(self.influence[self.active_card_i])

                                    for gain in self.influence[self.active_card_i].gain:
                                        if gain == "pioche":
                                            print("pioche")
                                        if gain == "recrue":
                                            player.add_recrue(1)
                                        if gain == "bracelet":
                                            player.add_bracelet(1)
                                        if gain == "renommee":
                                            player.add_renome(1)
                                        if gain == "victoire":
                                            player.add_score(1)
                                    del self.influence[self.active_card_i]
                                    self.active_card_i=None
                                    return True
                    self.active_card_i=None
                else:
                    self.active_card_i=None
            self.active_card_i=None
        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_i != None:
                #print("bouge")
                self.influence[self.active_card_i].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))
                #print((event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))
                #print((screen.get_width()/2-100,screen.get_width()/2+100))
                #print((screen.get_height()/2+100,screen.get_height()/2-100))
            
        #afficher l'image à la souris pendant le drag and drop si on bouge pas
        if self.active_card_i !=None:
            self.influence[self.active_card_i].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

        return False