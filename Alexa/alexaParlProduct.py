from selenium import webdriver
from selenium.webdriver import ActionChains
import os
import requests.packages.urllib3
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
requests.packages.urllib3.disable_warnings()

def startPage():
	driver = webdriver.Chrome(executable_path= r'D:\\InitialSetup\\Extras\\chromedriver.exe')

	driver.get('http://localhost/finalUI/login.html');

	element = driver.find_element_by_name("email")
	element.send_keys("shrinidhi@gmail.com")

	element = driver.find_element_by_name("pass")
	element.send_keys("shrinidhi123")
	#time.sleep(1)
	element = driver.find_element_by_name("Login")
	element.click()
	#time.sleep(2)
	driver.get('http://localhost/finalUI/tables.html')

	wait = WebDriverWait(driver, 10)

	input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "form-control-sm")))

	element = driver.find_element_by_class_name("form-control-sm")

	element.send_keys("products")
