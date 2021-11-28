# Escreva um programa em Python que informe se um determinado número é par ou ímpar.

# Definindo uma variável x inteira. Usando input para o usuário digitar o valor desejado. 
x = int(input("Digite um número: "))

if (x % 2) == 0:
    print("É par")
else: 
    print("É ímpar")

# x % 2 significa o resto da divisão de x por 2. Todo número par ao ser dividido por 2 tem resto zero. Então, se a divisão de x por 2 for identicamente igual a zero é um número par.  

# OBS: NÃO ESQUEÇA DOS DOIS PONTOS NO IF E ELSE!!! Eu esqueci...