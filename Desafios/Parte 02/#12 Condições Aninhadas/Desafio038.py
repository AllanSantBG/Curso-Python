num1 = float(input('Digite o 1º NÚMERO:'))
num2 = float(input('Digite o 2º NÚMERO:'))
if num1 > num2:
    print('-O primeiro valor é MAIOR\n-O segundo valor é MENOR')
elif num1 < num2:
    print('-O segundo valor é MAIOR\n-O primeiro valor é MENOR')
else:
    print('-Nenhum valor é MAIOR ou MENOR, os dois são IGUAIS')