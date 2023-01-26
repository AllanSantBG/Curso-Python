extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
            'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 
            'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 ate 20: '))
    if 0 <= num <= 20:
        break
    print('Valor inválido, tente novamente')
print(f'O número digitado foi {extenso[num].upper()}')