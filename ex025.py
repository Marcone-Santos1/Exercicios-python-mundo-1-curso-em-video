#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

while True:
    
    nome = str(input('Qual o seu nome completo? ')).strip().title()
    print(f'O nome informado tem Silva? {"Silva" in nome}')