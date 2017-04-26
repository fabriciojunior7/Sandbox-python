import pygame, random
import arvores
import cores

class Chunk(object):
	def __init__(self, x, y, largura, altura, numArvores):
		#Atributos
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura
		self.numArvores = numArvores
		self.flora = []
		for i in range(self.numArvores):
			self.flora.append(arvores.Arvore(random.randint(self.x, self.largura+self.x-50), random.randint(self.y, self.altura+self.y-50), 50, 50, cores.arvore))
			#self.flora.append(arvores.Arvore(random.randint(0, self.largura-50), random.randint(0, self.altura-50), 50, 50, cores.arvore))

	def desenhar(self, cameraX, cameraY, tela, posicao):
		for a in self.flora:
			#a.update(cameraX, cameraY)
			a.desenhar(tela, posicao[0], posicao[1])