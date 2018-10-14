'''
Created on Feb 24, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import  Gl
from setuptools.package_index import HREF
#Getaccount=Get_AllRoleAccountForTest()


class HeaderPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.loginaccount_loc=(By.XPATH,"//*[@id='container']/div/nav/ul/li/a/div/div/dl/dt")
        self.loginLOBSITE_loc=(By.XPATH,"//*[@id='container']/div/nav/ul/li/a/div/div/dl/dd")
        self.HeaderTittle_loc=(By.XPATH,"//*[@id='container']/div/nav/div/span")
        self.backbutton_loc=(By.XPATH,"//*[@id='container']/div/nav/a/div/div")
        self.settingButton_loc=(By.XPATH,"//*[@id='container']/div/nav/ul/li/a")
        #self.changePassword_loc=(By.XPATH,"//*[@id='logout-menu']/li[1]/a")
        # self.logout_loc=(By.XPATH,"//*[@id='logout-menu']/li[2]/a")
        self.changePassword_loc=(By.CSS_SELECTOR,"a[href='/changePassword']")
        self.logout_loc=(By.CSS_SELECTOR,"a[href='/logout']")
        #self.VPSVPlogout_loc=(By.XPATH,"//*[@id='logout-menu']/li[3]/a")
        self.settingButton_path='//*[@id="container"]/div/nav/ul/li/a/i' #yalan added
    def get_HeaderTittle(self):
        HeaderTittle=self.find_element(*self.HeaderTittle_loc).text
        return HeaderTittle
    
    def click_backbutton(self):
        self.find_element(*self.backbutton_loc).click()
        self.wait_loadingmask_disappear()
    
    def get_loginAccountlist(self):
        loginaccount=self.find_element(*self.loginaccount_loc).text
        list1=loginaccount.split(" (")
        return list1
    
    def get_loginName(self):
        loginaccount_list=self.get_loginAccountlist()
        loginname=loginaccount_list[0]
        return loginname
    
    def get_loginRole(self):
        loginaccount_list=self.get_loginAccountlist()
        loginrole=loginaccount_list[1].replace(")","")
        return loginrole
    
    def get_loginLOBSITElist(self):
        loginLOBSITE=self.find_element(*self.loginLOBSITE_loc).text
        list2=loginLOBSITE.split(", ")
        return list2
        
    def get_loginLob(self):
        loginLOBSITE_list=self.get_loginLOBSITElist()
        loginLOB=loginLOBSITE_list[0]
        return loginLOB
    
    def get_loginSite(self):
        loginLOBSITE_list=self.get_loginLOBSITElist()
        loginSite=loginLOBSITE_list[1]
        return loginSite
        
    def click_settingButton(self):
        self.find_element(*self.settingButton_loc).click()
        #self.wait_loadingmask_disappear()
    #yalan added bellow
    def settingButtonexisted(self):
        settingButton_loc=(By.XPATH, self.settingButton_path)
        return self.find_element(*settingButton_loc).get_attribute('class')

    def backbuttonexisted(self):
        return self.find_element(*self.backbutton_loc).get_attribute('class')
    def ChangePasword_existing(self):
        return self.find_element(*self.changePassword_loc).get_attribute('text')
    def Logout_existing(self):
        return self.find_element(*self.logout_loc).get_attribute('text')
    #yalan added above 
    
    def click_changePasswordLink(self):
        self.find_element(*self.changePassword_loc).click()
        self.wait_loadingmask_disappear()   
        
    def click_LogoutLink(self):
        self.find_element(*self.logout_loc).click()
        self.wait_loadingmask_disappear()
        
    def click_VPSVPLogoutLink(self):
        self.find_element(*self.VPSVPlogout_loc).click()
        self.wait_loadingmask_disappear()        
    
    def ChangePassword_Existed(self):
        return self.isElementExist(*self.changePassword_loc)
    def Logout_Existed(self):
        return self.isElementExist(*self.logout_loc)