import pygame
import random
width = 1080
height = 720

class Drop:
	x = 0
	y = 0
	dropWidth = 3
	dropHeight = 15
	vel = 3

	def fall(self):
		self.y += self.vel
		if self.y > (height):
			self.y = random.randint(0,height)-height
		pygame.draw.rect(win, (55,55,255), (self.x, self.y, self.dropWidth, self.dropHeight))

pygame.init()

win = pygame.display.set_mode((width,height))

pygame.display.set_caption("First Game")

sizes = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,5]

drops = []
for x in range(500):
	drops.append(Drop())
	drops[x].x = random.randint(0,width)
	drops[x].y = random.randint(0,height) - height
	size = sizes[random.randint(0,len(sizes)-1)]
	drops[x].dropWidth = size
	drops[x].dropHeight = size*5
	drops[x].vel = size * 3 + 2

run = True
while run:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	

	win.fill((0,0,0))
	for drop in drops:
		drop.fall()
	pygame.display.update()

pygame.quit()




