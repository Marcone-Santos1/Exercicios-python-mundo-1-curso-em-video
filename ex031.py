def new_func():

    distancia = float(input('Qual a distância da sua viagem? '))

    passagem_curta = distancia * 0.50

    passagem_longa = distancia * 0.45

    if distancia <= 200:
        print(f'O preço da passagem será R$ {passagem_curta:.2f}')

    else:
        print(f'O preço da passagem será R$ {passagem_longa:.2f}')
    new_func()
new_func()

