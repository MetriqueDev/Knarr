from classes.boat import Boat
from classes.hand import Hand
from classes.package import Package
from classes.card import Card
import pygame

class Player():

    def __init__(self,name,niveau,ia=False):
        self.name=name
        self.ia=ia
        self.niveau=niveau
        self.nombre_de_vicoire=0
        self.nombre_de_defaite=0

        self.hand=Hand()
        self.active_card_h=None
        self.active_card_p=None

        self.equipage={"rouge":[],"jaune":[],"vert":[],"bleu":[],"violet":[]}
    def init_boat(self):
        self.boat=Boat()

    def info(self):
        print("name:",self.name)
        print("niveau:",self.niveau)

    def game_init(self):
        self.score = 0
        self.renome = 0


        self.asplay = False
        self.Explore=False#destination et influence
        self.recrute=False#pioche et main 
        self.pioche=False#recrue 


        self.couleur=None

    def add_renome(self,add):
        if ((self.renome + add)<15) and ((self.renome+add)>(-1)):
            self.renome+=add
        else:
            self.renome=14

    def add_score(self,add):
        if ((self.score+add)>(-1)):
            self.score+=add
        if ((self.score + add)>40):
            self.score=40

    def get_renome(self):
        return self.renome

    def add_renome_to_score(self):
        if self.renome<3:
            self.score+=0
        elif self.renome<6:
            self.score+=1
        elif self.renome<10:
            self.score+=2
        elif self.renome<14:
            self.score+=3
        if self.renome==14:
            self.score+=5

    def get_score(self):
        return self.score

    def get_recrue(self):
        return self.boat.recrue
    
    def get_bracelet(self):
        return self.boat.bracelet
    
    def add_recrue(self,add):
        if ((self.boat.recrue + add)<=3):
            self.boat.recrue+=add
            if self.boat.recrue<0:
                self.boat.recrue=0
    
    def add_bracelet(self,add):
        if ((self.boat.bracelet + add)<=3):
            self.boat.bracelet+=add



    def add_equipage(self,card):
        self.equipage[card.couleur].append(card)

    def print_equipage(self,screen):
        
        self.taille=30
        pygame.draw.rect(screen, (100, 30, 22),  (1280-10, -410-200+int(screen.get_height() )-self.taille   ,125*5+20 ,220  ))
        x=0
        for couleur in self.equipage.keys():
            for i in range(len(self.equipage[couleur])):
                self.equipage[couleur][i].print(screen,(1280+125*x,-400+int(screen.get_height()-self.taille*len(self.equipage[couleur])+i*self.taille-self.equipage[couleur][i].size[1])))
            x+=1
    
    def dragndrop_hand(self,screen,event):#main to equipage
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, card in enumerate(self.hand.main):
                    print(num,card,card.front_rect.collidepoint(event.pos),card.front_rect.x,self.hand.main[num].front_rect.x,card.front_rect.y,self.hand.main[num].front_rect.y)
                    if card.front_rect.collidepoint(event.pos):
                        print("click_on")
                        self.active_card_h=num
                        mouse_x, mouse_y = event.pos
                        #position de la souris sur l'image
                        self.offset_x=mouse_x-self.hand.main[self.active_card_h].pos[0]
                        self.offset_y=mouse_y-self.hand.main[self.active_card_h].pos[1]
                        print("dragndrop_hand",self.offset_x,self.offset_y)

        if event.type == pygame.MOUSEBUTTONUP:
            
            if event.button==1:
                print("NTM",self.active_card_h)
                if ((1280-10)<event.pos[0]<(1280-10+125*5+20)) and ((-410-200+int(screen.get_height() ))-self.taille )<event.pos[1]<((-410-200+int(screen.get_height() ))-self.taille +220) and self.active_card_h != None: #position à adapter à l'equipage
                    print("hand")
                    self.add_equipage(self.hand.main[self.active_card_h]) 
                    self.couleur=self.hand.main[self.active_card_h].couleur
                    for card in self.equipage[self.hand.main[self.active_card_h].couleur]:
                        if card.gain == "renommee":
                            self.add_renome(1)
                        elif card.gain == "recrue":
                            self.add_recrue(1)
                        elif card.gain =="victoire":
                            self.add_score(1)
                        elif card.gain == "bracelet":
                            self.add_bracelet(1)
                    del self.hand.main[self.active_card_h]
                    self.active_card_h= None
                    return True
                else:
                    self.active_card_h=None
                self.active_card_h=None
            self.active_card_h=None
        

        #afficher l'image à la souris pendant le drag and drop si on bouge pas
        if self.active_card_h !=None:
            self.hand.main[self.active_card_h].print(screen,(event.pos[0]-self.offset_x,event.pos[1]-self.offset_y))





    #def recruter(self,screen,event,equipage):
    #        if event.button==1:
    #            if screen.get_width()/2-100<event.pos[0]<screen.get_width()/2+100 and event.pos[1]>screen.get_height()-200 and active_card != None: #position à adapter à l'equipage
    #                self.add_equipage(self.hand[active_card]) 
    #                for card in equipage[self.hand[active_card].couleur]:
    #                    if card.gain == "renommee":
    #                        self.add_renome(1)
    #                    elif card.gain == "recrue":
    #                        self.add_recrue(1)
    #                    elif card.gain =="victoire":
    #                        self.add_score(1)
    #                    elif card.gain == "bracelet":
    #                        self.add_bracelet(1)  
    #                self.hand= self.hand.pop(self.hand[active_card])
    #        self.dragndrop_pioche(screen, event)
    #        if event.button==1:
    #            if screen.get_width()/2-100<event.pos[0]<screen.get_width()/2+100 and event.pos[1]>screen.get_height()-200 and active_card != None: #position à adapter à la main
    #                if [self.pioche[active_card].couleur] == [self.hand[active_card].couleur]:
    #                    self.hand.append(self.pioche[active_card])
    #                    self.pioche.pop(self.pioche[active_card])
    #                    vik = self.package[-1]
    #                    del self.package[-1]
    #                    self.pioche.append(vik)
    #                    active_card=None       
    #                if [self.pioche[active_card].couleur] != [self.hand[active_card].couleur]:
    #                    self.add_recrue(-1)
    #                    self.hand.append(self.pioche[active_card])
    #                    self.pioche.pop(self.pioche[active_card])
    #                    vik = self.package[-1]
    #                    del self.package[-1]
    #                    self.pioche.append(vik)
    #                    active_card=None
    #                else:
    #                    active_card=None
    #        else:
    #                active_card=None