import pygame
from  classes.pion import Pion
from classes.destination import Card_bateau
from classes.package_destination import Package_Destination

class Boat():

    def __init__(self):
        self.size=(400,200)#(250,400)
        self.recrue=0
        self.bracelet=3
        self.init_image()
        self.liste=[]
        self.valeur_propre=["r","recrue","r"]

    def init_image(self):
        self.image_load=pygame.image.load(f".\\images\\bateau\\bateau_1.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.image=pygame.transform.scale(self.image_load, self.size) #changement de taille

    def print(self,screen):
        screen.blit(self.image, (int(screen.get_width()/2-self.size[0]/2),screen.get_height()-self.size[1]))

    def print_object(self,screen):

        pion = Pion("recrue")
        pos=(int(screen.get_width()/2-self.size[0]/2),screen.get_height()-self.size[1])
        if self.recrue >=1:
            pos1=(pos[0]+5,pos[1]+112)
            pion.print(screen,pos1)
        if self.recrue >=2:
            pos2=(pos[0]+15,pos[1]+65)
            pion.print(screen,pos2)
        if self.recrue ==3:
            pos3=(pos[0]+30,pos[1]+20)
            pion.print(screen,pos3)


        bracelet = Pion("bracelet")
        pos=(int(screen.get_width()/2-self.size[0]/2),screen.get_height()-self.size[1])
        if self.bracelet >=1:
            pos1_b=(pos[0]+5+345,pos[1]+112)
            bracelet.print(screen,pos1_b)
        if self.bracelet >=2:
            pos2_b=(pos[0]-10+345,pos[1]+65)
            bracelet.print(screen,pos2_b)
        if self.bracelet ==3:
            pos3_b=(pos[0]-25+345,pos[1]+20)
            bracelet.print(screen,pos3_b)

        for i in range(len(self.liste)):
            self.liste[i].print(screen,(((screen.get_width()/2)-self.liste[i].size[0]/2),(screen.get_height()-300-(i+1)*self.liste[i].size[1]/4)))

    def Cartes_desti(self,obj):
        self.liste.append(obj)

    def Commerce(self,n):
        liste_valeurs=[]
        for i in range(len(self.liste)):
            for j in range(n):
                if self.liste[i].gain_col[j] == "pioche":
                    liste_valeurs.append('pioche')
                elif self.liste[i].gain_col[j] == "recrue":
                    liste_valeurs.append('recrue')
                elif self.liste[i].gain_col[j] == "victoire":
                    liste_valeurs.append('victoire')
                elif self.liste[i].gain_col[j] == "renommee":
                    liste_valeurs.append('renommee')
                else :
                    liste_valeurs.append('r')
        for j in range(n):
            liste_valeurs.append(self.valeur_propre[j])
        return liste_valeurs
