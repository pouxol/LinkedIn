from selenium import webdriver
from config import *

chrome_driver_path = "C:/Users//DEV/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.linkedin.com")

login = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()

username = driver.find_element_by_id("username")
username.send_keys(UN)

pw = driver.find_element_by_id("password")
pw.send_keys(PW)

login = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login.click()

jobs = driver.find_element_by_xpath('//*[@id="ember28"]')
jobs.click()

driver.quit()
