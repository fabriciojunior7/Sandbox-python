import pygame, sys, random
import jogadores, arvores, zumbies
import cores

def jogo():
	largura = 600
	altura = 600
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

	areaX = 2000
	areaY = 2000

	#Objetos
	jogador = jogadores.Jogador(largura/2 - 10, altura/2 - 10, 20, 20, cores.vermelho, areaX, areaY)
	numZumbies = 10
	horda = []
	for i in range(numZumbies):
		horda.append(zumbies.Zumbie(random.randint(0, areaX-20), random.randint(0, areaY-20), 20, 20, cores.zumbie))
	numArvores = 50
	floresta = []
	for i in range(numArvores):
		#floresta.append(arvores.Arvore(random.randint(0, largura-50), random.randint(0, altura-50), 50, 50, cores.vermelho))
		floresta.append(arvores.Arvore(random.randint(0, areaX-50), random.randint(0, areaY-50), 50, 50, cores.arvore))

	def rodar():
		pygame.display.update()
		relogio.tick(frames)
		#Objetos
		global cameraX
		cameraX = jogador.atualizarPosicaoX(posicao[0])
		posicao[0] -= jogador.atualizarPosicaoX(posicao[0])
		global cameraY
		cameraY = jogador.atualizarPosicaoY(posicao[1])
		posicao[1] -= jogador.atualizarPosicaoY(posicao[1])
		print posicao
		
	def desenhar():
		tela.fill(cores.grama)
		#Objetos
		jogador.desenhar(tela)

		for z in horda:
			z.seguir(jogador.x, jogador.y, largura, altura)
			z.update(cameraX, cameraY)
			z.desenhar(tela)

		for a in floresta:
			a.update(cameraX, cameraY)
			a.desenhar(tela)

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