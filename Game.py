
from bs4 import BeautifulSoup
import re

# Fetch Game title
def getTitle(soup):
    try:
        gameTitle = soup.find("span",attrs={'id':'productTitle'}).text.strip()

    except AttributeError:
        gameTitle = ""

    return gameTitle


# Fetch Game Price
def getPrice(soup):
    try:
        gPrice = soup.find("span",attrs={'class':'a-price-whole'}).text.strip('.')

    except AttributeError:
        gPrice = ""

    return gPrice



# Fetch Game Rating
def getRating(soup):
    try:
        ratingTxt = soup.find("span",attrs={'data-hook':'rating-out-of-text'})
        rt = ratingTxt.text.strip() #comment leading/trailing spaces
        gRating = float(rt.split()[0]) #split the first element which is the rating and convert it into float 

    except AttributeError:
        gRating = ""

    return gRating 
    
 
# Fetch Game Release Date
def getReleaseDate(soup):
    try:
        rDate = soup.find("span", string=re.compile(r'Release date'))
        gDate = (rDate.find_next('span')).text.strip()

    except AttributeError:
        gDate = ""

    return gDate 
 
    
    
