while True:
    salario = float(input('Qual o seu salário? '))

    if salario <= 1250:
        aumento = (salario * (15 /100)) + salario
        print(f'O novo salário será: R$ {aumento}')
        
    elif salario > 1250:
        aumento1 = (salario * (10 /100)) + salario
        print(f'O novo salário será: R$ {aumento1}')
