def leiaint(num):
    valor = ' '
    while valor.isnumeric() == False:
        valor = str(input(num)).strip()
        if valor.isnumeric() == True:
            return int(valor)
        else:
            print('\033[7;30;41m' + 'ERRO! O valor digitado é inválido, tente novamente' + '\033[m')


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')