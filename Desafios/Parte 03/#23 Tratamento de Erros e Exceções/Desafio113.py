def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except KeyboardInterrupt:
            print('Valor não informado')
            num = 0
            return num
        except:
            print('\033[7;30;41m' + 'Erro! Digite um número INTEIRO' + '\033[m')
        else:
            return num
def leiaReal(txt):
    while True:
        try:
            num = float(input(txt).strip().replace(',', '.'))
        except KeyboardInterrupt:
            print('Valor não informado')
            num = 0
            return num
        except:
            print('\033[7;30;41m' + 'Erro! Digite um número REAL' + '\033[m')
        else:
            return num

inteiro = leiaInt('Número inteiro: ')
real = leiaReal('Número real: ')
print(f'Você digitou o número inteiro {inteiro} e o número real {real}')