'''
Created on 20180116

@author: luming.zhao
'''
import sys 
sys.path.append("\test_cases") 
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal

class VPSVPLoginTabletPage(BasePage.Action):
    
    def __init__(self):
        self.SettingButton_loc=(By.XPATH,"//*[@id='container']/div/nav/ul/li/a")
        self.SwitchLOBSites_loc=(By.XPATH,"//*[@id='logout-menu']/li[1]/a")
        self.ClickSwitchLOB_loc=(By.XPATH,"//*[@id='container']/div/div[3]/div/section/div[1]/span")
        self.SwitchLOB_path="//*[@id='container']/div/div[3]/div/section/div[1]/ul/li[%d]/a"
        #self.SwitchLOBname_loc = (By.XPATH,"//*[@id='container']/div/div[3]/div/section/div[1]/span")
        self.ClickSwitchSite_loc=(By.XPATH,"//*[@id='container']/div/div[3]/div/section/div[2]/span")
        self.SwitchSite_path="//*[@id='container']/div/div[3]/div/section/div[2]/ul/li[%d]/a"               
        self.Switchbutton_loc=(By.XPATH,"//*[@id='container']/div/div[3]/div/footer/ul/li[1]/a")   
        self.Cancelbutton_loc=(By.XPATH,"//*[@id='container']/div/div[3]/div/footer/ul/li[2]/a")   
        self.LoginpageLOB_path= "//*[@id='container']/div/div[1]/form/div[1]/div/ul/li[%d]/a"
        self.LoginpageSITE_path="//*[@id='container']/div/div[1]/form/div[2]/div/ul/li[%d]/a"
        
        
    def get_loginlob(self):
        Get_AnyText=Get_AnyText_ForNormal()
        LoginLobs_list=Get_AnyText.Get_Text_ForLoop(1, self.LoginpageLOB_path)
        return LoginLobs_list
    
    def click_loginlob(self,lobindex1):
        self.LoginpageLOB_loc=(By.XPATH,self.LoginpageLOB_path %lobindex1)
        self.find_element(*self.LoginpageLOB_loc).click()
        time.sleep(Gl.waittime)
        
    def get_loginsite(self):
        Get_AnyText=Get_AnyText_ForNormal()
        LoginSites_list=Get_AnyText.Get_Text_ForLoop(1, self.LoginpageSITE_path)
        return LoginSites_list
    
    def click_loginstie(self,siteindex1):
        self.LoginpageSITE_loc=(By.XPATH,self.LoginpageSITE_path %siteindex1)
        self.find_element(*self.LoginpageSITE_loc).click()
        time.sleep(Gl.waittime)
    
        
    def click_settingButton(self):
        self.find_element(*self.SettingButton_loc).click()
    
    def click_SwitchLOBSitesLink(self):
        self.find_element(*self.SwitchLOBSites_loc).click()
        time.sleep(Gl.waittime)
        
    def click_LOBdropdownbutton(self):
        self.find_element(*self.ClickSwitchLOB_loc).click()
        time.sleep(Gl.waittime)
        
    '''def get_checkLOBsnamepage(self,lobindex):
        CheckLOBsnamepage_loc=(By.XPATH,self.SwitchLOB_path %lobindex)
        #return self.find_element(*self.SwitchLOBsnamepage_loc).text
        self.find_element(*self.CheckLOBsnamepage_loc).text
        return CheckLOBsnamepage_loc '''
    
    def get_checkLOBsnamepage(self):
        Get_AnyText=Get_AnyText_ForNormal()
        checkLOBsname_list=Get_AnyText.Get_Text_ForLoop(1, self.SwitchLOB_path)
        return checkLOBsname_list
        
    def select_LOBtoswitch(self,lobindex):
        self.SwitchLOB_loc=(By.XPATH,self.SwitchLOB_path %lobindex)
        self.find_element(*self.SwitchLOB_loc).click()
        time.sleep(Gl.waittime)
        
    def get_swithloginLOBname(self):
        #self.SwitchLOBname_loc = (By.XPATH,"//*[@id='container']/div/div[3]/div/section/div[1]/ul/li[%d]/a" %lobindex)
        return self.find_element(*self.ClickSwitchLOB_loc).text
        
    def click_Sitedropdownbutton(self):
        self.find_element(*self.ClickSwitchSite_loc).click()
        time.sleep(Gl.waittime)
        
    '''def get_checkSitesnamepage(self,siteindex):
        CheckSitesnamepage_loc=(By.XPATH,self.SwitchSite_path %siteindex)
        #return self.find_element(*self.SwitchLOBsnamepage_loc).text
        self.find_element(*self.CheckSitesnamepage_loc).text
        return CheckSitesnamepage_loc'''
    
    def get_checkSitesnamepage(self):
        Get_AnyText=Get_AnyText_ForNormal()
        checkSitesname_list=Get_AnyText.Get_Text_ForLoop(1, self.SwitchSite_path)
        return checkSitesname_list    
    
    def select_Sitetoswitch(self,siteindex):
        self.SwitchSite_loc=(By.XPATH,self.SwitchSite_path %siteindex)
        self.find_element(*self.SwitchSite_loc).click()
        time.sleep(Gl.waittime)
        
    def get_swithloginSITEname(self):
        return self.find_element(*self.ClickSwitchSite_loc).text
    
    def click_Swichbutton(self):
        self.find_element(*self.Switchbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def click_Cancelbutton(self):
        self.find_element(*self.Cancelbutton_loc).click()
        time.sleep(Gl.waittime)
        