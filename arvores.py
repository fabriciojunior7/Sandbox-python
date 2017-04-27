import pygame
import entidades

class Arvore(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor, fisica):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor, fisica)

	def desenhar(self, tela, x, y):
		self.corpo = pygame.Rect(self.x-(x-300), self.y-(y-300), self.largura, self.altura)
		pygame.draw.rect(tela, self.cor, self.corpo)
		if(self.fisica == True):
			self.desenharFisica(tela)