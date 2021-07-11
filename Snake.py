#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Snake.py
#  
#  Copyright 2021 Carlos José Mendes <mendes@fedora>
#  
import pygame
from pygame.locals import *
from sys import exit
import random


#Definições Globais
LTela = 640
ATelaT = 640
ATela = 480
VERDE= (0, 100, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
relogio = pygame.time.Clock()
pontos = 0
Xc = 0
Yc = 0

pygame.font.init()
fonte = pygame.font.get_default_font()
fontepontos = pygame.font.SysFont(fonte, 40, bold = True)
fontegameover = pygame.font.SysFont(fonte, 60, bold = True)

#Definições da Cobrinha
St = 10 #Snake tamanho
Sx = random.randrange(0, LTela, St) #Snake x
Sy = random.randrange(0, ATela, St) #Snake y
Sc = VERDE #Snake Cor
Sv = 10 #Snake velocidade
Sd = 0 #Snake direção
Sh = [] #Snake head
Sb = [] #Snake body

#Definições da comida
Ft = 10 #Food tamanho
Fx = random.randrange(0, LTela, Ft) #Food x
Fy = random.randrange(0, ATela, Ft) #Food y
Fc = VERMELHO #Food cor

pygame.init()
tela = pygame.display.set_mode((LTela, ATelaT))
pygame.display.set_caption('Snake')
Xc = Sv

while True:
	
	relogio.tick(15)
	tela.fill(BRANCO)
	Tpontos = f"Pontuação: {pontos}"
	Tgameover = "Game Over"
	TContinuar = "Deseja continuar: S ou s"
	texto = fontepontos.render(Tpontos, 1, PRETO)
	tela.blit(texto, (20, 500))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
				
		if event.type == KEYDOWN:
			if event.key == K_UP:
				if Yc == Sv:
					pass
				else:
					Yc = -Sv 		
					Xc = 0

			if event.key == K_DOWN:
				if Yc == -Sv:
					pass
				else:
					Yc = Sv 		
					Xc = 0
			
			if event.key == K_RIGHT:
				if Xc == -Sv:
					pass
				else:
					Xc = Sv 		
					Yc = 0
				
			if event.key == K_LEFT:
				if Xc == Sv:
					pass
				else:
					Xc = -Sv 		
					Yc = 0
					
	Sx = Sx + Xc
	Sy = Sy + Yc
	
	if Sx > LTela:
		Sx=0
	if Sx < 0:
		Sx=LTela
	if Sy > ATela:
		Sy=0
	if Sy < 0:
		Sy=ATela
		
	if Sx == Fx and Sy == Fy:
		Fx = random.randrange(0, LTela, Ft)
		Fy = random.randrange(0, ATela, Ft)
		pygame.draw.rect(tela,Fc,(Fx,Fy,Ft,Ft))
		pontos += 1

		
	Sh=[]
	Sh.append(Sx)
	Sh.append(Sy)
	Sb.append(Sh)
	
	if Sb.count(Sh) > 1:
		exit()
	
	
		
	
	pygame.draw.rect(tela, Sc, (Sh[0], Sh[1], St, St))
	
	for i in Sb:
		pygame.draw.rect(tela, Sc, (i[0], i[1], St, St))
		
	pygame.draw.rect(tela, Fc, (Fx,Fy,Ft,Ft))
	
	if len(Sb) > pontos:
		del Sb[0]	
		
	pygame.display.update()
	
