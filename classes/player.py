

class Player():

    def __init__(self,name,level):
        self.name=name
        self.level=level

    def info(self):
        print("name:",self.name)
        print("level:",self.level)

    def game_init(self):
        self.score = 0
        self.renome = 0

    def get_renome(self):
        return self.renome