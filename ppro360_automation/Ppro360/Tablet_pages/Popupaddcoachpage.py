'''
Created on Jan 9, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
class Popupaddcoachpage(BasePage.Action):
    
    def __init__(self):
        #self.tittle_loc=(By.XPATH,"//*[@id='add-coaching-modal']/header/text()")
        self.title_loc=(By.XPATH,"//*[@id='add-coaching-modal']/header")
        self.closebutton_loc=(By.XPATH,"//*[@id='add-coaching-modal']/header/a")
        self.addbutton_loc=(By.LINK_TEXT,"Add")
        self.canclebutton_loc=(By.LINK_TEXT,"Cancel")

    #Get pop-up window tittle: add coaching form or add triad coaching form   
    def get_title(self):
        title = self.find_element(*self.title_loc).text
        return title
    
        
      
        
    def close_popup(self):
        self.find_element(*self.closebutton_loc).click()
        time.sleep(Gl.waittime)
        
    def add_coach(self):
        self.find_element(*self.addbutton_loc).click()
        self.wait_loadingmask_disappear()
        
    def cancle_addcoach(self):
        self.find_element(*self.canclebutton_loc).click()
        time.sleep(Gl.waittime)
    
    def get_coachname(self,coachnameindex):
        coachname_loc=(By.XPATH,"//*[@id='add-coaching-modal']/section/ul/li[%d]" %coachnameindex)
        coachformname = self.find_element(*coachname_loc).text
        return coachformname
    def coachname_exsit(self,coachnameindex):
        coachname_loc=(By.XPATH,("//*[@id='add-coaching-modal']/section/ul/li[%d]") %coachnameindex)
        #print "Get coachname_exsit",
        try:
            ExsitFlag=self.find_element(*coachname_loc).is_displayed()
            return ExsitFlag
        except:
            ExsitFlag=False
            return ExsitFlag
        
        #print self.isElementExist(*coachname_loc)
        #return self.isElementExist(*coachname_loc)
    
    
    def isornot_enable(self,coachnameindex):
        coachname_loc=(By.XPATH,"//*[@id='add-coaching-modal']/section/ul/li[%d]" %coachnameindex)
        flag = self.find_element(*coachname_loc).get_attribute("disabled")
        return flag

           
    def select_coach(self,coachnameindex):
        coachname_loc=(By.XPATH,"//*[@id='add-coaching-modal']/section/ul/li[%d]" %coachnameindex)
        self.find_element(*coachname_loc).click()
        time.sleep(Gl.waittime)

      
        