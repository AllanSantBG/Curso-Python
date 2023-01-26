frase = str(input('Digite algo: ')).replace(' ', '').strip().upper()
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase é um PALÍNDROMO')
else:
    print('A frase NÃO é um PALÍNDROMO')