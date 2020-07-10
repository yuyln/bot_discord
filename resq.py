"""
filmes = []
while True:
    filme = input('nome do filme: ')
    if filme != 'sair':
        filmes.append(Filme(filme))
    else:
        break

ratings = [filme.rotten() for filme in filmes]
for filme in filmes:
    print(f'{filme.tit} {filme.rotten()}')
"""


import googlesearch as gl
import requests as rq
from bs4 import BeautifulSoup as BS


class Filme:
    def __init__(self, titulo):
        self.titulo = titulo

    def rotten(self):
        nome = self.titulo
        filme = list(gl.search(f'{nome} rotten tomatoes', stop=1))[0].split('/')[-1]
        url = rq.get(f'https://www.rottentomatoes.com/m/{filme}')
        soup = BS(url.text, 'html.parser')
        soup1 = soup.find_all('span', {'class': 'mop-ratings-wrap__percentage'})
        rate1 = f'\N{TOMATO} {soup1[0].text.strip()}'
        rate2 = f'\N{POPCORN} {soup1[1].text.strip()}'
        return f'{rate1} {rate2}'

    @property
    def tit(self):
        return self.titulo.title()

    @property
    def link(self):
        return list(gl.search(f'{self.titulo} rotten tomatoes', stop=3))[0]