idadeSoma = 0
idadeMascMaior = 0
nomeVelho = ''
numMenor20Fem = 0
for i in range(1, 5):
    nome = str(input(f'Digite o NOME da {i}ª PESSOA: ').strip().title())
    idade = int(input(f'Digite a IDADE da {i}ª PESSOA: '))
    sexo = str(input(f'Digite o SEXO da {i}ª PESSOA(M/F): ').strip())
    print('')
    idadeSoma += idade
    if i == 1 and sexo in 'Mm':
        idadeMascMaior = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > idadeMascMaior:
        idadeMascMaior = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        numMenor20Fem += 1
print(f'A média de idade é {idadeSoma / 4}')
print(f'O homem mais velho tem {idadeMascMaior} anos e se chama {nomeVelho}')
print(f'Tem {numMenor20Fem} mulher(es) com menos de 20 anos')