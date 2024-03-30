import pygame

class Pion():

	def __init__(self,name):
		self.name=name
		self.size=(45,45)
		self.pos=[0,0]

		self.init_image()

	def init_image(self):
		self.pion_image_load=pygame.image.load(f".\\images\\{self.name}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
		self.pion_image=pygame.transform.scale(self.pion_image_load, self.size) #changement de taille

	def print(self,screen,pos=False):
		if pos !=False:
			self.pos=pos

		screen.blit(self.pion_image, self.pos)