import pygame

class Card():

    def __init__(self,card_type):
        self.card_type=card_type
        self.face="F" #F for Front & B for Back
        self.size=(125,200)#(250,400)

    def init_image(self):
        self.front=pygame.image.load(f".\images\\vikings\\{self.card_type}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.front=pygame.transform.scale(self.front, self.size) #changement de taille

    def print(self,screen,pos):
        screen.blit(self.front, pos)