'''
Created on 2018年6月28日

@author: Administrator
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://118.24.12.61:8080/")
cookie_list = driver.get_cookies()
print(cookie_list)
session = driver.get_cookie("PHPSESSID")
print(session)