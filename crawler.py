from pandas.io import json
import requests
import pandas as pd
import json
from fake_useragent import UserAgent

'''
dataset = pd.read_excel("data/dataset.xlsx", sheet_name="列表", usecols=["Scopus ID"])
for item in dataset["Scopus ID"]:
    print(item)

'''

response = requests.get("https://www.scopus.com/api/authors/7004547082")
print(response.text)