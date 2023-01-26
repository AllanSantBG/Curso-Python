from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = (date.today().year - dados['nascimento'])
dados['ctps'] = int(input('CTPS (0 = NÃO TEM): '))
if dados['ctps'] != 0:
    dados['ano da contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['idade na aposentadoria'] = (dados['ano da contratacao'] + 35 - dados['nascimento'])
dados.pop('nascimento')
print('=' * 30)
for k, v in dados.items():
    print(f'{k.upper()} = {v}')