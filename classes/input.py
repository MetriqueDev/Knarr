import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale,font=None,text="",sound=True):
		
		if type(image) is list:
			self.image=image
			width = image[0].get_width()
			height = image[0].get_height()
			self.image[0] = pygame.transform.scale(image[0], (int(width * scale), int(height * scale)))
			self.image[1] = pygame.transform.scale(image[1], (int(width * scale), int(height * scale)))
			self.rect = self.image[0].get_rect()
		else:
			width = image.get_width()
			height = image.get_height()
			self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
			self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.font=font
		self.text=text
		self.survole=False
		self.sound=sound

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if self.sound==True and self.survole==False:
				pygame.mixer.music.load(".\\musique\\gui_sound\\select.wav")
				pygame.mixer.music.play()
			self.survole=True
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		else:
			self.survole=False

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		if type(self.image) is list:
			if self.survole:
				surface.blit(self.image[1], (self.rect.x, self.rect.y))
			else:
				surface.blit(self.image[0], (self.rect.x, self.rect.y))
		else:
			surface.blit(self.image, (self.rect.x, self.rect.y))
		if self.text != "":
			text_img=self.font.render(self.text,True,(100,100,100))
			surface.blit(text_img,(self.rect.x+100, self.rect.y+50))

		return action


class Input():
	def __init__(self, x, y, image, scale,font,TEXT_COL):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.text=""
		self.clicked = False
		self.select=False
		self.font=font
		self.TEXT_COL=TEXT_COL

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.select=True
				action = True
		else:
			if pygame.mouse.get_pressed()[0] == 1:
				self.select=False

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		text_img=self.font.render(self.text,True,(100,100,100))
		surface.blit(text_img,(self.rect.x+10, self.rect.y+20))

		return action

	def write(self,event):
		if self.select:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					print(self.text)
					print(len(self.text))
					self.text = ''
				elif event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					if len(self.text)!=11:
						self.text += event.unicode

	def get_input(self):
		return self.text