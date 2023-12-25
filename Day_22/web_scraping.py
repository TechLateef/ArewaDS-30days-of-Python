                     ###==> Python Web Scraping <==###

###################################################################
# Web scraping is the process of extracting and collecting data 
# from websites and storing it on a local machine or in a database.
#################################################################

import json
import requests
from bs4 import BeautifulSoup
# url = 'https://archive.ics.uci.edu/ml/datasets.php'

# response = requests.get(url)
# content = response.content # we get all the content from the website
# soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
# print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
# print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # gives the whole page on the website
# print(response.status_code)

# tables = soup.find_all('table', {'cellpadding':'3'})
# # We are targeting the table with cellpadding attribute with the value of 3
# # We can select using id, class or HTML tag , for more information check the beautifulsoup doc
# table = tables[0] # the result is a list, we are taking out data from it
# for td in table.find('tr').find_all('td'):
#     print(td.text)

url1 = 'https://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url1)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title.get_text())
print(response.status_code)

lists = soup.find_all('ul',{'class':'row list'})

lst = lists[0]
data_lst = []
for li in lst.find_all('li'):
    print(li.text)
    clearn_text = li.text.strip()
    data_lst.append(clearn_text)

with open('first_site.json', "w") as f:
    json.dump(data_lst, f, indent=2)



president_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
pres_dic =[]
response = requests.get(president_url)
print(response.status_code)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
tables = soup.find_all('tbody')
rows = tables[0].find_all('tr')
for row in rows:
    col = row.find_all('td')
    if col:
        president_info = {
            "president": col[1].find('a').text.strip().replace('\n', ''),
            "terms": col[2].text.strip().replace('\n', ''),
            "party": col[4].text.strip().replace('\n', ''),
            "elections": col[5].text.strip().replace('\n', ''),
            "vice_president": col[6].text.strip().replace('\n', '')
        }
        pres_dic.append(president_info)

print(pres_dic)

with open('presidents.json','w') as f:
    json.dump(pres_dic,f,indent=2)


print("Data scraped and saved to presidents.json")    