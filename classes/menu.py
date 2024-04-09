import pygame

class Menu():

	def __init__(self,step):
		self.step=step
		self.size=(1059/2,282/2)

		self.init_image()

	def init_image(self):
		#les images des boutons
		self.background_menu_load=pygame.image.load(f".\\images\\MENU\\background.png").convert_alpha()
		

		#inscription et connexion
		self.inscription_image_load=pygame.image.load(f".\\images\\MENU\\inscrire.png").convert_alpha()
		self.inscription_image=pygame.transform.scale(self.inscription_image_load, self.size)
		self.inscription_rect = self.inscription_image.get_rect()

		self.connexion_image_load=pygame.image.load(f".\\images\\MENU\\connexion.png").convert_alpha() 
		self.connexion_image=pygame.transform.scale(self.connexion_image_load, self.size)
		self.connexion_rect = self.connexion_image.get_rect()

	def print(self,screen):
		#affichage
		self.background_menu_image=pygame.transform.scale(self.background_menu_load, (screen.get_width(),screen.get_height()))
		screen.blit(self.background_menu_image,(0,0))

		self.inscription_rect.x=int(screen.get_width()/2-self.size[0]/2)
		self.inscription_rect.y=int(screen.get_height()/2-self.size[1]/2-10)
		screen.blit(self.inscription_image, (self.inscription_rect.x,self.inscription_rect.y))

		self.connexion_rect.x=int(screen.get_width()/2-self.size[0]/2)
		self.connexion_rect.y=int(screen.get_height()/2+self.size[1]/2+10)
		screen.blit(self.connexion_image, (self.connexion_rect.x,self.connexion_rect.y))


	def menu_interaction(self,mouse_pos):
		if self.inscription_rect.collidepoint(mouse_pos):
			return True
		elif self.connexion_rect.collidepoint(mouse_pos):
			return True
		return False


      