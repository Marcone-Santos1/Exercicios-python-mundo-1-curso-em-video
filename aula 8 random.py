import random



valor_aleatorio = random.randint(1, 100)
acertou = False
while acertou == False:


    chute = int(input('Chute um numero: '))
    print('')

    if chute > 100 or chute < 1:    
        print('Apenas números entre 1 a 100, tente de novo')

    elif chute > valor_aleatorio:
        print('Chute um valor menor que,', chute)

    elif chute < valor_aleatorio:
        print('Chute um valor maior que,', chute)

    elif chute == valor_aleatorio:
        print('Você acertou.')
        print('Seu chute:', chute)
        acertou = True
