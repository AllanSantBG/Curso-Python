from pack import string
from pack import arquivos
from colorama import Fore

def menu(opcao1, opcao2, opcao3):
    string.titulo(f'{"MENU":^40}')
    print(Fore.CYAN + f'| 1 |' + Fore.RESET, opcao1)
    print(Fore.CYAN + f'| 2 |' + Fore.RESET, opcao2)
    print(Fore.CYAN + f'| 3 |' + Fore.RESET, opcao3)
    string.linhas()
def opcoes():
    try:
        opcao = int(input(Fore.BLUE + 'Opção: ' + Fore.RESET))
        string.linhas()
        if opcao == 1:
            string.titulo(f'{"CADASTRADOS":^40}')
            print(Fore.YELLOW)
            arquivos.ler()
            print(Fore.RESET)
        elif opcao == 2:
            string.titulo(f'{"NOVO CADASTRO":^40}')
            while True:
                try:
                    nome = str(input(Fore.BLUE + 'Nome: ' + Fore.RESET)).strip().title()
                    idade = int(input(Fore.BLUE + 'Idade: ' + Fore.RESET))
                except:
                    string.msgErro('ERRO! Valor inválido, tente novamente')
                else:
                    break
            arquivos.escrever(nome, idade)
            print(Fore.GREEN + f'Novo registro adicionado: {nome} {idade} Anos' + Fore.RESET)
        elif opcao == 3:
            return True
        else:
            print(string.msgErro('ERRO! Valor inválido, tente novamente'))
    except KeyboardInterrupt:
        return True
    except:
        print(string.msgErro('ERRO! Valor inválido, tente novamente'))