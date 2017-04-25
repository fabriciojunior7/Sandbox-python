import pygame

class Entidade(object):
	def __init__(self, x, y, largura, altura, cor):
		#Atributos
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura
		self.cor = cor
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)

	def desenhar(self, tela):
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		pygame.draw.rect(tela, self.cor, self.corpo)

	def update(self, x, y):
		self.x += x
		self.y += y