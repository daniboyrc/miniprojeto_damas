# coding: utf-8
# Autor: Daniel Rodrigues Coura
# Matrícula: 117111915

from damas import *

tabuleiro = []
inicializa_tabuleiro(tabuleiro)

####
#for i in range(8):
	#tabuleiro.append([])
	#for j in range(8):
		#tabuleiro[i].append(None)
			
#tabuleiro[5][0] = -1
#tabuleiro[4][1] = 1
#tabuleiro[4][3] = 1
#tabuleiro[4][5] = 1
#tabuleiro[2][1] = 1
#tabuleiro[2][3] = 1
#tabuleiro[2][5] = 1
#tabuleiro[6][3] = 1

####

vez = -1
while True:
	
	# Desenha tabuleiro
	for i in tabuleiro:
		print '\n', '-' * 63
		for j in i:
			if j == None:
				print '      |',
			elif j == -1:
				print '  x   |',
			else:
				print '  o   |',
	print '\n', '-' * 63
	
	# Mostra de quem é a vez
	if vez == -1:
		print '\nVez de x',
	else:
		print '\nVez de o',
	
	# Verifica se há capturas a serem feitas
	print '| Captura:', procura_capturas(tabuleiro, vez)
	
	# Pega coordenada e as possibilidades de jogada
	while True:
		antes = raw_input('De: ').split()
		for i in range(2):
			antes.append(int(antes[i]))
		antes.pop(0)
		antes.pop(0)
	
		possib = possibilidades(tabuleiro, antes, vez)
		if possib != [] and possib:
			print possib
			break
	
	# Pega a casa que a peca vai
	while True:
		depois = raw_input('Para: ').split()
		for i in range(2):
			depois.append(int(depois[i]))
		depois.pop(0)
		depois.pop(0)
		
		for i in possib:
			for j in i:
				if depois in j:
					tabuleiro[depois[0]][depois[1]] = vez
					tabuleiro[antes[0]][antes[1]] = None
					break
				else:
					print 'Opcao invalida'
	
	# Troca a vez
	if vez == 1:
		vez = -1
	else:
		vez = 1
	
	# Limpa a tela
	for i in range(20):
		print
