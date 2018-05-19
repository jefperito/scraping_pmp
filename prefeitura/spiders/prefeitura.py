# -*- coding: utf-8 -*-
import scrapy
import re

class PrefeituraSpider(scrapy.Spider):
    name = 'prefeitura'
    allowed_domains = ['www.cmp.sc.gov.br']

    custom_settings = {
        'CONCURRENT_ITEMS': 1,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1
    }

    def __init__(self, category='', **kwargs):
        super().__init__(**kwargs) 
        self.start_urls = [self.url]
        self.ANO = self.ano


    def parse(self, response):
        projeto = response.xpath('//*[@id="main_content"]/article[@class="main_article"]/a[@href="{}/0"]'.format(self.url))
        dados_ano = projeto.xpath('.//text()').extract()

        if len(dados_ano) > 1:
            quantidade = dados_ano[1].strip()

            elementos = projeto.xpath('./strong//text()').extract()

            if (len(elementos) > 0):
                for elemento in elementos:
                    ano = int(elemento)

                    if ano == self.ANO:
                        quantidade_atividade = int(re.search('\[(.*)\]', quantidade).group(1))
                        print('##########')
                        print('Vereador: ' + self.vereador)
                        print('Atividade: {}, quantidade de projetos: {}'.format(self.atividade, quantidade_atividade))
                        print('##########')
                        print()

