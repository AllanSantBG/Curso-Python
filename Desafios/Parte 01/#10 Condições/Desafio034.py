salario = float(input('Digite o do salario do funcionario: '))
if salario >= 1250:
    aumento = salario * (10 / 100)
    print(f'O salário de R${salario:.2f} foi aumentado para R${salario + aumento:.2f}')
else:
    aumento = salario * (15 / 100)
    print(f'O salário de R${salario:.2f} foi aumentado para R${salario + aumento:.2f}')