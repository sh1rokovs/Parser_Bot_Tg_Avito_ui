from collections import namedtuple

import bs4
import requests

InnerBlock = namedtuple('Block', 'title,price,currency,date,url')


class Block(InnerBlock):

    def __str__(self):
        return f'{self.title}\t{self.price} {self.currency}\t{self.date}\t{self.url}'


class AvitoParser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.0.1996 Yowser/2.5 Safari/537.36",
            'Accept-Language': 'ru',
        }

    def get_page(self, radius, sort, city, page, user, price):
        params = {
            'radius': radius,
            's': sort,
        }
        if sort == 0:
            params.pop('s')
        if page and page > 1:
            params['p'] = page
        url = f'https://www.avito.ru/{city}/avtomobili'
        if price > 0:
            url += "/do-1-mln-rubley-ASgCAgECAUXGmgwXeyJmcm9tIjowLCJ0byI6MTAwMDAwMH0"
        r = self.session.get(url, params=params)
        #print(r.text)
        return r.text

    def parse_block(self, item):
        url_block = item.select_one(
            'a.link-link-MbQDP.link-design-default-_nSbv.title-root-j7cja.iva-item-title-_qCwt.title-listRedesign-XHq38.title-root_maxHeight-SXHes')
        href = url_block.get('href')
        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        title_block = item.select_one(
            'h3.title-root-j7cja.iva-item-title-_qCwt.title-listRedesign-XHq38.title-root_maxHeight-SXHes.text-text-LurtD.text-size-s-BxGpL.text-bold-SinUO')
        title = title_block.string.strip()

        price_block = item.select_one('span.price-root-_Uey3.price-listRedesign-UZ7CL')
        price_block = price_block.get_text('\n')
        price_block = list(filter(None, map(lambda i: i.strip(), price_block.split('\n'))))
        if len(price_block) == 2:
            price, currency = price_block
        else:
            price, currency = None, None
            print('Что-то пошло не так при поиске цены:', price_block)

        date_block = item.select_one('div.date-text-VwmJG.text-text-LurtD.text-size-s-BxGpL.text-color-noaccent-P1Rfs')
        date = date_block.string.strip()

        return Block(
            url=url,
            title=title,
            price=price,
            currency=currency,
            date=date,
        )

    def get_extra(self, url):
        if len(url) != 0:
            #r = self.session.get(url)
            #r = r.text
            #soup = bs4.BeautifulSoup(r, 'lxml')
            #container = soup.select('div.styles-chart-2sQbJ')
            block = ""
            block1 = ""
            #for el in container:
                #block = el.select_one('h4.styles-heading-3Nr7X.heading-space-h4-2H37G.text-text-1PdBw.text-size-l-2gTpu.text-bold-3R9dt')
                #block1 = el.select_one('div.styles-subtitle-container-v7qnO')
               # block1 = block1.select_one('div.text-text-1PdBw.text-size-m-4mxHN')
            return 0

    def get_blocks(self, radius, sort, city, page, user, price):
        text = self.get_page(radius, sort, city, page, user, price)
        soup = bs4.BeautifulSoup(text, 'lxml')

        all_objects = []
        block = ""
        #kraf = 'div.iva-item-root-Nj_hb.photo-slider-slider-_PvpN.iva-item-list-H_dpX.iva-item-redesign-nV4C4.iva-item-responsive-gIKjW.items-item-My3ih.items-listItem-Gd1jN.js-catalog-item-enum'
        #kraf1 = 'div.iva-item-root-Nj_hb.photo-slider-slider-_PvpN.iva-item-list-H_dpX.iva-item-redesign-nV4C4.iva-item-responsive-gIKjW.items-item-My3ih.items-listItem-Gd1jN.js-catalog-item-enum'
        #if kraf == kraf1:
            #print("ok")
        container = soup.select(
            'div.iva-item-root-Nj_hb.photo-slider-slider-_PvpN.iva-item-list-H_dpX.iva-item-redesign-nV4C4.iva-item-responsive-gIKjW.items-item-My3ih.items-listItem-Gd1jN.js-catalog-item-enum')
        for item in container:
            block = self.parse_block(item=item)
            block = list(block)
            print(block)
            all_objects.append(block)
        if len(all_objects) == 0:
            return 0
        else:
            return all_objects


#p = AvitoParser()
#p.get_blocks(200, 104, 'nizhniy_novgorod', 1, 0, 1)
# 109.184.177.90
# 109.184.180.192
