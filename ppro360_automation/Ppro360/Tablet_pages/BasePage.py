'''
Created on Dec 6, 2016

@author: symbio
'''

from selenium.webdriver.support.wait import WebDriverWait
import public_method.Gl
from selenium.webdriver.common.by import By
import time
#from MySQLdb.constants import FLAG
#from pip._vendor.distlib._backport.tarfile import TUREAD


class Action(object):



    #def __init__(self, base_url,pagetilte,selenium_driver):
    def __init__(self, base_url,selenium_driver):

        self.base_url = base_url
        #self.pagetilte = pagetilte
        self.driver = selenium_driver
        

    #def _open(self,url,pagetile):
    def _open(self,url):
        #self.driver.get(url)
        #self.driver.maximize_window()
        #public_method.Gl.driver.get(url)
        #public_method.Gl.driver.maximize_window()
        self.driver.get(url)
        self.driver.maximize_window()


        #assert self.on_page(pagetile), "Can not open this page %s" % url
            
    def find_element(self,*loc):
        try:
            #WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            #return self.driver.find_element(*loc)
            WebDriverWait(public_method.Gl.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return public_method.Gl.driver.find_element(*loc)
        except:
            print(u"%s page can not find this %s element" % (self,loc))
    
    def isElementExist(self,*loc):#It is not used for our scripts
        flag=True
        browser=public_method.Gl.driver
        try:

            #browser.find_element_by_css_selector(*loc)
            browser.find_element_by_xpath(*loc)
            return flag
        except:
            flag=False
            return flag   
        
    def Element_displayed(self,*loc):
        flag=True
        try:
            self.find_element(*loc).is_displayed()
            return flag 
        except:
            flag=False
            return flag
    def Input_text(self,text,*loc):#By Sabrina Guo
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)           
    
    def open(self):
        self._open(self.base_url, self.pagetitle)   
        
    def on_page(self, pagetitle):
        #return pagetitle in self.driver.title
        return pagetitle in public_method.Gl.driver.title
    
      
    def send_keys(self, loc, vaule, clear_first=True, click_first=True): #For admin page to add OM
        try:
            #loc = getattr(self,"_%s"% loc)
            if click_first:
                self.find_element(*loc).click()
                if clear_first:
                    self.find_element(*loc).clear()
                    self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u"%s This page can not find this  %s element"%(self, loc))
                    
    def wait_loadingmask_disappear(self):
        exist_flag=self.Element_displayed(*(By.CLASS_NAME,"loading-mask"))
        while exist_flag==True:
            time.sleep(2*public_method.Gl.waittime)
            exist_flag=self.Element_displayed(*(By.CLASS_NAME,"loading-mask"))
            
       
                    
                    
                    