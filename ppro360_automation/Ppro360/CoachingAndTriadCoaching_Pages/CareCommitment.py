'''
Created on 20170626

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class CareCommitment(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.commitmentFromLast_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.boodybox_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[2]/div[%d]/div/div[%d]/textarea"
        self.lastinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea" 
         
         
         
         
         
         
         
         
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
        
    def input_commitmentFromLast(self,text):
        self.find_element(*self.commitmentFromLast_loc).send_keys(text);
        
    def input_boodybox(self,lineindex,moduleindex,columnindex,text):
        self.boodybox_loc=(By.XPATH,self.boodybox_path %(lineindex,moduleindex,columnindex))
        self.find_element(*self.boodybox_loc).send_keys(text)
        
    def input_lastinput(self,lineindex2,text):
        self.lastinput_loc=(By.XPATH,self.lastinput_path %lineindex2)
        self.find_element(*self.lastinput_loc).send_keys(text);
        