import pygame
import entidades

class Ferramenta(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor, fisica, imagem):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor, fisica)
		self.imagem = imagem
		self.corpo = self.imagem.get_rect()

	def desenharFerramenta(self, tela):
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		tela.blit(self.imagem, self.corpo)