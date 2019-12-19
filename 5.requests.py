import csv
import json
import requests
import pandas as pd
url = 'https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json'
re = requests.get(url) 
#導入JSON
a= re.json()

data = a ["XML_Head"]["Infos"]["Info"]
for dJson in data:
    a = dJson['Name'] 
    b = dJson['Travellinginfo']
    # c = (f'name:{a} info:{b}') /format/
    
    # print(a)
    
    
# 轉出 JSON
# with open('data.json','w',encoding='UTF-8') as jsFile:
#     electoin =json.dump(a,jsFile,ensure_ascii=False)
