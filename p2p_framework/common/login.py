'''
Created on 2018年6月28日
@author: Administrator
'''
from utils.parserXML import XmlHandler
from utils.mysql import get_verifycode
from pageObject.LoginObject import LoginPage
from selenium import webdriver
'''
    登录函数，实现用户登陆功能
'''

def login(driver):
    #解析XML文件内容，并以字典的形式返回数据
    para_dict = XmlHandler.get_xml("login")
    #打开网页，并传入用户登陆信息
    LO = LoginPage(driver,para_dict["url"])  
    LO.open()
    LO.into_login()
    #获取登陆页面的验证码
    cookie_list = driver.get_cookies()
    sessID = driver.get_cookie("PHPSESSID")
    verify_code = get_verifycode(sessID["value"])
    LO.loc_function(para_dict["username"],para_dict["password"])
    LO.input_verifycode(verify_code)
    return para_dict["username"]
def log_immediately(driver):
    #解析XML文件内容，并以字典的形式返回数据
    para_dict = XmlHandler.get_xml("logon") 
    #打开网页，并传入用户登陆信息
    LO = LoginPage(driver,para_dict["url"])
    LO.open() 
    LO.login_function(para_dict["username"],para_dict["password"])
    return driver
def backage_logon(driver):
    #解析XML文件内容，并以字典的形式返回数据
    para_dict = XmlHandler.get_xml("loc")
    LO = LoginPage(driver,para_dict["burl"])
    LO.open()
    LO.logon_function(para_dict["username"],para_dict["password"])
    #获取登陆页面的验证码
    cookie_list = driver.get_cookies()
    sessID = driver.get_cookie("PHPSESSID")
    verify_code = get_verifycode(sessID["value"])
    LO.logon_verifycode(verify_code)
if __name__ == "__main__":
    driver = webdriver.Chrome()
    login(driver)
    log_immediately(driver)
    backage_logon(driver)


    