def ajuda():
    valor = ' '
    while True:
        valor = str(input('Função/Biblioteca: '))
        if valor != 'fim':
            print('\033[0;30;40m')
            help(valor)
            print('\033[m')
        else:
            print('Programa finalizado, volte em breve!')
            break


ajuda()