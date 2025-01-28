#Escreva um programa que receba dois números do usuário e exiba na tela o valor
#absoluto da diferença do primeiro menos o segundo número

number_one = float(input("Digite o primeiro número: "))
number_two = float(input("Digite o segundo número: "))

difference = abs(number_one - number_two)

print(f'a diferença entre o valor {number_one} para o {number_two} é de {difference}')

# O abs() é uma função embutida no Python que calcula o valor absoluto de um número.
# O valor absoluto é a distância de um número em relação ao zero na reta numérica,
# independentemente de ser positivo ou negativo.
# Em termos simples, ele "remove" o sinal negativo de um número.

# Outra maneira de fazer, sem usar o abs
# if(number_two > number_one):
#  difference = difference * (-1)


