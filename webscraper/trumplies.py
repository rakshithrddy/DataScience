from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup

r = 'https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html'
data = ureq(r)
html_data = data.read()
data.close()
filename = 'trump lies.csv'
f = open(filename, 'w')

headers = 'date, lie, writers view, link,\n'
f.write(headers)

soup = BeautifulSoup(html_data, 'html.parser')
result = soup.find_all('span', attrs={'class': 'short-desc'})

for first_result in result:
    date = first_result.find('strong').text + '2017'
    lie = first_result.contents[1]
    writers_view = first_result.find('span').text
    link = first_result.find('a')['href']
    print(date)
    print(lie)
    print(writers_view)
    print(link)
    f.write(date + "," + lie + "," + writers_view + "," + link + "\n")
f.close()
