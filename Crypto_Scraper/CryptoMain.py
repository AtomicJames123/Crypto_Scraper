from bs4 import BeautifulSoup
import urllib.request

url = "https://coinmarketcap.com/currencies/litecoin/#markets"

content = urllib.request.urlopen(url).read()

soup = BeautifulSoup(content, 'html.parser')

#print(soup.prettify())

list(soup.children)

print(soup.find('span', 'h2 text-semi-bold details-panel-item--price__value').getText())
#soup.select('')

