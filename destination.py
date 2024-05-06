import pygame

class Card_bateau():

	def __init__(self,id,cout_coul,gain,gain_col,echange=True):
		self.echange=echange #if True = ehcnage if False = Influence
		self.size=(300,150)
		self.id=id
		self.face="F"
		self.cout_coul = cout_coul
		self.gain = gain
		self.gain_col = gain_col
		self.pos=None
		self.init_image()
		

	def init_image(self):
		if self.echange:
			self.image_echange_front_load = pygame.image.load(f".\\images\\echange\\echange_{self.id}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
			self.image_echange_front = pygame.transform.scale(self.image_echange_front_load, self.size) #changement de taille
			self.image_echange_back_load = pygame.image.load(f".\\images\\echange\\echange_verso.png").convert_alpha() 
			self.image_echange_back = pygame.transform.scale(self.image_echange_back_load, self.size)
			self.back_rect=self.image_echange_back.get_rect()
			self.front_rect=self.image_echange_front.get_rect()
		else:
			self.image_influence_front_load = pygame.image.load(f".\\images\\influence\\influence_{self.id}.png").convert_alpha() #pour la transaprance on utilise convert_alpha
			self.image_influence_front = pygame.transform.scale(self.image_influence_front_load, self.size) #changement de taille
			self.image_influence_back_load = pygame.image.load(f".\\images\\influence\\influence_verso.png").convert_alpha() 
			self.image_influence_back = pygame.transform.scale(self.image_influence_back_load, self.size)
			self.back_rect=self.image_influence_back.get_rect()
			self.front_rect=self.image_influence_front.get_rect()

	def print(self,screen,pos):
		if  self.face =="F":
			if self.echange:
				self.front_rect.x=pos[0]
				self.front_rect.y=pos[1]
				screen.blit(self.image_echange_front, (self.front_rect.x,self.front_rect.y))
			else :
				self.front_rect.x=pos[0]
				self.front_rect.y=pos[1]
				screen.blit(self.image_influence_front, (self.front_rect.x,self.front_rect.y))
		else:
			if self.echange:
				self.back_rect.x=pos[0]
				self.back_rect.y=pos[1]
				screen.blit(self.image_echange_back, (self.back_rect.x,self.back_rect.y))
			else:
				self.back_rect.x=pos[0]
				self.back_rect.y=pos[1]
				screen.blit(self.image_influence_back, (self.back_rect.x,self.back_rect.y))
		self.pos=pos
	

	def info(self):
		print(f"échange : {self.echange}")
		print(f"id : {self.id}")
		print(f"cout : {self.cout_coul}")
		print(f"gain : {self.gain}")
		print(f"gain colonnes : {self.gain_col}")
