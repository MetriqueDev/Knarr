import pygame
from  classes.pion import Pion
from classes.destination import Card_bateau
from classes.package_destination import Package_Destination

class Boat():

    def __init__(self):
        self.size=(400,200)#(250,400)
        self.recrue=0
        self.bracelet=0
        self.init_image()

    def init_image(self):
        self.image_load=pygame.image.load(f".\\images\\bateau\\bateau_1.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.image=pygame.transform.scale(self.image_load, self.size) #changement de taille

    def print(self,screen):
        screen.blit(self.image, (int(screen.get_width()/2-self.size[0]/2),screen.get_height()-self.size[1]))

    def print_object(self,screen,liste):

        pion = Pion("recrue")
        pos=(int(screen.get_width()/2-self.size[0]/2),screen.get_height()-self.size[1])

        pos1=(pos[0]+5,pos[1]+112)
        pion.print(screen,pos1)

        pos2=(pos[0]+15,pos[1]+65)
        pion.print(screen,pos2)

        pos3=(pos[0]+30,pos[1]+20)
        pion.print(screen,pos3)


        bracelet = Pion("bracelet")
        pos=(int(screen.get_width()/2-self.size[0]/2),screen.get_height()-self.size[1])

        pos1_b=(pos[0]+5+345,pos[1]+112)
        bracelet.print(screen,pos1_b)

        pos2_b=(pos[0]-10+345,pos[1]+65)
        bracelet.print(screen,pos2_b)

        pos3_b=(pos[0]-25+345,pos[1]+20)
        bracelet.print(screen,pos3_b)

        for i in range(len(liste)):
            liste[i].print(screen,(((screen.get_width()/2)-liste[i].size[0]/2),(screen.get_height()-300-(i+1)*liste[i].size[1]/4)))

    def Cartes_desti(self,obj,liste):
        liste.append(obj)

    def Commerce(self,liste):
        for i in range(len(liste)):
            for j in range(3):
                if liste[i].card_gain_col[j] == "pioche":
                    print('pioche')
                elif liste[i].card_gain_col[j] == "recrue":
                    print('recrue')
                elif liste[i].card_gain_col[j] == "victoire":
                    print('victoire')
                elif liste[i].card_gain_col[j] == "renommee":
                    print('renommee')
                else :
                    print('rien')
