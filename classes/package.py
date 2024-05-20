import random
import pickle
import classes.card
from classes.card import Card
class Package():
    def __init__(self,nbr_player=4):
        self.nbr_player=nbr_player
        self.package=[]

        
        card_types=["rouge2","rouge2","rouge3","rouge4","rouge4","rouge1","rouge2","rouge3","rouge4","rouge4",
                    "bleu1","bleu2","bleu3","bleu3","bleu4","bleu1","bleu1","bleu3","bleu3","bleu4",
                    "violet1","violet2","violet3","violet4","violet4","violet1","violet2","violet3","violet4","violet4",
                    "jaune2","jaune3","jaune3","jaune4","jaune4","jaune1","jaune2","jaune2","jaune2","jaune2",
                    "vert4","vert4","vert3","vert3","vert2","vert1","vert1","vert1","vert1","vert4"]
        card_gains=['bracelet','bracelet','recrue','victoire','victoire','renommee','bracelet','recrue','victoire','victoire',
                    'renommee','recrue','victoire','victoire','bracelet','renommee','renommee','victoire','victoire','bracelet',
                    'bracelet','renommee','recrue','victoire','victoire','bracelet','renommee','recrue','victoire','victoire',
                    'victoire','bracelet','bracelet','renommee','renommee','recrue','victoire','victoire','victoire','victoire',
                    'recrue','recrue','bracelet','bracelet','renommee','victoire','victoire','victoire','victoire','recrue']
        self.card_num=[3,0,4,0,4,3,0,0,0,0,0,0,4,0,0,0,4,3,0,3,0,0,0,3,4,0,3,0,4,0,4,4,0,0,0,3,0,0,0,3,0,3,0,4,0,0,0,3,4,0]
        for j in range(3):
            for i in range(len(self.card_num)):
                card=Card(card_types[i],card_gains[i],self.card_num[i])
                card.init_image()
                if self.nbr_player == 4:
                    self.package.append(card)
                elif self.nbr_player ==3:
                    if card.num != 4:
                        self.package.append(card)
                elif self.nbr_player <=2:
                    if card.num ==0:
                        self.package.append(card)


    def print_package(self,screen):
        try:

            self.package[0].face="B"
            self.package[0].print(screen,(200,200))
        except:
            pass

    def pioche_hand(self,hand):
   
        if len(self.package) >0:
            vik = self.package[-1]
            del self.package[-1]
            hand.main.append(vik)
        else:
            return False

    def shuffle(self):
        random.shuffle(self.package)
   
