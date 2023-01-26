import urllib.request

def conectar(url):
    if url[:5] == 'https':
        url = url.replace('s','')
    try:
        urllib.request.urlopen(url) #Python 3.x
        print('\033[7;30;42m' + f'O site {url} está acessivel' + '\033[m')
    except:
        print('\033[7;30;41m' + f'O site {url} não está acessivel' + '\033[m')


conectar('https://www.pudim.com.br')