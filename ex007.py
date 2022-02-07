nome = str(input('Qual é o seu nome? '))


print(f'olá, {nome}!')
print('')

entrar = input('aperte ENTER para comecar...')
print('')

print(20*'=')
print('')


escola = str(input('Em que escola você estuda? '))
print('')

print('A nota média da escola é 5')
print('')

nota_minima = 5.0

while True:

    nota_1 = float(input('Qual a sua nota em Matemática? '))
    nota_2 = float(input('Qual a sua nota em Português? '))
    print('')

    media = (nota_1 + nota_2) / 2

    if media >= nota_minima:
        print(f'{nome}, com a média de {media}, você foi aprovado para mais um ano na {escola}.')
        break

    elif media < nota_minima:
        print(f'{nome}, foi uma pena, mas você não foi aprovado. por ter uma média {media} abaixo da {nota_minima}.')
        break

