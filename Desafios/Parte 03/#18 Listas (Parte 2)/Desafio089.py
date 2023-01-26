dados = list()
alunos = list()
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().title()
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    dados = [nome, nota1, nota2, media]
    resposta = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if resposta not in 'SN':
        dados.clear()
    alunos.append(dados[:])
    dados.clear()
    if resposta in 'N':
        break
    print('-' * 40)
print(f'{"Nº":>3} {"NOME":^6} {"Média":>8}')
print('=' * 20)
for i in range(len(alunos)):
    print(f'{i:>2} {alunos[i][0]:^10} {alunos[i][3]:>2}')
print('=' * 20)
while True:
    num = int(input('Número do aluno (999 = PARAR): '))
    if num == 999:
        break
    elif len(alunos) > num >= 0:
        print(f'As notas de {alunos[num][0]} são [{alunos[num][1]}, {alunos[num][2]}]')
    print('-' * 40)
print('O programa foi finalizado, volte sempre!')