def maior(* num):
    print('=' * 50)
    print(f'Registrado(s) {len(num)} número(s): ', end='')
    for i in num:
        print(i, end=' ')
    if num == ():
        print(f'\nO maior número registrado foi 0')
    else:
        print(f'\nO maior número registrado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
