from bs4 import BeautifulSoup
from collections import defaultdict
import codecs
from glob import glob


arquivos = glob('*.ht*')
info_produto = list()
dados = defaultdict(list)

dados = defaultdict(list)
for arq in arquivos:
    if arq.endswith('.html'):
        with codecs.open(arq, encoding='utf-8') as fp:
            submarino = BeautifulSoup(fp, 'lxml')

        titulo_Html = submarino.title.string

        # acha as informacoes html na árvore
        informacoes_Html = submarino.select('tbody tr td span')

        # transforma a lista em uma string
        informacoes_Html = ''.join([str(i) for i in informacoes_Html])

        # converte para objeto beautifulSoup
        informacoes_Html = BeautifulSoup(informacoes_Html, 'lxml')
        for texto in informacoes_Html.stripped_strings:
            info_produto.append(texto)
        dados[titulo_Html].extend(info_produto)
print(dados)
