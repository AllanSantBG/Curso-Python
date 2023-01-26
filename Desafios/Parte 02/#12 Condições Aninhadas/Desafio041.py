from datetime import date
ano = int(input('Digite o ANO DE NASCIMENTO do ATLETA: '))
anoHoje = date.today().year
idade = anoHoje - ano
print(f'Idade do atleta: {idade} ANOS')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')