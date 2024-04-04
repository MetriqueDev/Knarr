import pickle
from  classes.destination import Card_bateau


#rouge bleu vert violet jaune
for i in range(20):
    ok=False
    while ok == False:
        print(f"Vous êtes à l'id {i+1}")
        card=Card_bateau(i+1,tuple(input("cout : rouge bleu vert violet jaune ->").split(" ")),int(input("gain->")),tuple(input("gain colonne: ->").split(" ")))
        card.info()
        ok=bool(input("Vous convient ?"))
    file1 = open(f"destinations\\echange_{i+1}", "wb")
    pickle.dump(card, file1)


