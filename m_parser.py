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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.91 (Edition Yx GX)',
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
        return r.text

    def parse_block(self, item):
        url_block = item.select_one('a.link-link-MbQDP.link-design-default-_nSbv.title-root-j7cja.iva-item-title-_qCwt.title-listRedesign-XHq38.title-root_maxHeight-SXHes')
        href = url_block.get('href')
        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        title_block = item.select_one('h3.title-root-j7cja.iva-item-title-_qCwt.title-listRedesign-XHq38.title-root_maxHeight-SXHes.text-text-LurtD.text-size-s-BxGpL.text-bold-SinUO')
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

    def get_blocks(self, radius, sort, city, page, user, price):
        text = self.get_page(radius, sort, city, page, user, price)
        soup = bs4.BeautifulSoup(text, 'lxml')

        all_objects = []
        block = ""

        container = soup.select('div.iva-item-root-Nj_hb.photo-slider-slider-_PvpN.iva-item-list-H_dpX.iva-item-redesign-nV4C4.iva-item-responsive-gIKjW.items-item-My3ih.items-listItem-Gd1jN.js-catalog-item-enum')
        for item in container:
            block = self.parse_block(item=item)
            block = list(block)
            all_objects.append(block)
            print(block)
        return all_objects
