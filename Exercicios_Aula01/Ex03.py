# Modifique o programa apresentado na aula passada sobre o cálculo da distância, de forma a incluir mais uma coordenada e faça o seguinte teste:
# Se distância <= 3.5, "NPC ataca”;
# Senão se (3.5<distância<=6), "NPC em alerta"
# Senão "NPC não ataca"

# O programa da aula passada é esse: 
import math #necessário importar essa biblioteca para fazer a fórmula de distância 

p = [2.3,2.1]
q = [2.4,2.5]

# p e q são pontos de uma coordenada 

print(math.dist(p,q)) #fórmula simples e fácil do python para calcular a distância entre os pontos p e q

# A questão pede para incluir mais uma coordenada, foi incluso mais um valor em p e q
p = [2.3,3.1,5.5]
q = [1.5,4.2,2.3]

# Calculate Euclidean distance

x = (math.dist(p, q))

# Fazendo os teste através do SE (IF) para mostrar a condição desejada: 

if (x <= 3.5):

	print(x,"NPC ataca")

elif(3.5<x<=6):

	print(x,"NPC em alerta")

else:

	print(x,"NPC não ataca")