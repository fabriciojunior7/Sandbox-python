import pygame, random
import entidades

class Zumbie(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor)
		#Atributos
		self.velocidadeAndar = random.randint(2, 6)/10.0
		self.campoVisao = 300

	def desenhar(self, tela, x, y):
		self.corpo = pygame.Rect(self.x-(x-340), self.y-(y-340), self.largura, self.altura)
		pygame.draw.rect(tela, self.cor, self.corpo)
		#print("%i - %i" % (self.x, self.y))

	def seguir(self, x, y, largura, altura):
		if((x >= self.x-self.campoVisao and x <= self.x+self.campoVisao) and (y >= self.y-self.campoVisao and y <= self.y+self.campoVisao)):
			#X
			if(self.x < x):
				self.x += self.velocidadeAndar

			elif(self.x > x):
				self.x -= self.velocidadeAndar
			#Y
			if(self.y < y):
				self.y += self.velocidadeAndar

			elif(self.y > y):
				self.y -= self.velocidadeAndar