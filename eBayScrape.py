from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import pandas as pd
ID_APP = 'Prabhdee-iPhonePr-PRD-52eb6be68-fa668bde'

Keywords = input('what are you searching for? \n')
api = finding(appid = ID_APP,config_file = None)
api_request = {'keywords':Keywords}
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')
cat_list = []
title_list = []
price_list = []
url_list = []
totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')
for item in items:

    cat = item.categoryname.string.lower()
    cat_list.append(cat)
    title = item.title.string.lower()
    title_list.append(title)
    price = int(round(float(item.currentprice.string)))
    price_list.append(price)
    url = item.viewitemurl.string.lower()
    url_list.append(url)
d = {'Category':cat_list,'Title':title_list,'Price':price_list,'URL':url_list}
df = pd.DataFrame(d)
df.to_csv(Keywords+'.csv',columns=['Category','Title','Price','URL'],index= False)