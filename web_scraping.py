import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
# print(type(response.content))
soup  = BeautifulSoup(response.text, 'lxml')
# print(soup)
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
fileout = open('outfile.txt','w', encoding='utf-8')
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quotetags = tags[i].find_all('a',class_='tag')
    lst_quotetags = []
    for quotetag in quotetags:
        print(quotetag.text)
        lst_quotetags.append(quotetag.text)
    # write output to file
    line = quotes[i].text + ' ' + authors[i].text + str(lst_quotetags) +'\n'
    fileout.write(line)
    print('-----------------')