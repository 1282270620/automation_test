'''
Created on 20170705

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class BehaviorCoachingForm(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.firstfourcomments_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div[%d]/div[2]/input"
        self.lastfourcomments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea" 
        self.firstfourcomments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div[%d]/div"
        self.lastfourcomments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        self.CoachName_path="//*[@id='container']/div/section/div/div/div/div/div[2]/div/span"
        self.CoachNameselect_path="//*[@id='container']/div/section/div/div/div/div/div[2]/div/ul/li/a"
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path % checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.Input_text(text,*self.callRecordingNumber_loc)
        
    def get_callRecordingNumber(self):
        return self.find_element(*self.callRecordingNumber_loc).get_attribute("value")
            
    def callRecordingNumber_disabled(self):
        flag=self.find_element(*self.callRecordingNumber_loc).get_attribute("disabled")
        
    def input_firstfourcomments (self,lineindex,text):
        self.firstfourcomments_loc=(By.XPATH,self.firstfourcomments_path %lineindex)
        self.Input_text(text,*self.firstfourcomments_loc)
    
    def get_firstfourcomments(self,lineindex):
        self.firstfourcomments_loc=(By.XPATH,self.firstfourcomments_path %lineindex)
        return self.find_element(*self.firstfourcomments_loc).get_attribute("value")
    
    def firstfourcomments_disabled(self,lineindex):
        self.firstfourcomments_loc=(By.XPATH,self.firstfourcomments_path %lineindex)
        flag=self.find_element(*self.firstfourcomments_loc).get_attribute("disabled")
        return flag 
    
    def get_firstfourcommentsBoxTitle(self,lineindex):
        self.firstfourcomments_title_loc=(By.XPATH,self.firstfourcomments_title_path %lineindex)
        return self.find_element(*self.firstfourcomments_title_loc).text
        
    def input_lastfourcomments (self,lineindex,text):
        self.lastfourcomments_loc=(By.XPATH,self.lastfourcomments_path %lineindex)
        self.Input_text(text,*self.lastfourcomments_loc)
        
    def get_lastfourcomments(self,lineindex):
        self.lastfourcomments_loc=(By.XPATH,self.lastfourcomments_path %lineindex)
        return self.find_element(*self.lastfourcomments_loc).get_attribute("value")
    
    def lastfourcomments_disabled(self,lineindex):
        self.lastfourcomments_loc=(By.XPATH,self.lastfourcomments_path %lineindex)
        flag=self.find_element(*self.lastfourcomments_loc).get_attribute("disabled")
        return flag 
    
    def get_lastfourcommentsBoxTitle(self,lineindex):
        self.lastfourcomments_title_loc=(By.XPATH,self.lastfourcomments_title_path %lineindex)
        return self.find_element(*self.lastfourcomments_title_loc).text
    
    def click_CoachName(self):
        self.CoachName_loc=(By.XPATH,self.CoachName_path)
        self.find_element(*self.CoachName_loc).click()
        
    def click_CoachNameselect(self):
        self.CoachNameselect_loc=(By.XPATH,self.CoachNameselect_path)
        self.find_element(*self.CoachNameselect_loc).click()