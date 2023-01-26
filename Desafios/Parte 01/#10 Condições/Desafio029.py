velocidade = int(input('Digite a velocidade do carro em Km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado por execeder o limite de velocidade de 80Km/h \nSua multa vai custar R${multa:.2f}')
else:
    print('Você não foi multado, continue assim!')