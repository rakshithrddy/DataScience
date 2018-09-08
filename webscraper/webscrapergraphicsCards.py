from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%2050001669%20601321570&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.find_all("div", {'class': "item-container"})

filename = 'product.csv'
f = open(filename, 'w')
headers = "brand, produce_name, shipping,\n"
f.write(headers)
for container in containers:
    brand = container.div.div.a.img["title"]
    container_name = container.find_all('a',{'class':'item-title'})
    product_name = container_name[0].text
    ship = container.find_all('li',{'class':'price-ship'})
    shipping = ship[0].text.strip()

    print(f'brand : {brand}')
    print(f'product_name: {product_name}')
    print(f'shipping: {shipping}')

    f.write(brand.replace(',', ' ') + "," + product_name.replace(',',' ') + "," + shipping + '\n')

f.close()
