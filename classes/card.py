import pygame

class Card():

    def __init__(self,card_type):
        self.card_type=card_type
        self.face="B" #F for Front & B for Back
        self.size=(125,200)#(250,400)

        self.init_image()

    def init_image(self):
        self.front=pygame.image.load(f".\\images\\vikings\\{self.card_type}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.front=pygame.transform.scale(self.front, self.size) #changement de taille

        self.back=pygame.image.load(f".\\images\\vikings\\dosdecarte.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.back=pygame.transform.scale(self.back, self.size) #changement de taille

    def print(self,screen,pos):
        if self.face == "F":
            screen.blit(self.front, pos)
        else:
            screen.blit(self.back, pos)