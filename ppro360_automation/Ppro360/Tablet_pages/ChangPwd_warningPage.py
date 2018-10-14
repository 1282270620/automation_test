'''
Created on Mar 10, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
class ChangPwd_warningPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        self.WarningTitle_loc=(By.XPATH,"//*[@id='msg-modal']/header")
        self.WarningMessage_loc=(By.XPATH,"//*[@id='msg-modal']/section/p") 
        self.Okbutton_loc=(By.XPATH,"//*[@id='msg-modal']/footer/ul/li/a")
        
    def click_OKbutton(self):
        self.find_element(*self.Okbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def get_waringtitle(self):
        return self.find_element(*self.WarningTitle_loc).text
    
    def get_warningmessage(self):
        return self.find_element(*self.WarningMessage_loc).text
    
    
