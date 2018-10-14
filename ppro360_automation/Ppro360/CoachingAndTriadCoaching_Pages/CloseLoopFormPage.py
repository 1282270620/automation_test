'''
Created on 2018.3.27

@author: haodong.liu
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class CloseLoopFormPage(BasePage.Action):
    
    def __init__(self):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[3]/td[%d]/i'
        self.TextKpiComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[%d]/div[%d]/div[2]/input'
        self.RemarkComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[4]/div/div[2]/input')
        self.DateButton_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[3]/div[%d]/div[2]/div/div/div[2]/span/span'
        self.Date_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/div[3]/div[%d]/div[2]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[1]/td[1]'
        self.BodyComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[3]/textarea'
        self.ClickBodyButton_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[4]/div[%d]/i'
        self.LastComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea'

    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_TextKpiComments(self,index1,index2,text):
        self.TextKpiComments_loc=(By.XPATH, self.TextKpiComments_path %(index1,index2))
        self.find_element(*self.TextKpiComments_loc).clear()
        self.find_element(*self.TextKpiComments_loc).send_keys(text)
    def get_TextKpiComments(self,index1,index2):
        self.TextKpiComments_loc=(By.XPATH, self.TextKpiComments_path %(index1,index2))
        return self.find_element(*self.TextKpiComments_loc).get_attribute("value")
    def TextKpiComments_disabled(self,index1,index2):
        self.TextKpiComments_loc=(By.XPATH, self.TextKpiComments_path %(index1,index2))
        flag=self.find_element(*self.TextKpiComments_loc).get_attribute("disabled")
        return flag
    
    def input_RemarkComments(self,text):
        self.find_element(*self.RemarkComments_loc).clear()
        self.find_element(*self.RemarkComments_loc).send_keys(text)
    def get_RemarkComments(self):
        return self.find_element(*self.RemarkComments_loc).get_attribute("value")
    def RemarkComments_disabled(self):
        flag=self.find_element(*self.RemarkComments_loc).get_attribute("disabled")
        return flag
    
    def click_DateButton(self,index):
        self.DateButton_loc=(By.XPATH, self.DateButton_path %index)
        self.find_element(*self.DateButton_loc).click()
    def click_Date(self,index):
        self.Date_loc=(By.XPATH, self.Date_path %index)
        self.find_element(*self.Date_loc).click()
    
    def input_BodyComments(self,index,text):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        self.find_element(*self.BodyComments_loc).clear()
        self.find_element(*self.BodyComments_loc).send_keys(text)
    def get_BodyComments(self,index):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        return self.find_element(*self.BodyComments_loc).text
    def BodyComments_disabled(self,index):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        flag=self.find_element(*self.BodyComments_loc).get_attribute("disabled")
        return flag
    
    def Click_BodyButton(self,index1,index2):
        self.BodyButton_loc=(By.XPATH, self.ClickBodyButton_path %(index1,index2))
        self.find_element(*self.BodyButton_loc).click()
    def get_BodyButtonStatus(self,index1,index2):
        self.BodyButton_loc=(By.XPATH, self.ClickBodyButton_path %(index1,index2))
        return self.find_element(*self.BodyButton_loc).get_attribute("class")
    
    def get_OverScoreComments(self):
        self.OverScoreComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[7]/div[2]/input')
        return self.find_element(*self.OverScoreComments_loc).get_attribute("value")
    def get_OverScoreStatus(self):
        self.OverScoreStatus_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[7]/div[2]/i')
        return self.find_element(*self.OverScoreStatus_loc).get_attribute("class")
    
    
    def input_LastComments(self,index,text):
        self.LastComments_loc=(By.XPATH, self.LastComments_path %index)
        self.find_element(*self.LastComments_loc).clear()
        self.find_element(*self.LastComments_loc).send_keys(text)
    def get_LastComments(self,index):
        self.LastComments_loc=(By.XPATH, self.LastComments_path %index)
        return self.find_element(*self.LastComments_loc).text
    def LastComments_disabled(self,index):
        self.LastComments_loc=(By.XPATH, self.LastComments_path %index)
        flag=self.find_element(*self.LastComments_loc).get_attribute("disabled")
        return flag
    
    
    
    