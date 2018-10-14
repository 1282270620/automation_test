'''
Created on 2018年6月28日
@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.BasePage import BasePage
from common.login import login,log_immediately,backage_logon      #导入用户登录模块
from utils.mysql import get_verifycode,get_bid
'''
    我的投资界面操作封装，继承BasePage基类
'''

class MyInvestmentPage(BasePage):
    my_investment = (By.XPATH,"/html/body/div[1]/div/div/div/ul/li[2]/a")        #我的投资元素定位
    type_all = (By.XPATH,".//*[@id='types']/dd[1]/a")        #借款类型->"全部" 元素定位
    mortgage = (By.XPATH,"//*[@id='types']/dd[2]/a")     #抵押标元素定位
    pledge = (By.XPATH,".//*[@id='types']/dd[3]/a")       #质押标元素定位
    current_standard = (By.XPATH,"//*[@id='states']/dd[4]/a")       #已流标元素定位
    mortgage_title = (By.XPATH,".//a[@data-rel='tooltip']")      #抵押标的信息名称定位，定位一列元素
#   investment_bid = (By.XPATH,".//dd[@class="span2 loan_sumb"]/a")    #被投资的信息投标按钮定位，定位一列元素
    bid_title = (By.XPATH,"/html/body/div[3]/div/div[2]/dl[2]/dd[2]/ul/li[1]/a")       #第一个，投标对象标题元素定位
    bid_now = (By.XPATH,"/html/body/div[3]/div/div[2]/dl[2]/dd[6]/a")       #第一个，进入立即投标元素定位
    select_bid_now = (By.XPATH,"/html/body/div[3]/div[1]/div[1]/div/div[2]/div[1]/dl/dd[11]/a")     #立即投标生效按钮元素定位
    #投标确认对话框
    tender_amount = (By.XPATH,"//*[@id='price']")       #投标金额输入框元素定位
    payment_passwd = (By.XPATH,"//*[@id='tEnder']/div[2]/div[2]/form/dl/dd[2]/input")       #支付密码输入框元素定位
    verifycode = (By.XPATH,"//*[@id='tEnder']/div[2]/div[2]/form/dl/dd[4]/input")       #验证码输入框元素定位
    confirm_submit = (By.XPATH,"//*[@id='tEnder']/div[2]/div[2]/form/dl/dd[5]/button")      #确认提交按钮元素定位
    login_out = (By.XPATH,"/html/body/div[1]/div/div/div/ul/li[10]/a")      #退出元素定位
    def into_investment(self):
        self.click(self.my_investment)
        self.log.info("--进入我要投资页面")
    def into_bid_now(self,type_of_loan = "全部"):
        self.into_investment()
        if type_of_loan == "全部":
            self.click(self.type_all)
            text_title = self.find_element(self.bid_title).text
            self.log.info("--选择全部")
        elif type_of_loan == "抵押标":
            self.click(self.mortgage)
            text_title = self.find_element(self.bid_title).text
            self.log.info("--选择抵押标")
        elif type_of_loan == "质押标":
            self.click(self.pledge)
            text_title = self.find_element(self.bid_title).text
            self.log.info("--选择质押标")
        self.click(self.bid_now)
        self.click(self.select_bid_now)
        self.log.info("--点击立即投标")
        return text_title,text_title+type_of_loan
    def alert_operation(self, driver,money_value = "10", passwd_value = "123456"):
        self.input_values(self.tender_amount, money_value)
        self.input_values(self.payment_passwd,passwd_value)
        cookie_list = driver.get_cookies()
        sessID = driver.get_cookie("PHPSESSID")
        verify_code = get_verifycode(sessID["value"])
        self.input_values(self.verifycode,verify_code)
        self.click(self.confirm_submit)
    def _comparestate(self,state):
        if state == "抵押标":
            list_mortgage = []
            list_mortgage.append(state)
            self.click(self.mortgage)
            elements = self.find_elements(self.mortgage_title)
            for element in elements:
                list_mortgage.append(element.text)
            list_mortgage.sort()
            self.log.info("--获取所有抵押标title信息")
            return list_mortgage
        elif state == "质押标":
            list_pledge = []
            self.click(self.pledge)
            list_pledge.append(state)
            elements = self.find_elements(self.mortgage_title)
            for element in elements:
                list_pledge.append(element.text)
            list_pledge.sort()
            self.log.info("--获取所有质押标title信息")
            return list_pledge
        elif state == "已流标":
            list_cursta = []
            self.click(self.current_standard)
            list_cursta.append(state)
            elements = self.find_elements(self.mortgage_title)
            for element in elements:
                list_cursta.append(element.text)
            list_cursta.sort()
            self.log.info("--获取所有质押标title信息")
            return list_cursta
    def get_bid_info(self):
        list_tit = []
        tit = []
        info_bids = get_bid()
        for info_bid in info_bids:
            list_tit.append(self._comparestate(info_bid[0]))
        list_tit.sort()
        self.log.info("--获取我要投资页面所有标的title信息")
        for infos in list_tit:
            for info in infos:
                tit.append(info) 
        tit.sort()
        return tit
    def get_bid_mysql(self):
        mysql_info = []
        info_tit_mysql = []
        info_mysql = get_bid()
        for info_bid in info_mysql:
            info_bid.sort()
            info_tit_mysql.append(info_bid)
        info_tit_mysql.sort()
        for infos in info_tit_mysql:
            for info in infos:
                mysql_info.append(info)
        self.log.info("--获取数据库所有标的title信息")
        mysql_info.sort()
        return mysql_info
    def logon_out(self):
        self.click(self.login_out)
        self.log.info("--退出")
if __name__ == "__main__":
    driver = webdriver.Firefox()
    log_immediately(driver)
    MIP = MyInvestmentPage(driver)
    test = MIP.get_bid_mysql()

   