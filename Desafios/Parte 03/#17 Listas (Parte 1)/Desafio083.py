exp = str(input('Digite uma expressão matemática: '))
if exp.count('(') == exp.count(')'):
    print('Esta expressão é válida')
else:
    print('Esta expressão não é válida')