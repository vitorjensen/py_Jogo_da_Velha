
#Criando um função com uma variável de escopo "local" de forma global

# Criando a função que recebe dois parâmentros.
#def soma(a, b):
    #return a + b

#Criando a lista que será transformada em dois argumentos atravéz do *arg
#valores = [1,2]

#Utilizando o *arg para LISTAS
#b = soma(*valores)
#print(b)

# Creating a function using "Decorators"

#def primeira_funcao(valor):
    #quadrado = valor * valor
   # def segunda_funcao():
      #  return "O quadrado é {0}".format(quadrado)
   # return segunda_funcao()

# An example of behavior change can be seen below
def digitar_nome(nome_1):
    nome_1 = print(input(("Digite o seu nome")))
  
    #def apresentar(info):
        #return "Bem vindo ao nosso sistema, {0}".format(nome_1)

#def decorador_p(func):
  #  def funcao_encapsulada(nome_1):
   #     return "<p>{0}</p>".format(func(nome_1))
    #return funcao_encapsulada

#info_em_p = decorador_p(digitar_nome)
#print(info_em_p)