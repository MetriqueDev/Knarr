import pygame
import random

class Board():

    def __init__(self):
        self.size=(600,250)#(250,400)
        self.recrues={"p_rouge":None,"p_jaune":None,"p_vert":None,"p_bleu":None,"p_violet":None}
        self.active_card_b=None
        self.active_card_RE=None
        self.init_image()

    def init_cartes(self,package):
        for card in self.recrues:

            if self.recrues[card] == None:
                self.recrues[card] = package.package[0]
                del package.package[0]


    def init_image(self):
        self.image_board_load = pygame.image.load(f".\\images\\plateau.png").convert_alpha() #pour la transaprance on utilise convert_alpha
        self.image_board = pygame.transform.scale(self.image_board_load, self.size) #changement de taille
        self.image_renome_piece_load = pygame.image.load(f".\\images\\renome_piece.png").convert_alpha()
        self.image_renome_piece = pygame.transform.rotate(pygame.transform.scale(self.image_renome_piece_load, (20,20)),45)

        self.image_renome_piece2_load = pygame.image.load(f".\\images\\renome_piece2.png").convert_alpha()
        self.image_renome_piece2 = pygame.transform.rotate(pygame.transform.scale(self.image_renome_piece2_load, (20,20)),45)

        self.image_renome_piece3_load = pygame.image.load(f".\\images\\renome_piece3.png").convert_alpha()
        self.image_renome_piece3 = pygame.transform.rotate(pygame.transform.scale(self.image_renome_piece3_load, (20,20)),45)

        self.image_renome_piece4_load = pygame.image.load(f".\\images\\renome_piece4.png").convert_alpha()
        self.image_renome_piece4 = pygame.transform.rotate(pygame.transform.scale(self.image_renome_piece4_load, (20,20)),45)

    def print(self,screen):
        screen.blit(self.image_board, (int(10),screen.get_height()-660))

    def update_renome_pos(self,screen,players):
        i=0
        for player in players:
           
            if i==0:
                image = self.image_renome_piece
            elif i==1:
                image = self.image_renome_piece2
            elif i==2:
                image = self.image_renome_piece3
            elif i==3:
                image = self.image_renome_piece4
            renome = player.get_renome()
            if renome%2 == 0:
                screen.blit( image, (int(10)+317+15*renome,screen.get_height()-660+122))
            else:
                screen.blit(image, (int(10)+317+15*renome,screen.get_height()-660+122-17))
            i+=1




    def update_score_pos(self,screen,players):
        i=0
        for player in players:
            if i==0:
                color = (255,0,0)
            elif i==1:
                color = (255,255,0)
            elif i==2:
                color = (0,255,0)
            elif i==3:
                color = (0,0,255)
            score = player.get_score()
            if score <= 16:
                pygame.draw.circle(screen, color, (int(10)+20 +35*score ,screen.get_height()-660+47), 15)
            elif score <=20:
                pygame.draw.circle(screen, color, (int(10)+20 +35*16 ,screen.get_height()-660+47 +40*(score-16) ), 15)
            elif score <= 36:
                pygame.draw.circle(screen, color, (int(10)+20 +35*16-35*(score-20) ,screen.get_height()-660+47 +40*(20-16) ), 15)
            elif score <= 40:
                pygame.draw.circle(screen, color, (int(10)+20 +35*16-35*(36-20) ,screen.get_height()-660+47 +40*(20-16)-40*(score-36) ), 15)
            i+=1
    def recrutement_print(self,screen):
        a=0
        for couleur_card in self.recrues:
            if self.recrues[couleur_card] != None:
                self.recrues[couleur_card].print(screen,(10+a*120,screen.get_height()-400))
                a+=1

    def dragndrop_recrutement(self,screen,event,hand,package,player): #du recrutement à la main
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for couleur in self.recrues:
                    if self.recrues[couleur].front_rect.collidepoint(event.pos):

                        #si la carte cliqué est de la couelur de la dernière carte du joueur

                        self.active_card_b=couleur

                        mouse_x, mouse_y = event.pos
                        #position de la souris sur l'image

                        self.offset_x=mouse_x-self.recrues[couleur].pos[0]
                        self.offset_y=mouse_y-self.recrues[couleur].pos[1]

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                if (1440<event.pos[0]<1826 )and (690<event.pos[1]<910) and self.active_card_b != None:
                    if len(hand.main)<3:
                        if  self.active_card_b == str("p_"+player.couleur):
                            hand.main.append(self.recrues[self.active_card_b])
                            self.recrues[self.active_card_b]=None
                            self.recrues[self.active_card_b]=package.package[0]
                            del package.package[0]
                            self.active_card_b=None
                            return True
                        else:
                            if player.get_recrue() !=0:
                                player.add_recrue(-1)
                                hand.main.append(self.recrues[self.active_card_b])
                                self.recrues[self.active_card_b]=None
                                self.recrues[self.active_card_b]=package.package[0]
                                del package.package[0]
                                self.active_card_b=None
                                return True

                self.active_card_b=None
                
            else:
                self.active_card_b=None
            self.active_card_b=None#
        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_b != None:

                self.recrues[self.active_card_b].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))

        return False

    def dragndrop_recrue_to_equipage(self,screen,event,player,package): #du recrutement à l'équipage
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for card in self.recrues:
                    if self.recrues[card].front_rect.collidepoint(event.pos):
                        self.active_card_RE = card
                        mouse_x, mouse_y = event.pos
                        self.offset_x = mouse_x - self.recrues[card].pos[0]
                        self.offset_y = mouse_y - self.recrues[card].pos[1]
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if ((1280-10)<event.pos[0]<(1280-10+125*5+20)) and ((-410-200+int(screen.get_height() ))-player.taille )<event.pos[1]<((-410-200+int(screen.get_height() ))-player.taille +220) and self.active_card_RE != None:
                    player.add_equipage(self.recrues[self.active_card_RE])
                    self.recrues[self.active_card_RE] = None
                    self.recrues[self.active_card_RE] = package.package[0]
                    del package.package[0]
                    self.active_card_RE = None
                    return True
                self.active_card_RE = None
            else:
                self.active_card_RE = None
            self.active_card_RE = None
        elif event.type == pygame.MOUSEMOTION:
            if self.active_card_RE != None:
                self.recrues[self.active_card_RE].print(screen, (event.pos[0] - self.offset_x, event.pos[1] - self.offset_y))

        return False