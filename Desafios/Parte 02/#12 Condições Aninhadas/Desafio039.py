from datetime import date
sexo = str(input('Digite o seu SEXO(M para MASCULINO ou F para FEMININO): ')).strip().lower()
if sexo == 'm':
    nascimento = int(input('Digite o seu ANO DE NASCIMENTO: '))
    anoHoje = date.today().year
    idade = anoHoje - nascimento
    if idade < 18:
        resto = 18 - idade
        print('-Você NÃO ESTA APTO a se alistar no exercito')
        print(f'-Você deverá se alistar em {anoHoje + resto}')
        print(f'-Ainda faltam {resto} ANOS')
    elif idade > 18:
        resto = idade - 18
        print(f'-Você ESTA APTO a se alista no exercito')
        print(f'-Você deveria ter se alistado em {anoHoje - resto}')
        print(f'-Já se passou {resto} anos do prazo, Aliste-se!')
    else:
        print(f'-Você ESTA APTO a se alistar no exercito\n-Você deve se alistar AGORA!')
else:
    print('Você não é obrigatório a se alistar no exercito')