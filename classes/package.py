import random
import pickle
import classes.card
from classes.card import Card
class Package():
    def __init__(self,nbr_player=4):
        self.nbr_player=nbr_player
        self.package=[]

        card_types=["bleu1","bleu2","bleu3","bleu4",    "jaune1","jaune2","jaune3","jaune4",    "rouge1","rouge2","rouge3","rouge4",    "vert1","vert2","vert3","vert4",    "violet1","violet2","violet3","violet4"]
        card_gains=["renommee","recrue","victoire","bracelet","recrue","victoire","bracelet","renommee","renommee","bracelet","recrue","victoire","victoire","renommee","bracelet","recrue","bracelet","renommee","recrue","victoire"]
        card_num=[0,0,3,3,3,0,4,0,3,0,0,0,0,0,4,0,0,3,0,4]
        for i in range(len(card_num)):
            card=Card(card_types[i],card_gains[i],card_num[i])
            card.init_image()
            if self.nbr_player == 4:
                self.package.append(card)
            elif self.nbr_player ==3:
                if card.num != 4:
                    self.package.append(card)
            elif self.nbr_player ==2:
                if card.num ==0:
                    self.package.append(card)
        print(self.package)
    

    def init_pioche(self):
        for i in range(5):
            vik = self.package[-1]
            del self.package[-1]
            self.pioche.append(vik)
        
    def print_pioche(self,screen):
        for i in range(len(self.pioche)):
            self.pioche[i].print(screen,(int(screen.get_width()/2-len(self.pioche)*125/2)+i*125, 310))
        
    def print_package(self,screen):
        try:
            print("1")
            self.package[0].face="B"
            print("2")
            self.package[0].print(screen,(200,200))
        except:
            print("Oh non!")
            print(self.package)
            pass

    def pioche_hand(self,hand):
        print(self.package)
        if len(self.package) >0:
            vik = self.package[-1]
            del self.package[-1]
            hand.main.append(vik)
        else:
            return False

    def shuffle(self):
        random.shuffle(self.package)
        print(self.package)