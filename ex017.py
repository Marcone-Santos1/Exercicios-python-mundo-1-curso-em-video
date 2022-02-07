import math

cateto_1 = float(input('Digite o cateto oposto: '))
cateto_2 = float(input('Digite o cateto adjacente: '))

hipotenusa = math.hypot(cateto_1, cateto_2)

print(f'{hipotenusa:.2F}')

'''
Formula matemática:

hi = (co ** 2 + ca ** 2) ** (0.5)

'''