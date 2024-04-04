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
			self.image_front_load = pygame.image.load(f".\\images\\echange\\{self.name}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
			self.image_front = pygame.transform.scale(self.image_front_load, self.size) #changement de taille
			self.front_rect = self.image_front.get_rect()

			self.image_back_load = pygame.image.load(f".\\images\\echange\\echange_verso.png").convert_alpha() 
			self.image_back = pygame.transform.scale(self.image_back_load, self.size)
			self.back_rect = self.image_back.get_rect()
		else:
			self.image_front_load = pygame.image.load(f".\\images\\influence\\{self.name}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
			self.image_front = pygame.transform.scale(self.image_front_load, self.size) #changement de taille
			self.front_rect = self.image_front.get_rect()

			self.image_back_load = pygame.image.load(f".\\images\\influence\\influence_verso.png").convert_alpha() 
			self.image_back = pygame.transform.scale(self.image_back_load, self.size)
			self.back_rect = self.image_back.get_rect()


	def print(self,screen):
		if  self.face =="F":
			self.front_rect.x=10
			self.front_rect.y=10
			screen.blit(self.image_front, (self.front_rect.x,self.front_rect.y))
		else:
			self.back_rect.x=10
			self.back_rect.y=150+10
			screen.blit(self.image_back, (self.back_rect.x,self.back_rect.y))


def liste(ech,infl):
	for i in range(20):
		ech.append(str("echange_"+str(i+1)))
	for i in range(15):
		infl.append(str("influence_"+str(i+1)))
