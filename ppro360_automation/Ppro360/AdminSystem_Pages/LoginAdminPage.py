'''
Created on Dec 6, 2016

@author: symbio
'''
#import sys 
#sys.path.append("\test_cases") 
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LoginAdminPage(BasePage.Action):
    
    lobname_loc = (By.ID,"lob_dropdown")
    
    sitename_loc = (By.ID,"site_dropdown")
    userid_loc = (By.XPATH,"/html/body/div/div/div/form/div[4]/label/input")
    password_loc = (By.XPATH,"/html/body/div/div/div/form/div[5]/label/input")
    loginbutton_loc = (By.XPATH,"/html/body/div/div/div/form/div[6]/label/button")
    span_loc = (By.CSS_SELECTOR,"body > div > div > div > form > div.form-err > p")
    username_loc = (By.XPATH,"/html/body/div[1]/div/div/a/div/div/dl/dt")
    lobsite_loc = (By.XPATH,"/html/body/div[1]/div/div/a/div/div/dl/dd")
    nopermission_loc=(By.XPATH,"/html/body/div/div/div/form/div[1]/p")
    
    settingbutton_loc = (By.CSS_SELECTOR,"i.icon-user")
    logoutbutton_loc = (By.LINK_TEXT,"Logout")
    
    ServerDate_loc=(By.XPATH,"/html/body/div/div/div/comment()")
    
    #Action
    def open(self):
        #self._open(self.base_url, self.pagetilte)
        self._open(self.base_url)
        
    def select_lob(self,lobname):
        Select(self.find_element(*self.lobname_loc)).select_by_visible_text(lobname)
    
    def select_site(self,sitename):
        Select(self.find_element(*self.sitename_loc)).select_by_visible_text(sitename)
    
    def input_userid(self,userid):
        self.find_element(*self.userid_loc).send_keys(userid)
    
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
        
    def click_login(self):
        self.find_element(*self.loginbutton_loc).click()
        
    def click_setting(self):
        self.find_element(*self.settingbutton_loc).click()
        
    def click_logout(self):
        self.find_element(*self.logoutbutton_loc).click()
        
    def show_span(self):
        return self.find_element(*self.span_loc).text
    
    def show_username(self):
        return self.find_element(*self.username_loc).text
    
    def show_lobsite(self):
        return self.find_element(*self.lobsite_loc).text
    
    def get_nopermission(self):
        return self.find_element(*self.nopermission_loc).text
    
    def get_ServerDate(self):
        DateTime=self.find_element(*self.ServerDate_loc).text
        print(DateTime)
    

  

        