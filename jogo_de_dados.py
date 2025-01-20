#!/usr/bin/env python3.10.13


"""
Jogo de dados.
Programa sob licença  GNU V.3
Versão 0.0.1 
"""

from random import randint

print("##### Jogo de dados #####")
print("    #Teste sua sorte#")

while(True):
    numero = int(input("Escolha uma número: "))
    dado = randint(1, 6)
    if dado == numero:
        print("Parabéns, você acertou!!")
        print("Gostaria de tentar novamente? ")
        escolha = input("Escolha S para SIM ou N para NÃO:")
        if escolha == 'N' or escolha == 'n':
         break
    else:
        print("Não foi dessa vez.")
        print("O número sorteado foi: {0}". format(dado))
    print("Deseja tentar a sorte novamente?")
    escolha_2 = input("Escolha S para sim ou N para não:")

    if escolha_2 == 'N'or escolha_2 == 'n':
        break