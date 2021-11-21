import json

from sqliter import Sqliter as sq
from a_parser import AvitoParser as avito


def write_f(data):
    with open("keys.json", "w") as w_file:
        json.dump(data, w_file)


def read_f():
    with open("keys.json", "r") as r_file:
        data = json.load(r_file)
    return data


# ----------------- Редактируем JSON -------------------------
def check_json(user_id, user_name):
    data = read_f()
    user_id = str(user_id)
    test = data.get(user_id)
    if not test:  # если пользователя нет в json
        data.setdefault(user_id, {
            "name": user_name,
            "keys": {}
        })
        write_f(data)


def clear_json():
    data = read_f()
    for el in data.keys():
        new_item = list(data[el]["keys"].keys())
        for elem in new_item:
            data[el]["keys"].pop(elem)
    write_f(data)


def new_items(radius, sort, city, page, user, price):
    p = avito()
    test = p.get_blocks(radius, sort, city, page, user, price)
    new_list = []
    print(f'test:{test}')
    if test == 0:
        print(f'Проблема!!!')
        return []
    else:
        for el in test:
            print(el)
            el[1] = el[1].replace(u'\xa0', u' ')
            if el[3] == "Несколько секунд назад":
                new_list.append(el)
        print(f'new_items:{new_list}')
        return new_list


def write_on_json(users_id, auto_list):
    data = read_f()
    for el in users_id:
        for elem in auto_list:
            if not str(elem) in data[el]["keys"].keys():
                data[el]["keys"].setdefault(str(elem), 0)
    print(f'write_f:{data}')
    write_f(data)


#


def read_from_json(users_id):
    data = read_f()
    new_data = []
    for elem in data['798469096']["keys"].keys():
        if data['798469096']["keys"][elem] == 0:
            data['798469096']["keys"][elem] = 1
            elem = elem.replace("'", "")
            elem = elem.replace("]", "")
            elem = elem.replace("[", "")
            elem = elem.split(",")
            new_data.append(elem)
    print(f'read_f:{new_data}')
    write_f(data)
    return new_data


def exit_on(users_id, user_name, radius, sort, city, page, user, price):
    for el, elem in zip(users_id, user_name):
        check_json(el, elem)
    write_on_json(users_id, new_items(radius, sort, city, page, user, price))
    return read_from_json(users_id)


