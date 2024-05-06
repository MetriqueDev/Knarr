import pygame

class Pioche():

    def __init__(self):
        self.cards=[]

    def append(self,card):
        self.cards.append(card)

    def print(self):
        #Afficher les cartes
        for i in range(len(self.cards)):
            cards[i].print(screen,(int(screen.get_width()/2-len(self.cards)*125/2)+i*125, 310))