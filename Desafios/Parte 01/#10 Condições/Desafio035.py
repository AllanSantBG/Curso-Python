reta1 = float(input('Digite o comprimento da 1ª reta: '))
reta2 = float(input('Digite o comprimento da 2ª reta: '))
reta3 = float(input('Digite o comprimento da 3ª reta: '))
if reta2 + reta3 > reta1 and reta1 + reta3 > reta2 and reta1 + reta2 > reta3:
    print('PODE SER FORMADO um triângulo com estes comprimentos de reta')
else:
    print('NÃO PODE SER FORMADO um triângulo com estes comprimentos de reta')