#clear_json()
#
"""[['Chevrolet Rezzo, 2007', '175\xa0000', '₽', 'Несколько секунд назад', 'https://www.avito.ru/nikologory/avtomobili/chevrolet_rezzo_2007_2122964050']
['LADA Largus, 2021', '810\xa0000', '₽', 'Несколько секунд назад', 'https://www.avito.ru/vologda/avtomobili/lada_largus_2021_2227240077']
['ВАЗ 2107, 2010', '240\xa0000', '₽', 'Несколько секунд назад', 'https://www.avito.ru/arzamas/avtomobili/vaz_2107_2010_2262339390']
['Ford Kuga, 2012', '980\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/kstovo/avtomobili/ford_kuga_2012_2243168808']
['Nissan X-Trail, 2008', '800\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/nizhniy_novgorod/avtomobili/nissan_x-trail_2008_1940632101']
['ВАЗ (LADA) Vesta Cross, 2019', '935\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/krasnodar/avtomobili/vaz_lada_vesta_cross_2019_2264348611']
['LADA Granta, 2013', '350\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/gorohovets/avtomobili/lada_granta_2013_2275684646']
['Peugeot 308, 2009', '355\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/moskva/avtomobili/peugeot_308_2009_2151466637']
['Chevrolet Cruze, 2013', '619\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/moskva/avtomobili/chevrolet_cruze_2013_2278909720']
['Honda Civic, 2010', '609\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/moskva/avtomobili/honda_civic_2010_2278925854']
['Renault Sandero, 2011', '499\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/moskva/avtomobili/renault_sandero_2011_2278988815']
['Opel Zafira, 2008', '469\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/moskva/avtomobili/opel_zafira_2008_2279022753']
['Honda Civic, 2010', '577\xa0000', '₽', '1 минуту назад', 'https://www.avito.ru/moskva/avtomobili/honda_civic_2010_2279523305']
['Great Wall Hover H5, 2013', '698\xa0000', '₽', '2 минуты назад', 'https://www.avito.ru/vorsma/avtomobili/great_wall_hover_h5_2013_2274323516']
['Hyundai Santa Fe, 2010', '947\xa0000', '₽', '2 минуты назад', 'https://www.avito.ru/moskva/avtomobili/hyundai_santa_fe_2010_2247226958']
['Nissan Juke, 2013', '807\xa0000', '₽', '2 минуты назад', 'https://www.avito.ru/moskva/avtomobili/nissan_juke_2013_2215088843']
['Chevrolet Cruze, 2014', '587\xa0000', '₽', '2 минуты назад', 'https://www.avito.ru/moskva/avtomobili/chevrolet_cruze_2014_2279398657']
['FIAT Doblo, 2013', '610\xa0000', '₽', '3 минуты назад', 'https://www.avito.ru/nizhniy_novgorod/avtomobili/fiat_doblo_2013_2281677127']
['Hyundai Santa Fe, 2011', '977\xa0000', '₽', '3 минуты назад', 'https://www.avito.ru/moskva/avtomobili/hyundai_santa_fe_2011_2247242457']
['Volkswagen Tiguan, 2011', '995\xa0000', '₽', '3 минуты назад', 'https://www.avito.ru/moskva/avtomobili/volkswagen_tiguan_2011_2252386149']
['Ford Kuga, 2013', '949\xa0000', '₽', '4 минуты назад', 'https://www.avito.ru/moskva/avtomobili/ford_kuga_2013_2247217903']
['Volvo XC90, 2008', '985\xa0000', '₽', '4 минуты назад', 'https://www.avito.ru/moskva/avtomobili/volvo_xc90_2008_2247722160']
['Volkswagen Tiguan, 2013', '997\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/moskva/avtomobili/volkswagen_tiguan_2013_2124273542']
['Mazda 3, 2012', '765\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/ust-labinsk/avtomobili/mazda_3_2012_2213970006']
['Skoda Fabia, 2014', '515\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/moskva/avtomobili/skoda_fabia_2014_2220607812']
['Nissan X-Trail, 2011', '945\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/moskva/avtomobili/nissan_x-trail_2011_2251910509']
['Skoda Octavia, 2013', '775\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/moskva/avtomobili/skoda_octavia_2013_2252032025']
['Skoda Octavia, 2012', '575\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/moskva/avtomobili/skoda_octavia_2012_2252282041']
['ВАЗ (LADA) Vesta, 2021', '975\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/moskva/avtomobili/vaz_lada_vesta_2021_2252643709']
['Hyundai Tucson, 2009', '750\xa0000', '₽', '7 минут назад', 'https://www.avito.ru/arzamas/avtomobili/hyundai_tucson_2009_2284534755']
['Volkswagen Passat CC, 2010', '669\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/nizhniy_novgorod/avtomobili/volkswagen_passat_cc_2010_2268199743']
['Citroen C4, 2013', '679\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/sankt-peterburg/avtomobili/citroen_c4_2013_2264590572']
['Hyundai Solaris, 2016', '768\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/hyundai_solaris_2016_2227965226']
['Ford Focus, 2016', '968\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/ford_focus_2016_2228475207']
['Peugeot 206, 2008', '199\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/arzamas/avtomobili/peugeot_206_2008_2240180291']
['Opel Astra, 2013', '719\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/opel_astra_2013_2247518282']
['Toyota Corolla, 2011', '663\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/toyota_corolla_2011_2228037189']
['Ford Fusion, 2008', '424\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/ford_fusion_2008_2228433153']
['Nissan Qashqai, 2012', '700\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/nissan_qashqai_2012_2228653449']
['Hyundai Solaris, 2013', '482\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/hyundai_solaris_2013_2259885787']
['Kia Rio, 2015', '788\xa0000', '₽', '8 минут назад', 'https://www.avito.ru/moskva/avtomobili/kia_rio_2015_2260022039']
['ВАЗ (LADA) Kalina, 2016', '429\xa0900', '₽', '9 минут назад', 'https://www.avito.ru/samara/avtomobili/vaz_lada_kalina_2016_2246151245']
['Chevrolet Lacetti, 2009', '325\xa0000', '₽', '9 минут назад', 'https://www.avito.ru/arzamas/avtomobili/chevrolet_lacetti_2009_2272870861']
['LADA Vesta, 2020', '815\xa0000', '₽', '10 минут назад', 'https://www.avito.ru/arzamas/avtomobili/lada_vesta_2020_2272568320']
['Ford Focus, 2012', '679\xa0000', '₽', '10 минут назад', 'https://www.avito.ru/sankt-peterburg/avtomobili/ford_focus_2012_2296734563']
['Mitsubishi Pajero, 2007', '999\xa0000', '₽', '10 минут назад', 'https://www.avito.ru/moskva/avtomobili/mitsubishi_pajero_2007_2239531864']
['Opel Astra, 2008', '579\xa0000', '₽', '10 минут назад', 'https://www.avito.ru/moskva/avtomobili/opel_astra_2008_2271062919']
['Opel Astra, 2010', '475\xa0000', '₽', '10 минут назад', 'https://www.avito.ru/moskva/avtomobili/opel_astra_2010_2271759454']
['Renault Logan, 2006', '275\xa0000', '₽', '10 минут назад', 'https://www.avito.ru/nizhniy_novgorod/avtomobili/renault_logan_2006_2280344079']
['Mercedes-Benz C-класс, 2008', '753\xa0000', '₽', '11 минут назад', 'https://www.avito.ru/balashiha/avtomobili/mercedes-benz_c-klass_2008_2207408256']]"""
