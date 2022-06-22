from logging import raiseExceptions
import streamlit as st
import requests
import pandas as pd

st.title('玄海町オープンデータ App')

# selectbox
option = st.selectbox(
    '1.検索する対象を選択してください。:',
    ['公共施設一覧','玄海町AED', '公衆無線LANアクセスポイント', '公衆トイレ','子育て施設','観光施設','指定緊急避難場所','医療機関一覧','介護サービス事業所一覧']
    )

def serach_genkai():
    place = []
    address = []
    ido = []
    keido = []
    res = requests.get(url)
    data = res.json()
    data = data['result']['records']
    for data in data:
        try:
            place.append(data['名称'])
        except KeyError:
            place.append(data['介護サービス事業所名称'])
        # if data['名称']:
        #     place.append(data['名称'])
        # else:
        #     place.append(data['介護サービス事業名称'])
        address.append(data['住所']) 
        ido.append(data['緯度'])
        keido.append(data['経度'])
        df_place = pd.DataFrame(place,columns=['名称'])
        df_address = pd.DataFrame(address,columns=['住所'])
        df_ido =  pd.DataFrame(ido,columns=['緯度'])
        df_keido =  pd.DataFrame(keido,columns=['経度'])
        
    df_info = pd.concat([df_place, df_address, df_ido, df_keido], axis='columns')
    st.dataframe(df_info.iloc[:,:2])
    
    option_2 = st.selectbox(
    '2.目的地を選択してください。:',
    place
    )
    df_sp = df_info[df_info.名称 == option_2]
    ido = df_sp.iloc[0,2]
    keido = df_sp.iloc[0,3]
    # option_3 = st.selectbox(
    # '3.交通手段を選択してください。:',
    # ['driving','transit','walking','bicycling']
    # )
    
    serach_url = f"https://www.google.com/maps/dir/?api=1&destination={round(ido,5)},{round(keido,5)}&travelmode=driving"
    st.write('3.目的地までの経路を検索する。')
    st.markdown(serach_url, unsafe_allow_html=True)

if  option == '公共施設一覧':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=5ebffc78-0e95-4a1f-a305-a26847447da5" #公共施設
    serach_genkai()

elif option == '玄海町AED':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=c9d523b9-0a5f-4095-8c28-0fb323d5d1f0" #AED
    serach_genkai()

elif option == '公衆無線LANアクセスポイント':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=54dee2ca-64d3-4fe6-b0e8-e7cf87ee0ba5" #wifi
    serach_genkai()
    
elif option == '公衆トイレ':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=8329a381-52d2-49e0-8cfc-951bced684f7" #トレイ
    serach_genkai()

elif option == '子育て施設':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=f5803abb-efb7-40bb-8bc4-360e9ecffaa6" #子育て施設
    serach_genkai()
    
elif option == '観光施設':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=64e98170-dcf7-4362-9420-22e9de792bd4" #観光施設
    serach_genkai()

elif option == '指定緊急避難場所':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=fc77bcee-d373-4981-9f93-45ef1ce53908" #指定緊急避難場所
    serach_genkai()

elif option == '医療機関一覧':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=35866e59-d5bb-4b1a-809f-247af94a1cab" #医療機関一覧
    serach_genkai()

elif option == '介護サービス事業所一覧':
    url = "https://data.bodik.jp/api/3/action/datastore_search?resource_id=ece2abd0-36c5-4110-b7c8-c823c210f9e4" #介護サービス事業所一覧
    serach_genkai()
    
else:
    st.write('未選択です。検索するものを選択してください。')