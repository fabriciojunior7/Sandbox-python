import pygame
import ferramentas

class Picareta(ferramentas.Ferramenta):
	def __init__(self, x, y, largura, altura, cor, fisica, imagem):
		ferramentas.Ferramenta.__init__(self, x, y, largura, altura, cor, fisica, imagem)
		