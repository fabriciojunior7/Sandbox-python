'''
Fabricio Vidal da Costa Junior
Inicio: 25/04/2017
Ultima Atualizacao: 27/04/2017
'''

import pygame, sys, random, math
import jogadores, arvores, zumbies, barras, chunks, pedras, picaretas
import cores

def jogo():
	largura = 700
	altura = 700
	frames = 60

	pygame.init()
	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption("SANDBOX")
	relogio = pygame.time.Clock()
	global rodando
	rodando = True
	global framesTotais
	framesTotais = 0

	global clicado
	clicado = False

	areaMouse = pygame.Rect(20, 20, 20, 20)

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
	#posicao = [300, 300]

	#Imagens
	#picareta = pygame.image.load("imagens/picareta.png")

	mapa = []
	linha = 0
	coluna = 0
	loading = 0
	for i in range(numChunks):
		mapa.append(chunks.Chunk(linha*tamanhoChunk, coluna*tamanhoChunk, tamanhoChunk, tamanhoChunk, random.randint(0, 21), random.randint(0, 10)))
		linha += 1
		if(linha == math.sqrt(numChunks)):
			linha = 0
			coluna += 1
		loading += 1.0
		pygame.display.set_caption("SANDBOX - Carregando %.1f" % ((loading/numChunks)*100)+"%")

	#Objetos
	jogador = jogadores.Jogador(largura/2 - 10, altura/2 - 10, 20, 20, cores.vermelho, areaX, areaY, False)
	#jogador.slots.append(picaretas.Picareta(159, 659, 30, 30, cores.branco, False, picareta))
	jogador.slots.append(pedras.Pedra(160, 660, 30, 30, cores.pedra, False))
	numZumbies = 2
	horda = []
	for i in range(numZumbies):
		horda.append(zumbies.Zumbie(random.randint(posicao[0]-1000, posicao[0]+1000), random.randint(posicao[0]-1000, posicao[0]+1000), 20, 20, cores.zumbie, True))

	barraSuperficie = pygame.Surface((400, 50))
	barraSuperficie.set_alpha(150)
	vida1 = pygame.Surface((15, 15))
	vida1.set_alpha(150)
	numBarras = 8
	barrinhas = []
	for i in range(numBarras):
		barrinhas.append(barras.Barra(155+(i*50), 655, 40, 40, cores.cinza, False))

	def gameOver():
		print("====== Game Over ======")
		global rodando
		rodando = False

	def rodar():
		global framesTotais
		framesTotais += 1
		pygame.display.update()
		relogio.tick(frames)
		areaMouse.x = pygame.mouse.get_pos()[0]-10
		areaMouse.y = pygame.mouse.get_pos()[1]-10
		pygame.display.set_caption("Sandbox - | Posicao: (%.1f - %.1f) FPS: (%.1f) Chunks: (%i) |" % (posicao[0], posicao[1], relogio.get_fps(), chunksCarregando))
		#Objetos
		global cameraX
		cameraX = jogador.atualizarPosicaoX(posicao[0])
		posicao[0] -= jogador.atualizarPosicaoX(posicao[0])
		global cameraY
		cameraY = jogador.atualizarPosicaoY(posicao[1])
		posicao[1] -= jogador.atualizarPosicaoY(posicao[1])
		if(jogador.vida <= 0):
			gameOver()
		if(framesTotais > 1000):
			framesTotais = 1

	def desenhar():
		tela.fill(cores.grama)
		#Objetos
		jogador.desenhar(tela)
		i = 0
		global chunksCarregando
		chunksCarregando = 0

		i = 0
		for z in horda:
			z.seguir(posicao[0], posicao[1], largura, altura)
			z.desenharChunk(tela, posicao[0], posicao[1])
			if((z.x < posicao[0]-2000 or z.x > posicao[0]+2000) or (z.y < posicao[1]-2000 or z.y > posicao[1]+2000)):
				horda.pop(i)
			i += 1
			if((z.x > posicao[0]-200 and z.x < posicao[0]+200) and (z.y > posicao[1]-200 and z.y < posicao[1]+200)):
				z.desenharFisica(tela, z.x-(posicao[0]-340), z.y-(posicao[1]-340))
				if(jogador.corpo.colliderect(z.topo)):
					posicao[1] += jogador.empurrarCima(20)
					jogador.tirarVida(2)
				elif(jogador.corpo.colliderect(z.base)):
					posicao[1] += jogador.empurrarBaixo(20)
					jogador.tirarVida(2)
				elif(jogador.corpo.colliderect(z.direita)):
					posicao[0] += jogador.empurrarDireita(20)
					jogador.tirarVida(2)
				elif(jogador.corpo.colliderect(z.esquerda)):
					posicao[0] += jogador.empurrarEsquerda(20)
					jogador.tirarVida(2)

				for zz in horda:
					if((z.x != zz.x and z.y != zz.y) and ((zz.x > posicao[0]-200 and zz.x < posicao[0]+200) and (zz.y > posicao[1]-200 and zz.y < posicao[1]+200))):
						if(z.corpo.colliderect(zz.topo)):
							z.y += z.empurrarCima(1)
						elif(z.corpo.colliderect(zz.base)):
							z.y += z.empurrarBaixo(1)
						elif(z.corpo.colliderect(zz.direita)):
							z.x += z.empurrarDireita(1)
						elif(z.corpo.colliderect(zz.esquerda)):
							z.x += z.empurrarEsquerda(1)
			'''
			if(not (z.x < posicao[0]-200 or z.x > posicao[0]+200) or not (z.y < posicao[1]-200 or z.y > posicao[1]+200)):
				z.desenharFisica(tela, z.x-(posicao[0]-340), z.y-(posicao[1]-340))
				for zz in horda:
					#zz.desenharFisica(tela, zz.x-(posicao[0]-340), zz.y-(posicao[1]-340))
					if(z.x != zz.x and z.y != zz.y):
						if(z.corpo.colliderect(zz.topo)):
							z.y += z.empurrarCima(1)
						elif(z.corpo.colliderect(zz.base)):
							z.y += z.empurrarBaixo(1)
						elif(z.corpo.colliderect(zz.direita)):
							z.x += z.empurrarDireita(1)
						elif(z.corpo.colliderect(zz.esquerda)):
							z.x += z.empurrarEsquerda(1)
			'''
		if(i < numZumbies):
			horda.append(zumbies.Zumbie(random.randint(posicao[0]-1000, posicao[0]+1000), random.randint(posicao[1]-1000, posicao[1]+1000), 20, 20, cores.zumbie, True))

		for c in mapa:
			colicao = False
			if((c.x <= posicao[0]+(2*largura/3) and c.x+tamanhoChunk >= posicao[0]-(2*largura/3)) and (c.y <= posicao[1]+(2*altura/3) and c.y+tamanhoChunk >= posicao[1]-(2*altura/3))):
				c.desenhar(cameraX, cameraY, tela, posicao)
				for p in c.rochas:
					if((p.x > posicao[0]-100 and p.x < posicao[0]+100) and (p.y > posicao[1]-100 and p.y < posicao[1]+100)):
						p.desenharFisica(tela, p.x-(posicao[0]-300), p.y-(posicao[1]-300))
						#for pp in c.rochas:
						#	if(pp.x != p.x and pp.y != p.y and pp.corpo.colliderect(p.corpo)):
						#		c.rochas.remove(pp)

						if(jogador.corpo.colliderect(p.topo)):
							posicao[1] += jogador.empurrarCima(jogador.velocidadeAndar)
						elif(jogador.corpo.colliderect(p.base)):
							posicao[1] += jogador.empurrarBaixo(jogador.velocidadeAndar)
						elif(jogador.corpo.colliderect(p.direita)):
							posicao[0] += jogador.empurrarDireita(jogador.velocidadeAndar)
						elif(jogador.corpo.colliderect(p.esquerda)):
							posicao[0] += jogador.empurrarEsquerda(jogador.velocidadeAndar)
						#Mouse Quebrar
						if(pygame.mouse.get_pressed()[0] == True and p.corpo.collidepoint(pygame.mouse.get_pos()) and framesTotais % 15 == 0):
							p.durabilidade -= 1
							print("Quebrando %i" %  p.durabilidade)
							if(p.durabilidade <= 0):
								jogador.numPedras += 1
								c.rochas.remove(p)
								print(jogador.numPedras)
				#Mouse Criar
				if((pygame.mouse.get_pos()[0] >= jogador.x-100 and pygame.mouse.get_pos()[0] <= jogador.x+100) and (pygame.mouse.get_pos()[1] >= jogador.y-100 and pygame.mouse.get_pos()[1] <= jogador.y+100)):
					global clicado
					
					if(pygame.mouse.get_pressed()[2] == True and clicado == False and jogador.slot == 0 and jogador.numPedras > 0):
						for p in c.rochas:
							if(areaMouse.colliderect(p.corpo) == True):
								colicao = True
								break
						for z in horda:
							if(areaMouse.colliderect(z.corpo)):
								colicao = True
								break
						if(colicao == False):
							jogador.numPedras -= 1
							c.rochas.append(pedras.Pedra(pygame.mouse.get_pos()[0]+posicao[0]-310, pygame.mouse.get_pos()[1]+posicao[1]-310, 20, 20, cores.pedra, True))
							print(jogador.numPedras)
					#Madeira	
					elif(pygame.mouse.get_pressed()[2] == True and clicado == False and jogador.slot == 1):
						pass
					clicado = pygame.mouse.get_pressed()[2]

				chunksCarregando += 1

		barraSuperficie.fill(cores.preto)
		tela.blit(barraSuperficie, (150, 650))
		for i in range(jogador.vida):
			vida1.fill(cores.vermelho)
			tela.blit(vida1, (152+(i*20), 630))

		for b in barrinhas:
			b.desenhar(tela)
		
		for s in jogador.slots:
			s.desenhar(tela)

		#pygame.draw.rect(tela, cores.vermelho, areaMouse)

	while (rodando):
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

			#Mouse Pressionado
			if(pygame.mouse.get_pressed()[0] == True):
				for i in range(len(barrinhas)):
					if(barrinhas[i].corpo.collidepoint(pygame.mouse.get_pos())):
						jogador.slot = i
						barrinhas[i].cor = cores.amarelo
						print(jogador.slot)
					else:
						barrinhas[i].cor = cores.cinza


		#Rodando
		rodar()
		desenhar()

jogo()