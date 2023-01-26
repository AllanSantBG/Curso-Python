opcao = 0
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
while opcao != 5:
    print(f'1º Número: {num1}\n2º Número: {num2}')
    print("""---------> OPÇÕES <---------
    |( 1 ) SOMAR
    |( 2 ) MULTIPLICAR
    |( 3 ) MAIOR
    |( 4 ) NOVOS NÚMEROS
    |( 5 ) SAIR DO PROGRAMA""")
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print(f'A soma dos números {num1} e {num2} é igual a {(num1 + num2):.2f}')
    elif opcao == 2:
        print(f'A multiplicação dos números {num1} e {num2} é igual a {(num1 * num2):.2f}')
    elif opcao == 3:
        if num1 >= num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior entre os números {num1} e {num2} é o {maior}')
    elif opcao == 4:
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
    elif opcao != 5:
        print('Valor inválido, insira o valor correto')
    print('=' * 50)
print('FIM')