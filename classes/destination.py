import pygame

class Card_bateau():

	def __init__(self,name,echange=True):
		self.echange=echange #if True = ehcnage if False = Influence
		self.size=(300,150)
		self.name=name
		self.face="F"
		self.init_image()

	def init_image(self):
		if self.echange:
			self.image_echange_front_load = pygame.image.load(f".\\images\\echange\\{self.name}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
			self.image_echange_front = pygame.transform.scale(self.image_echange_front_load, self.size) #changement de taille
			self.image_echange_back_load = pygame.image.load(f".\\images\\echange\\echange_verso.png").convert_alpha() 
			self.image_echange_back = pygame.transform.scale(self.image_echange_back_load, self.size)
		else:
			self.image_influence_front_load = pygame.image.load(f".\\images\\influence\\{self.name}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
			self.image_influence_front = pygame.transform.scale(self.image_influence_load, self.size) #changement de taille
			self.image_influence_back_load = pygame.image.load(f".\\images\\influence\\influence_verso.png").convert_alpha() 
			self.image_influence_back = pygame.transform.scale(self.image_influence_back_load, self.size)

	def print(self,screen):
		if self.echange:
			if  self.face =="F":
				screen.blit(self.image_echange_front, (10,10))
				screen.blit(self.image_echange_back, (10,150+10))

def liste(ech,infl):
	for i in range(20):
		ech.append(str("echange_"+str(i+1)))
	for i in range(15):
		infl.append(str("influence_"+str(i+1)))
