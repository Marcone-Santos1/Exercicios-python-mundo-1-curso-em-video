import random
from time import sleep

num = random.randint(0,5)

print('-='*30)
print('\nVou pensar em um número de 0 a 5\n')
print('-='*30)

chute = int(input('\nChute um número: '))

print('\nprocessando.....')
sleep(1)

if chute > 5 or chute < 0:
    print('\nSomente números de 0 a 5.')

elif chute == num:
    print('\nVocê ganhou!')

else:
    print(f"\nVocê perdeu! O número era {num}")

'''
elif chute > num:
    print(f'Chute um número menor que {chute}')

elif chute < num:
    print(f'Chute um número maior que {chute}')
'''

