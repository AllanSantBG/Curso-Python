aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["media"] >= 7:
    aluno['situacao'] = 'aprovado(a)'
elif 5 <= aluno["media"] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado(a)'
print(f'A média de {aluno["nome"]} é igual a {aluno["media"]:.2f}\nSituação: {aluno["situacao"]}')