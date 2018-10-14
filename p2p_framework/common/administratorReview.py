'''
Created on 2018年7月3日

@author: Administrator
'''
from common.login import backage_logon
from pageObject.backHomeObject import BackHomePage

def adminstration_review(driver):
    backage_logon(driver)
    BHP = BackHomePage(driver)
    BHP.into_examine() 
    assert_list = BHP.info_list()  
    BHP.examine_click()