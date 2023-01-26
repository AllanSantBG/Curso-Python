reta1 = float(input('Digite o COMPRIMENTO da 1ª RETA: '))
reta2 = float(input('Digite o COMPRIMENTO da 2ª RETA: '))
reta3 = float(input('Digite o COMPRIMENTO da 3ª RETA: '))
if reta2 + reta3 > reta1 and reta1 + reta3 > reta2 and reta1 + reta2 > reta3:
    print('PODE SER FORMADO um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('NÃO PODE SER FORMADO um triângulo')