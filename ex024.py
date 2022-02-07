#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

while True:

    cidade = str(input('Digite um nome de uma cidade: ')).strip()

    # divido a string
    dividido = cidade.split()
    
    # transformo tudo em titulo e pego a primeira palavra com o 'divido[0]'
    t = dividido[0].title()

    # se em cidade tem santo no dividido
    cidade = 'Santo' in t

    print(f'Sua cidade começa com "Santo": {cidade}')