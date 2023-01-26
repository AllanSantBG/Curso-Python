cont = maiores = homens = mulheresVinte = 0
while True:
    cont += 1
    idade = int(input(f'Digite a idade da {cont}ª pessoa: '))
    sexo = ' '
    resposta = ' '
    while sexo not in 'FM':
        sexo = str(input(f'Digite o sexo da {cont}ª pessoa (M/F): ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar (S/N): ').strip().upper()[0])
    print('=' * 30)
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresVinte += 1
    if resposta in 'N':
        break
print('Programa Finalizado')
print(f"""As informações inseridas das {cont} pessoas:
1. {maiores} pessoas são maiores de 18 anos
2. {homens} pessoas são homens
3. {mulheresVinte} pessoas são mulheres com menos de 20 anos""")