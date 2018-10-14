'''
Created on 20180104

@author: luming.zhao
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl


class VPSVPaccountPage(BasePage.Action):

    def __init__(self,VPSVPindex):
        self.VPSVPadd_loc = (By.LINK_TEXT,"Add")
        self.Back_loc = (By.LINK_TEXT,"Back to home")
        self.newVPSVPname_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[1]" %VPSVPindex)
        self.newVPSVPhrid_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[2]" %VPSVPindex)
        self.newVPSVPpwd_loc = (By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[3]" %VPSVPindex)
        self.Role_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[4]" %VPSVPindex)
        self.switchrole_loc=(By.XPATH,"//*[@id='single-button']")
        self.selectrole_path="/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/ul/li[%d]/a" #1 is VP,2 is SVP
        self.VPSVPAtittle_loc = (By.XPATH,"/html/body/div[2]/div/div[1]/div/h2")
        self.Editbutton_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[5]/div/a[1]" %VPSVPindex)
        self.ResetPWDbutton_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[5]/div/a[2]" %VPSVPindex)
        self.modifydate_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[%d]/td[5]" %VPSVPindex)
        self.alert_loc=(By.XPATH,"/html/body/div[2]/div/div[3]/div/span")
    def click_VPSVPadd(self):
        self.find_element(*self.VPSVPadd_loc).click()
        time.sleep(3*Gl.waittime)
    
    def click_back(self):
        self.find_element(*self.Back_loc).click()
        time.sleep(Gl.waittime)
    
    def click_VPSVPaccount(self):
        self.find_element(*self.newVPSVPhrid_loc).click()
        time.sleep(Gl.waittime)
    
    def click_Editbutton(self):
        self.find_element(*self.Editbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def click_ResetPWDbutton(self):
        self.find_element(*self.ResetPWDbutton_loc).click()
        time.sleep(Gl.waittime)
    
    def click_switchrole(self):
        self.find_element(*self.switchrole_loc).click()
        time.sleep(Gl.waittime)    
        
    def get_newVPSVPname(self):
        return self.find_element(*self.newVPSVPname_loc).text
    def get_newVPSVPhrid(self):
        return self.find_element(*self.newVPSVPhrid_loc).text
    def get_newVPSVPpwd(self):
        return self.find_element(*self.newVPSVPpwd_loc).text
    def get_role(self):
        return self.find_element(*self.Role_loc).text
    def select_role(self,roleindex):
        self.selectrole_loc=(By.XPATH,self.selectrole_path %roleindex)
        self.find_element(*self.selectrole_loc).click()
    def get_modifydate(self):
        return self.find_element(*self.modifydate_loc).text

    def get_VPSVPAtittle(self):
        return self.find_element(*self.VPSVPAtittle_loc).text
    
    def get_alert(self):
        return self.find_element(*self.alert_loc).text
    
    def account_existed(self):
        return self.isElementExist(self.newVPSVPname_loc)
        
