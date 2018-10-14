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

class OMAddPage(BasePage.Action):


    def __init__(self):
        self.addOM_loc=(By.LINK_TEXT,"Add")
        self.CancelAdd_loc=(By.LINK_TEXT,"Cancel")
        self.firstname_loc=(By.XPATH,"//input[@type='text']")
        self.lastname_loc=(By.XPATH,"(//input[@type='text'])[2]")
        self.hrid_loc=(By.XPATH,"(//input[@type='text'])[3]")
        self.password_loc=(By.XPATH,"(//input[@type='text'])[4]")
        self.RegeneratePWD_loc=(By.LINK_TEXT,"Re-generate")
        self.warningpopup_loc=(By.XPATH,"/html/body/div[4]")
        self.lastnameWarning_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[3]/p")
        
        
    
    def click_addOM(self):
        self.find_element(*self.addOM_loc).click()
        time.sleep(Gl.waittime)
    
    def click_Cancel(self):
        self.find_element(*self.CancelAdd_loc).click()
        time.sleep(Gl.waittime)
    def input_fisrtname(self,firstname):
        time.sleep(Gl.waittime)
        self.send_keys(self.firstname_loc,firstname)
        time.sleep(Gl.waittime)
    def input_lastname(self,lastname):
        self.send_keys(self.lastname_loc,lastname)
        time.sleep(Gl.waittime)
        
    def input_hrid(self,hrid):
        self.send_keys(self.hrid_loc,hrid)
        time.sleep(Gl.waittime)
        
    def clear_firstname(self):
        self.find_element(*self.firstname_loc).clear() 
    def clear_lastname(self):
        self.find_element(*self.lastname_loc).clear()   
    def clear_hrid(self):
        self.find_element(*self.hrid_loc).clear()
        
    def get_password(self):
        pass
    def regenerate_password(self):
        self.find_element(*self.RegeneratePWD_loc).click()
        
    def warningwidonw_ispopup(self):
        Flag=False
        try:
            self.find_element(*self.warningpopup_loc).is_displayed()
            Flag=True
            return Flag
        except:
            return Flag
    def lastnameWarning_isdisplayed (self):
        Flag=False
        try:
            self.find_element(*self.lastnameWarning_loc).is_displayed()
            Flag=True
            return Flag
        except:
            return Flag
    def get_lastnameWarning(self):
        return self.find_element(*self.lastnameWarning_loc).text
            
        