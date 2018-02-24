import requests
from bs4 import BeautifulSoup as soup1
from selenium import webdriver
import shutil
import os
csvfile = open("data.csv", 'a')
headers = "title,description\n"
csvfile.write(headers)

dircount = 1
url = "https://www.amazon.com/amp/mobiles/1715147/buy"
#change to your download path
browser = webdriver.Chrome(executable_path='/Users/shrinidhipg/Downloads/chromedriver')
while(True):
	try:
		url = input()
	except:
		break
#Remove above comments and select all below lines and hit tab
	browser.get(url)

	html = browser.page_source
	soup = soup1(html, "lxml")
	for brk in soup.findAll('br'):
	    brk.replace_with('.')
	#print(soup)
	description = ""
	for detail in soup.findAll("p", {"class" : "pdp-product-description-content"}):
		print(detail.text)
		description = description + detail.text +"."
	description = "\"" + description + "\""
	try:
		print(soup.find("h1",{"class" : "pdp-title"}).text)
		title = "\"" + soup.find("h1",{"class" : "pdp-title"}).text + "\""
	except:
		title = "none"
		pass

	
	i=0
	directory = "./"+str(dircount)
	if not os.path.exists(directory):
	    os.makedirs(directory)
	
	
	csvfile.write(title + "," + style + "," + description + "," + breadcrumb + "," + discount + "," + sp + "," + "\n")

	dircount = dircount + 1
