#import pygame
#
#class Destination:
#    def __init__(self, d_type,cout_c,cout_v):
#        self.d_type= d_type
#        self.cout_c = cout_c
#        self.cout_v = cout_v
#
#
#    def image(self, nbr):
#        self.image = str(self.d_type+"_"+str(nbr))
#        self.init_image()
#
#    def init_image(self, nbr):
#        if self.d_type == 'influence':
#            self.front=pygame.image.load(f".\\images\\influence\\{self.image}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
#            self.front=pygame.transform.scale(self.front, self.size) #changement de taille
#        if self.d_type == 'echange':
#            self.front=pygame.image.load(f".\\images\\echange\\{self.d_type}_{nbr}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
#            self.front=pygame.transform.scale(self.front, self.size) #changement de taille
#
#    def print(self,screen,pos):
#        screen.blit(self.front, pos)