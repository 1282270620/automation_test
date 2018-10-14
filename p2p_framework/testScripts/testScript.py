'''
Created on 2018年6月28日
@author: Administrator
'''

import unittest     #导入unittest框架
from selenium import webdriver
from common.login import login,log_immediately,backage_logon      #导入用户登录模块
from common.ReleaseMortgage import release_mortgage     #发布抵押标流程
from common.ReleasePledge import release_pledge      #导入发布质押标页面对象
from pageObject.backHomeObject import BackHomePage      #导入后台页面元素对象
from pageObject.myInvestmentObject import MyInvestmentPage      #导入我的投资界面元素对象
from pageObject.MyAccount import MyAccount      #导入我的账户界面元素对象
import time,os
from utils.setFlash import DefineFlash      #导入设置flash的操作
from common.administratorReview import adminstration_review
from pageObject.paymentGoodsObject import PaymentGoodsPage

from utils.logs import get_log_path     #日志文件的路径
from utils.log_decorator import log_decorator       #日志记录和异常重试判断的功能

class TestLogin(unittest.TestCase):
    #前置方法，用于打开指定的浏览器网址
    log = get_log_path(__file__, __name__)    
    @classmethod
    @log_decorator(log)
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        path = os.path.dirname(os.path.abspath("."))
        DefineFlash.init_method(self.driver, path)
        DefineFlash.set_flash()
    #后置方法，用于关闭浏览器网页
    @classmethod
    @log_decorator(log)
    def tearDownClass(self):
        DefineFlash.del_method()
        self.driver.quit()
    #发布质押标，后台审核通过，并验证
#    @unittest.skip('skip')
    @log_decorator(log)      
    def test_mortage(self):
        release_mortgage(self.driver)
        adminstration_review(self.driver)
    #发布质押标，后台审核通过，并验证
#    @unittest.skip('skip')
    @log_decorator(log)  
    def test_pledge(self):
        release_pledge(self.driver) 
        adminstration_review(self.driver)
    #断言我要投资界面的所有信息，将数据库和投资界面的信息比对
#    @unittest.skip("skip")
    @log_decorator(log)
    def test_info_assert(self):
        log_immediately(self.driver)
        MIP = MyInvestmentPage(self.driver) 
        MIP.into_investment()
        actual = MIP.get_bid_info()
        expected = MIP.get_bid_mysql()
        for act in actual:
            self.assertIn(act,expected)
        MIP.logon_out()  
    #我要投资界面，选择项目标进行投标，投标成功进行验证
#    @unittest.skip("skip")
    @log_decorator(log)
    def test_my_investment(self):
        log_immediately(self.driver)     
        MIP = MyInvestmentPage(self.driver)   
        title,expected = MIP.into_bid_now(type_of_loan="质押标") 
        MIP.alert_operation(self.driver)    
        MA = MyAccount(self.driver)
        MA.into_tender_loan()
        actual = MA.search_tender_info(title)
        self.assertEqual(actual,expected)
        MIP.logon_out()
    #前后台验证我的投资信息的正确性
#    @unittest.skip("skip")
    @log_decorator(log)
    def test_assertbid_info(self): 
        bidder = login(self.driver)
        MA = MyAccount(self.driver)              
        MA.into_tender_loan()
        expected = MA.get_info_bid()
        backage_logon(self.driver)
        PGP = PaymentGoodsPage(self.driver)
        PGP.into_investment_record()       
        actual = PGP.get_investment_info(bidder) 
        self.assertEqual(expected,actual) 