

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

    def add_scoe(self,add):
        if ((self.score+add)>(-1)):
            self.score+=add

    def get_renome(self):
        return self.renome