import pygame
import cores

class Entidade(object):
	def __init__(self, x, y, largura, altura, cor, fisica):
		#Atributos
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura
		self.cor = cor
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		self.fisica = fisica
		if(fisica == True):
			self.larguraTB = self.largura
			self.alturaTB = 5
			self.larguraDE = 5
			self.alturaDE = self.altura
			self.separacao = 15
			self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
			self.topo = pygame.Rect(self.x, (self.y - self.alturaTB), self.larguraTB, self.alturaTB)
			self.base = pygame.Rect(self.x, (self.y + self.altura), self.larguraTB, self.alturaTB)
			self.direita = pygame.Rect((self.x - self.larguraDE), self.y, self.larguraDE, self.alturaDE)
			self.esquerda = pygame.Rect((self.x + self.largura), self.y, self.larguraDE, self.alturaDE)

	def desenhar(self, tela):
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		pygame.draw.rect(tela, self.cor, self.corpo)
		if(self.fisica == True):
			self.desenharFisica(tela)

	def desenharFisica(self, tela, x, y):
		self.topo = pygame.Rect(x, (y - self.alturaTB), self.larguraTB, self.alturaTB)
		self.base = pygame.Rect(x, (y + self.altura), self.larguraTB, self.alturaTB)
		self.esquerda = pygame.Rect((x - self.larguraDE), y, self.larguraDE, self.alturaDE)
		self.direita = pygame.Rect((x + self.largura), y, self.larguraDE, self.alturaDE)
		pygame.draw.rect(tela, cores.branco, self.topo)
		pygame.draw.rect(tela, cores.branco, self.base)
		pygame.draw.rect(tela, cores.branco, self.direita)
		pygame.draw.rect(tela, cores.branco, self.esquerda)

	def update(self, x, y):
		self.x += x
		self.y += y

	def empurrarCima(self, forca):
		return -forca
	def empurrarBaixo(self, forca):
		return forca
	def empurrarDireita(self, forca):
		return forca
	def empurrarEsquerda(self, forca):
		return -forca