'''Suponha que um HD seja composto de quatro partições, denominadas de B1, B2, B3 e B4, que respondem respectivamente por 50%, 25%, 15% e 10% do disco em questão. Uma falha denominada de A pode ocorrer em qualquer umas dessas partições. Testes realizados pelo controle de qualidade da empresa que desenvolve esse equipamento, sugerem que taxa de falha para A dado B1, B2, B3 e B4, são respectivamente, 10%, 5%, 2% e 1%. Escreva um programa em Python que retorna a probabilidade da falha de A, considerando o cenário em questão'''

# Esse problema é resolvido através do Teorema da probabilidade total (veja a imagem do teorema da probabilidade total), no qual é o somatório da multiplicação entre a probabilidade do evento ocorrer condicionado a uma situação e a situação. Em outras palavras: "Dado um resultado A, com probabilidades condicionais conhecidas dado qualquer evento de Bn, cada um com sua probabilidade, qual é a probabilidade total de que A vai acontecer?". Esse teorema vai nos permitir calcular a probabilidade de um evento a partir do conjunto de probabilidades condicionais que envolvam esse evento. 

# A fórmula é: somatório de P(A|Bk)*P(Bk)

a = [0.1,0.05,0.02,0.01] #a taxa de cada partição falhar 
b = [0.5,0.25,0.15,0.1] #as partes em que o HD está dividido

res_list = [a[i] * b[i] for i in range(len(b))] #aqui ele está multiplicando as probabilidades: de ocorrer A, ou seja, de falhar na partição B1 é 0.1 multiplicado pelo espaço B1 que é 0.50. E assim por diante..

sum(res_list) #aqui ele só soma todo mundo

print(sum(res_list)) #O resultado é 0.0665, ou seja, existe uma probabilidade de 6,65% de ocorrer uma falha. 