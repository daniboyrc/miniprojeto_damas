# coding: utf-8

def inicializa_tabuleiro(tabuleiro):
	for i in range(8):
		tabuleiro.append([])
		for j in range(8):
			tabuleiro[i].append(None)

	for i in range(3):
		if i % 2 != 0:
			for j in range(8):
				if j % 2 == 0:
					tabuleiro[i][j] = 1
		else:
			for j in range(8):
				if j % 2 != 0:
					tabuleiro[i][j] = 1
			
	for i in range(5, 8):
		if i % 2 != 0:
			for j in range(8):
				if j % 2 == 0:
					tabuleiro[i][j] = -1
		else:
			for j in range(8):
				if j % 2 != 0:
					tabuleiro[i][j] = -1

def possibilidades(tabuleiro, coord, vez):
	if tabuleiro[coord[0]][coord[1]] == vez:
		if vez == 1 or vez == -1:	# se nao for dama
			possib = []
			
			if vez == 1:
				final = 7
			else:
				final = 0
			
			# 1. Se n estiver no final - 2. Se n estiver na lateral - 3. Se n tiver peca na frente 
			if coord[0] != final and coord[1] != 0 and tabuleiro[coord[0] + vez][coord[1] - 1] != vez:
				possib.append([coord[0] + vez, coord[1] - 1])
			if coord[0] != final and coord[1] != 7 and tabuleiro[coord[0] + vez][coord[1] + 1] != vez:
				possib.append([coord[0] + vez, coord[1] + 1])
			
			return possib	
	else:
		return False


tabuleiro = []
inicializa_tabuleiro(tabuleiro)

vez = -1
while True:
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
	
	if vez == -1:
		print '\nVez de x'
	else:
		print '\nVez de o'
	
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
	
	while True:
		depois = raw_input('Para: ').split()
		for i in range(2):
			depois.append(int(depois[i]))
		depois.pop(0)
		depois.pop(0)
		
		if depois in possib:
			tabuleiro[depois[0]][depois[1]] = vez
			tabuleiro[antes[0]][antes[1]] = None
			break
		else:
			print 'Opcao invalida'
	
	if vez == 1:
		vez = -1
	else:
		vez = 1
	
	for i in range(20):
		print
		
