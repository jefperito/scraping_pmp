# -*- coding: utf-8 -*-

import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner

atividades_legislativas = [
    #'Emendas-Modificativas',
    #'Indicacoes',
    #'Mocoes',
    #'Projeto-de-Decreto-Legislativo',
    'Projeto-de-Lei',
    #'Projeto-de-Lei-Complementar',
    #'Projeto-de-Resolucao',
    #'Proposta-de-Emenda-a-Lei-organica',
    #'Requerimento',
    #'Substitutivos-Globais'
]

vereadores = [
    {'8': 'André Carlos Xavier'},
    {'3': 'Edemir Niehues'},
    {'10': 'Elton Esomérico de Quadros'},
    {'5': 'Fábio Coelho'},
    {'15': 'Jean Henrique Dias Carneiro'},
    {'18': 'João Carlos Amândio'},
    {'12': 'Joel Filipe Gaspar'},
    {'158': 'Laurita Maria da Silva dos Santos'},
    {'13': 'Luciano Pereira'},
    {'166': 'Marcelo Prim'},
    {'17': 'Marcos Roberto de Melo'},
    {'2': 'Maria Rosângela Pratis'},
    {'14': 'Maurício Roque da Silva'},
    {'1': 'Nelson Martins Filho'},
    {'4': 'Nirdo Artur Luz'},
    {'6': 'Otávio Marcelino Martins Filho'},
    {'9': 'Rosinei de Souza Horácio'}
]

url_template = 'https://www.cmp.sc.gov.br/camara/proposicao/{}/{}/1/{}'
ANO_DE_ANALISE = 2017
url_atual = ''

def main():
    print('Rodando app... \n')

    runner = CrawlerRunner(get_project_settings())

    for atividade in atividades_legislativas:
        for vereador in vereadores:
            identidade_vereador = list(vereador.keys())[0]
            url_atual = url_template.format(atividade, ANO_DE_ANALISE, identidade_vereador)

            runner.crawl(
                'prefeitura', 
                url = url_atual, 
                ano = ANO_DE_ANALISE, 
                vereador = vereador[identidade_vereador],
                atividade = atividade
            )
    
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()


if __name__ == '__main__':
    main()