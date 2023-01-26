from colorama import Fore

def linhas():
    print(Fore.BLACK + '-' * 40 + Fore.RESET)
def titulo(txt):
    linhas()
    print(Fore.BLUE + txt + Fore.RESET)
    linhas()
def msgErro(txt):
    print(Fore.RED + txt + Fore.RESET)