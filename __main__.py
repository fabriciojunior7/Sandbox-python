import pygame, sys, random
import jogadores, arvores, zumbies, barras
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
	global posicao
	posicao = [300, 300]

	areaX = 50000
	areaY = 50000

	#Objetos
	jogador = jogadores.Jogador(largura/2 - 10, altura/2 - 10, 20, 20, cores.vermelho, areaX, areaY)
	barraSuperficie = pygame.Surface((400, 50))
	barraSuperficie.set_alpha(150)
	numBarras = 8
	barrinhas = []
	for i in range(numBarras):
		barrinhas.append(barras.Barra(155+(i*50), 655, 40, 40, cores.amarelo))
	#barra = barras.Barra(150, 650, 400, 50, cores.branco)
	numZumbies = 1000
	horda = []
	for i in range(numZumbies):
		horda.append(zumbies.Zumbie(random.randint(0, areaX-20), random.randint(0, areaY-20), 20, 20, cores.zumbie))
	numArvores = 10000
	floresta = []
	for i in range(numArvores):
		#floresta.append(arvores.Arvore(random.randint(0, largura-50), random.randint(0, altura-50), 50, 50, cores.vermelho))
		floresta.append(arvores.Arvore(random.randint(0, areaX-50), random.randint(0, areaY-50), 50, 50, cores.arvore))

	def rodar():
		pygame.display.update()
		relogio.tick(frames)
		pygame.display.set_caption("Sandbox - | Posicao: (%.1f - %.1f) FPS: %.1f |" % (posicao[0], posicao[1], relogio.get_fps()))
		#Objetos
		global cameraX
		cameraX = jogador.atualizarPosicaoX(posicao[0])
		posicao[0] -= jogador.atualizarPosicaoX(posicao[0])
		global cameraY
		cameraY = jogador.atualizarPosicaoY(posicao[1])
		posicao[1] -= jogador.atualizarPosicaoY(posicao[1])
		#print(posicao)
		#print("%.1f" % relogio.get_fps())
		#print("%.1f" % relogio.get_rawtime())
		
	def desenhar():
		tela.fill(cores.grama)
		#Objetos
		jogador.desenhar(tela)

		for z in horda:
			z.update(cameraX, cameraY)
			if((z.x >= -z.largura and z.x <= largura) and (z.y >= -z.altura and z.y <= altura)):
				z.seguir(jogador.x, jogador.y, largura, altura)
				z.desenhar(tela)

		for a in floresta:
			a.update(cameraX, cameraY)
			if((a.x >= -a.largura and a.x <= largura) and (a.y >= -a.altura and a.y <= altura)):
				a.desenhar(tela)

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