import pygame
import random

class Board():

    def __init__(self):
        self.size=(600,250)#(250,400)
        self.recrues={"p_rouge":[],"p_jaune":[],"p_vert":[],"p_bleu":[],"p_violet":[]}
        self.active_card_b=None
        self.init_image()

    def init_cartes(self,package):
        a=0
        for card in self.recrues:
            #print(package.package)
            if self.recrues[card] == []:
                self.recrues[card] = package.package[a]
                a+=1


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

    def recrutement_print(self,screen):
        a=0
        for card in self.recrues:
            if self.recrues[card] != []:
                self.recrues[card].print(screen,(10+a*120,screen.get_height()-400))
                a+=1

    def dragndrop_recrutement(self,screen,event,hand,package):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("click")
                for card in self.recrues:
                    if self.recrues[card].front_rect.collidepoint(event.pos):
                        #print(type(self.equipage[card]))
                        #print("ok")
                        self.active_card_b=card
                        print(self.active_card_b, type(self.active_card_b))
                        print(self.recrues[self.active_card_b])
                        print(self.recrues)
                        mouse_x, mouse_y = event.pos
                        #position de la souris sur l'image
                        #print(self.equipage[card])
                        self.offset_x=mouse_x-self.recrues[card].pos[0]
                        self.offset_y=mouse_y-self.recrues[card].pos[1]
                        #print(self.offset_x,self.offset_y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                if (1450<event.pos[0]<1450+370 )and (700<event.pos[1]<900) and self.active_card_b != None:
                    if len(hand.main)<3:
                        hand.main.append(self.recrues[self.active_card_b])
                        self.recrues[self.active_card_b]=[]
                        self.recrues[self.active_card_b]=package.package[0]
                        del package.package[0]
                        self.active_card_b=None
                        #print(self.equipage)
                        #print(len(self.equipage))
                        print("posé")
                        #print(len(package.package))
                        #print(len(package.package))
                        return True
                self.active_card_b=None
                
            else:
                self.active_card_b=None
            self.active_card_b=None#
        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_b != None:
                #print("bouge")
                self.recrues[self.active_card_b].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))
                #print((event.pos[0],event.pos[1]))
                #print((screen.get_width()/2-200,screen.get_width()/2+200))
                #print((screen.get_height()/2))
        return False

#circle()

#150 haut +28
#164 bas