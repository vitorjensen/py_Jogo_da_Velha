#!/usr/bin/env python3.10.13


"""
Jogo da velha simples.
Programa sob licença  GNU V.3
Versão 0.0.1 

"""
from curses import initscr, wrapper
from random import randint

def main(stdscr):
        pass

if __name__ == "__main__":
    initscr() #Faz a inicialização do terminal do nosso jogo
    wrapper(main) #Recebe como argumento a função "main", indica para 
                  # o curse, que a manipulação do terminal do jogo será feita pela "main"
    
################## CÓDIGO DO JOGO ##################
#Função inicial do jogo de "Boas vindas" aprensentando as strings padrões
def boas_vindas(stdscr):
    stdscr.addstr(1, 1, "Bem vindo ao Jogo da Velha.")
    stdscr.addstr(2, 1, "Pressione q para sair ou h para obter ajuda.")
    stdscr.addstr(16, 1, "Desenvolvido por: V. N. F. Jensen.")
    stdscr.addstr(17, 1, "Licensa Nova BSD.")

#Função de ajuda, caso o jogador necessite saber dos comandos e suas respectivas teclas
def ajuda(stdscr):
     stdscr.clear()
     stdscr.border()
     stdscr.addstr(1, 1, "Pressione Q para sair ou H para exibir essa ajuda.")
     stdscr.addstr(2, 1, "Para mudar a posição, use as teclas: A, D, S, W.")
     stdscr.addstr(3, 1, "Para definir uma posição no jogo, digite: L.")
     stdscr.addstr(4, 1, "Para reiniciar a partida, digite: Y.")
     stdscr.addstr(5, 1, "Pressione espaço para sair da tela.")
     stdscr.refresh()

def reiniciar_tela(stdscr, limpar = True):
 if limpar is True:
      stdscr.clear()
 stdscr.border()
 boas_vindas(stdscr)
 stdscr.refresh()

#Função para a criação do tabuleiro
def tabuleiro(stdscr, posicoes, x_center):
      stdscr.clear()
      reiniciar_tela(stdscr, limpar=False)

      stdscr.addstr(10, x_center - 3, "------") # A variável x_center defini o centro do tabuleiro
      stdscr.addstr(12, x_center - 3, "------")
      i = 9
      for linha in posicoes:
           tela = "%s|%s|%s "% tuple(linha)
           stdscr.addstr(i, x_center - 3, tela)
           i += 2
#Utilizando as teclas W e S para mover para cima e para baixo
#Funções para mapear o espaço do jogo em sí numa matriz 3x3
def limites(pos_x, pos_y):
     if pos_x > 2:
          pos_x = 0
     if pos_x < 0:
          pos_x = 2
     if pos_y > 2:
          pos_y = 0
     if pos_y < 0:
          pos_y = 2
     return pos_x, pos_y

def espaço_do_tabuleiro(pos_x, pos_y, entrada):
     if entrada == 'a':
          pos_x, pos_y = limites(pos_x - 1, pos_y)
     elif entrada == 'd':
           pos_x, pos_y = limites(pos_x + 1, pos_y)
     elif entrada == 's':
           pos_x, pos_y = limites(pos_x, pos_y + 1)
     elif entrada == 'w':
           pos_x, pos_y = limites(pos_x, pos_y - 1)
     else:
          pass
     return pos_x, pos_y

#Função que usa as informações de posição relativa da tela para mover o cursor no terminal 
#para posição equivalente na tela
def cursor(stdscr, pos_x, pos_y, x_center):
     cursor_y = 9
     cursor_x = x_center -3
     if pos_y == 1:
          cursor_y += 2
     if pos_y == 2:
          cursor_y += 4
     if pos_x == 1:
           cursor_x += 2
     if pos_x == 2:
          cursor_x += 4
     stdscr.move(cursor_y, cursor_x) # Atualização do cursor na tela foi feita usando o comando .move

