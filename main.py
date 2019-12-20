import time
import shutil
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://twitter.com/_JKT48TeamT"
SCROLL_TIMES = 5

if __name__=="__main__":
	current_scroll_time = 0
	img_counter = 0
	driver = webdriver.Chrome()
	driver.get(url=URL)

	# while current_scroll_time < SCROLL_TIMES:
	# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# 	current_scroll_time+=1
	# 	time.sleep(2)


	source = driver.page_source
	soup = BeautifulSoup(source, 'html.parser')
	# print(soup)
	images = soup.find_all("div", class_="AdaptiveMedia-photoContainer")

	for img in images:
		img_url = img['data-image-url']
		filename = img_url.split("/")[-1]
		response = requests.get(img_url, stream=True)
		with open(f"DownloadedImages/{filename}", 'wb') as outfile:
			shutil.copyfileobj(response.raw, outfile)
		print(f"[{img_counter}] Downloaded: {img_url}")
		img_counter+=1
		del response


	driver.quit()