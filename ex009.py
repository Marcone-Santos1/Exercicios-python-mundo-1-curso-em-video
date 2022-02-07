import time

def calculators():
    

    print("\nMenu:\n 1 = caluladora normal \n 2 = alculadora for\n")


    escolha = input("Escolha um opção: ")
    print("")

    if escolha == "1":
        n = int(input('Digite um número: '))

        print('')

        # pode ser assim:
        print(20*'=')
        print(f'{n} * 1 =', n * 1)
        print(f'{n} * 2 =', n * 2)
        print(f'{n} * 3 =', n * 3)
        print(f'{n} * 4 =', n * 4)
        print(f'{n} * 5 =', n * 5)
        print(f'{n} * 6 =', n * 6)
        print(f'{n} * 7 =', n * 7)
        print(f'{n} * 8 =', n * 8)
        print(f'{n} * 9 =', n * 9)
        print(f'{n} * 10 =', n * 10)
        print(20*'=')

    elif escolha == "2":
        n = int(input('Digite um número de: '))
        print('')
    

        for nu in range (10):
            print(f'{n} * {nu} = {n * nu}' )


    else:
        print("opção invalída")
        print('')
        time.sleep(1.2)

    calculators()
calculators()
    
