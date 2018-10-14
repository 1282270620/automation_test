'''
Created on 2018年6月28日
@author: Administrator
@para url: p2p网址
@para loc: 元素位置，传入的是元组
@para value: 输入的值
'''

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.select import Select
from utils.record_log import Log
from utils.parserXML import XmlHandler

dict_info = XmlHandler.get_xml()

'''
    基本类，用以所有测试页面的继承
'''

class BasePage(object):
    log = Log()     #实例化日志对象
    #初始化实例对象  
    def __init__(self, driver, url=dict_info["url"]):
        self.driver = driver
        self.url = url
    #打开浏览器
    def open(self):
        self.driver.get(self.url)
    #传入页面元素定位，并返回页面元素
    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print("%s" %e)
    #传入页面元素定位，返回一组页面元素
    def find_elements(self, loc):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(*loc)
    #输入参数值
    def input_values(self, loc, para):
        try:
            self.find_element(loc).clear()
            self.find_element(loc).send_keys(para)
        except AttributeError as e:
            print("%s page does not have %s"%(self,e))
    #点击页面元素
    def click(self, loc):
        self.find_element(loc).click()
    #切换导致指定的frame框
    def switchframe(self):
        self.driver.switch_to_frame(0)
    #切换到默认页面
    def switchdefault(self):
        self.driver.switch_to_default_content()
    #定位下拉框，再选择选项
    def select_list(self, loc, value):
        element = self.find_element(loc)
        Select(element).select_by_visible_text(value)
    def text_list(self,loc):
        for element in self.find_elements(loc):
            return element

        