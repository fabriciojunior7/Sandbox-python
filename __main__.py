'''
Fabricio Vidal da Costa Junior
Inicio: 25/04/2017
Ultima Atualizacao: 26/04/2017
'''

import pygame, sys, random, math
import jogadores, arvores, zumbies, barras, chunks
import cores

def jogo():
	largura = 700
	altura = 700
	frames = 60

	pygame.init()
	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption("SANDBOX")
	relogio = pygame.time.Clock()

	global cameraX
	cameraX = 0
	global cameraY
	cameraY = 0

	global chunksCarregando
	chunksCarregando = 0
	global tamanhoChunk
	tamanhoChunk = 700
	numChunks = 10000

	areaX = tamanhoChunk*math.sqrt(numChunks)
	areaY = tamanhoChunk*math.sqrt(numChunks)
	print areaX

	global posicao
	posicao = [areaX/2-10, areaY/2-10]

	mapa = []
	linha = 0
	coluna = 0
	loading = 0
	for i in range(numChunks):
		mapa.append(chunks.Chunk(linha*tamanhoChunk, coluna*tamanhoChunk, tamanhoChunk, tamanhoChunk, random.randint(0, 21)))
		linha += 1
		if(linha == math.sqrt(numChunks)):
			linha = 0
			coluna += 1
		loading += 1.0
		pygame.display.set_caption("SANDBOX - Carregando %.1f" % ((loading/numChunks)*100)+"%")

	#Objetos
	jogador = jogadores.Jogador(largura/2 - 10, altura/2 - 10, 20, 20, cores.vermelho, areaX, areaY)
	barraSuperficie = pygame.Surface((400, 50))
	barraSuperficie.set_alpha(150)
	numBarras = 8
	barrinhas = []
	for i in range(numBarras):
		barrinhas.append(barras.Barra(155+(i*50), 655, 40, 40, cores.amarelo))

	def rodar():
		pygame.display.update()
		relogio.tick(frames)
		pygame.display.set_caption("Sandbox - | Posicao: (%.1f - %.1f) FPS: (%.1f) Chunks: (%i) |" % (posicao[0], posicao[1], relogio.get_fps(), chunksCarregando))
		#Objetos
		global cameraX
		cameraX = jogador.atualizarPosicaoX(posicao[0])
		posicao[0] -= jogador.atualizarPosicaoX(posicao[0])
		global cameraY
		cameraY = jogador.atualizarPosicaoY(posicao[1])
		posicao[1] -= jogador.atualizarPosicaoY(posicao[1])

	def desenhar():
		tela.fill(cores.grama)
		#Objetos
		jogador.desenhar(tela)
		i = 0
		global chunksCarregando
		chunksCarregando = 0
		for c in mapa:
			if((c.x <= posicao[0]+(2*largura/3) and c.x+tamanhoChunk >= posicao[0]-(2*largura/3)) and (c.y <= posicao[1]+(2*altura/3) and c.y+tamanhoChunk >= posicao[1]-(2*altura/3))):
				c.desenhar(cameraX, cameraY, tela, posicao)
				chunksCarregando += 1
			i += 1

		barraSuperficie.fill(cores.preto)
		tela.blit(barraSuperficie, (150, 650))

		for b in barrinhas:
			b.desenhar(tela)

	while (True):
		for event in pygame.event.get():
			#Fechar tela
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()

			#Botao Pressionado
			if(event.type == pygame.KEYDOWN):
				jogador.botaoPressionado(event.key)
				if(event.key == pygame.K_F5):
					jogo()
				if(event.key == pygame.K_ESCAPE):
					pygame.quit()
					sys.exit()

			#Botao Solto
			if(event.type == pygame.KEYUP):
				jogador.botaoSolto(event.key)

		#Rodando
		rodar()
		desenhar()

jogo()