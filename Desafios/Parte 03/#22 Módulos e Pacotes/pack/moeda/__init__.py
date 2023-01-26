def aumentar(valor, porcentagem, f=True):
    if f == True:
        return corrigir(valor + (valor * (porcentagem / 100)))
    return valor + (valor * (porcentagem / 100))
def diminuir(valor, porcentagem, f=True):
    if f == True:
        return corrigir(valor - (valor * (porcentagem / 100)))
    return valor - (valor * (porcentagem / 100))
def dobro(valor, f=True):
    if f == True:
        return corrigir(valor * 2)
    return valor * 2
def metade(valor, f=True):
    if f == True:
        return corrigir(valor / 2)
    return valor / 2
def corrigir(valor):
    return f'{valor:.2f}'
def resumo(valor, a, b):
    print('=' * 50)
    print(f'{"RESUMO":^50}')
    print('=' * 50)
    print(f'Preço inserido: R${corrigir(valor)}')
    print(f'Preço aumentado em {a}%: R${aumentar(valor, a, True)}')
    print(f'Preço reduzido em {b}%: R${diminuir(valor, b, True)}')
    print(f'Preço dobrado: R${dobro(valor, True)}')
    print(f'Preço pela metade: R${metade(valor, True)}')
    print('=' * 50)