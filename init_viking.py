import pickle
from  classes.card import Card


#rouge bleu vert violet jaune
card_types=["bleu1","bleu2","bleu3","bleu4",    "jaune1","jaune2","jaune3","jaune4",    "rouge1","rouge2","rouge3","rouge4",    "vert1","vert2","vert3","vert4",    "violet1","violet2","violet3","violet4"]
card_num=[0,0,3,3,3,0,4,0,3,0,0,0,0,0,4,0,0,3,0,4]
for i in range(len(card_types)):

    viking=Card(card_types[i],input("gain->"),card_num[i])
    viking.print_info()
    src = "vikings\\viking"+str(i)+".pkl"
    file1 = open(src, "wb")
    pickle.dump(viking, file1)
    file1.close()
    f=open(src,'rb')
    vik = pickle.load(f)
    f.close()
    vik.print_info()


