from htmlsnippet import urlSnippet
import pandas as pd
import os
import requests
from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup
print('● Libs imported')


results = []
digimonsDict = {
    'name': {
        'cover': 'url',
        'level': 'level',
        'type': 'type',
        'atrribute': 'atrribute',
        'move': 'move',
        'description': 'description'
    }
}


def ScrappingSnippet():

    bs = BeautifulSoup(urlSnippet, 'html.parser')
    for a in bs.find_all('a', attrs={"class": "p-reflist__wrap"}, href=True):
        results.append(a['href'].replace(
            "./", "https://digimon.net/reference/"))

    ScrappingEachOne()


def ScrappingEachOne():

    for link in results:
        print('● Soap scrapping ...')
        url = link
        content = urlopen(url)
        bs = BeautifulSoup(content, 'html.parser')

        def errPrevent(var):
            if var == "":
                var = "default"
                print(f'No text inside, var value changed to {var}')

        dName = bs.find("div", attrs={"class": "c-titleSet__sub"}).text
        errPrevent(dName)
        dCover = bs.find("li", attrs={"class": "p-ref__picitem"}
                         ).findChild()['src'].replace("..", "https://digimon.net")
        errPrevent(dCover)
        dLevel = bs.select('dd')[0].get_text()
        errPrevent(dLevel)
        dType = bs.select('dd')[1].get_text()
        errPrevent(dType)
        dAttr = bs.select('dd')[2].get_text()
        errPrevent(dAttr)
        dMove = bs.select('dd')[3].get_text()
        errPrevent(dMove)
        dDesc = bs.find('section', {"class": "p-ref__profile u-mgn"}).text
        errPrevent(dDesc)

        print(f'- {dName} scraped!')

        if os.path.isdir('images') == False:
            print('● Creating new path to storage images')
            os.mkdir("./images")

        print(f'- Downloading {dName} images')

        if os.path.isfile(f'./images/{dName}.png') == False:
            img_data = requests.get(dCover).content
            with open(f'./images/{dName}.png', 'wb') as handler:
                handler.write(img_data)
            print('- Image downloaded')
        else:
            print(f"- {dName} is already downloaded, skiping.")

        name = dName
        digimonsDict[name] = {'cover': dCover, 'level': dLevel, 'type': dType,
                              'attribute': dAttr, 'move': dMove, 'description': dDesc}


def csvMaker():
    df = pd.DataFrame.from_dict([digimonsDict])
    df.to_json('digimonData.json')
    print('● Exported to json')

# ScrappingSnippet()
# print('Finished!')
# csvMaker()
