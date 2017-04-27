import pygame
import entidades

class Jogador(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor, areaX, areaY, fisica):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor, fisica)
		#Atributos
		self.velocidadeAndar = 3
		self.wasd = [False, False, False, False]
		self.areaX = areaX
		self.areaY = areaY
		self.vida = 20
		self.ultimaDirecao = "w"
		self.slot = 0
		self.slots = []
		self.numPedras = 0

	def darVida(self, pontos):
		self.vida += pontos
	def tirarVida(self, pontos):
		self.vida -= pontos

	def botaoPressionado(self, key):
		#Y
		if(key == pygame.K_w or key == pygame.K_UP):
			self.wasd[0] = True
		elif(key == pygame.K_s or key == pygame.K_DOWN):
			self.wasd[2] = True
		#X
		if(key == pygame.K_a or key == pygame.K_LEFT):
			self.wasd[1] = True
		elif(key == pygame.K_d or key == pygame.K_RIGHT):
			self.wasd[3] = True

	def botaoSolto(self, key):
		#Y
		if(key == pygame.K_w or key == pygame.K_UP):
			self.wasd[0] = False
			self.ultimaDirecao = "w"
		elif(key == pygame.K_s or key == pygame.K_DOWN):
			self.wasd[2] = False
			self.ultimaDirecao = "s"
		#X
		if(key == pygame.K_a or key == pygame.K_LEFT):
			self.wasd[1] = False
			self.ultimaDirecao = "a"
		elif(key == pygame.K_d or key == pygame.K_RIGHT):
			self.wasd[3] = False
			self.ultimaDirecao = "d"

	def atualizarPosicaoY(self, y):
		if(self.wasd[0] == True and y > 0):
			return self.velocidadeAndar
		elif(self.wasd[2] == True and y < self.areaY):
			return -self.velocidadeAndar
		else:
			return 0

	def atualizarPosicaoX(self, x):
		if(self.wasd[1] == True and x > 0):
			return self.velocidadeAndar
		elif(self.wasd[3] == True and x < self.areaX):
			return -self.velocidadeAndar
		else:
			return 0
