num = int(input('Digite um NÚMERO INTEIRO qualquer: '))
conversor = int(input(
"""|(1) Binário
|(2) Octadecimal
|(3) Hexadecimanl
Digite um NÚMERO DE 1 A 3 de acordo com a base de conversão: """))
if conversor == 1:
    print(f'O número {num} em BINÁRIO é {bin(num)[2:]}')
elif conversor == 2:
    print(f'O número {num} em OCTADECIMAL é {oct(num)[2:]}')
elif conversor == 3:
    print(f'O número {num} em HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Você digitou um número diferente de 1, 2 ou 3, tente novamente')