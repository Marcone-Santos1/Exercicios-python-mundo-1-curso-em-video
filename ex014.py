def temp():
    Opção = input('1 - celsius \n2 - fahrenheit \n3 - Sair \nQual a escolha? ')


    while True:

        if Opção == '3':
            exit()

        
        elif Opção == '1':
            celsius = float(input("\nQual a temperatura? "))

            conversão = ((celsius * 9) / 5) + 32

            print(f"\nA conversão de {celsius} para fahrenheit fica {conversão:.2f}\n")
            temp()

            
        

        elif Opção == '2':
            fahrenheit = float(input('\nDigite a temperatura em Fahrenheit, ou seja, de 20F à 120F: '))

            c = 5

            celcius = c * ((fahrenheit - 32)) / 9

            print(f'\nA conversão de {fahrenheit}ºF para Celcius fica: {celcius:.2f}ºC\n')
            temp()

        
            
        
        else:
            print('\nOpção inválida')
            temp()

temp()