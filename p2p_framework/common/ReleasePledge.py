'''
Created on 2018年7月4日
@author: Administrator
'''
from utils.setFlash import DefineFlash
import time,os
from pageObject.PledgeObject import PledgePage  #导入发布抵押标页面对象
from common.login import login

def release_pledge(driver):
    login(driver)
    PP = PledgePage(driver)
    PP.into_myloan()
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    PP.send_content("自动化测试"+now,"2","200")
    PP.select_option("生活周转","3个月","月付息到期还本","5天","50元","无限制")
    PP.input_frame()
    DefineFlash.upload_picture()
    PP.input_verifycode(driver)
    PP.submit_pledge()
    PP.logon_out()
