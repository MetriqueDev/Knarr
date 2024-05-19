from classes.package import Package
import pygame

class Hand:

    def __init__(self):
        self.main=[]
        
    def afficher_main(self, screen):
        pos_x, pos_y = (1450,700)  # Détermine les coordonnées de départ pour afficher les cartes
        pygame.draw.rect(screen, ( 112, 123, 124), pygame.Rect(1440, 690, 386, 220))
        for card in self.main:
            card.print(screen, (pos_x, pos_y))  # Affiche chaque carte à l'emplacement spécifié
            pos_x += card.size[0] + 2  # Ajuste la position X pour la prochaine carte, en ajoutant un espacement entre les cartes

