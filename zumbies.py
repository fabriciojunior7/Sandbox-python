import pygame, random
import entidades

class Zumbie(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor)
		#Atributos
		self.velocidadeAndar = random.randint(2, 6)/10.0
		self.campoVisao = 100

	def seguir(self, x, y, largura, altura):
		if((self.x+self.largura >= self.campoVisao and self.x <= largura-self.campoVisao) and (self.y+self.altura >= self.campoVisao and self.y <= altura-self.campoVisao)):
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