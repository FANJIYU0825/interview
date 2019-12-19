
"""
臺中市政府公有零售市場每日蔬果價格表

功能定義：
1. 列出蔬果[青蔥 青江白菜 香蕉] 在 市場名稱[建國市場] 2019年價格走勢
2. 列出各個蔬果每月平均價格趨勢
3. 市場別
"""

import pandas as pd
import requests
import os
import csv
import matplotlib.pyplot as plt

MARKET_1 = '建國市場'
MARKET_2 = '合作市場'
MARKET_3 = '清水第一市場'

#########################################
# 資料處理 類別定義
#########################################
class DataProc():
    mdata = pd.DataFrame()
    data1 = pd.DataFrame()

    #def __init__(self):

    # 下載 Open Data
    def download_data(self):
        url = 'https://datacenter.taichung.gov.tw/swagger/OpenData/8170ee88-7d37-4432-82f4-c314a895b5e7'
        #data = pd.read_json(river_json)
        #df = pd.read_json('river_data.json')
        #self.mdata = pd.read_csv('公有零售市場每日蔬果價格108.csv')
        self.mdata = pd.read_json(requests.get(url, verify=False).text)

    def filter_data(self):
        global MARKET_1, MARKET_2, MARKET_3
        
        self.data1 = self.mdata
        
        self.data1 = self.data1.loc[:, ('訪價日期', '市場名稱', '青蔥', '青江白菜', '香蕉')]

        mask = (self.data1['市場名稱'] == MARKET_1) 
        #        (self.data1['市場名稱'] == MARKET_2) |
        #        (self.data1['市場名稱'] == MARKET_3)
        self.data1 = self.data1.loc[mask]

        data_len = len(self.data1['訪價日期'])
        
        # 轉換日期格式: 31/12/2019 => 2019/12/31
        for p in range(data_len):
            a = self.data1.iloc[p, 0].split('/')
            self.data1.iloc[p, 0] = a[2] + '/' + a[1] + '/' + a[0]

            #print(self.data1[p, 0])

        self.data1 = self.data1.loc[self.data1['訪價日期'] >= '2019/01/01']

    def save_data1(self, filename):
        self.data1.to_csv(filename)



#########################################
# 應用程式 類別定義
#########################################
class Application():
    def __init__(self):
        self.dp = DataProc()

    def run(self):
        while True:
            self.menu()
            choice = input('請輸入您的選擇：')
            print()

            if choice == '1':
                self.dp.download_data()
                self.dp.filter_data()

                input('下載資料完成，按任意鍵返回主選單。')
            elif choice == '2':
                print(self.dp.data1)

                input('按任意鍵返回主選單。')
            elif choice == '3':
                self.dp.save_data1('data1.csv')

                input('CSV儲存完成，按任意鍵返回主選單。')
            elif choice == '4':
                self.draw_chart()

                input('按任意鍵返回主選單。')
            else:
                break

    def menu(self):
        os.system('cls')    # windows
        os.system('clear')  # macos
        print('臺中市政府公有零售市場每日蔬果價格表')
        print('------------------------------')
        print('1. 下載『每日蔬果價格表』資料')
        print('2. 顯示 2019年建國市場每日價格')
        print('3. 儲存為CSV檔')
        print('4. 2019年建國市場價格走勢圖')
        print('0. 結束程式')
        print('------------------------------')

    def draw_chart(self):
        ax = plt.gca()

        #plt.rcParams['font.sans-serif'] = ['SimHei']
        
        app.dp.data1.plot(kind='line',x='訪價日期',y='青蔥', color='blue', ax=ax)
        app.dp.data1.plot(kind='line',x='訪價日期',y='青江白菜', color='red',ax=ax)
        app.dp.data1.plot(kind='line',x='訪價日期',y='香蕉', color='green',ax=ax)

        #plt.legend() #要使用label要加這行
        plt.title("Fruit price of market")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.show()




app = Application()
app.run()

"""
測試程式
app.dp.download_data()
app.dp.filter_data()
app.draw_chart()
"""