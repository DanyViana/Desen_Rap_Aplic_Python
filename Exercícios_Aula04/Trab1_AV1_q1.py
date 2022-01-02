# Problema 1: Escreva um programa python para ler uma linha aleatória de um arquivo. Depois o programa deve modificar a linha que foi lida, por uma texto informado pelo o usuário.

# SAPORRA rodou na minha máquina!!!

import random #Biblioteca para gerar o aleatório

frase = input("Digite a frase que gostaria de escrever no arquivo :") #solicitando ao usuário a frase que ele gostaria de imputar no arquivo

with open('aula04_prob1.txt', 'r') as arquivo: 
    #Esse 'r' é de read, está lendo o arquivo txt chamado 'aula04_prob1' crie um arquivo na sua máquina com algumas linhas escritas. 
    linhas = arquivo.readlines() #Criando uma variável chamada 'linhas' e fazendo com que o programa leia linha a linha. Se usar o .read() ele transforma todo o texto numa única string, o .readline() cria uma lista de strings, cada linha vira um elemento da lista. 

x = random.randint(0,len(linhas)) #Criando uma variável 'x' que gere aleatoriamente entre 0 e de acordo com o tamanho da variável linhas. Estamos importando do módulo random. Aqui ele vai escolher qualquer linha aleatória no meio do texto. 


linhas[x] = frase + "\n" #Na lista de strings criada, ele vai no índice que foi gerado aleatoriamente através da variável 'x' e acrescenta a frase que usuário digitou no início. 


with open('aula04_prob1.txt', 'w') as arquivo: #Esse 'w' é de write, ou seja, está escrevendo no arquivo
    arquivo.writelines(linhas)

# O arquivo não estava rodando na minha máquina devido ao local que ele estava sendo salvo. Não sei o motivo, mas salvar ele dentro da pasta "Exercícios_Aula04" não estava dando certo, ele não estava sendo localizado. Ele acabou ficando dentro da pasta "Desen_rap_aplic_python", que é a pasta 'mãe' onde tem todos os exercícios. 
