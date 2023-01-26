from random import shuffle
name1 = str(input('Digite o 1° nome: '))
name2 = str(input('Digite o 2° nome: '))
name3 = str(input('Digite o 3° nome: '))
name4 = str(input('Digite o 4° nome: '))
nameList = [name1, name2, name3, name4]
shuffle(nameList)
print(f'Ordem de apresentação: \n1º {nameList[0]} \n2º {nameList[1]} \n3º {nameList[2]} \n4º { nameList[3]}')