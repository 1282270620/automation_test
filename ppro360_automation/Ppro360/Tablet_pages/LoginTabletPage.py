'''
Created on Dec 6, 2016

@author: symbio
'''
import sys 
sys.path.append("\test_cases") 
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
#from selenium.webdriver.support.ui import Select

class LogintabletPage(BasePage.Action):
    
    lobnamebox_loc = (By.XPATH,"//*[@id='container']/div/div[1]/form/div[1]/div/span")
    #sitenamebox_loc = (By.XPATH,"//*[@id='container']/div/div[1]/form/div[2]/div/span")
    sitenamebox_loc = (By.XPATH,"(//span[@type='button'])[2]")
    userid_loc = (By.XPATH,"//*[@id='container']/div/div[1]/form/div[3]/input")
    password_loc = (By.XPATH,"//*[@id='container']/div/div[1]/form/div[4]/input")
    loginbutton_loc = (By.XPATH,"//button[@type='button']")
    
    span_loc = (By.CSS_SELECTOR,"body > div > div > div > form > div.form-err > p")
    username_loc = (By.XPATH,"/html/body/div[1]/div/div/a/div/div/dl/dt")
    lobsite_loc = (By.XPATH,"/html/body/div[1]/div/div/a/div/div/dl/dd")
    
    settingbutton_loc = (By.XPATH,"//*[@id='container']/div/nav/ul/li/a/i")
    logoutbutton_loc = (By.LINK_TEXT,"Logout")
    IDorPWDincorrect_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div/p[2]")
     
    nopermission_loc=(By.XPATH,"/html/body/div/div/div/form/div[1]/p")

    
    
    
    defaultSite_loc=(By.XPATH,"//*[@id='container']/div/div[1]/form/div[2]/div/span")
    
    TabletTitleVersion_loc=(By.XPATH,"//*[@id='container']/div/div[1]/h1/figcaption")

    
    #Action
    def open(self):
        #self._open(self.base_url, self.pagetilte)
        self._open(self.base_url)
        self.wait_loadingmask_disappear()
        
    def ScrollToBottom(self):#Find the element of web bottom, and scroll to button
        target=self.find_element(*self.loginbutton_loc)
        Gl.driver.execute_script("arguments[0].scrollIntoView();", target)
           
    def get_TabletTitleVersion(self):
        TabletTitleVersion=self.find_element(*self.TabletTitleVersion_loc).text
        TabletTitleVersion_list=TabletTitleVersion.split("\n")
        return TabletTitleVersion_list    
    
    def get_eachlobname(self,lobindex):
        eachlobname_loc=(By.XPATH,("//*[@id='container']/div/div[1]/form/div[1]/div/ul/li[%d]/a") %lobindex)
        eachlobname=self.find_element(*eachlobname_loc).text
        return eachlobname
    def eachlob_Exist(self,lobindex):
        eachlobname_loc=(By.XPATH,("//*[@id='container']/div/div[1]/form/div[1]/div/ul/li[%d]/a") %lobindex)
        Flag=self.isElementExist(*eachlobname_loc)
        return Flag
            
    
    def get_eachsitename(self,siteindex):
        eachsite_loc=(By.XPATH,("//*[@id='container']/div/div[1]/form/div[2]/div/ul/li[%d]/a") %siteindex) 
        eachsitename=self.find_element(*eachsite_loc).text
        return eachsitename  
    def eachsite_Exist(self,siteindex): 
        eachsite_loc=(By.XPATH,("//*[@id='container']/div/div[1]/form/div[2]/div/ul/li[%d]/a") %siteindex)
        Flag=self.isElementExist(*eachsite_loc)
        return Flag
    def get_defaultsitename(self):
        defaultsitename=self.find_element(*self.defaultSite_loc).text
        return defaultsitename
    
    def click_lobname_box_dropdown(self):
        self.find_element(*self.lobnamebox_loc).click()
        #self.wait_loadingmask_disappear()
    def select_lob(self,lobname):
        lobname_loc=(By.LINK_TEXT,lobname)
        self.find_element(*lobname_loc).click()
        #self.wait_loadingmask_disappear()
    
    def click_sitename_box_dropdown(self):
        self.find_element(*self.sitenamebox_loc).click()
        #self.wait_loadingmask_disappear()
    
    
    def select_site(self,sitename):
        sitename_loc=(By.LINK_TEXT,sitename)
        self.find_element(*sitename_loc).click()
        #time.sleep(Gl.waittime)
        
    
    def input_userid(self,userid):
        self.find_element(*self.userid_loc).send_keys(userid)
        time.sleep(Gl.waittime)
    
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
        time.sleep(Gl.waittime)
        
    def click_login(self):
        self.find_element(*self.loginbutton_loc).click()
        self.wait_loadingmask_disappear()
        
    def show_span(self):
        return self.find_element(*self.span_loc).text
    
    def show_username(self):
        return self.find_element(*self.username_loc).text
    
    def show_lobsite(self):
        return self.find_element(*self.lobsite_loc).text
    
    def click_setting(self):
        self.find_element(*self.settingbutton_loc).click()
        
    def click_logout(self):
        self.find_element(*self.logoutbutton_loc).click()
        
    def get_IDorPWDincorectInfo(self):
        return self.find_element(*self.IDorPWDincorrect_loc).text
    
        
    def get_nopermission(self):
        return self.find_element(*self.nopermission_loc).text
    

  

        