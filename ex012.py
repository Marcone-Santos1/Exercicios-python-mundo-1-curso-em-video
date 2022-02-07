# Faça um algoritmo quue laia o preço do produto e mostre seu novo preço com 5% de desconto

preço = float(input('Digite o preço do produto: '))

desconto = preço * (5/100)

novo_preço = preço - desconto

print(f'O desconto é de: R${desconto:.2f},  e o novo preço é de: R${novo_preço:.2f}')
