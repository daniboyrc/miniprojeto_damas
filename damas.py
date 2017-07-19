# coding: utf-8

def inicializa_tabuleiro(tabuleiro):
	for i in range(8):
		tabuleiro.append([])
		for j in range(8):
			tabuleiro[i].append(None)

	for i in range(8):
		if i < 3:
			if i % 2 != 0:
				for j in range(8):
					if j % 2 == 0:
						tabuleiro[i][j] = 1
			else:
				for j in range(8):
					if j % 2 != 0:
						tabuleiro[i][j] = 1
		if i > 4:
			if i % 2 != 0:
				for j in range(8):
					if j % 2 == 0:
						tabuleiro[i][j] = -1
			else:
				for j in range(8):
					if j % 2 != 0:
						tabuleiro[i][j] = -1
			
def procura_capturas(tabuleiro, vez):
	if vez == 1 or vez == -1:
		for i in range(len(tabuleiro)):
			for j in range(len(tabuleiro[i])):
				if tabuleiro[i][j] == vez:		
					if i < 6 and j > 1 and tabuleiro[i + 1][j - 1] == (-1 * vez) and tabuleiro[i + 2][j - 2] == None: # tras - esquerda
						return True
					if i < 6 and j < 6 and tabuleiro[i + 1][j + 1] == (-1 * vez) and tabuleiro[i + 2][j + 2] == None: # tras - direita
						return True
					if i > 1 and j > 1 and tabuleiro[i - 1][j - 1] == (-1 * vez) and tabuleiro[i - 2][j - 2] == None: # frente - esquerda
						return True
					if i > 1 and j < 6 and tabuleiro[i - 1][j + 1] == (-1 * vez) and tabuleiro[i - 2][j + 2] == None: # frente - direita
						return True
		return False

def possibilidades(tabuleiro, coord, vez):
	if tabuleiro[coord[0]][coord[1]] == vez: 
		if vez == 1 or vez == -1:	# se nao for dama
			possib = []
			linha = coord[0]
			col = coord[1]
			if procura_capturas(tabuleiro, vez):
				if linha < 6 and col > 1 and tabuleiro[linha + 1][col - 1] == (-1 * vez) and tabuleiro[linha + 2][col - 2] == None: # tras - esquerda
					possib.append([linha + 2, col - 2])
				if linha < 6 and col < 6 and tabuleiro[linha + 1][col + 1] == (-1 * vez) and tabuleiro[linha + 2][col + 2] == None: # tras - direita
					possib.append([linha + 2, col + 2])
				if linha > 1 and col > 1 and tabuleiro[linha - 1][col - 1] == (-1 * vez) and tabuleiro[linha - 2][col - 2] == None: # frente - esquerda
					possib.append([linha - 2, col - 2])
				if linha > 1 and col < 6 and tabuleiro[linha - 1][col + 1] == (-1 * vez) and tabuleiro[linha - 2][col + 2] == None: # frente - direita
					possib.append([linha - 2, col + 2])
			else:
				final = 7 if vez == 1 else 0
				
				if linha != final and col != 0 and tabuleiro[linha + vez][col - 1] != vez:
					possib.append([linha + vez, col - 1])
				if linha != final and col != 7 and tabuleiro[linha + vez][col + 1] != vez:
					possib.append([linha + vez, col + 1])
		return possib
	else:
		return False


		
