import pygame
import entidades

class Barra(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor, fisica):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor, fisica)