lista = []
for i in range(1, 6):
    peso = float(input(f'Digite o PESO da {i}ª PESSOA em Kg: '))
    lista.append(peso)
print(f'O MAIOR peso registrado foi {max(lista):.2f}Kg\nO MENOR peso registrado foi {min(lista):.2f}Kg')