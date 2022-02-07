'''

Exercício Python 015: Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais 
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.

'''

km_percorridos = float(input('\nDigite a distância percorrida em Km: '))
uso_do_carro = int(input('\nDigite por quantos dias o carro foi usado: '))

diaria_carro = 60 * uso_do_carro

km_rodado = km_percorridos * 0.15

print(f'\nO veiculo percorreu: {km_percorridos} \nO veiculo foi utilizado por: {uso_do_carro} dias \n\nSendo:\n \nDiaria carro: R${diaria_carro} \nValor Km rodado: R${km_rodado:.2f} por Km\n')

