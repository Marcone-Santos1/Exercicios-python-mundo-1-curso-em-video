n1 = input('Digite um número: ')
n2 = input('Digite um número: ')

print(n1.isalpha())
print(n2.isalpha())

soma = n1 + n2

print('A soma entre {} + {} é {}'.format(n1, n2, soma))

n = input('Digite algo: ')

print('é um numero alfanumérico:', n.isalnum())
print('é alfabético:', n.isalpha())
print('é decimal:', n.isdecimal())
print('é minusculo:', n.islower())
print('é maiusculo:', n.isupper())
print('é printavel:', n.isprintable())
