from bs4 import BeautifulSoup, SoupStrainer
import requests
import sys

year = sys.argv[1]

url = "https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-%s" % (year)

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
	print(link.get('href'))

