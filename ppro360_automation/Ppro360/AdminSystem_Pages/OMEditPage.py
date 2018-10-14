'''
Created on Mar 3, 2017

@author: SabrinaGuo
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By

class OMEditPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Pagetitle_loc=(By.XPATH,"/html/body/div[2]/div/div[1]/div/h2")  
        self.Savebutton_loc=(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/a[2]")  
        self.Cancelbutton_loc=(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/a[3]")
        self.firstnametitle_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[2]/label")
        self.lastnametitle_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[3]/label")
        self.firstnameInput_loc=(By.XPATH,"//input[@type='text']")
        self.lastnameInput_loc=(By.XPATH,"(//input[@type='text'])[2]")
        self.hridtitle_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[4]/label")
        self.hridInput_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[4]/div/input")
        self.pwdtitle_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[5]/label")
        self.pwdInput_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[5]/div[1]/input")
        self.lastnameWarning_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[3]/p")
        
    def get_pagetitle(self):
        return self.find_element(*self.Pagetitle_loc).text
    
    def get_savebutton(self):
        return self.find_element(*self.Savebutton_loc).text
    def click_savebutton(self):
        self.find_element(*self.Savebutton_loc).click()
    
    def get_cancelbutton(self):
        return self.find_element(*self.Cancelbutton_loc).text
    def click_cancelbutton(self):
        self.find_element(*self.Cancelbutton_loc).click()
    
    def get_firstnametitle(self):
        return self.find_element(*self.firstnametitle_loc).text
    
    def Input_firstname(self,newfirstname):
        self.send_keys(self.firstnameInput_loc, newfirstname)
       
    def get_lastnametitle(self):
        return self.find_element(*self.lastnametitle_loc).text
    
    def Input_lastname(self,newlastname):
        self.send_keys(self.lastnameInput_loc,newlastname)
        
    def clear_firstname(self):
        self.find_element(*self.firstnameInput_loc).clear() 
    def clear_lastname(self):
        self.find_element(*self.lastnameInput_loc).clear()  
    
    def get_hridtitle(self):
        return self.find_element(*self.hridtitle_loc).text
    
    def get_pwdtitle(self):
        return self.find_element(*self.pwdtitle_loc).text
    
    
    def hridInput_disabled(self):
        return self.find_element(*self.hridInput_loc).get_attribute("disabled")
    
    def pwdInput_disabled(self):
        return self.find_element(*self.pwdInput_loc).get_attribute("disabled")
    
    
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