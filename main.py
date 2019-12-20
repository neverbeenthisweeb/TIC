import time

from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://twitter.com/_JKT48TeamT"
SCROLL_TIMES = 5

if __name__=="__main__":
	current_scroll_time = 0
	driver = webdriver.Chrome()
	driver.get(url=URL)

	while current_scroll_time < SCROLL_TIMES:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		current_scroll_time+=1
		time.sleep(2)


	source = driver.page_source
	soup = BeautifulSoup(source, 'html.parser')
	# print(soup)
	images = soup.find_all("div", class_="AdaptiveMedia-photoContainer")

	for img in images:
		print(img['data-image-url'])

	driver.quit()