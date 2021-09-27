# Problema 1: Escreva um programa python para ler uma linha aleatória de um arquivo. Depois o programa deve modificar a linha que foi lida, por uma texto informado pelo o usuário.

import random #Bibliotec para gerar o aleatório

frase = input("Digite a frase que gostaria de escrever no arquivo :") #solicitando ao usuário a frase que ele gostaria de imputar no arquivo

with open('prob1.txt', 'r') as arquivo: 
    #Esse 'r' é de read, está lendo o arquivo txt chamado 'prob1' - crie um arquivo na sua máquina. 
    linhas = arquivo.readlines() #Criando uma variável chamada 'linhas' e fazendo com que o programa leia linha a linha. Se usar o .read() ele transforma todo o texto numa única string, o .readline() cria uma lista de strings.

x = random.randint(0,len(linhas)) #Criando uma variável 'x' que gere aleatoriamente entre 0 e de acordo com o tamanho da variável linhas. Estamos importando do módulo random. 


linhas[x] = frase + "\n" #Na lista de strings criada, ele vai no índice que foi gerado aleatoriamente através da variável 'x' e acrescenta a frase que usuário digitou no início. 


with open('prob1.txt', 'w') as arquivo: #Esse 'w' é de write, ou seja, está escrevendo no arquivo
    arquivo.writelines(linhas)