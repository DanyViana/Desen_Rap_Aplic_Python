# Dado uma lista com n elementos, escreva um programa em Python que retorne as seguintes medidas:
# A média aritmética e geométrica;
# Moda;
# Mediana. 

import numpy #importação para o cálculo do produto dos números da lista
from math import prod #importação para o cálculo do produto dos números da lista
import statistics #importação para a moda
import math #importação para efetuar alguns cálculos matemáticos (fórmulas)

lista_elementos = [1,5,6,2,5,9,10,15,2,5] #lista aleatória

#len() é a fórmula para contar a quantidade de elementos que tem na lista

# Média aritimética: a soma dos elementos da lista dividido pela quantidade de elementos que a lista tem
media_arit = sum(lista_elementos)/len(lista_elementos) #sun() é a fórmula de soma
print("A média aritmética é ", media_arit)

# Média geométrica: é a raíz dos N elementos da multiplicação dos elementos.ATENÇÃO para o 1/len pois é raíz
media_geo = numpy.prod(lista_elementos)**(1/len(lista_elementos))
print("A média geométrica é ", media_geo)
media_goe2 = prod(lista_elementos)**(1/len(lista_elementos))
print("A média geométrica de outro jeito é: ",media_goe2) 

# Para calcular a mediana precisamos organizar a lista, e para facilitar eu criei um valor com a quantidade de elementos da lista para facilitar nos cálculos, pra não ficar um fórmula dentro de outra. 

lista_ordenada = sorted(lista_elementos) #função para ordenar os elementos da lista de forma crescente
print(lista_ordenada)

elementos = len(lista_elementos) 
print("Quantidade de elementos na lista: ", elementos)

meio=int(elementos/2) #função para verificar qual a posição do meio na lista (é posição, não é o número)
print("Posição do elemento central: ", meio+1) #como começa com índice zero, considerei o + 1 porque iniciamos a contagem em 1, 2, 3... e o python inicia a contagem do index em 0, 1, 2...

# Medida: SE a quantidade de elementos é par, a mediana é a soma do valor antecessor ao meio e o valor do meio, divido por 2. SE a quantidade de elementos é ímpar, a mediana é o valor central. 
if (len(lista_ordenada)%2)==0: #verificar se o resto da divisão por 2 é zero, se for é par. 
    mediana = ((lista_ordenada[meio-1])+lista_ordenada[meio])/2
    print("A mediana é: ", mediana)
else: 
    mediana = lista_ordenada[meio] #função que acessa o valor do meio da lista
    print("A mediana é: ", mediana)
# Volte ao Ex05 para ver maiores explicações sobre essa questão do posicionamento. 

# Moda: valor que aparece mais vezes na lista
# não consegui fazer sem usar fórumla!!!
# SE a quantidade de elementos da fórmula multimodal for apenas 1, significa que não é multimodal, é apenas 1 número com maior frequência. Caso contrário, significa que os valores são multimodais. 
if (len(statistics.multimode(lista_ordenada))==1):
    moda = statistics.mode(lista_ordenada) #para o caso de ser somente uma moda
    print("A moda é: ",moda)
else:
    moda2 = statistics.multimode(lista_ordenada) #para o caso de ser multimodal
    print("A moda multimodal é: ", moda2)   
#Fazer com a lista original gera resultados diferentes, pois ela vai considerar o primeiro valor que se repete da lista, por exemplo, vai retornar [5,2] na multimodal. E não [2,5] na lista ordenada. 

#Statistics.multimode e statistics.mode são fórmulas de moda e moda multimodal. 

# Prof indicou esse site: https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/ para o cálculo da moda sem usar uma fórmula já definida. 

# OBS: se você conseguir entender, por gentileza, me explique!!!! 

#Segue o código que tem no link: 

# Python program to print
# mode of elements
from collections import Counter
  
# list of elements to calculate mode
n_num = [1, 2, 3, 4, 5, 2]
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)