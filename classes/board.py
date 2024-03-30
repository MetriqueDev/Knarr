import pygame

class Board():

    def __init__(self):
        self.size=(600,250)#(250,400)

        self.init_image()

    def init_image(self):
        self.image_board_load = pygame.image.load(f".\\images\\plateau.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.image_board = pygame.transform.scale(self.image_board_load, self.size) #changement de taille
        self.image_renome_piece_load = pygame.image.load(f".\\images\\renome_piece.png").convert_alpha()
        self.image_renome_piece = pygame.transform.rotate(pygame.transform.scale(self.image_renome_piece_load, (20,20)),45)

    def print(self,screen):
        screen.blit(self.image_board, (int(screen.get_width()/2-self.size[0]/2),screen.get_height()-660))

    def update_renome_pos(self,screen,players):
        for player in players:
            renome = player.get_renome()
            if renome%2 == 0:
                screen.blit(self.image_renome_piece, (int(screen.get_width()/2-self.size[0]/2)+317+15*renome,screen.get_height()-660+122))
            else:
                screen.blit(self.image_renome_piece, (int(screen.get_width()/2-self.size[0]/2)+317+15*renome,screen.get_height()-660+122-17))


    def update_renome_pos(self,screen,players):
        for player in players:
            renome = player.get_renome()
            if renome%2 == 0:
                screen.blit(self.image_renome_piece, (int(screen.get_width()/2-self.size[0]/2)+317+15*renome,screen.get_height()-660+122))
            else:
                screen.blit(self.image_renome_piece, (int(screen.get_width()/2-self.size[0]/2)+317+15*renome,screen.get_height()-660+122-17))


    def update_score_pos(self,screen,players):

        for player in players:
    
            score = player.get_score()
            if score <= 16:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(screen.get_width()/2-self.size[0]/2)+20 +35*score ,screen.get_height()-660+47), 15)
            elif score <=20:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(screen.get_width()/2-self.size[0]/2)+20 +35*16 ,screen.get_height()-660+47 +40*(score-16) ), 15)
            elif score <= 36:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(screen.get_width()/2-self.size[0]/2)+20 +35*16-35*(score-20) ,screen.get_height()-660+47 +40*(20-16) ), 15)
            elif score <= 40:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(screen.get_width()/2-self.size[0]/2)+20 +35*16-35*(36-20) ,screen.get_height()-660+47 +40*(20-16)-40*(score-36) ), 15)

#circle()

#150 haut +28
#164 bas
