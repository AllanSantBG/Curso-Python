frase = str(input('Digite algo: ').strip().upper())
vezesA = frase.count('A')
primeiroA = frase.find('A') + 1
ultimoA = frase.rfind('A') + 1
print(f'A letra "A" aparece {vezesA} vezes')
print(f'A letra "A" aparece na {primeiroA}ª posição pela primeira vez')
print(f'A letra "A" aparece na {ultimoA}ª posição pela ultima vez')