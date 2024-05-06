import random
import pickle
import classes.card
from classes.card import Card
class Package():
    def __init__(self,nbr_player=4):
        self.nbr_player=nbr_player
        self.package=[]
        
        for i in range(20):
            src = "vikings\\viking"+str(i)+".pkl"
            f=open(src,'rb')
            vik = pickle.load(f)
            vik.print_info()
            f.close()
            if self.nbr_player == 4:
                self.package.append(vik)
            elif self.nbr_player ==3:
                if vik.num != 4:
                    self.package.append(vik)
            elif self.nbr_player ==2:
                if vik.num ==0:
                    self.package.append(vik)
        print(self.package)
        
    def print_package(self,screen):
        try:
            print("1")
            self.package[0].face="B"
            print("2")
            self.package[0].print(screen,(200,200))
        except:
            print("Oh non!")
            pass

    def pioche_hand(self,hand):
        if len(self.package) >0:
            vik = self.package[-1]
            del self.package[-1]
            hand.main.append(vik)
        else:
            return False

    def shuffle(self):
        self.package=random.shuffle(self.package)