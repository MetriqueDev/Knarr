from boat import Boat

class Player():

    def __init__(self,name,niveau,ia=False):
        self.name=name
        self.ia=ia
        self.niveau=niveau
        self.nombre_de_vicoire=0
        self.nombre_de_defaite=0
        self.bracelet=3
        self.recrue=3

        self.equipage={"vert":[],"rouge":[],"bleu":[],"violet":[],"jaune":[]}

    def init_boat(self):
        self.boat=Boat()

    def info(self):
        print("name:",self.name)
        print("niveau:",self.niveau)

    def game_init(self):
        self.score = 0
        self.renome = 0

    def add_renome(self,add):
        if ((self.renome + add)<15) and ((self.renome+add)>(-1)):
            self.renome+=add

    def add_score(self,add):
        if ((self.score+add)>(-1)):
            self.score+=add
        if ((self.score + add)>40):
            self.score=40

    def get_renome(self):
        return self.renome

    def add_renome_to_score(self):
        if self.renome<=3:
            self.score+=1
        elif self.renome<=6:
            self.score+=2
        elif self.renome<=10:
            self.score+=3
        elif self.renome<=14:
            self.score+=4

    def get_score(self):
        return self.score

    def get_recrue(self):
        return self.recrue
    
    def get_bracelet(self):
        return self.bracelet


    def add_equipage(self,card):
        self.equipage[card.couleur].append(card)

    def print_equipage(self,screen):
        taille=30
        x=0
        for couleur in self.equipage.keys():
            for i in range(len(self.equipage[couleur])):
                self.equipage[couleur][i].print(screen,(5+125*x,int(screen.get_height()-taille*len(self.equipage[couleur])+i*taille-self.equipage[couleur][i].size[1])))
            x+=1