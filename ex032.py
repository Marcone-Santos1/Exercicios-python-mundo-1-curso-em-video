'''
ano bissexto
'''

ano = int(input('DIgite um ano: '))

if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano não Bissexto')

# com calendar
import calendar

ano1 = int(input('DIgite um ano: '))

ano_bi = calendar.isleap(ano)
if ano_bi is True:
    print(f'O ano de {ano1} é bissesxto')
else:
    print(f'O ano de {ano1} não é bissexto')

# com datetime

from datetime import date

ano2 = int(input('DIgite um ano; ou 0 para o ano atual: '))
if ano2 == 0:
    ano2 = date.today().year

if ano2 % 4 and ano2 % 100 != 0 or ano2 % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano não Bissexto')


