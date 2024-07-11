#5 rows and 11 columns of aliens, they move collectively to the right or left
#ocasionally shoot lasers
#when they reach the edge of the window they move slightly downward

import pygame, random


class Alien(pygame.sprite.Sprite):
	def __init__(self, type, x, y):
		super().__init__()
		self.type = type
		path = f"Graphics/alien_{type}.png"
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(topleft = (x, y))

	def update(self, direction):
		self.rect.x += direction 


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width, offset): 
        super().__init__()

        self.screen_width = screen_width

        self.offset = offset
        
        path = "Graphics/mystery.png"
        self.image = pygame.image.load(path)

        #it can spawn from either the top left or right
        x=random.choice([self.offset/2, screen_width +self.offset - self.image.get_width()]) 
        
        self.rect = self.image.get_rect(topleft = (x, 90))

        if x==self.offset/2: 
            self.speed = 3
        else:
            self.speed = -3


    def update(self):
        self.rect.x += self.speed 

        #we kill it if it exits the screen
        if self.rect.right > self.screen_width + self.offset/2:
            self.kill()
        elif self.rect.left < self.offset/2:
            self.kill()
