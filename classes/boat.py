import pygame
from  classes.pion import Pion

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

    def print_object(self,screen):

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