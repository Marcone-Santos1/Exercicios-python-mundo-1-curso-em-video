while True:

    nome = str(input('Digite seu nome completo: ')).strip().title()
    print('\nmuito prazer em te conhecer!')
    n = nome.split()
    print(f'\nO seu primeiro nome é: {n[0]}')
    print(f'O seu ultimo nome é: {n[-1]}\n')

