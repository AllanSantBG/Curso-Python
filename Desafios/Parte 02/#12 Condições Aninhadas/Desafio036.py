casa = float(input('Digite o VALOR do ÍMOVEL: '))
salario = float(input('Digite o SALÁRIO do COMPRADOR: '))
anos = int(input('Digite em quantos ANOS págara o ÍMOVEL: '))
prestacao = casa / (anos * 12)
prestacaoRound = round(prestacao, 2)
msg = f'Suas prestações seriam de R${prestacaoRound} em {anos} anos'
if (prestacao) <= (salario * (30 / 100)):
    print(msg + f'\nSeu financiamento foi APROVADO!')
else:
    print(msg + f'\nInfelizmente seu financiamento foi NEGADO!')