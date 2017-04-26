import pygame, random
import arvores, pedras
import cores

class Chunk(object):
	def __init__(self, x, y, largura, altura, numArvores, numPedras):
		#Atributos
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura

		self.numArvores = numArvores
		self.flora = []
		for i in range(self.numArvores):
			self.flora.append(arvores.Arvore(random.randint(self.x, self.largura+self.x-50), random.randint(self.y, self.altura+self.y-50), 50, 50, cores.arvore))

		self.numPedras = numPedras
		self.rochas = []
		for i in range(self.numPedras):
			self.rochas.append(pedras.Pedra(random.randint(self.x, self.largura+self.x-20), random.randint(self.y, self.altura+self.y-20), 20, 20, cores.pedra))

	def desenhar(self, cameraX, cameraY, tela, posicao):
		for p in self.rochas:
			p.desenhar(tela, posicao[0], posicao[1])
		for a in self.flora:
			a.desenhar(tela, posicao[0], posicao[1])