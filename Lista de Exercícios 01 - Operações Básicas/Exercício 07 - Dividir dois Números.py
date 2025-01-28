#Escreva um programa que receba dois números do usuário e exiba na
#tela o resultado do primeiro divido pelo segundo.

number_one = int(input("Digite o primeiro número: "))
number_two = int(input("Digite o segundo número: "))

if number_two != 0:
    result = number_one / number_two
    print(f'O resultado da divisão é {result}')
else:
    print("Erro: Não é possível dividir por zero!")
