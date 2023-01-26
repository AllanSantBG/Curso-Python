while True:
    num = int(input(f'Digite o valor: '))
    if num < 0:
        break
    for multi in range(1, 11):
        print(f'{num} x {multi} = {num * multi}')
    print('=' * 40)
print('=' * 40)
print('Programa finalizado')