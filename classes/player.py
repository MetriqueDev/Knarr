

class Player():

    def __init__(self,name,niveau):
        self.name=name
        self.niveau=niveau
        self.nombre_de_vicoire=0
        self.nombre_de_defaite=0

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