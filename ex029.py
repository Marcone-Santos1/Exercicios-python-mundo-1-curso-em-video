
velocidade = float(input('Qual a velocidade do veículo? '))

velocidade_maxima = 80.0

multa = (velocidade - velocidade_maxima) * 7

if velocidade > 80.0:
    print(f'Você foi mmultado no valor de {multa}')

else:
    print('Você não foi multado')
