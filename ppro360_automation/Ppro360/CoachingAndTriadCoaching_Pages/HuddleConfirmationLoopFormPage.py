'''
Created on 2018.3.14

@author: haodong.liu
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class HuddleConfirmationLoopFormPage(BasePage.Action):
    
    def __init__(self):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[3]/td[%d]/i'
        self.TheFirstFouComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[%d]/div[%d]/div[2]/input'
        self.DateComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[3]/div[%d]/div[2]/div/div/div[2]/input'
        self.DateButton_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[3]/div[%d]/div[2]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[1]/td[1]'
        self.Date_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[3]/div[%d]/div[2]/div/div/div[2]/span/span'
        self.RemarksComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[4]/div/div[2]/input')
        self.BodyComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[3]/textarea'
        self.OverallScoreComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[7]/div[2]/input')
        self.OverallScoreColor_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[7]/div[2]/i')
        self.ScoreButton_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[4]/div[%d]/i'
        self.LastComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea'
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
    
    def click_Date(self,index):
        self.DateButton_loc=(By.XPATH, self.DateButton_path %index)
        self.find_element(*self.DateButton_loc).click()
    def click_DateButton(self,index):
        self.Date_loc=(By.XPATH, self.Date_path %index)
        self.find_element(*self.Date_loc).click()
    def DateComments_disabled(self,index):
        self.DateComments_loc=(By.XPATH, self.DateComments_path %index)
        return self.find_element(*self.DateComments_loc).get_attribute("disabled")
        
    def input_TheFirstFour(self,index1,index2,text):
        self.FirstFourComments_loc=(By.XPATH, self.TheFirstFouComments_path %(index1,index2))
        self.find_element(*self.FirstFourComments_loc).send_keys(text)
    def get_TheFirstFouComments(self,index1,index2):
        self.FirstFourComments_loc=(By.XPATH, self.TheFirstFouComments_path %(index1,index2))
        return self.find_element(*self.FirstFourComments_loc).get_attribute("value")
    def TheFirstFouComments_disabled(self,index1,index2):
        self.FirstFourComments_loc=(By.XPATH, self.TheFirstFouComments_path %(index1,index2))
        flag=self.find_element(*self.FirstFourComments_loc).get_attribute("disabled")
        return flag
    
    def input_BodyComments(self,index,text):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        self.find_element(*self.BodyComments_loc).send_keys(text)
    def get_BodyComments(self,index):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        return self.find_element(*self.BodyComments_loc).text
    def BodyComments_disabled(self,index):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        flag=self.find_element(*self.BodyComments_loc).get_attribute("disabled")
        return flag
    
    def input_RemarksComments(self,text):
        self.find_element(*self.RemarksComments_loc).send_keys(text)
    def get_RemarksComments(self):
        return self.find_element(*self.RemarksComments_loc).get_attribute("value")
    def RemarksComments_disabled(self):
        flag=self.find_element(*self.RemarksComments_loc).get_attribute("disabled")
        return flag
    
    def get_OverallScoreComments(self):
        return self.find_element(*self.OverallScoreComments_loc).get_attribute("value")
    def OverallScore_disabled(self):
        flag=self.find_element(*self.OverallScoreColor_loc).get_attribute("disabled")
        return flag
    def get_OverallScoreColor(self):
        return self.find_element(*self.OverallScoreColor_loc).get_attribute("class")
    
    def ClickScoreButton(self,index1,index2):
        self.ScoreButton_loc=(By.XPATH, self.ScoreButton_path %(index1,index2))
        self.find_element(*self.ScoreButton_loc).click()
    def get_ScoreButton(self,index1,index2):
        self.ScoreButton_loc=(By.XPATH, self.ScoreButton_path %(index1,index2))
        return self.find_element(*self.ScoreButton_loc).get_attribute("class")
    
    def input_LastComments(self,index,text):
        self.LastComments_loc=(By.XPATH, self.LastComments_path %index)
        self.find_element(*self.LastComments_loc).send_keys(text)
    def get_LastComments(self,index):
        self.LastComments_loc=(By.XPATH, self.LastComments_path %index)
        return self.find_element(*self.LastComments_loc).text
    def LastComments_disabled(self,index):
        self.LastComments_loc=(By.XPATH, self.LastComments_path %index)
        flag=self.find_element(*self.LastComments_loc).get_attribute("disabled")
        return flag
    
    
    
