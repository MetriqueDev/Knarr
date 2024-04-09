import random

class Package():
    def __init__(self,nbr_player=4):
        self.nbr_player=nbr_player
        self.package=[]
        
        for i in range(20):
            src = "vikings\\viking"+str(i)+".pkl"
            f=open(src,'rb')
            vik = pickle.load(f)
            f.close()
            if self.nbr_player == 4:
                self.package.append(vik)
            elif self.nbr_player ==3:
                if vik.num != 4:
                    self.package.append(vik)
            elif self.nbr_player ==2:
                if vik.num ==0:
                    self.package.append(vik)
        
    def print(self):
        for vik in self.package:
            vik.print_info()

    def pioche(self):
        if len(self.package) >0:
            vik = self.package[-1]
            del self.package[-1]
            return vik
        else:
            return False

    def shuffle(self):
        self.package=random.shuffle(self.package)