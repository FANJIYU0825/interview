"""
旅遊景點 測試
1. 搜尋想去地點
2.  跑出各縣市的旅遊景點統計
"""
import pandas as pd
import requests
#########################################
# 資料處理 類別定義
#########################################
class DataProc():
    mdata = pd.DataFrame()
    data1 = pd.DataFrame()
    # def __init__(self):
        

    def download_data(self):
        url = 'https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json'
        file = requests.get(url)
        
        self.mdata =pd.read_json(file) 
        self.data1 = self.mdata
        self.data1 = self.data1.loc[:('Name'),('Region'),]
        

    




#導入JSON
# a= re.json()

# data = a ["XML_Head"]["Infos"]["Info"]
# for dJson in data:
#     a = dJson['Name']
#     print(a)
# 轉出 JSON