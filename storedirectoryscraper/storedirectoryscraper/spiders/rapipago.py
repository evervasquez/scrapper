import scrapy
from storedirectoryscraper.items import RucItem
import unicodedata


class RucSpider(scrapy.Spider):
    name = 'rapipago'
    allowed_domains = ["wmtechnology.org"]
    start_urls = ['http://www.wmtechnology.org/Consultar-RUC/index.jsp']
    response = {}
    ruc = None

    def __init__(self, ruc='', *args, **kwargs):
        super(RucSpider, self).__init__(*args, **kwargs)
        self.ruc = ruc

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response=response,
            formdata={'nruc': self.ruc},
            callback=self.after_post
        )

    def after_post(self, response):
        self.logger.info('Parse function called on %s', response.url)
        divs = response.css("div.list-group-item")
        count = 0
        for div in divs:
            title = div.css('div.col-sm-5').css("h4.list-group-item-heading::text").extract_first()
            result = div.css('div.col-sm-7').css("p.list-group-item-text::text").extract_first()
            if result is None:
                result = div.css('div.col-sm-7').css("h4.list-group-item-heading::text").extract_first()

            if result is None:
                result = div.css('div.col-sm-7::text').extract_first().strip()

            if count == 0:
                data = result.split('-')
                self.response[title[:-1].title()] = data[0]
                self.response["Nombre"] = data[1].strip()
            else:
                self.response[elimina_tildes(title[:-1].title())] = result
            count += 1

        ruc_item = RucItem()
        ruc_item['Nombre'] = self.response['Nombre']
        ruc_item['Provincia'] = self.response['Provincia']
        ruc_item['Condicion'] = self.response['Condicion']
        ruc_item['Ruc'] = self.response['Ruc']
        ruc_item['Departamento'] = self.response['Departamento']
        ruc_item['Domicilio'] = self.response['Domicilio Fiscal']
        ruc_item['Distrito'] = self.response['Distrito']
        ruc_item['Estado'] = self.response['Estado']
        ruc_item['Ubigeo'] = self.response['Ubigeo']

        yield ruc_item


def elimina_tildes(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))