#Escreva um script que receba um número inteiro do usuário e exiba na tela
#se o número é divisível por 3 ou 5.

number = int(input('Digite o número: '))

if( (number % 3) == 0 or (number % 5) == 0):
    print(f'O número {number} é divisível por 3 ou 5')
else:
     print(f'O número {number} NÃO é divisível por 3 ou 5')
