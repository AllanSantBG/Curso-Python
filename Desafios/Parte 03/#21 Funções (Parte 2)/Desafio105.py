def notas(* n, sit=False):
    """=-=-=>Função de análise de notas e situação do aluno
    :param n: notas do aluno
    :param sit: opcional, mostrar a situação do aluno
    :return dados: retorna um dicionário com a análise e situação do aluno"""
    dados = dict()
    dados['Qntd de Notas'] = len(n)
    dados['Maior Nota'] = max(n)
    dados['Menor Nota'] = min(n)
    dados['Média'] = round(sum(n) / len(n), 2)
    if sit == True:
        if dados['Média'] >= 7:
            dados['Situação'] = 'Aprovado'
        elif dados['Média'] < 5:
            dados['Situação'] = 'Reprovado'
        else:
            dados['Situação'] = 'Recuperação'
    return dados


print(notas(5.5, 9.5, 10, 6.5, sit=True))
help(notas)