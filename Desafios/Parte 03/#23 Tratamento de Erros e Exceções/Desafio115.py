from pack import arquivos
from pack import funcional
from colorama import Fore

arquivos.criar()
while True:
    funcional.menu('Visualizar Pessoas Cadastradas', 'Cadastrar Outra Pessoa', 'Finalizar Sistema')
    v = funcional.opcoes()
    if v:
        break
print(Fore.YELLOW + 'Programa finalizado, volte sempre!' + Fore.RESET)