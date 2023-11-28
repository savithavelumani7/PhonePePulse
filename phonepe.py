# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:49:09 2023

@author: ELCOT
"""

import os
import json
import pandas as pd
#aggregate_transaction

path1="C:/Users/ELCOT/GUVI/Python/DTM9/.spyder-py3/PhonePe/pulse/data/aggregated/transaction/country/india/state/"
agg_trans_list=os.listdir(path1)
# print(agg_trans_list)

columns={'States':[], 'Years':[], "Quarter":[], 'Transaction_Type': [], "Transaction_Count":[], "Transaction_Amount":[]}
for state in agg_trans_list:
    state_now=path1+state+'/'
    agg_years_list=os.listdir(state_now)
    # print(agg_years_list)
    
    
    for year in agg_years_list:
        year_now=state_now+year+'/'
        agg_files_list=os.listdir(year_now)
        # print(agg_files_list)
        
        for file in agg_files_list:
            file_now=year_now+file
            file_read=open(file_now,'r')
            
            A=json.load(file_read)
            for i in A['data']['transactionData']:
                name=i['name']
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                columns['Transaction_Type'].append(name)
                columns['Transaction_Count'].append(count)
                columns['Transaction_Amount'].append(amount)
                columns['States'].append(state)
                columns['Years'].append(year)
                columns['Quarter'].append(int(file.strip(".json")))
            
aggregate_transaction=pd.DataFrame(columns)


path2="C:/Users/ELCOT/GUVI/Python/DTM9/.spyder-py3/PhonePe/pulse/data/aggregated/user/country/india/state/"
agg_users_list=os.listdir(path2)
# print(agg_trans_list)

columns1={'States':[], 'Years':[], "Quarter":[], 'Brands': [], "Count":[], "Percentage":[]}
for state in agg_users_list:
    state_now=path2+state+'/'
    agg_years_list=os.listdir(state_now)
    # print(agg_years_list)
    
    
    for year in agg_years_list:
        year_now=state_now+year+'/'
        agg_files_list=os.listdir(year_now)
        # print(agg_files_list)
        
        for file in agg_files_list:
            file_now=year_now+file
            file_read=open(file_now,'r')
            
            B=json.load(file_read)
            try:
                for i in B['data']['usersByDevice']:
                    brand=i['brand']
                    count=i["count"]
                    percentage=i["percentage"]
                    columns1['Brands'].append(brand)
                    columns1['Count'].append(count)
                    columns1['Percentage'].append(percentage)
                    columns1['States'].append(state)
                    columns1['Years'].append(year)
                    columns1['Quarter'].append(int(file.strip(".json")))
            except:
                pass
aggregate_users=pd.DataFrame(columns1)


path3="C:/Users/ELCOT/GUVI/Python/DTM9/.spyder-py3/PhonePe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(path3)

columns3={'States':[], 'Years':[], "Quarter":[], 'Districts': [], "Transaction_Count":[], "Transaction_Amount":[]}

for state in map_trans_list:
    state_now=path3+state+'/'
    map_years_list=os.listdir(state_now)
    # print(map_years_list)
    
    for year in map_years_list:
        year_now=state_now+year+'/'
        map_files_list=os.listdir(year_now)
        # print(map_files_list)
        
        for file in map_files_list:
            file_now=year_now+file
            file_read=open(file_now,'r')
            
            C=json.load(file_read)
            try:
                for i in C['data']['hoverDataList']:
                    name=i['name']
                    count=i['metric'][0]['count']
                    amount=i['metric'][0]["amount"]
                    columns3['Districts'].append(name)
                    columns3['Transaction_Count'].append(count)
                    columns3['Transaction_Amount'].append(amount)
                    columns3['States'].append(state)
                    columns3['Years'].append(year)
                    columns3['Quarter'].append(int(file.strip(".json")))
            except:
                pass
map_transaction=pd.DataFrame(columns3)
    


path4="C:/Users/ELCOT/GUVI/Python/DTM9/.spyder-py3/PhonePe/pulse/data/map/user/hover/country/india/state/"
map_users_list=os.listdir(path4)

columns4={'States':[], 'Years':[], "Quarter":[], 'Districts': [], "Registered_Users":[], "App_Opens":[]}

for state in map_users_list:
    state_now=path4+state+'/'
    map_years_list=os.listdir(state_now)
    #print(map_years_list)
    
    for year in map_years_list:
        year_now=state_now+year+'/'
        map_files_list=os.listdir(year_now)
        # print(map_files_list)
        
        for file in map_files_list:
            file_now=year_now+file
            file_read=open(file_now,'r')
            
            D=json.load(file_read)
            for i in D['data']['hoverData'].items():
                    district=i[0]
                    registeredUsers=i[1]['registeredUsers']
                    appOpens=i[1]['appOpens']
                    columns4['Districts'].append(district)
                    columns4['Registered_Users'].append(registeredUsers)
                    columns4['App_Opens'].append(appOpens)
                    columns4['States'].append(state)
                    columns4['Years'].append(year)
                    columns4['Quarter'].append(int(file.strip(".json")))
        
map_users=pd.DataFrame(columns4)


path5="C:/Users/ELCOT/GUVI/Python/DTM9/.spyder-py3/PhonePe/pulse/data/top/transaction/country/india/state/"
top_trans_list=os.listdir(path5)

columns5={'States':[], 'Years':[], "Quarter":[], 'Districts': [], "Registered_Users":[], "App_Opens":[]}

for state in top_trans_list:
    state_now=path5+state+'/'
    top_years_list=os.listdir(state_now)
    #print(map_years_list)
    
    for year in top_years_list:
        year_now=state_now+year+'/'
        top_files_list=os.listdir(year_now)
        # print(map_files_list)
        
        for file in top_files_list:
            file_now=year_now+file
            file_read=open(file_now,'r')
            
            E=json.load(file_read)
            for i in E['data']['hoverData'].items():
                    district=i[0]
                    registeredUsers=i[1]['registeredUsers']
                    appOpens=i[1]['appOpens']
                    columns5['Districts'].append(district)
                    columns5['Registered_Users'].append(registeredUsers)
                    columns5['App_Opens'].append(appOpens)
                    columns5['States'].append(state)
                    columns5['Years'].append(year)
                    columns5['Quarter'].append(int(file.strip(".json")))
        
map_users=pd.DataFrame(columns5)




