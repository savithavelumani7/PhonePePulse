# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:43:40 2023

@author: ELCOT
"""
from phonepe_main import *

def Transaction_Amount_All():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response =requests.get(url)
    
    data1 = json.loads(response.content)
    
    state_names = [feature["properties"]["ST_NM"] for feature in data1["features"]]
    
    state_names.sort()

    df_state_names = pd.DataFrame({"States":state_names})

    frames = []

    for year in Map_user["Years"].unique():
        for quarter in Aggre_trans["Quarter"].unique():

            AG_Tr = Aggre_trans[(Aggre_trans["Years"]==year)&(Aggre_trans["Quarter"]==quarter)]
            
            AG_F = AG_Tr[["States","Transaction_amount"]]
            
            AG_F = AG_F.sort_values(by="States")
            
            AG_F["Years"]=year
            
            AG_F["Quarter"]=quarter
            
            frames.append(AG_F)

    merged_df = pd.concat(frames)
    
    colorscale = ["rgb(255, 51, 51)", "rgb(210, 231, 154)", "rgb(94, 179, 39)", "rgb(67, 136, 33)", "rgb(33, 74, 12)"]

    Trans_Map = px.choropleth(merged_df, geojson= data1, locations= "States", featureidkey= "properties.ST_NM", color= "Transaction_amount",
                            color_continuous_scale= colorscale, range_color= (0,4000000000), hover_name= "States", title = "TRANSACTION AMOUNT",
                            animation_frame="Years", animation_group="Quarter")

    
    Trans_Map.update_geos(fitbounds= "locations", visible =False)
    
    Trans_Map.update_layout(width =1000, height= 1200)
    
    Trans_Map.update_layout(title_font= {"size":25})
    
    Trans_Map.update_layout(geo_bgcolor='rgba(0, 0, 0, 0)')

    return st.plotly_chart(Trans_Map)

def Typewise_Bar_Amount_All():
    AG_ty= Aggre_trans[["Transaction_type", "Transaction_count"]]
    
    AG_T= AG_ty.groupby("Transaction_type")["Transaction_count"].sum()
    
    AG_Tf= pd.DataFrame(AG_T).reset_index()
    
    Type_Bar= px.bar(AG_Tf,x= "Transaction_type",y= "Transaction_count",title= "TRANSACTION TYPE and TRANSACTION COUNT",
                color_discrete_sequence=px.colors.sequential.Redor_r)
    
    Type_Bar.update_layout(width=600, height= 500)
    
    return st.plotly_chart(Type_Bar)

def Transaction_Count_All():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    
    data1= json.loads(response.content)
    
    state_names= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    
    state_names.sort()

    df_state_names_tra= pd.DataFrame({"States":state_names})


    frames= []

    for year in Aggre_trans["Years"].unique():
        for quarter in Aggre_trans["Quarter"].unique():

            AG_Tr= Aggre_trans[(Aggre_trans["Years"]==year)&(Aggre_trans["Quarter"]==quarter)]
            
            AG_Tf1= AG_Tr[["States", "Transaction_count"]]
            
            AG_Tf1=AG_Tf1.sort_values(by="States")
            
            AG_Tf1["Years"]=year
            
            AG_Tf1["Quarter"]=quarter
            
            frames.append(AG_Tf1)

    merged_df = pd.concat(frames)

    fig_tra= px.choropleth(merged_df, geojson= data1, locations= "States",featureidkey= "properties.ST_NM",
                        color= "Transaction_count", color_continuous_scale="blackbody", range_color= (0,3000000),
                        title="TRANSACTION COUNT", hover_name= "States", animation_frame= "Years", animation_group= "Quarter")

    fig_tra.update_geos(fitbounds= "locations", visible= False)
    fig_tra.update_layout(width= 1000, height= 1200)
    fig_tra.update_layout(title_font={"size":25})
    fig_tra.update_layout(geo_bgcolor='rgba(0, 0, 0, 0)')
    return st.plotly_chart(fig_tra)

def Typewise_Bar_Count_All():
    attype= Aggre_trans[["Transaction_type","Transaction_amount"]]
    att1= attype.groupby("Transaction_type")["Transaction_amount"].sum()
    df_att1= pd.DataFrame(att1).reset_index()
    fig_tra_pa= px.bar(df_att1, x= "Transaction_type", y= "Transaction_amount", title= "TRANSACTION TYPE and TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Blues_r)
    fig_tra_pa.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_tra_pa)



def Transaction_Amount_Year(sel_year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)
    state_names_tra= [feature["properties"]['ST_NM']for feature in data1["features"]]
    state_names_tra.sort()

    year= int(sel_year)
    atay= Aggre_trans[["States","Years","Transaction_amount"]]
    atay1= atay.loc[(Aggre_trans["Years"]==year)]
    atay2= atay1.groupby("States")["Transaction_amount"].sum()
    atay3= pd.DataFrame(atay2).reset_index()

    fig_atay= px.choropleth(atay3, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_amount", color_continuous_scale="blackbody", range_color=(0,800000000000),
                            title="TRANSACTION AMOUNT and STATES", hover_name= "States")

    fig_atay.update_geos(fitbounds= "locations", visible= False)
    fig_atay.update_layout(width=600,height=700)
    fig_atay.update_layout(title_font= {"size":25})
    fig_atay.update_traces(geo_bgcolor='rgba(0, 0, 0, 0)')

    return st.plotly_chart(fig_atay)

def Typewise_Bar_Amount_Year(sel_year):
    year= int(sel_year)
    apc= Aggre_trans[["Transaction_type", "Years", "Transaction_count"]]
    apc1= apc.loc[(Aggre_trans["Years"]==year)]
    apc2= apc1.groupby("Transaction_type")["Transaction_count"].sum()
    apc3= pd.DataFrame(apc2).reset_index()

    fig_apc= px.bar(apc3,x= "Transaction_type", y= "Transaction_count", title= "PAYMENT COUNT and PAYMENT TYPE",
                    color_discrete_sequence=px.colors.sequential.Brwnyl_r)
    fig_apc.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apc)


def Transaction_Count_Year(sel_year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1=json.loads(response.content)
    state_names_tra= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    state_names_tra.sort()

    year= int(sel_year)
    atcy= Aggre_trans[["States", "Years", "Transaction_count"]]
    atcy1= atcy.loc[(Aggre_trans["Years"]==year)]
    atcy2= atcy1.groupby("States")["Transaction_count"].sum()
    atcy3= pd.DataFrame(atcy2).reset_index()

    fig_atcy= px.choropleth(atcy3, geojson=data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_count", color_continuous_scale= "blackbody",range_color=(0,3000000000),
                            title= "TRANSACTION COUNT and STATES",hover_name= "States")
    fig_atcy.update_geos(fitbounds= "locations", visible= False)
    fig_atcy.update_layout(width=600, height= 700)
    fig_atcy.update_layout(title_font={"size":25})
    fig_atcy.update_layout(geo_bgcolor='rgba(0, 0, 0, 0)')

    return st.plotly_chart(fig_atcy)


def Typewise_Bar_Count_Year(sel_year):
    year= int(sel_year)
    apay = Aggre_trans[["Years", "Transaction_type", "Transaction_amount"]]
    apay1= apay.loc[(Aggre_trans["Years"]==year)]
    apay2= apay1.groupby("Transaction_type")["Transaction_amount"].sum()
    apay3= pd.DataFrame(apay2).reset_index()

    fig_apay= px.bar(apay3, x="Transaction_type", y= "Transaction_amount", title= "PAYMENT TYPE and PAYMENT AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Burg_r)
    fig_apay.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apay)
