def contador(inicio, final, pula):
    print('=' * 50)
    print(f'CONTADOR DE {inicio} ATÉ {final}, DE {pula} EM {pula}')
    print('=' * 50)
    if pula == 0:
        pula == 1
    if inicio > final and pula > 0:
        pula *= -1
    if final < 0:
        final -= 1
    else:
        final += 1
    lista = list()
    for i in range(inicio, final, pula):
        lista.append(i)
    for i in lista:
        print(i, end=' ')
    print('')


contador(1, 10, 1)
contador(10, 0, -2,)
contador(int(input('Início: ')), int(input('Final: ')), int(input('Pula: ')))
