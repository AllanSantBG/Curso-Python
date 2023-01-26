def leiaDinheiro(valor):
    while True:
        if valor.strip().replace(',', '').replace('.', '').isnumeric() == False:
            print(f'ERRO! O valor {valor} é inválido, tente novamente')
            valor = str(input('Preço: R$'))
        else:
            return float(valor.replace(',', '.'))