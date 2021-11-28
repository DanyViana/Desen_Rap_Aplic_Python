# Problema 2: Em muitas situações práticas em inteligência artificial, probabilidade e estatística, é necessário manipular os fatoriais de grandes números inteiros e não inteiros. Uma aproximação comumente aplicada ao cenário em questão, é conhecida como a aproximação de Stirling, dada por n! ∼ √2πn (n/e)**n (veja a fórmula na imagem do trabalho), em que o valor aproximado de e = 2.7182818284590452. Escreva um programa em python que retorne o valor do fatorial do número 5.5, a partir dessa aproximação. 

import math #importando a biblioteca de cálculos matemáticos

n= 5.5 
pi = 3.1415926535897932
e = 2.71828182845904523
#Valores das variáveis. 'pi' e 'e' foram tiradas da internet. 

fatorial = ((2*pi*n)**0.5)*((n/e)**n) #Escrevendo a fórmula - Cuidado e atenção com os parênteses e ordem de ocorrência dos cálculos matemáticos. 

print("2 questao: " , fatorial)
print(fatorial)

#Imprimindo de duas formas. 