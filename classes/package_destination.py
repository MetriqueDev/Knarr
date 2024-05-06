import random
import pickle
from classes.destination import Card_bateau

class Package_Destination():
    def __init__(self):
        self.echange=[]
        self.influence=[]

        #INITIALISATION DES CARTES ÉCHANGE ET INFLUENCE (échange en premier)
        self.card_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.card_cout=[('violet','violet'),('vert','vert'),('rouge','rouge'),('different','different','different'),('different','different','different'),('vert','vert'),
        ('rouge','rouge'),('violet','violet'),('jaune','jaune'),('different','different','different'),('different','different','different'),('bleu','bleu'),
        ('violet','violet'),('bleu','bleu'),('different','different','different'),('rouge','rouge'),('vert','vert'),('jaune','jaune'),('bleu','bleu'),('jaune','jaune'),
        ('egal','egal','egal','egal'),('violet','violet','violet','rouge','rouge'),('violet','violet','jaune','jaune'),
        ('egal','egal','egal','egal'),('vert','vert','violet','violet'),('bleu','bleu','bleu','violet','violet'),
        ('jaune','jaune','bleu','bleu'),('rouge','jaune','vert','bleu','violet'),('vert','vert','vert','bleu','bleu')
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
        self.card_gain_col=[('pioche','rien','victoire'),('rien','recrue','rien'),('victoire','rien','victoire'),('victoire','renommee','recrue'),('rien','victoire','rien'),('le 6e')






        ]
        self.card_ech=[]
        for i in range(len(self.card_id)):
            self.echange.append(Card_bateau(self.card_id[i], self.card_cout[i], self.gain[i], self.card_gain_col[i]))
        

        