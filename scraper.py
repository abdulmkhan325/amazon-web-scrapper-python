

from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import requests
import re
import Game

linksList = []

dictGame  = {"Title":[],"Price":[],"Rating":[],"Date":[]}

URL = "https://www.amazon.com.au/s?k=ps5+games&crid=1TIMG8SX739RP&sprefix=ps5+gam%2Caps%2C332&ref=nb_sb_noss_2"

# Headers for http request 
httpHeader = ({'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43', 
               'Accept-Language':'en-US, en;q=0.5'})

# Headers for http request 
webPage = requests.get(URL,httpHeader)

# Soup object to convert webpage into HTML DOM format  
soup = BeautifulSoup(webPage.content, "html.parser")

# Fetch links as List of Tag Objects
links = soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
  
# Loop for extracting links from the Tag Objects   
for linky in links:
    linksList.append(linky.get('href'))

# Loop for extracting game specific detail 
for link in linksList:
    gameLink = "https://amazon.com.au" + link
    
    # Using the Game Link to extract game details 
    webPage2 = requests.get(gameLink,httpHeader)
    soup2 = BeautifulSoup(webPage2.content, "html.parser")

    dictGame["Title"].append(Game.getTitle(soup2))        # Fetch Game title
    dictGame["Price"].append(Game.getPrice(soup2))        # Fetch Game Price 
    dictGame["Rating"].append(Game.getRating(soup2))      # Fetch Game Rating 
    dictGame["Date"].append(Game.getReleaseDate(soup2))   # Fetch Game Release Date 
    

# Create a Pandas DataFrame (df) using Python dictionary (dictGame)
# and store the data in csv format 
df = pd.DataFrame.from_dict(dictGame) 
df['Title'].replace('',np.nan, inplace=True)
df = df.dropna(subset=['Title'])
df.to_csv("amazon_games_data.csv", header=True, index=False)
