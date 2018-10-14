'''
Created on 2018.3.19

@author: haodong.liu
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class OfferStrengthFormPage(BasePage.Action):
    
    def __init__(self):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[3]/td[%d]/i'
        self.ScoreComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/input'
        self.ScoreColor_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/i'
        self.ScoreColorStatus_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/i'
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_ScoreComments(self,index,text):
        self.ScoreComments_loc=(By.XPATH, self.ScoreComments_path %index)
        self.find_element(*self.ScoreComments_loc).send_keys(text)
    def get_ScoreComments(self,index):
        self.ScoreComments_loc=(By.XPATH, self.ScoreComments_path %index)
        return self.find_element(*self.ScoreComments_loc).get_attribute("value")  
    def ScoreComments_disabled(self,index):
        self.ScoreComments_loc=(By.XPATH, self.ScoreComments_path %index)
        flag=self.find_element(*self.ScoreComments_loc).get_attribute("disabled")
        return flag
        
    def get_ScoreColorStatus(self,index):
        self.ScoreColorStatus_loc=(By.XPATH, self.ScoreColorStatus_path %index)
        return self.find_element(*self.ScoreColorStatus_loc).get_attribute("class")
        