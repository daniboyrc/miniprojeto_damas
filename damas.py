# coding: utf-8

def possibilidades(coord, vez):
	if vez == 1 or vez == -1:	# se nao for dama
		possib = []
		
		# resolve laterais
		if coord[1] != 0 and possib[coord[0] + vez][[coord[1] - 1]] != vez:
			possib = [[coord[0] + vez], [coord[1] - 1]]
		if coord[1] != 7 and possib[coord[0] + vez][[coord[1] + 1]] != vez:
			possib = [[coord[0] + vez], [coord[1] + 1]]
		
		return possib
		
