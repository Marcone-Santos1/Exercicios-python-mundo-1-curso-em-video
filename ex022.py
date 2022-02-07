'''
Crie um programa que leie o nome completo de uma pessoa e mostre:

nome com todas as letras maiusculas
o nome com todas minusculas
quantas letras ao todo(sem considerar espaços)
quantas letras tem o primeiro nome

'''

nome = str(input('Digite seu nome completo:\nNome: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
print(nome.find(' '))

separa = nome.split()
print(f'{separa[0]} e tem {len(separa[0])}')
