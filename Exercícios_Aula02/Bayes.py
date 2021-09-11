''' Suponha que você faça parte de uma equipe que deseja desenvolver um Role-playing game, também conhecido como RPG (Jogo eletrônico de aventura e de representação). Seu trabalho na equipe, consiste em desenvolver o sistema de drop  (Sistema de obtenção de itens) para os baús. Sendo assim, suponha que o jogo possua três tipos de baús B1, B2 e B3 e que cada um dos baús pode fornecer um item lendário com probabilidades dadas respectivamente por: 3%, 5% e 8%. Os baús podem ser encontrados em calabouços e as chances de se obtê-los são: 10%, 30% e 60%. (B1, B2 e B3). Sabendo-se que a equipe responsável pelos testes obteve um item lendário, qual é a probabilidade desse item ter vindo de cada um dos baús?'''

# Teorema de Bayes: Descobrir quais são as chances de determinado ato acontecer decorrentem de outros atos.

# A fórmula é: P(B|Ai)*P(Ai) / somatório de P(B|Ak)*P(Ak)

a = [0.03,0.05,0.08]  #probabilidade de encontrar o item lendário no baú
b = [0.1,0.3,0.6] #probabilidade de encontrar cada baú

res_list = [a[i] * b[i] for i in range(len(b))] #fazendo a parte da multiplicação do dividor da fórmula (antes do somatório)

divisor = sum(res_list) #aqui ele só soma todo mundo (somatório)

# O divisor nada mais é do que a probabilidade total de encontrar um item lendário em um dos baús, qualquer baú.

# O Teorema de Bayes é para calcular a probabilidade de ecnontrar um item lendário num baú específico. De encontrar e ser especificamente no baú 1, é a probabilidade de encontrar o baú 1 (0,1) vezes ter um item lendário nele (0,03) dividido pela probabilidade total de encontrar um item lendário seja em qualquer baú.

prob_cada = [(a[i] * b[i])/divisor for i in range(len(b))]

print(prob_cada)
print(f'A probabilidade de encontrar um item lendário no baú 1 é: {prob_cada[0]}')
print(f'A probabilidade de encontrar um item lendário no baú 2 é: {prob_cada[1]}')
print(f'A probabilidade de encontrar um item lendário no baú 3 é: {prob_cada[2]}')

print() #só para organizar

# Outra forma de fazer seria: 

prob_1 = (a[0]*b[0])/divisor
print(f'A probabilidade de encontrar um item lendário no baú 1 é: {prob_1}')

prob_2 = (a[1]*b[1])/divisor
print(f'A probabilidade de encontrar um item lendário no baú 2 é: {prob_2}')

prob_3 = (a[2]*b[2])/divisor
print(f'A probabilidade de encontrar um item lendário no baú 3 é: {prob_3}')
