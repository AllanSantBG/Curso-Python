sexo = str(input('Digite seu sexo (M/F): ').strip()[0])
while sexo not in 'MmFf':
    sexo = str(input('Caracteré invalido, Digite seu sexo (M/F): ').strip()[0])
print(f'O dado foi computado.')