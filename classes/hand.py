from classes.package import Package
import pygame

class Hand:

    def __init__(self):
        self.main=[]

    def afficher_main(self, screen):
        pos_x, pos_y = (1450,700)  # Détermine les coordonnées de départ pour afficher les cartes

        for card in self.main:
            print(pos_x,pos_y)
            card.print(screen, (pos_x, pos_y))  # Affiche chaque carte à l'emplacement spécifié
            print(card.front_rect.x,card.front_rect.y)
            pos_x += card.size[0] + 2  # Ajuste la position X pour la prochaine carte, en ajoutant un espacement entre les cartes

