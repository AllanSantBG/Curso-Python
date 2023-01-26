from datetime import date
anoHoje = date.today().year
menor = 0
maior = 0
for i in range(1, 8):
    nascimento = int(input(f'Digite ANO de NASCIMENTO da {i} PESSOA: '))
    if (anoHoje - nascimento) < 18:
        menor += 1
    else:
        maior += 1
print(f'{maior} pessoas ATINGIRAM A MAIORIDADE\n{menor} pessoas NÃO ATINGIRAM A MAIORIDADE')