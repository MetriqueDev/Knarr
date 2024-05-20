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
        self.card_gain=[('pioche',),('recrue','recrue'),('bracelet','renommee'),('bracelet',),('bracelet','recrue','pioche'),
        ('bracelet','recrue'),('bracelet',),('pioche',),('renommee',),('bracelet','renommee','pioche'),('bracelet',),('renommee','renommee'),
        ('bracelet','pioche'),('bracelet','renommee'),('recrue','renommee','pioche'),('bracelet','pioche'),('recrue',),('recrue',),
        ('recrue','renommee'),('',),('victoire','victoire','victoire','victoire','victoire','recrue'),('victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire','pioche'),
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
        for j in range(3):
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
    
    def trouver_plus_grande_liste(self,dictionnaire):
        max_taille = float('-inf')  # Initialisation avec une valeur négative infinie
        cle_max = None
    
        for cle, liste in dictionnaire.items():
            taille_liste = len(liste)
            if taille_liste > max_taille:
                max_taille = taille_liste
                cle_max = cle
    
        return cle_max
    
    def verif_liste_vide(self,dictionnaire):
        for cle, liste in dictionnaire.items():
            if liste:
                return False
        return True

    def Compter_cartes(self,equipage,active_card,liste,joueur):
        # Cette fonction compte le nombre de cartes dans l'équipage qui correspondent aux conditions de coût de la carte active.
        # Elle prend en paramètre l'équipage, l'indice de la carte active et la liste des cartes.
        cpt=0
        cpt_egal=0
        cpt_diff=0
        for cost in liste[active_card].cout_coul:
            print('cpt=',cpt)
            # Parcourt les différentes couleurs du coût de la carte active.
            if cost != "egal" and cost != "different" : #and len(equipage[cost])>cpt:
                # Si la couleur n'est ni "egal" ni "different", on vérifie si le nombre de cartes de cette couleur dans l'équipage est suffisant.
                cpt+=len(equipage[cost])
            if cost == "egal":
                # Si la couleur est "egal", on vérifie si l'équipage a au moins autant de cartes que le coût de la carte active.
                cpt_egal=self.trouver_plus_grande_liste(equipage)
            if cost == "different":
                # Si la couleur est "different", on vérifie si l'équipage a au moins une carte de couleur différente.
                for couleur in equipage:
                    if len(equipage[couleur])!=0:
                        cpt_diff+=1
            print('cpt=',cpt)
            if cpt == len(liste[active_card].cout_coul) or cpt_egal == len(liste[active_card].cout_coul) or cpt_diff !=0:
                # Si le nombre de cartes correspond au coût de la carte active, on retourne True.
                return True
        if (cpt < len(liste[active_card].cout_coul) or cpt_egal == len(liste[active_card].cout_coul)) and joueur.ia==False:
            print("recrue")
            print(joueur.boat.recrue)
            print(len(liste[active_card].cout_coul)-cpt)
            if joueur.boat.recrue >= len(liste[active_card].cout_coul)-cpt:
                print("oui")
                return len(liste[active_card].cout_coul)-cpt



    def dragndrop_echange(self,screen,event,boat,equipage,player):
        # Cette fonction gère le glisser-déposer des cartes d'échange.
        # Elle prend en paramètres l'écran, l'événement, le bateau, l'équipage et le joueur.
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, card in enumerate(self.echange):
                    if card.front_rect.collidepoint(event.pos):
                        self.active_card_e=num
                        mouse_x, mouse_y = event.pos
                        # position de la souris sur l'image
                        self.offset_x=mouse_x-self.echange[self.active_card_e].pos[0]
                        self.offset_y=mouse_y-self.echange[self.active_card_e].pos[1]
        
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                if screen.get_width()/2-100<event.pos[0]<screen.get_width()/2+100 and event.pos[1]>screen.get_height()-200 and self.active_card_e != None:

                    if len(boat.liste)<1000:
                        can =self.Compter_cartes(equipage,self.active_card_e,self.echange,player)
                        print("can =",can)
                        if can == True or can ==1 or can ==2 or can ==3:
                            a=0
                            b=0
                            prec_couleurs=[]
                            p_pioche=False
                            for cout in self.echange[self.active_card_e].cout_coul:
                                #print("équipage",equipage[cout])

                                print(self.echange[self.active_card_e].cout_coul)
                                if cout == "egal" and self.verif_liste_vide(equipage)==False:
                                    if (equipage[cout]!=None or equipage[cout]!=[]):
                                        print('egal')
                                        for couleur in equipage:
                                                if len(equipage[couleur])>=len(self.echange[self.active_card_e].cout_coul):
                                                    active_card=couleur
                                                del equipage[active_card][0]
                                        a+=1

                                if cout == "different" and self.verif_liste_vide(equipage)==False:
                                    print('different')
                                    for couleur in equipage:
                                        if equipage[couleur] and couleur not in prec_couleurs:
                                            if b == len(self.echange[self.active_card_e].cout_coul):
                                                break
                                            del equipage[couleur][0]
                                            prec_couleurs.append(couleur)
                                            b+=1
                                            
                                    a+=1

                                if cout != "egal" and cout != "different" and equipage[cout] != []:
                                    print('normal')
                                    del equipage[cout][0]
                                    a+=1
                            if a == len(self.echange[self.active_card_e].cout_coul):
                                boat.Cartes_desti(self.echange[self.active_card_e])
                                for gain in self.echange[self.active_card_e].gain:
                                    print(gain)
                                    if gain == "pioche":
                                        p_pioche=True
                                    elif gain == "recrue":
                                        player.add_recrue(1)
                                    elif gain == "bracelet":
                                        player.add_bracelet(1)
                                    elif gain == "renommee":
                                        player.add_renome(1)
                                    elif gain == "victoire":
                                        player.add_score(1)
                                del self.echange[self.active_card_e]
                                self.active_card_e=None
                                return True, p_pioche
                            elif can ==1 or can ==2 or can ==3:
                                print("lets go !")
                                player.add_recrue(-can)
                                boat.Cartes_desti(self.echange[self.active_card_e])
                                for gain in self.echange[self.active_card_e].gain:
                                    print(gain)
                                    if gain == "pioche":
                                        p_pioche=True
                                    elif gain == "recrue":
                                        player.add_recrue(1)
                                    elif gain == "bracelet":
                                        player.add_bracelet(1)
                                    elif gain == "renommee":
                                        player.add_renome(1)
                                    elif gain == "victoire":
                                        player.add_score(1)
                                del self.echange[self.active_card_e]
                                self.active_card_e=None
                                return True, p_pioche
                        else:

                            self.active_card_e=None
                else:
                    self.active_card_e=None
            self.active_card_e=None

        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_e != None:

                self.echange[self.active_card_e].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

            
        # afficher l'image à la souris pendant le glisser-déposer si on ne bouge pas
        if self.active_card_e != None:
            self.echange[self.active_card_e].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

        return False, False
        
    def dragndrop_influence(self,screen,event,boat,equipage,player):
        # Cette fonction gère le glisser-déposer des cartes d'influence.
        # Elle prend en paramètres l'écran, l'événement, le bateau, l'équipage et le joueur.
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, card in enumerate(self.influence):
                    if card.front_rect.collidepoint(event.pos):
                        self.active_card_i=num
                        mouse_x, mouse_y = event.pos
                        # position de la souris sur l'image
                        self.offset_x=mouse_x-self.influence[self.active_card_i].pos[0]
                        self.offset_y=mouse_y-self.influence[self.active_card_i].pos[1]
                       
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                if screen.get_width()/2-100<event.pos[0]<screen.get_width()/2+100 and event.pos[1]>screen.get_height()-200 and self.active_card_i != None:
  
                    if len(boat.liste)<1000:
                        can =self.Compter_cartes(equipage,self.active_card_i,self.influence,player)
                        print("can =",can)
                        if can == True or can ==1 or can ==2 or can ==3:
                            a=0
                            b=0
                            prec_couleurs=[]
                            p_pioche=False
                            for cout in self.influence[self.active_card_i].cout_coul:
                                #print("équipage",equipage[cout])

                                print(self.influence[self.active_card_i].cout_coul)
                                if cout == "egal" and self.verif_liste_vide(equipage)==False:
                                    if (equipage[cout]!=None or equipage[cout]!=[]):
                                        print('egal')
                                        for couleur in equipage:
                                            if len(equipage[couleur])>=len(self.influence[self.active_card_i].cout_coul):
                                                active_card=couleur
                                            del equipage[active_card][0]
                                        a+=1

                                if cout == "different" and self.verif_liste_vide(equipage)==False:
                                    print('different')
                                    for couleur in equipage:
                                        if equipage[couleur] and couleur not in prec_couleurs:
                                            if b == len(self.influence[self.active_card_i].cout_coul):
                                                break
                                            del equipage[couleur][0]
                                            prec_couleurs.append(couleur)
                                            b+=1
                                    a+=1

                                if cout != "egal" and cout != "different" and equipage[cout] != []:
                                    print('normal')
                                    del equipage[cout][0]
                                    a+=1
                            if a == len(self.influence[self.active_card_i].cout_coul):
                                boat.Cartes_desti(self.influence[self.active_card_i])
                                for gain in self.influence[self.active_card_i].gain:
                                    print(gain)
                                    if gain == "pioche":
                                        p_pioche=True
                                    elif gain == "recrue":
                                        player.add_recrue(1)
                                    elif gain == "bracelet":
                                        player.add_bracelet(1)
                                    elif gain == "renommee":
                                        player.add_renome(1)
                                    elif gain == "victoire":
                                        player.add_score(1)
                                del self.influence[self.active_card_i]
                                self.active_card_i=None
                                return True, p_pioche
                            elif can ==1 or can ==2 or can ==3:
                                print("lets go !")
                                player.add_recrue(-can)
                                boat.Cartes_desti(self.influence[self.active_card_i])
                                for gain in self.influence[self.active_card_i].gain:
                                    print(gain)
                                    if gain == "pioche":
                                        p_pioche=True
                                    elif gain == "recrue":
                                        player.add_recrue(1)
                                    elif gain == "bracelet":
                                        player.add_bracelet(1)
                                    elif gain == "renommee":
                                        player.add_renome(1)
                                    elif gain == "victoire":
                                        player.add_score(1)
                                del self.influence[self.active_card_i]
                                self.active_card_i=None
                                return True, p_pioche
                        else:
                            print("pas assez de cartes")
                    self.active_card_i=None
                else:
                    self.active_card_i=None
            self.active_card_i=None
        
        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_i != None:

                self.influence[self.active_card_i].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

            
        # afficher l'image à la souris pendant le drag and drop si on bouge pas
        if self.active_card_i !=None:
            self.influence[self.active_card_i].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

        return False,False