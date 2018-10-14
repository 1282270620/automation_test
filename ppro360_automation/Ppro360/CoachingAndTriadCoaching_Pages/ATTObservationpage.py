'''
Created on 20170627

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class ATTObservationpage(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.boodybox_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/table/tbody/tr[%d]/td[2]/div[%d]/i"
        self.lastthreeinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        
        
        
        
         
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, self.KPIcheckbox_path %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
        
    def click_boodybox (self,moduleindex,lineindex,columnindex):
        self.boodybox_loc=(By.XPATH,self.boodybox_path %(moduleindex,lineindex,columnindex))
        self.find_element(*self.boodybox_loc).click()
        
    def input_lastthreeinput (self,lineindex2,text):
        self.lastthreeinput_loc=(By.XPATH,self.lastthreeinput_path %lineindex2)
        self.find_element(*self.lastthreeinput_loc).send_keys(text)