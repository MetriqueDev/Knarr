import pygame
from package import Package

class Game():
    def __init__(self,nbr_player=4):
        self.nbr_player=nbr_player
        self.package=Package(self.nbr_player)
    

