import random
import pickle
from classes.destination import Card_bateau

class Package_Destination():
    def __init__(self):
        self.echange=[]
        self.influence=[]
        self.verso=[]

        #INITIALISATION DES CARTES ÉCHANGE ET INFLUENCE (échange en premier)
        self.card_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.card_cout=[('violet','violet'),('vert','vert'),('rouge','rouge'),('different','different','different'),('different','different','different'),('vert','vert'),
        ('rouge','rouge'),('violet','violet'),('jaune','jaune'),('different','different','different'),('different','different','different'),('bleu','bleu'),
        ('violet','violet'),('bleu','bleu'),('different','different','different'),('rouge','rouge'),('vert','vert'),('jaune','jaune'),('bleu','bleu'),('jaune','jaune'),
        ('egal','egal','egal','egal'),('violet','violet','violet','rouge','rouge'),('violet','violet','jaune','jaune'),
        ('egal','egal','egal','egal'),('vert','vert','violet','violet'),('bleu','bleu','bleu','violet','violet'),
        ('jaune','jaune','bleu','bleu'),('rouge','jaune','vert','bleu','violet'),('vert','vert','vert','bleu','bleu'),
        ('rouge','rouge','vert','vert'),('jaune','jaune','jaune','vert','vert'),('bleu','bleu','rouge','rouge'),('rouge','jaune','vert','bleu','violet'),
        ('rouge','rouge','rouge','jaune','jaune'),('egal','egal','egal','egal')]
        self.card_gain=[('pioche'),('recrue','recrue'),('bracelet','renommee'),('bracelet'),('bracelet','recrue','pioche'),
        ('bracelet','recrue'),('bracelet'),('pioche'),('renommee'),('bracelet','renommee','pioche'),('bracelet'),('renommee','renommee'),
        ('bracelet','pioche'),('bracelet','renommee'),('recrue','renommee','pioche'),('bracelet','pioche'),('recrue'),('recrue'),
        ('recrue','renommee'),(''),('victoire','victoire','victoire','victoire','victoire','recrue'),('victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire','pioche'),
        ('victoire','victoire','victoire','victoire','victoire','victoire'),('victoire','victoire','victoire','victoire','victoire','bracelet'),('victoire','victoire','victoire','victoire','victoire','victoire'),
        ('victoire','victoire','victoire','victoire','victoire','victoire','victoire','renommee','renommee'),('victoire','victoire','victoire','victoire','victoire','victoire'),
        ('victoire','victoire','victoire','victoire','bracelet','recrue','renommee','pioche'),('victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire','recrue'),
        ('victoire','victoire','victoire','victoire','victoire','victoire'),('victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire','victoire'),
        ('victoire','victoire','victoire','victoire','victoire','victoire'),('victoire','victoire','victoire','victoire','bracelet','recrue','renommee','pioche'),
        ('victoire','victoire','victoire','victoire','victoire','victoire','victoire','bracelet'),('victoire','victoire','victoire','victoire','victoire','renommee')]
        self.card_gain_col=[('pioche','rien','victoire'),('rien','recrue','rien'),('victoire','rien','victoire'),('victoire','renommee','recrue'),('rien','victoire','rien'),('victoire','rien','recrue'),
        ('victoire','victoire','rien'),('victoire','pioche','rien'),('victoire','victoire','rien'),('rien','victoire','rien'),('victoire','renommee','recrue'),('rien','victoire','renommee'),('rien','victoire','pioche'),
        ('rien','renommee','victoire'),('rien','victoire','rien'),('victoire','rien','victoire'),('recrue','victoire','rien'),('victoire','victoire','rien'),
        ('renommee','rien','victoire'),('victoire','victoire','victoire'),('rien','rien','victoire'),('rien','rien','victoire'),('rien','victoire','rien'),('rien','rien','victoire'),
        ('rien','victoire','rien'),('rien','rien','victoire'),('rien','victoire','rien'),('rien','rien','victoire'),('rien','rien','victoire'),('rien','victoire','rien'),
        ('rien','rien','victoire'),('rien','victoire','rien'),('rien','rien','victoire'),('rien','rien','victoire'),('rien','rien','victoire')]
        self.card_ech=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        for i in range(20):
            self.echange.append(Card_bateau(self.card_id[i], self.card_cout[i], self.card_gain[i], self.card_gain_col[i], echange=self.card_ech[i]))
        for i in range(15):
            self.influence.append(Card_bateau(self.card_id[i+20], self.card_cout[i+20], self.card_gain[i+20], self.card_gain_col[i+20], self.card_ech[i+20]))



        #CRÉATION DES VERSO
        self.verso.append(Card_bateau(1, "rien", "rien", "rien", echange=True))
        self.verso.append(Card_bateau(1, "rien", "rien", "rien", echange=False))
        self.verso[0].face="V"
        self.verso[1].face="V"

        #MÉLANGE DES CARTES
        random.shuffle(self.echange)
        random.shuffle(self.influence)


        

    def print_pioche_dest(self,screen):
        print(self.echange)
        print(self.influence)
        for i in range(3):
            self.echange[i].print(screen, (int(i*300+305),5))
        for i in range(3):
            self.influence[i].print(screen,(int(i*300+305),155))
        self.verso[0].print(screen, (5,5))
        self.verso[1].print(screen, (5,155))

        