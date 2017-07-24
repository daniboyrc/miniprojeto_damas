# coding: utf-8

# <sumary> Função que inicializa o tabuleiro </sumary>
# <param name="tabuleiro"> Lista vazia </param>
# <returns> Tabuleiro com peças nas posições iniciais </returns>
def inicializa_tabuleiro(tabuleiro):
	for i in range(8):
		tabuleiro.append([])
		for j in range(8):
			tabuleiro[i].append(None)

	for i in [0, 1, 2, 5, 6, 7]:
		peca = 1 if i < 3 else -1		
		if i % 2 != 0:
			for j in range(8):
				if j % 2 == 0:
					tabuleiro[i][j] = peca
		else:
			for j in range(8):
				if j % 2 != 0:
					tabuleiro[i][j] = peca
			
# <sumary> Função que verifica se há pelo menos uma captura a ser feita </sumary>
# <param name="tabuleiro"> Tabuleiro </param>
# <param name="vez"> Jogador da vez </param>
# <returns> Se há ou não capturas a serem feitas </returns>
def procura_capturas(tabuleiro, vez):
	if vez == 1 or vez == -1:
		for i in range(len(tabuleiro)):
			for j in range(len(tabuleiro[i])):
				if tabuleiro[i][j] == vez:
					if i < 6 and j > 1 and tabuleiro[i + 1][j - 1] == (-1 * vez) and tabuleiro[i + 2][j - 2] == None:
						return True
					if i < 6 and j < 6 and tabuleiro[i + 1][j + 1] == (-1 * vez) and tabuleiro[i + 2][j + 2] == None: 
						return True
					if i > 1 and j > 1 and tabuleiro[i - 1][j - 1] == (-1 * vez) and tabuleiro[i - 2][j - 2] == None:
						return True
					if i > 1 and j < 6 and tabuleiro[i - 1][j + 1] == (-1 * vez) and tabuleiro[i - 2][j + 2] == None:
						return True
		return False

# <sumary> Função que calcula as possíveis jogadas em caso de captura e calcula possibilidade que captura mais peças </sumary>
# <param name="tabuleiro"> Tabuleiro </param>
# <param name="coord"> Coordenada da peça </param>
# <param name="vez"> Jogador da vez </param>
# <returns> Possiblidades de jogadas com maior captura de peças </returns>
def possibilidade_captura(tabuleiro, coord, vez):
	if vez == 1 or vez == -1:
		possib = []
		ramos = [[coord]]
		while len(ramos) != 0:
			copia = []
			for i in tabuleiro:
				copia.append(i[:])		
			linha = ramos[-1][-1][0]
			col = ramos[-1][-1][1]
			for i in range(len(ramos[-1]) - 1, 0, - 1):
				a = (ramos[-1][i][0] - ramos[-1][i-1][0]) / -2
				b = (ramos[-1][i][1] - ramos[-1][i-1][1]) / -2
				copia[ramos[-1][i][0] + a][ramos[-1][i][1] + b] = 'x'
			copia[ramos[-1][0][0]][ramos[-1][0][1]] = None
			x = True
			
			if linha < 6 and col > 1 and copia[linha + 1][col - 1] == (-1 * vez) and copia[linha + 2][col - 2] == None:
				sttef = ramos[-1][:]
				sttef.append([linha + 2, col - 2])
				ramos.insert(0, sttef)
				x = False
			if linha < 6 and col < 6 and copia[linha + 1][col + 1] == (-1 * vez) and copia[linha + 2][col + 2] == None:
				sttef = ramos[-1][:]
				sttef.append([linha + 2, col + 2])
				ramos.insert(0, sttef)
				x = False
			if linha > 1 and col > 1 and copia[linha - 1][col - 1] == (-1 * vez) and copia[linha - 2][col - 2] == None:
				sttef = ramos[-1][:]
				sttef.append([linha - 2, col - 2])
				ramos.insert(0, sttef)
				x = False
			if linha > 1 and col < 6 and copia[linha - 1][col + 1] == (-1 * vez) and copia[linha - 2][col + 2] == None:
				sttef = ramos[-1][:]
				sttef.append([linha - 2, col + 2])
				ramos.insert(0, sttef)
				x = False

			if x:
				possib.append(ramos[-1][:])
				ramos.pop()
			else:
				ramos.pop(-1)
		
		maior = 0
		for i in possib:
			if len(i) > maior:
				maior = len(i)
		
		jogadas = []
		for i in possib:
			if len(i) == maior:
				i.pop(0)
				jogadas.append(i)
		
		return jogadas

def captura(tabuleiro, saida, chegada):
	x = (chegada[0] - saida[0]) / 2
	y = (chegada[1] - saida[1]) / 2

	tabuleiro[saida[0] + x][saida[1] + y] = None
	return [saida[0] + x, saida[1] + y]

# <sumary> Função que calcula as possíveis jogadas de uma peça </sumary>
# <param name="tabuleiro"> Tabuleiro </param>
# <param name="coord"> Coordenada da peça </param>
# <param name="vez"> Jogador da vez </param>
# <returns> Possiblidades de jogadas </returns>		
def possibilidades(tabuleiro, coord, vez):
	if tabuleiro[coord[0]][coord[1]] == vez:
		if vez == 1 or vez == -1:
			possib = []
			linha = coord[0]
			col = coord[1]
			if procura_capturas(tabuleiro, vez):
				jogadas = possibilidade_captura(tabuleiro, coord, vez)
				return jogadas
			else:
				final = 7 if vez == 1 else 0
				
				if linha != final and col != 0 and tabuleiro[linha + vez][col - 1] == None:
					possib.append([linha + vez, col - 1])
				if linha != final and col != 7 and tabuleiro[linha + vez][col + 1] == None:
					possib.append([linha + vez, col + 1])
		return [possib]
	else:
		return [[]]


		
