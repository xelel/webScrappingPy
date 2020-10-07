from bs4 import BeautifulSoup
from collections import defaultdict
import codecs
from glob import glob


arquivos = glob('*.ht*')
dados = defaultdict(list)


for arq in arquivos:
    if arq.endswith('.htm'):
        with codecs.open(arq, encoding='utf-8') as m:
            magazine = BeautifulSoup(m, 'lxml')
        titulo = magazine.title.string
        # print(titulo)

        # extrai as informações tecnicas na árvore
        info_Produto_Html = magazine.find_all(
            'td', class_=['description__information-left', 'description__information-right'])

        # transforma a lista em uma string
        texto = ''.join([str(i) for i in info_Produto_Html])

        # converte a string para objeto BeautifulSoup()
        texto = BeautifulSoup(texto, 'lxml')

        # coloca os valores de texto em uma lista

        for i in texto.stripped_strings:
            dados[titulo].append(i)

for title, info in dados.items():
    print('-='*30)
    print(title)
    print('-='*30)
    for i in info:
        print(i)
