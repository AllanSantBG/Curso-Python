def criar():
    try:
        open('dados.txt', 'x')
        print('O arquivo dados.txt foi criado com sucesso')
    except:
        return
def ler():
    print(open('dados.txt', 'r').read())
def escrever(valor1, valor2):
    arquivo = open('dados.txt', 'a')
    arquivo.write(f'\n{valor1:<30}{valor2} anos')