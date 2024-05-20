import pickle
from  classes.destination import Card_bateau


#rouge bleu vert violet jaune
for i in range(20):
    ok=False
    while ok == False:
  
        ide=i+1
        card=Card_bateau(ide,tuple(input("cout : rouge bleu vert violet jaune ->").split(" ")),tuple(str(input("gain->"))).split(" "),tuple(input("gain colonne: ->").split(" ")))
        card.info()
        ok=bool(input("Vous convient ?"))
    src = "destinations\\echange_"+str(int(i+1))+".pkl"
    file1 = open(src, "wb")
    pickle.dump(card, file1)
    file1.close()

    f = open(src, 'rb')
    obj = pickle.load(f)
    obj.info()