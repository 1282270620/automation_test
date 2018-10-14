'''
Created on 20170629

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class CoachingRhythmProcessConfirmation(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.firsttwoinput_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[4]/textarea"
        self.midinput_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[3]/textarea"
        self.lastthreeinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.firsttwoclick_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[%d]/div[%d]/i "
        self.otherclick_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[%d]/div[%d]/i "
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
        
    def input_firsttwoinput (self,lineindex,text):
        self.firsttwoinput_loc=(By.XPATH,self.firsttwoinput_path %lineindex)
        self.find_element(*self.firsttwoinput_loc).send_keys(text); 
        
    def input_midinput (self,lineindex2,text):
        self.midinput_loc=(By.XPATH,self.midinput_path %lineindex2)
        self.find_element(*self.midinput_loc).send_keys(text);
        
    def input_lastthreeinput(self,lineindex3,text):
        self.lastthreeinput_loc=(By.XPATH,self.lastthreeinput_path %lineindex3)
        self.find_element(*self.lastthreeinput_loc).send_keys(text);
        
    def click_firsttwoclick (self,moduleindex,lineindex4,columnindex):
        self.firsttwoclick_loc=(By.XPATH,self.firsttwoclick_path %(moduleindex,lineindex4,columnindex,))
        self.find_element(*self.firsttwoclick_loc).click()
        
    def click_otherclick (self,moduleindex2,lineindex5,columnindex2):
        self.otherclick_loc=(By.XPATH,self.otherclick_path %(moduleindex2,lineindex5,columnindex2))
        self.find_element(*self.otherclick_loc).click()
        