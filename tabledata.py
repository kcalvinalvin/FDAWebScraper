from bs4 import BeautifulSoup
import requests
import sys

url = sys.argv[1]

page = requests.get(url)
text = page.text
soup = BeautifulSoup(text)

data = []
table = soup.find('table',{'class':'table'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	data.append([ele for ele in cols if ele]) # Get rid of empty values
	print(cols)
