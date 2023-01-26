for i in range(1, 6):
    peso = float(input(f'Digite o PESO da {i}ª PESSOA em Kg: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR peso registrado foi {maior:.2f}Kg\nO MENOR peso registrado foi {menor:.2f}Kg')