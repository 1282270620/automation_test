'''
Created on 2018年7月4日
@author: Administrator
'''
from pageObject.BasePage import BasePage
from common.login import backage_logon
from selenium.webdriver.common.by import By
import re

class PaymentGoodsPage(BasePage):
    '''
        后台贷款列表页面
    '''
    #货款列表
    money_management = (By.XPATH,"/html/body/div[2]/div/div[1]/div[4]/a/p")     #货款管理元素定位
    list_of_goods = (By.XPATH,"/html/body/div[2]/div/div[1]/div/ul/li[4]/a/span")       #货款列表元素定位
    page_display_number = (By.XPATH,"//*[@id='DataTables_Table_0_length']/label/select")    #每页显示数元素定位
    search = (By.XPATH,"//*[@id='DataTables_Table_0_filter']/label/input")      #搜索框元素定位
    repay_info = (By.XPATH,"//*[@id='DataTables_Table_0']/tbody/tr[1]/td")       #元素信息定位   
    title = (By.XPATH,"//*[@id='DataTables_Table_0']/tbody/tr/td[2]")        #标题元素定位  
    #投资记录
    investment_record = (By.XPATH,"/html/body/div[2]/div/div[1]/div/ul/li[6]/a/span")   #投资记录元素定位
    page_displaynumber = (By.XPATH,"//*[@id='DataTables_Table_0_length']/label/select")     #每页显示数元素定位
    search_useropt = (By.XPATH,"//*[@id='DataTables_Table_0_filter']/label/input")     #搜索输入框元素定位
    operate_description = (By.XPATH,"//*[@id='DataTables_Table_0']/tbody/tr/td[7]")      #操作说明元素定位
       
    def into_listgoods(self):
        self.click(self.money_management)
        self.click(self.list_of_goods)
        self.log.info("--进入货款列表")
    def get_repay_info(self,bidder):
        total = []
        self.select_list(self.page_display_number, "100")
        self.log.info("--每页显示数100行信息")
        self.input_values(self.search, bidder)
        self.log.info("--搜索发标者发布的标的信息")
        title_ele = self.find_elements(self.title)
        row = len(title_ele)
        for i in range(1,24):
            loc = "//*[@id='DataTables_Table_0']/tbody/tr["+str(i)+"]/td"
            self.repay_info = (By.XPATH,loc)
            elements = self.find_elements(self.repay_info)
            repay_info = []
            flag = 0
            for element in elements:
                if flag not in [4,6,7,8]: 
                    repay_info.append(element.text)
                flag = flag + 1
            total.append(repay_info)
        self.log.info("--获取货款列表信息")
        return total
    def into_investment_record(self):
        self.click(self.money_management)
        self.click(self.investment_record)
        self.log.info("--进入投资记录")
    def get_investment_info(self,bidder):
        info_title = []
        self.select_list(self.page_displaynumber, "100")
        self.input_values(self.search_useropt,bidder)
        self.log.info("--搜索用户的投标操作信息")
        description = self.find_elements(self.operate_description)
        for descript in description:
            info = descript.text
            investor = re.findall(r"：(.+?)对",info)
            invest_title = re.findall(r"\【(.+?)\】",info)
            info_title.append(invest_title[0])
        self.log.info("--获取当前用户的投标信息")
        info_title.sort()
        return info_title
            