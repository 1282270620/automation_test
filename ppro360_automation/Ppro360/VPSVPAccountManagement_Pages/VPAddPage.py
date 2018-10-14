'''
Created on 20180104

@author: luming.zhao
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl


class VPAddPage(BasePage.Action):


    def __init__(self):
        self.addVPSVP_loc=(By.LINK_TEXT,"Add")
        self.CancelAdd_loc=(By.LINK_TEXT,"Cancel")
        self.firstname_loc=(By.XPATH,"//input[@type='text']")
        self.lastname_loc=(By.XPATH,"(//input[@type='text'])[2]")
        self.hrid_loc=(By.XPATH,"(//input[@type='text'])[3]")
        self.password_loc=(By.XPATH,"(//input[@type='text'])[4]")
        self.RegeneratePWD_loc=(By.LINK_TEXT,"Re-generate")
        self.VPSVP_loc=(By.XPATH,"//*[@id='single-button']")
        self.chooseRoleVP_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/ul/li[1]/a")
        self.chooseRoleSVP_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/ul/li[2]/a")
        self.loblist_path="/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input"  #lineindex start from 1
        self.warningpopup_loc=(By.XPATH,"/html/body/div[4]")
        self.lastnameWarning_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[3]/p")
    
    def click_addVPSVP(self):
        self.find_element(*self.addVPSVP_loc).click()
        time.sleep(Gl.waittime)
        
    def click_Cancel(self):
        self.find_element(*self.CancelAdd_loc).click()
        time.sleep(Gl.waittime)
        
    def input_VPSVPfirstname(self,firstname):
        time.sleep(Gl.waittime)
        self.send_keys(self.firstname_loc, firstname)
        time.sleep(Gl.waittime)
        
    def input_VPSVPlastname(self,lastname):
        self.send_keys(self.lastname_loc,lastname)
        time.sleep(Gl.waittime)
        
    def input_VPSVPhrid(self,hrid):
        self.send_keys(self.hrid_loc, hrid)
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
  
    def click_vpsvp(self):
        self.find_element(*self.VPSVP_loc).click()
        
    def select_RoleVP(self):
        self.find_element(*self.chooseRoleVP_loc).click()
        
    def select_RoleSVP(self):
        self.find_element(*self.chooseRoleSVP_loc).click()    
       
    def select_loblist(self,lobindex):   
        loblist_loc=(By.XPATH,self.loblist_path %lobindex)
        self.find_element(*loblist_loc).click()
    '''    
    def get_loblist_ALL(self):
        lobindex=0
        flag=True
        while flag:
            Loblist=lobindex
            lobindex=lobindex+1
            anyLOB_loc=(By.XPATH,("/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input")% lobindex)
            flag=self.Element_displayed(*anyLOB_loc)
        return Loblist
    '''
        
        
    def get_loblistNumber(self):
        lobindex=1
        flag=True
        while flag:
            Loblist=lobindex
            lobindex=lobindex+1
            anyLOBnumber_loc=(By.XPATH,self.loblist_path %lobindex)
            flag=self.Element_displayed(*anyLOBnumber_loc)
        return Loblist
          
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
            
            
    
    
    
    
    
    