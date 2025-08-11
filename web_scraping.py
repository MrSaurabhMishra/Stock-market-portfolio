import pandas as pd
import requests
from bs4 import BeautifulSoup
from sklearn import KMeans
from sklearn.preprocessing import StandardScaler
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    
    
}

webpage=requests.get("https://www.ambitionbox.com/list-of-companies?page=1",headers=headers,timeout=30).text
print(webpage[:500])




