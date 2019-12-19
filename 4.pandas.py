# import pandas as pd 
import json

# data = pd.read_json('scenic_spot_C_f.json')
#print(data)ensure_ascii=False

with open('scenic_spot_C_f.json',encoding ='utf-8-sig') as f:
    data = json.load(f)
    print(data)
    
    
# a= data ["XML_Head"]["Infos"]["Info"]
    
#     # data = data
# for aa in a:
#     #     print(aa["XML_Head"])
#     b = aa['Region']
#     c = aa['Name']
#             #   print(aa["Name"])
    # print(f'Region: {b}, NAME: {c}')
    

