# coding: utf-8
# Autor: Daniel Rodrigues Coura
# Matrícula: 117111915

from damas import *
import pygame, sys
from pygame.locals import *

pygame.init()
larg = 800
alt = 600
screen = pygame.display.set_mode((larg, alt))
lado_casa = alt / 8.0

tab = pygame.image.load('img/tabuleiro.png')
back = pygame.image.load('img/back.jpg')
peca1 = pygame.image.load('img/peca1.png')
peca2 = pygame.image.load('img/peca2.png')

def desenha_tabuleiro():
	for i in range(len(tabuleiro)):
		for j in range(len(tabuleiro[i])):
			if tabuleiro[i][j] == -1:
				screen.blit(peca2, (j * 75, i * 75))
			elif tabuleiro[i][j] == 1:
				screen.blit(peca1, (j * 75, i * 75))

tabuleiro = []
inicializa_tabuleiro(tabuleiro)
possib = []
vez = -1

while True:
	screen.blit(tab, (0,0))
	screen.blit(back, (600,0))
	
	desenha_tabuleiro()
	
	for i in possib:
		retang = pygame.Rect(i[1] * 75, i[0] * 75 , lado_casa, lado_casa)
		pygame.draw.rect(screen, (255, 214, 20), retang)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
			y = pygame.mouse.get_pos()[0] // 75
			x = pygame.mouse.get_pos()[1] // 75
			print pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
			print x,y
			if [x, y] in possib:
				print possib, '- possib'
				######
				if procura_capturas(tabuleiro, vez):
					print peca, possib[-1], '- captura'
					print captura(tabuleiro, [peca[0], peca[1]], possib[0])
					possib.pop(0)
				tabuleiro[x][y] = vez
				tabuleiro[peca[0]][peca[1]] = None
				if not procura_capturas(tabuleiro, vez):
					vez *= -1
					possib = []
				
			else:
				peca = [x, y]
				for i in possibilidades(tabuleiro, (x, y), vez):
					possib = i
				
	pygame.display.update()

