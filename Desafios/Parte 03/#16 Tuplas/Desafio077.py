palavras = ('imagem', 'loja', 'internacional', 'resultado', 'potro',
            'sol', 'pomada', 'chefe', 'trombone', 'bolso')
for p in palavras:
    print(f'\nAs vogais da palavra {p.upper()}: ', end='')
    for i in range(0, len(p)):
        if p[i].lower() in 'aeiou':
            print(p[i], end=' ')