nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média foi {media:.1f}\nO aluno foi REPROVADO')
elif media >= 7:
    print(f'Sua média foi {media:.1f}\nO aluno foi APROVADO')
else:
    print(f'Sua média foi {media:.1f}\nO aluno está em RECUPERAÇÃO')