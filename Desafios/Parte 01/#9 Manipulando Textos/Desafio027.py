nome = str(input('Digite um nome: ')).title()
lista = nome.split()
tamanho = len(lista) - 1
print(f'O primeiro nome é {lista[0]} \nO ultimo nome é {lista[tamanho]}')