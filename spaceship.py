import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):

	def __init__(self, screen_width, screen_height, offset):
		super().__init__()

		self.screen_width = screen_width
		self.screen_height = screen_height
		self.speed = 6
		self.offset = offset 

		self.lasers_group = pygame.sprite.Group()

		self.laser_ready = True #laser is initially ready
		self.laser_time = 0 #how long since the last shot - we need it for the delay so the spaceship can't shoot 60 times per second
		self.laser_delay = 200 #ms

		self.image = pygame.image.load("Graphics/spaceship.png")

		self.rect = self.image.get_rect(midbottom = ((self.screen_width + self.offset)/2,self.screen_height))

		#sounds
		self.laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")
		

	def get_user_input(self):
		keys = pygame.key.get_pressed() 

		if keys[pygame.K_RIGHT]:	
			self.rect.x += self.speed	
		if keys[pygame.K_LEFT]:	
			self.rect.x -= self.speed	

		if keys[pygame.K_SPACE] and self.laser_ready: 
			self.laser_ready = False
			self.laser_time = pygame.time.get_ticks()

			laser = Laser(self.rect.center, 5, self.screen_height)
			self.lasers_group.add(laser)
			self.laser_sound.play()


	def update(self):
		self.get_user_input()
		self.constrain_movement()
		self.lasers_group.update() 
		self.recharge_laser()


	#so the player can't move outside the screen
	def constrain_movement(self):
		if self.rect.right > self.screen_width: 
			self.rect.right = self.screen_width
		if self.rect.left < self.offset: 
			self.rect.left = self.offset 

	def recharge_laser(self):
		if not self.laser_ready:
			current_time = pygame.time.get_ticks() 
			if current_time - self.laser_time >= self.laser_delay:
				self.laser_ready = True


	def reset(self):
		self.rect = self.image.get_rect(midbottom = ((self.screen_width+self.offset)/2, self.screen_height))
		self.lasers_group.empty() 





















