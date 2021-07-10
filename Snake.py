#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Snake.py
#  
#  Copyright 2021 Carlos José Mendes <mendes@fedora>
#  
import pygame
import random

#Definições Globais
LTela = 640
ATela = 480
VERDE= (0, 100, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
relogio=pygame.time.Clock()

#Definições da Cobrinha
St = 10
Sx = random.randrange(0, LTela, St)
Sy = random.randrange(0, ATela, St)
Sc = VERDE
Sv = 10

#Definições da comida
Ft = 10
Fx = random.randrange(0, LTela, Ft)
Fy = random.randrange(0, ATela, Ft)
Fc = VERMELHO

pygame.init()
tela = pygame.display.set_mode((LTela, ATela))
pygame.display.set_caption('Snake')


while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
		
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_UP]:
		Sy -= Sv
	if keys[pygame.K_DOWN]:
		Sy += Sv
	if keys[pygame.K_RIGHT]:
		Sx += Sv
	if keys[pygame.K_LEFT]:
		Sx -= Sv
	
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
		
	tela.fill(BRANCO)
	pygame.draw.rect(tela,Sc,(Sx,Sy,St,St))
	pygame.draw.rect(tela,Fc,(Fx,Fy,Ft,Ft))
	pygame.display.update()
	relogio.tick(15)
