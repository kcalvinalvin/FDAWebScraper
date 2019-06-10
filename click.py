from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
import sys
import time

link = sys.argv[1]

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": "/Users/calvin/Documents/python_projects/webScraping/csv",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": False
})
driver = webdriver.Chrome(options=options)
driver.get(link)

elem = driver.find_elements_by_class_name('collapsed')

for x in range(0,len(elem)):
	time.sleep(1)
	elem[x].click()
	time.sleep(1)
	csv = driver.find_elements_by_link_text('CSV')
	for y in range(0,len(csv)):
		time.sleep(1)
		csv[y].click()
	time.sleep(1)

driver.close()
