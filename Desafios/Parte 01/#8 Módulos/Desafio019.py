import random
name1 = str(input('Digite o 1° nome: '))
name2 = str(input('Digite o 2° nome: '))
name3 = str(input('Digite o 3° nome: '))
name4 = str(input('Digite o 4° nome: '))
list = [name1, name2, name3, name4]
print(f'O nome sorteado foi {random.choice(list)}')