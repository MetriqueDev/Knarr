from package import package
import pygame

class Hand:

    def __init__(self):
        self.main=[]

    def afficher_main(self, screen, position):
        x_offset, y_offset = (400,200)  # Détermine les coordonnées de départ pour afficher les cartes 

        for card in self.main:
          card.print(screen, (x_offset, y_offset))  # Affiche chaque carte à l'emplacement spécifié
          x_offset += card.size[0] + 10  # Ajuste la position X pour la prochaine carte, en ajoutant un espacement entre les cartes

