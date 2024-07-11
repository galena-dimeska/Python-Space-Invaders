import pygame

class Laser(pygame.sprite.Sprite):

	def __init__(self, position, speed, screen_height): 
		super().__init__()

		self.speed = speed
		self.screen_height = screen_height

		self.image = pygame.Surface((4,15))
		self.image.fill((243, 216, 63))
		self.rect = self.image.get_rect(center = position) 

	def update(self):
		self.rect.y -= self.speed 

		#destroy every laser obj when it exits game window 
		if self.rect.y > self.screen_height +15 or self.rect.y < 0:
			self.kill() #removes sprite from all groups it belongs to 
