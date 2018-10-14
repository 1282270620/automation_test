'''
Created on 2018.02.27

@author: haodong.liu
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class SideBySideProcessConfirmationPage(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.BodyComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div[4]/textarea'
        self.LastThreeComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea'
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, self.KPIcheckbox_path %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
    
    def input_BodyComments(self,index,text):
        self.BodyComments_loc=(By.XPATH,self.BodyComments_path %index)
        self.find_element(*self.BodyComments_loc).send_keys(text)
    def get_BodyComments(self,index):
        self.BodyComments_loc=(By.XPATH,self.BodyComments_path %index)
        return self.find_element(*self.BodyComments_loc).text
    def BodyComments_disabled(self,index):
        self.BodyComments_loc=(By.XPATH,self.BodyComments_path %index)
        flag=self.find_element(*self.BodyComments_loc).get_attribute("disabled")
        return flag
    
    def input_LastThreeComments(self,index,text):
        self.LastThreeComments_loc=(By.XPATH,self.LastThreeComments_path %index)
        self.find_element(*self.LastThreeComments_loc).send_keys(text)
    def get_LastThreeComments(self,index):
        self.LastThreeComments_loc=(By.XPATH,self.LastThreeComments_path %index)
        return self.find_element(*self.LastThreeComments_loc).text
    def LastThreeComments_disabled(self,index):
        self.LastThreeComments_loc=(By.XPATH,self.LastThreeComments_path %index)
        flag=self.find_element(*self.LastThreeComments_loc).get_attribute("disabled")
        return flag