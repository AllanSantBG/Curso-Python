peso = float(input('Digite o SEU PESO em KG: '))
altura = float(input('Digite a SUA ALTURA em METROS: '))
indice = peso / (altura ** 2)
print(f'Seu IMC é {indice:.2f}')
if indice < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= indice < 25:
    print('Você está no peso normal')
elif 25 <= indice < 30:
    print('Você está com sobrepeso')
elif 30 <= indice < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')