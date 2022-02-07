#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
while True:

    frase = str(input('Digite uma frase: ')).strip().upper()

    numero_de_a = print(f"A frase tem: {frase.count('A')} A's")
    primeiro_a = print(f'A posição da primeira letra "A" foi: {frase.find("A") + 1}')
    ultimo_a = print(f'A posição do ultimo "A" foi: {frase.rfind("A") + 1}')

    # find() para primeira letra ou frase
    # rfind() para a ultima letra ou frase