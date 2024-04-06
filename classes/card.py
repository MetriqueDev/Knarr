import pygame

class Card():

    def __init__(self,card_type,num=0):
        self.card_type=card_type
        self.couleur=self.card_type[0:-1]
        print(self.couleur)
        self.face="F" #F for Front & B for Back
        self.size=(125,200)#(250,400)
        self.num=num

        self.init_image()

    def init_image(self):
        self.front=pygame.image.load(f".\\images\\vikings\\{self.card_type}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.front=pygame.transform.scale(self.front, self.size) #changement de taille
        self.front_rect=self.front.get_rect()

        self.back=pygame.image.load(f".\\images\\vikings\\dosdecarte.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.back=pygame.transform.scale(self.back, self.size) #changement de taille
        self.back_rect=self.back.get_rect()

    def print(self,screen,pos):
        if self.face == "F":
            self.front_rect.x=pos[0]
            self.front_rect.y=pos[1]
            screen.blit(self.front, (self.front_rect.x,self.front_rect.y))
        else:
            self.back_rect.x=pos[0]
            self.back_rect.y=pos[1]
            screen.blit(self.back, (self.back_rect.x,self.back_rect.y))

    def print_info(self):
        print(f"Type:{self.card_type}\nNumero:{self.num}")