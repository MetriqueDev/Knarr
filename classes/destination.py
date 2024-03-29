import pygame

class Destination:
    def __init__(self, d_type,cout_c,cout_v):
        self.d_type= d_type
        self.cout_c = cout_c
        self.cout_v = cout_v

    def init_image(self, nbr):
        if d_type == 'influence':
            self.front=pygame.image.load(f".\images\\influence\\{self.d_type}_{nbr}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
            self.front=pygame.transform.scale(self.front, self.size) #changement de taille
        if d_type == 'echange':
            self.front=pygame.image.load(f".\images\\echange\\{self.d_type}_{nbr}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
            self.front=pygame.transform.scale(self.front, self.size) #changement de taille

    def print(self,screen,pos):
        screen.blit(self.front, pos)