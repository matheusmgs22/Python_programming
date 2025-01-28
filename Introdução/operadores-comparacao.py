# declarando a variável
x = y = z = False

n1 = n2 = 0


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

# Quero comparar n1 e n2
x = n1 == n2
print('São iguais? ', x , '\n')


z = n1 > n2
print(n1 ,' é maior que ', n2, '?', z,'\n')

y = n1 != n2

#print(n1, 'São diferentes', n2, '?' , y , '\n' )
print('São diferentes ' + str(y)) # a concatenação com '+' só funciona com Strings.

