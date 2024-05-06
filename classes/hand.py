from classes.package import Package
import pygame

class Hand:

    def __init__(self):
        self.main=[]

    def afficher_main(self, screen):
        x_offset, y_offset = (1400,800)  # Détermine les coordonnées de départ pour afficher les cartes 

        for card in self.main:
          card.print(screen, (x_offset, y_offset))  # Affiche chaque carte à l'emplacement spécifié
          x_offset += card.size[0] + 2  # Ajuste la position X pour la prochaine carte, en ajoutant un espacement entre les cartes

