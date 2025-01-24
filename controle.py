#!/usr/bin/env python3.10.13


"""
Módulo responsável por controlar as ações do jogo.

"""
#Módulo padrão para ter acesso a algumas variáveis usadas ou mantidas pelo interpretador

import sys

class Controle(object):

    def __init__(self, stdscr):
        self.stdscr = stdscr 
        width = stdscr.getmaxyx()[1] 
        self.x_center = (width - 1) 
        self.pos_x = 0 
        self.pos_y = 0 
        self.entrada = None

    def _limite(self):

        if self.pos_x > 2:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = 2
        
        if self.pos_y > 2:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = 2
    
    def espaco_do_tabuleiro(self):

        self.entrada = self.stdscr.getkey()

        if self.entrada == 'q':
            sys.exit(0)
        
        if self.entrada == 'a':
            self.pos_x -= 1
        elif self.entrada == 'd':
            self.pos_x += 1
        elif self.entrada == 's':
            self.pos_y += 1
        elif self.entrada == 'w':
            self.pos_y -= 1
        else:
            pass
        self._limite()




#DICIONÁRIO DO MÓDULO DE CONTROLE
#  def __init__(self, stdscr): Método construtor que recebe como atributo inicializador: stdscr
#  self.stdscr = stdscr: Declarando o atributo que corresponde a tela Standard "inicial"
#  width = stdscr.getmaxyx()[1]: Atributo criado para armazenar a largura total da tela
#  self.x_center = (width - 1): Atributo criado para capturar o centro horizontal da tela
#  self.pos_x = 0: Atributo criado para guardar o movimento relativo do jogador
#  self.pos_y = 0: Atributo criado para guardar o movimento relativo do jogador
#  self.entrada = None: Atributo para capturar a entrada do teclado do jogador, começando em vazio
# 
# ## MÉTODO PRIVADO _limites ##
# def _limite(self): Faz o papel de verificar se a posição relativa da jogada ainda está dentro dos limites do tabuleiro
# pos_x = representa o movimento para esquerda e direira, na horizontal
# pos_y = representa o movimento para baixo e para cima, na vertical
# 
# ## MÉTODO ESPAÇO DO TABULEIRO ##
# self.entrada = self.stdscr.getkey(): Deifinimos um atributo que receberá o método getkey()
# #
