import requests
import json


def encode_cd1251(string):
    return str(string.encode('windows-1251')).replace("\\x", '%').replace(' ', '+').replace("'", '').upper()[1:]


def scrapPrice(enter, sites=["chitai-gorod.ru", "book24.ru", "labirint.ru"]):
    enter = enter.replace(' ', '+')

    headers = {
        'User-Agent': 'ReqBin Python Client/1.0'
    }

    # Scraping bookradar
    resp = requests.get(f'https://bookradar.ru/api/search?q={enter}&page=1', headers=headers)
    pageCount = resp.json()["pageCount"]
    for i in range(1, pageCount + 1):
        with open(f'scrap/cache/bookradar_{i}.json', 'w', encoding='UTF-8') as file:
            json.dump(
                json.loads(requests.get(f'https://bookradar.ru/api/search?q={enter}&page={i}', headers=headers).text),
                file,
                indent=4,
                ensure_ascii=False)

    unreadyScrap = []
    for i in range(1, pageCount + 1):
        with open(f'scrap/cache/bookradar_{i}.json', 'r', encoding='UTF-8') as file:
            text = json.load(file)
            for j in text["offers"]:
                if j['site'] in sites:
                    if j not in unreadyScrap:
                        unreadyScrap.append(j)

    for i in sites:
        arr = []
        with open(f'scrap/cache/{i}_offers.json', 'w', encoding='UTF-8') as file:
            for j in unreadyScrap:
                if j['site'] == i:
                    arr.append(j)
            json.dump(arr, file, indent=4, ensure_ascii=False)

    finn = []

    for i in sites:
        price = []
        with open(f'scrap/cache/{i}_Price.json', 'w', encoding='UTF-8') as fprice:
            with open(f'scrap/cache/{i}_offers.json', 'r', encoding='UTF-8') as foffers:
                text = json.load(foffers)
                for j in text:
                    price.append(j['price'])
            json.dump(price, fprice, indent=4, ensure_ascii=False)
    for i in sites:
        with open(f'scrap/cache/{i}_offers.json', 'r', encoding='UTF-8') as foffers:
            with open(f'scrap/cache/{i}_Price.json', 'r', encoding='UTF-8') as fprice:
                offers = json.load(foffers)
                price = json.load(fprice)
                for j in offers:
                    if j['price'] == min(price):
                        finn.append(j)

    print('OK')

    return finn
