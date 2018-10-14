'''
Created on 20170703

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class DetractorLessThanVerySatisfiedCoaching(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.commentsinput_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[2]/textarea"
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def input_commentsinput (self,text,lineindex):
        self.commentsinput_loc=(By.XPATH,self.commentsinput_path %lineindex)
        self.find_element(*self.commentsinput_loc).send_keys(text);