'''
Created on Dec 22, 2016

@author: symbio
'''
#import sys 
#sys.path.append("\test_cases") 
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl

class OMaccountPage(BasePage.Action):

    def __init__(self,OMindex):
        self.OMadd_loc = (By.LINK_TEXT,"Add")
        self.Back_loc = (By.LINK_TEXT,"Back to home")
        self.newOMhrid_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[2]" %OMindex)
        self.newOMname_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[1]" %OMindex)
        self.newOMpwd_loc = (By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[3]" %OMindex)
        self.OMAtittle_loc = (By.XPATH,"/html/body/div[2]/div/div[1]/div/h2")
        self.Editbutton_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[4]/div/a[1]" %OMindex)
        self.ResetPWDbutton_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[4]/div/a[2]" %OMindex)
        self.modifydate_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[4]" %OMindex)
        self.alert_loc=(By.XPATH,"/html/body/div[2]/div/div[3]/div/span")
    def click_OMadd(self):
        self.find_element(*self.OMadd_loc).click()
        time.sleep(Gl.waittime)
    
    def click_back(self):
        self.find_element(*self.Back_loc).click()
        time.sleep(Gl.waittime)
    
    def click_OMaccount(self):
        self.find_element(*self.newOMhrid_loc).click()
        time.sleep(Gl.waittime)
    
    def click_Editbutton(self):
        self.find_element(*self.Editbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def click_ResetPWDbutton(self):
        self.find_element(*self.ResetPWDbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def get_newOMname(self):
        return self.find_element(*self.newOMname_loc).text
    def get_newOMhrid(self):
        return self.find_element(*self.newOMhrid_loc).text
    def get_newOMpwd(self):
        return self.find_element(*self.newOMpwd_loc).text
    def get_modifydate(self):
        return self.find_element(*self.modifydate_loc).text

    def get_OMAtittle(self):
        return self.find_element(*self.OMAtittle_loc).text
    
    def get_alert(self):
        return self.find_element(*self.alert_loc).text
    
    def account_existed(self):
        return self.isElementExist(self.newOMname_loc)
        