''' Faça 1 programa que peça a largura e altura de uma parede em metros. Calcule a area e a quantidade de tinta a necessária sabendo que cada
litro de tinta, pinta uma area de 2m**2'''

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

area_em_metros_quadrados = altura * largura

tinta_gasta = area_em_metros_quadrados / 2

print(f'A quantidade de tinta necessária para pintar a parede é de: {tinta_gasta:.2f} Litros de tinta.')

