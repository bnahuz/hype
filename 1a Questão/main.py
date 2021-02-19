from urllib.request import urlopen
from models.indices import Ipca
import json, peewee

if __name__ == '__main__':

    try:
        Ipca.create_table()
    except peewee.OperationalError:
        print ('Tabela IPCA ja existe!')


def save_json(url, save = True):
    data = urlopen(url)
    text = json.loads(data.read())

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(text[0], json_file, ensure_ascii= False, indent=4)

url = "https://servicodados.ibge.gov.br/api/v3/agregados/1420/periodos/201201%7C201202%7C201203%7C201204%7C201205%7C201206%7C201207%7C201208%7C201209%7C201210%7C201211%7C201212%7C201301%7C201302%7C201303%7C201304%7C201305%7C201306%7C201307%7C201308%7C201309%7C201310%7C201311%7C201312%7C201401%7C201402%7C201403%7C201404%7C201405%7C201406%7C201407%7C201408%7C201409%7C201410%7C201411%7C201412%7C201501%7C201502%7C201503%7C201504%7C201505%7C201506%7C201507%7C201508%7C201509%7C201510%7C201511%7C201512%7C201601%7C201602%7C201603%7C201604%7C201605%7C201606%7C201607%7C201608%7C201609%7C201610%7C201611%7C201612%7C201701%7C201702%7C201703%7C201704%7C201705%7C201706%7C201707%7C201708%7C201709%7C201710%7C201711%7C201712%7C201801%7C201802%7C201803%7C201804%7C201805%7C201806%7C201807%7C201808%7C201809%7C201810%7C201811%7C201812%7C201901%7C201902%7C201903%7C201904%7C201905%7C201906%7C201907%7C201908%7C201909%7C201910%7C201911%7C201912/variaveis/306?localidades=N1%5Ball%5D&classificacao=315%5B7169%5D"

data = {
                            "201201": "0.48",
                            "201202": "0.48",
                            "201203": "0.19",
                            "201204": "0.63",
                            "201205": "0.39",
                            "201206": "0.15",
                            "201207": "0.50",
                            "201208": "0.45",
                            "201209": "0.62",
                            "201210": "0.57",
                            "201211": "0.51",
                            "201212": "0.73",
                            "201301": "0.78",
                            "201302": "0.61",
                            "201303": "0.42",
                            "201304": "0.51",
                            "201305": "0.40",
                            "201306": "0.35",
                            "201307": "0.13",
                            "201308": "0.29",
                            "201309": "0.40",
                            "201310": "0.55",
                            "201311": "0.46",
                            "201312": "0.87",
                            "201401": "0.46",
                            "201402": "0.71",
                            "201403": "0.87",
                            "201404": "0.64",
                            "201405": "0.50",
                            "201406": "0.51",
                            "201407": "0.10",
                            "201408": "0.29",
                            "201409": "0.60",
                            "201410": "0.38",
                            "201411": "0.44",
                            "201412": "0.73",
                            "201501": "1.15",
                            "201502": "1.22",
                            "201503": "1.25",
                            "201504": "0.69",
                            "201505": "0.76",
                            "201506": "0.88",
                            "201507": "0.72",
                            "201508": "0.29",
                            "201509": "0.59",
                            "201510": "0.79",
                            "201511": "0.95",
                            "201512": "0.91",
                            "201601": "1.16",
                            "201602": "0.90",
                            "201603": "0.37",
                            "201604": "0.58",
                            "201605": "0.81",
                            "201606": "0.46",
                            "201607": "0.61",
                            "201608": "0.51",
                            "201609": "0.14",
                            "201610": "0.24",
                            "201611": "0.10",
                            "201612": "0.25",
                            "201701": "0.29",
                            "201702": "0.34",
                            "201703": "0.20",
                            "201704": "0.11",
                            "201705": "0.37",
                            "201706": "-0.12",
                            "201707": "0.30",
                            "201708": "0.23",
                            "201709": "0.20",
                            "201710": "0.40",
                            "201711": "0.21",
                            "201712": "0.40",
                            "201801": "0.20",
                            "201802": "0.33",
                            "201803": "0.03",
                            "201804": "0.19",
                            "201805": "0.42",
                            "201806": "1.35",
                            "201807": "0.41",
                            "201808": "-0.03",
                            "201809": "0.51",
                            "201810": "0.42",
                            "201811": "-0.27",
                            "201812": "0.12",
                            "201901": "0.22",
                            "201902": "0.44",
                            "201903": "0.67",
                            "201904": "0.52",
                            "201905": "0.19",
                            "201906": "0.10",
                            "201907": "0.29",
                            "201908": "0.19",
                            "201909": "-0.01",
                            "201910": "0.07",
                            "201911": "0.44",
                            "201912": "1.09"
                    }

for anomes in data:
    book = Ipca.create(anomes = anomes, indice = data.get(anomes))
    print(anomes + "=" +  data.get(anomes))
