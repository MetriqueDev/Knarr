import pygame

class Board():

    def __init__(self):
        self.size=(600,250)#(250,400)
        self.equipage={"vert":[],"rouge":[],"bleu":[],"violet":[],"jaune":[]}
        self.active_card_b=None

        self.init_image()

    def init_image(self):
        self.image_board_load = pygame.image.load(f".\\images\\plateau.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.image_board = pygame.transform.scale(self.image_board_load, self.size) #changement de taille
        self.image_renome_piece_load = pygame.image.load(f".\\images\\renome_piece.png").convert_alpha()
        self.image_renome_piece = pygame.transform.rotate(pygame.transform.scale(self.image_renome_piece_load, (20,20)),45)

    def print(self,screen):
        screen.blit(self.image_board, (int(10),screen.get_height()-660))

    def update_renome_pos(self,screen,players):
        for player in players:
            renome = player.get_renome()
            if renome%2 == 0:
                screen.blit(self.image_renome_piece, (int(10)+317+15*renome,screen.get_height()-660+122))
            else:
                screen.blit(self.image_renome_piece, (int(10)+317+15*renome,screen.get_height()-660+122-17))


    def update_renome_pos(self,screen,players):
        for player in players:
            renome = player.get_renome()
            if renome%2 == 0:
                screen.blit(self.image_renome_piece, (int(10)+317+15*renome,screen.get_height()-660+122))
            else:
                screen.blit(self.image_renome_piece, (int(10)+317+15*renome,screen.get_height()-660+122-17))


    def update_score_pos(self,screen,players):

        for player in players:
    
            score = player.get_score()
            if score <= 16:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(10)+20 +35*score ,screen.get_height()-660+47), 15)
            elif score <=20:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(10)+20 +35*16 ,screen.get_height()-660+47 +40*(score-16) ), 15)
            elif score <= 36:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(10)+20 +35*16-35*(score-20) ,screen.get_height()-660+47 +40*(20-16) ), 15)
            elif score <= 40:
                pygame.draw.circle(screen, ( 169, 50, 38 ), (int(10)+20 +35*16-35*(36-20) ,screen.get_height()-660+47 +40*(20-16)-40*(score-36) ), 15)

    def recrutement(self,screen):
        a=0
        for card in self.equipage:
            self.equipage[card].print(screen,(10+a*120,screen.get_height()-400))
            a+=1

    def dragndrop_recrutement(self,screen,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for card in self.equipage:
                    if self.equipage[card].front_rect.collidepoint(event.pos):
                        print(type(self.equipage[card]))
                        print("ok")
                        self.active_card_b=card
                        mouse_x, mouse_y = event.pos
                        #position de la souris sur l'image
                        self.offset_x=mouse_x-self.equipage[card].pos[0]
                        self.offset_y=mouse_y-self.equipage[card].pos[1]
                        print(self.offset_x,self.offset_y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                    self.active_card_b=None
            else:
                self.active_card_e=None
            self.active_card_b=None
        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_b != None:
                #print("bouge")
                self.equipage[self.active_card_b].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))
                print((event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))
                print((screen.get_width()/2-100,screen.get_width()/2+100))
                print((screen.get_height()/2+100,screen.get_height()/2-100))
#circle()

#150 haut +28
#164 bas