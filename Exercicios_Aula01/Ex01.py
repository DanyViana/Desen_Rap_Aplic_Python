# Escrever um programa em python em que tupla recebe conteúdo de outras duas e em seguida, imprime-se o conteúdo da nova tupla e o seu quarto elemento. 

# Tupla são representadas por () com os elementos separados por vírgula. Uma tupla não pode ser alterada - desvantagem com relação as listas. 

tupla1 = ('a','b','c')
tupla2 = ('d','e','f','g')

tupla1e2 = tupla1 + tupla2
print(tupla1e2)

print(tupla1e2[3]) #Os elementos começam em 0, 1, 2, 3... por isso o quarto elemento é o índice 3. 

