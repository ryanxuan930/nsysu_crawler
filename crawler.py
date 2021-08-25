import pandas as pd
from selenium import webdriver
import json
import time
MAC_OS_ROUTE = '/Users/ryanchang/Project/nsysu_crawler/chromedriver'
WINDOWS_ROUTE = ''
driver = webdriver.Chrome(MAC_OS_ROUTE)
driver.get("https://www.scopus.com/api/authors/7004547082")
dataset = pd.read_excel("data/dataset.xlsx", sheet_name="列表", usecols=["Scopus ID"])
result = {
    'Scopus_ID': dict(),
    'Name': dict(),
    'Affiliated': dict(),
    'Is_NSYSU': dict()
}
i=0
for item in dataset["Scopus ID"]:
    result['Scopus_ID'][i] = item
    result['Name'][i] = ''
    result['Affiliated'][i] = ''
    result['Is_NSYSU'][i] = 'X'
    print("https://www.scopus.com/api/authors/"+str(item))
    driver.get("https://www.scopus.com/api/authors/"+str(item))
    html = driver.find_element_by_tag_name("pre")
    json_data = json.loads(html.text)
    if 'preferredName' in json_data and json_data['preferredName'] is not None:
        if 'full' in json_data['preferredName']:
            result['Name'][i] = json_data['preferredName']['full']
    if 'latestAffiliatedInstitution' in json_data and json_data['latestAffiliatedInstitution']is not None:
        if 'name' in json_data['latestAffiliatedInstitution']:
            result['Affiliated'][i] = json_data['latestAffiliatedInstitution']['name']
            if json_data['latestAffiliatedInstitution']['name']=='National Sun Yat-Sen University':
                result['Is_NSYSU'][i] = ''
    i+=1
print(result)
sheet_data = pd.DataFrame(result)
sheet_data.to_csv("output.csv")
