from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return 'Não pode votar', idade
    elif 18 < idade >= 16 or idade >= 65:
        return 'Voto opcional', idade
    else:
        return 'Voto obrigatório', idade


v = voto(int(input('Ano de nascimento: ')))
print(f'Você tem {v[1]} anos, {v[0]}')