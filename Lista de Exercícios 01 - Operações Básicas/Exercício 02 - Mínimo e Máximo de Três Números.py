#Escreva um script que receba três números inteiros e exiba o mínimo e o máximo

number_one = int(input('Digite o primeiro número: '))
number_two = int(input('Digite o segundo número: '))
number_three = int(input('Digite o terceiro número: '))

# max_number = max(number_one, number_two, number_three)
# min_number = min(number_one, number_two, number_three)

max_number = number_one
min_number = number_one

# Determinar o máximo
if number_two > max_number:
    max_number = number_two
if number_three > max_number:
    max_number = number_three

# Determinar o mínimo
if number_two < min_number:
    min_number = number_two
if number_three < min_number:
    min_number = number_three

print(f'O valor máximo é: {max_number}')
print(f'O valor mínimo é: {min_number}')