#Função para marcar o X da jogada
def jogador(pos_x, pos_y, posicoes):
     #Verifica se a lista "posicoes" tem um espaço em branco e, 
     #se for verdade, vai substituir esse espaço por um x
     if posicoes[pos_y][pos_x] == " ":
          posicoes[pos_y][pos_x] == "x"
          return True, posicoes
     return False, posicoes
     return posicoes


############# CRIANDO UMA IA PARA O BOT DO JOGO #############


def robo(posicoes):
     vazias = []
     for i in range(0, 3):
          for j in range(0, 3):
               if posicoes[i][j] == " ":
                   vazias.append([j, i])

     n_escolhas = len(vazias)
     if n_escolhas != 0:
          j, i = vazias[randint(0, n_escolhas - 1)]
          posicoes[j][i] = "o"

          return posicoes


############# DETERMINANDO O GANHADOR #############
def ganhador(posicoes):
     #Analisando as diagonais estão alinhadas
     diagonal1 = [posicoes[0][0], posicoes[1][1], posicoes[2][2]]
     diagonal2 = [posicoes[0][2], posicoes[1][1], posicoes[2][0]]
     #Criando a matriz transposta da matriz de posições
     transposta = [[], [], []]
     for i in range(3):
          for j in range(3):
               transposta[i].append(posicoes[j][i])
     
     gan = total_alinhado(diagonal1)
     if gan is not None:
          return gan
     
     gan = total_alinhado(diagonal2)

     if gan is not None:
          return gan
     
     velha = 9
     for i in range(3):

          gan = total_alinhado(posicoes[i])
          if gan is not None:
               return gan
          
          gan = total_alinhado(transposta[i])
          if gan is not None:
               return gan
          
          velha -= posicoes[i].count("x")
          velha -= posicoes[i].count("o")

     if velha == 0:
          return "velha"
     return None

#Função auxiliar que retornará 'x'ou 'o' ou None
def total_alinhado(linha):
     num_x = linha.count("x")
     num_o = linha.count("o")

     if num_x == 3:
          return "x"
     if num_o == 3:
          return "o"
     
     return None

############# REINICIANDO A PARTIDA #############
def fim_de_jogo(stdscr, vencedor):
     stdscr.addstr(6, 1, "O %s venceu..." %vencedor)
     stdscr.addstr(7, 1, "Pressione Y para jogar novamente ou Q para sair.")
     stdscr.refresh()

############# FUNÇÃO MAIN #############
# Função  principal do jogo, que irá gerencial a tela do terminal
def main(stdscr):

#Função de reiniciar tela declarada para ser usada sempre que necessária
    reiniciar_tela(stdscr)
   
    width = stdscr.getmaxyx()[1] #Função getmaxyx() que pega a altura e a largura do terminal
    x_center = (width - 1) // 2 #Calculo do centro, feito usando o //
    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    pos_x, pos_y = 0, 0

    fim_de_partida = None

   #Laço infinito de repetição mais importante do jogo para definir o escopo das execuções 
    while True:
         entrada = stdscr.getkey() # Mapeia as teclas que o usuário está digitando
         if entrada == 'q':
              break
         
         if fim_de_partida is None:

          if (entrada in ['a', 's', 'w', 'd']):
              pos_x, pos_y = espaço_do_tabuleiro(pos_x, pos_y, entrada)

         if entrada == "\n": #\n representa gerador de novas linhas, portanto a função jogador será chamada
              
              #Fará com que o bot só jogue assim que o Jogador tiver efetivamente marcado uma posição válida 
              jogou, posicoes = jogador(pos_x, pos_y, posicoes)
              fim_de_partida = ganhador(posicoes) #Vai interromper o jogo caso alguém ganhe
              if jogou is True and fim_de_partida is None:
                   posicoes = robo(posicoes)

              if entrada == "y":
                    fim_de_partida = None
                    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

                    pos_x = 0
                    pos_y = 0
         if entrada == 'h':
              ajuda(stdscr)
         else:
              tabuleiro(stdscr, posicoes, x_center)
              if fim_de_partida is not None:
                   fim_de_jogo(stdscr, fim_de_partida)
              cursor(stdscr, pos_x, pos_y, x_center) # O cursor sempre fica no último elemento desenhado


