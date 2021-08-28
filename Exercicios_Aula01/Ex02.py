# Forneça exemplos de listas com caracteres, inteiros e listas aninhadas. Use o conceito de indexador para demonstrar o uso em python.

# O conceito de indexador é referente ao acesso a lista, para demonstrar algum valor específico dela ou ou fazer alguma alteração na lista. 

# No site https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html temos a seguinte definição: A sintaxe para acessar um elemento de uma lista é a mesma usada para acessar um caractere de um string. Nós usamos o operador de indexação ( [] – não confundir com a lista vazia). A expressão dentro dos colchetes especifica o índice. Lembrar que o índice do primeiro elemento é 0. Qualquer expressão que tenha como resultado um número inteiro pode ser usada como índice e como com strings, índices negativos indicarão elementos da direita para a esquerda ao invés de da esquerda para a direita.

caracteres = ["dany", "estacio", "corona-vírus"]
inteiros = [1,2,3,4,5,6]
aninhada = ["ads", 2021, ["python", "melhor linguagem"]]

print(caracteres[2])
print(aninhada[1])
print(aninhada[2])
print(len(inteiros))