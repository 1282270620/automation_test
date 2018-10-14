'''
Created on 2018年7月4日
@author: Administrator
'''

from utils.setFlash import DefineFlash
import time,os
from pageObject.MortgageObject import MortgagePage  #导入发布抵押标页面对象
from common.login import login

def release_mortgage(driver):
    login(driver)
    MO = MortgagePage(driver)
    MO.into_myloan()
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    MO.send_content("自动化测试"+now,"2","200")
    MO.select_option("生活周转","3个月","月付息到期还本","5天","50元","无限制")
    MO.input_frame()
    DefineFlash.upload_picture()
    MO.input_verifycode(driver)
    MO.submit_mortgage()
    MO.logon_out() 