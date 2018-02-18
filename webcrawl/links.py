import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver

url = "https://www.amazon.com/amp/mobiles?rows=500&p=10"
browser = webdriver.Chrome(executable_path='/Users/shrinidhipg/Downloads/chromedriver')
browser.get(url)
html = browser.page_source
soup = soup(html, "lxml")
file = open('links.txt','a')
for link in soup.findAll("div",{"class" : "product"}):
	file.write("https://amazon.com"+link.a['href']+"\n")
browser.quit()
