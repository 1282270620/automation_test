'''
Created on 20170721

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class MeetGreetGTNKProcessConfirmation(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div/div/table/tbody/tr[4]/td[%d]/i"
        self.comments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.comments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.Input_text(text,*self.callRecordingNumber_loc)
        
    def get_callRecordingNumber(self):
        return self.find_element(*self.callRecordingNumber_loc).get_attribute("value")
            
    def callRecordingNumber_disabled(self):
        flag=self.find_element(*self.callRecordingNumber_loc).get_attribute("disabled")
        
    def input_comments(self,lineindex,text,):
        self.comments_loc=(By.XPATH,self.comments_path %lineindex)
        self.Input_text(text,*self.comments_loc)
    
    def get_comments(self,lineindex2):
        self.comments_loc=(By.XPATH,self.comments_path %lineindex2)
        return self.find_element(*self.comments_loc).get_attribute("value")
    
    def comments_disabled(self,lineindex3):
        self.comments_loc=(By.XPATH,self.comments_path %lineindex3)
        flag=self.find_element(*self.comments_loc).get_attribute("disabled")
        return flag 
    def get_commentsBoxTitle(self,lineindex4):
        self.comments_title_loc=(By.XPATH,self.comments_title_path %lineindex4)
        return self.find_element(*self.comments_title_loc).text