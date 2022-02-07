
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

list = [n1, n2, n3]

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior')

elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior')

elif n3 > n1 and n3 > n2:
    print(f'{n3} é maior')

else:
    print('temos números semelhantes')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O menor valor foi {menor}')


print(f'O maior número da lista é {max(list)} e o menor número é {min(list)}')