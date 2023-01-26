i = soma = 0
resposta = 'S'
while resposta not in 'Nn':
    i += 1
    num = float(input(f'Digite o {i}ª valor: '))
    resposta = str(input('Deseja continuar (S/N): ')).strip()[0]
    if resposta not in 'SsNn':
        i -= 1
        num = 0
        print('Caractere inválido, tente novamente')
    soma += num
    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'A média entre os {i} números foi {soma / i:.2f}')
print(f'O maior número registrado foi {maior}\nO menor número registrado foi {menor}' if maior != menor else (f'Os {i} números registrados são iguais'))