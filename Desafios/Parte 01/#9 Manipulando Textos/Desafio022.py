nome = str(input('Digite o seu nome completo: ')).strip()
nomeSemEspaço = nome.replace(' ', '')
primeiroNome = nome.split()[0]
print('Nome em letras maiúsculas:', nome.upper())
print('Nome em letras minúsculas:', nome.lower())
print('Quantidade de letras no nome completo:', len(nomeSemEspaço))
print('Quantidade de letras no primeiro nome):', len(primeiroNome))