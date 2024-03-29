import pygame

class Board():

    def __init__(self):
        self.size=(600,250)#(250,400)

    def init_image(self):
        self.image_board_load = pygame.image.load(f".\images\\plateau.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.image_board = pygame.transform.scale(self.image_board_load, self.size) #changement de taille
        self.image_renome_piece_load = pygame.image.load(f".\images\\renome_piece.png").convert_alpha()
        self.image_renome_piece = pygame.transform.rotate(pygame.transform.scale(self.image_renome_piece_load, (20,20)),45)

    def print(self,screen):
        screen.blit(self.image_board, (int(screen.get_width()/2-self.size[0]/2),screen.get_height()-660))

    def update_renome_pos(self,screen,players):
        for player in players:
            renome = player.get_renome()
            if renome%2 == 0:
                screen.blit(self.image_renome_piece, (int(screen.get_width()/2)+16 + int(31/2)*renome ,360))
            else:
                screen.blit(self.image_renome_piece, (int(screen.get_width()/2)+16 + int(31/2)*renome ,360-1))





#circle()

#150 haut +28
#164 bas
