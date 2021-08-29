# Dado uma lista com n elementos, escreva um programa em Python que retorne as seguintes medidas:
# A média aritmética e geométrica;
# Moda;
# Mediana. 

# A ideia aqui pe fazer com que o usuário digite a sua própria lista. 

# Fazendo com que o usúario defina a lista que ele quer:

lista_do_usuario = [] #criando uma lista vazia
elementos = int(input("Olá, por gentileza, insira a quantidade de elementos que serão utilizados na sua lista para o cálculo das medidas de tendência: " )) #solicitando ao usuário o tamanho da lista, usando int para transformar em inteiro, caso contrário ele considera como uma string

c = 0 #contador básico do while

while (c<elementos): #enquanto não chegar no valor total de elementos informado pelo usuário, percorre o while
    lista_do_usuario.append(int(input("Digite o valor: "))) #solicitando o input de dados. A função append insere novos valores numa lista
    c=c+1 #acrescentando valores ao contador

print("A sua lista de elementos digitada foi: ", lista_do_usuario) #mostrando para o usuário a lista dele

# Se precisar entender sobre as fórmulas de medidas de tendência, volte ao Ex06

import numpy 
from math import prod 
import statistics 
import math 

media_arit = sum(lista_do_usuario)/len(lista_do_usuario) 
print("A média aritmética é ", media_arit)

media_geo = numpy.prod(lista_do_usuario)**(1/len(lista_do_usuario))
print("A média geométrica é ", media_geo)

lista_ordenada = sorted(lista_do_usuario) 
print(lista_ordenada)
 
print("Quantidade de elementos na lista: ", elementos)

meio=int(elementos/2) 
print("Posição do elemento central: ", meio+1)

if (len(lista_do_usuario)%2)==0:  
    mediana = ((lista_ordenada[meio-1])+lista_ordenada[meio])/2
    print("A mediana é: ", mediana)
else: 
    mediana = lista_ordenada[meio] 
    print("A mediana é: ", mediana)

if (len(statistics.multimode(lista_ordenada))==1):
    moda = statistics.mode(lista_ordenada)
    print("A moda é: ",moda)
else:
    moda2 = statistics.multimode(lista_ordenada) 
    print("A moda multimodal é: ", moda2)   