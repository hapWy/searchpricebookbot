import requests
import json


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104"
}


# Scraping bookradar
def scrapBookradar(enter):
    enter = enter.replace(' ', '+')
    resp = requests.get(f'https://bookradar.ru/api/search?q={enter}&page=1', headers=headers)
    pageCount = resp.json()['pageCount']
    if pageCount > 30: 
        pageCount = 30
    for i in range(1, pageCount + 1):
        yield json.loads(requests.get(f'https://bookradar.ru/api/search?q={enter}&page={i}', headers=headers).text)


# Scraping FindBook
def scrapPrice(enter):
    cg = []
    lab = []
    bk24 = []

    sites = ["chitai-gorod.ru", "book24.ru", "labirint.ru"]
    for i in scrapBookradar(enter):
        for j in i["offers"]:
            if j['site'] in sites and j not in cg and j not in lab and j not in bk24:
                if j['site'] == "chitai-gorod.ru":
                    cg.append(j)
                if j['site'] == "book24.ru":
                    bk24.append(j)
                if j['site'] == 'labirint.ru':
                    lab.append(j)

    finn = []
    priceCg = [i['price'] for i in cg]
    finn = [i for i in cg if i['price'] == min(priceCg)]

    priceLab = [i['price'] for i in lab]
    finn += [i for i in lab if i['price'] == min(priceLab)]

    priceBk24 = [i['price'] for i in bk24]
    finn += [i for i in bk24 if i['price'] == min(priceBk24)]

    return finn
