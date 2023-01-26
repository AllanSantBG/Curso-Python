days = int(input('Quantos dias alugado: '))
kilometers = float(input('Quantos quilometrôs o carro percorreu: '))
cost = (days * 60) + (kilometers * 0.15)
print(f'O carro andou {kilometers:.2f}km e foi alugado por {days} dias, o aluguel custará R${cost}')