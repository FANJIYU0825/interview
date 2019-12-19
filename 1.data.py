import csv
import json
import requests
url = 'https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json'
re = requests.get(url) 
#讀取JSON
def read_json(url):
    rejson = re.json()
    return rejson


#儲存JSON file
def save_json_file(rejson):
    with open('data.json','w',encoding='UTF-8') as jsFile:
        electoin =json.dump(rejson, jsFile, ensure_ascii=False, indent=4)
    

        
#資料型態
def data_type(re):
    datatype = re.headers['Content-Type']
    # print (datatype)
    return datatype

def dic_data(rejson):
        data02 =  rejson["XML_Head"]["Infos"]["Info"]
        for aa in data02:
            b = str(aa['Region'])
            c = str(aa['Orgclass'])
            print(f'Region: {b}, Orgclass: {c}')
            return data02


# key word[1]:Region, "Orgclass"
#key word [2]:"Orgclass","Name"

#主網站

read_json(url)

save_json_file(read_json)
