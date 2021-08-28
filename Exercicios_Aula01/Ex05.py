# Escreva um programa em Python para obter a mediana de um conjunto de dados com n elementos o sem uso de funções matemáticas / Estatísticas.
# Obs: Para entender esse exemplo é necessário conhecimento de medidas de tendência central. 

# Para calcular a mediana é necessário ordenar os elementos de forma crescente.

# Mediana com número de elementos ímpar: 
# Fórmula para indicar a posição do valor da mediana: (n+1)/2 
# n é a quantidade de elementos 

# Mediana com número de elementos par:
# Fórmula: n/2 e (n/2)+1. Logo a mediana será a média desses valores que estão nessas posiçãoes. 
# n é a quantidade de elementos 

dados = [1, 2, 3, 4, 5, 6] #lista de dados pré-definida
n = len(dados) #fórmula para contar a quantidade de elementos que tem na lista
dados.sort() #fórmula para ordenar os valores da lista de forma crescente

if n % 2 == 0: #se a quantidade de elementos da lista for par (volte ao Ex04 que tem explicações sobre ser par)
    mediana1 = dados[n//2] # // é o floor division: retorna ao maior inteiro possível da divisão
    #nesse caso, 6 elementos: 6//2=3, o número será 4 (posição 0: 1, posição 1: 2, posição 2: 3, posição 3: 4, posição 4: 5 e posição 5: 6)
    mediana2 = dados[n//2 - 1] #mediana1 e 2: estou acessando na lista de dados o número equivalente a essa posição
    #com o primeiro índice é 0, temos que voltar uma posição, pois a quantidade começa a contar de 1,2,3..., diferente os índices de python que começam em 0,1,2...
    mediana = (mediana1 + mediana2)/2

else: #caso contrário será uma quantidade ímpar de elementos:
    mediana = dados[n//2]

print("Mediana é:", mediana)

print("Mediana é: " + str(mediana)) #outra forma de mostrar em python. 