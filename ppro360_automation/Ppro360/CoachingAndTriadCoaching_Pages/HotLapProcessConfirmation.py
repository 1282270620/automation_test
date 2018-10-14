'''
Created on 20171101

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class HotLapProcessConfirmation(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.comments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.comments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        self.scoreinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/div[4]/input"
        self.scoreballstataus_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/div[4]/i"
        self.overallscore_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/label/div[2]/input")
        self.overallball_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/label/div[2]/i")
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
        
    def input_comments(self,lineindex,text):
        self.comments_loc=(By.XPATH,self.comments_path %lineindex)
        self.Input_text(text,*self.comments_loc)
    
    def get_comments(self,lineindex):
        self.comments_loc=(By.XPATH,self.comments_path %lineindex )
        return self.find_element(*self.comments_loc).get_attribute("value")

    def comments_disabled(self,lineindex):
        self.comments_loc=(By.XPATH,self.comments_path %lineindex )
        flag=self.find_element(*self.comments_loc).get_attribute("disabled")
        return flag 
        
    def get_commentsBoxtitle(self,lineindex):
        self.comments_title_loc=(By.XPATH,self.comments_title_path %lineindex)
        return self.find_element(*self.comments_title_loc).text
    
    def input_scoreinput(self,lineindex,text):
        self.scoreinput_loc=(By.XPATH,self.scoreinput_path %lineindex)
        self.Input_text(text,*self.scoreinput_loc)
        
    def get_scoreinput(self,lineindex):
        self.scoreinput_loc=(By.XPATH,self.scoreinput_path %lineindex )
        return self.find_element(*self.scoreinput_loc).get_attribute("value")

    def scoreinput_disabled(self,lineindex):
        self.scoreinput_loc=(By.XPATH,self.scoreinput_path %lineindex )
        flag=self.find_element(*self.scoreinput_loc).get_attribute("disabled")
        return flag 
        
    def get_scoreballstataus(self,lineindex):
        scoreballstataus_loc=(By.XPATH,self.scoreballstataus_path %lineindex )
        scoreballstataus=self.find_element(*scoreballstataus_loc).get_attribute("class")
        return scoreballstataus
        
    def get_overallscore(self):
        return self.find_element(*self.overallscore_loc).get_attribute("value")
    
    def overallscore_disabled(self):
        flag=self.find_element(*self.overallscore_loc).get_attribute("disabled")
        return flag

    def get_overallballstataus(self):
        scoreballstataus=self.find_element(*self.overallball_loc).get_attribute("class")
        return scoreballstataus
        
        
