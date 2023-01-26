distancia = float(input('Digite a distância da viagem em Km: '))
print(f'Serão {distancia}Km de viagem')
if distancia < 200:
    preco = distancia * 0.5
    print(f'O valor da viagem vai ser de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O valor da viagem vai ser de R${preco:.2f}')