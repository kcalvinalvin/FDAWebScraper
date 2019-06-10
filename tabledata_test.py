from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import sys
import time

link = sys.argv[1]

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": "/Users/calvin/Documents/python_projects/webScraping/csv",  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(options=options)
driver.get(link)

def getTable(url):
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

elem = driver.find_elements_by_class_name('collapsed')
csv = driver.find_elements_by_class_name('buttons-csv')

for x in range(0,len(elem)):
	time.sleep(1)
	elem[x].click()
	time.sleep(1)
	csv[x].click()
	url = driver.current_url
	getTable(url)
