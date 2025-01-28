#Receba um número inteiro do usuário e exiba se o número é ímpar ou par

number = int(input('Digite o número: '))

if((number % 2) == 0):
    print(f'O número {number} é par')
else:
    print(f'O número {number} é Ímpar')

