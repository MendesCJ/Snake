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
fps = 10
relogio = pygame.time.Clock()
pontos = 0
Xc = 0
Yc = 0

pygame.font.init()
pygame.mixer.init()
fonte = pygame.font.get_default_font()
fontepontos = pygame.font.SysFont(fonte, 40, bold = True)
fonteveloc = pygame.font.SysFont(fonte, 40, bold = True)
fontegameover = pygame.font.SysFont(fonte, 60, bold = True)
fontecontinuar = pygame.font.SysFont(fonte, 30, bold = False)
somcolide = pygame.mixer.Sound('Plank.ogg')
somveloc = pygame.mixer.Sound('bing.ogg')

#Definições da Cobrinha
St = 20 #Snake tamanho
Sx = random.randrange(0, LTela, St) #Snake x
Sy = random.randrange(0, ATela, St) #Snake y
Sc = VERDE #Snake Cor
Sv = 20 #Snake velocidade
Sd = 0 #Snake direção
Sh = [] #Snake head
Sb = [] #Snake body

#Definições da comida
Ft = 20 #Food tamanho
Fx = random.randrange(0, LTela, Ft) #Food x
Fy = random.randrange(0, ATela, Ft) #Food y
Fc = VERMELHO #Food cor

pygame.init()
tela = pygame.display.set_mode((LTela, ATelaT))
pygame.display.set_caption('Snake')
Xc = Sv

while True:
	relogio.tick(fps)
	tela.fill(BRANCO)
	Tpontos = f"Pontuação: {pontos}"
	Tvelocidade = f"Velocidade: {fps}"
	Tgameover = "Game Over"
	Tcontinuar = "Tecle s para continuar ou qualquer outra para sair"
	texto = fontepontos.render(Tpontos, 1, PRETO)
	texto2 = fonteveloc.render(Tvelocidade, 1, PRETO)
	tela.blit(texto, (20, 500))
	tela.blit(texto2, (20, 550))
	
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
		somcolide.play()
		pontos += 1
		if pontos % 10 == 0:
			somveloc.play()
			fps += 1

		
	Sh = []
	Sh.append(Sx)
	Sh.append(Sy)
	Sb.append(Sh)
	
	if Sb.count(Sh) > 1:
		
		Sh = []
		
		while Sh == []:
			texto = fontepontos.render(Tgameover, 1, VERMELHO)
			tela.blit(texto, (240, 210))
			texto2 = fontecontinuar.render(Tcontinuar, 1, VERDE)
			tela.blit(texto2, (70, 250))
					
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					exit()
				if event.type == KEYDOWN:
					if event.key == K_s:
						pontos=0
						Sh.append(Sx)
						Sh.append(Sy)
						Sb=[]
					else:
						pygame.quit()
						exit()
			pygame.display.update()
	
	
		
	
	pygame.draw.rect(tela, Sc, (Sh[0], Sh[1], St, St))
		
	for i in Sb:
		pygame.draw.rect(tela, Sc, (i[0], i[1], St, St))
		
	pygame.draw.rect(tela, Fc, (Fx,Fy,Ft,Ft))
			
	if len(Sb) > pontos:
		del Sb[0]
	
	pygame.display.update()
	
