import pygame

class Board():

    def __init__(self):
        self.size=(500,200)#(250,400)

    def init_image(self):
        self.image_load=pygame.image.load(f".\images\\plateau.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.image=pygame.transform.scale(self.image_load, self.size) #changement de taille

    def print(self,screen,pos):
        screen.blit(self.image, pos)