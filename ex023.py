#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

def digitos():

    num = str(input('Digite um número de 0 a 9999 \nNúmero: '))

    len(num)

    if len(num) == 4:
        print(f'''
        Milhar: {num[0]}
        Centena: {num[1]}
        Dezena: {num[2]}
        Unidade: {num[3]}
        ''')
        
    elif len(num) == 1:
        print(f'''
        Unidade: {num[0]}
        ''')

    elif len(num) == 2:
        print(f'''
        Dezena: {num[0]}
        Unidade: {num[1]}
        ''')

    elif len(num) == 3:
        print(f'''
        Centena: {num[0]}
        Dezena: {num[1]}
        Unidade: {num[2]}
        ''')

    elif len(num) >= 5:
        print('\nApenas números de 0 a 9999\n')

    while True:
        digitos()

digitos()