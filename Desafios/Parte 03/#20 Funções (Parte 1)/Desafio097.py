def escreva(txt):
    tam = len(txt) + 2
    print('=' * tam)
    print(f' {txt}')
    print('=' * tam)


escreva(str(input('Digite algo: ')).strip())
