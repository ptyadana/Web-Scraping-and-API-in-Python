import requests
import json
import pandas as pd

base_site = "https://itunes.apple.com/search"

response = requests.get(base_site,params={"term":"fifth harmony", "country":"us","limit": 200})

info = response.json()

#dataframe with pandas
songs_df = pd.DataFrame(info['results'])
print(songs_df)

#export to csv or excel
songs_df.to_csv('songs_info.csv')

songs_df.to_excel('songs_info.xlsx')



    
