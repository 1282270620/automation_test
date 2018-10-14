'''
Created on 2018.3.28

@author: haodong.liu
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class ICHYWTFormPage(BasePage.Action):
    
    def __init__(self):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[3]/td[%d]/i'
        self.BodyButton_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/div[%d]/i'
        self.BodyComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[3]/input'

    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
    
    def Click_BodyButton(self,index1,index2):
        self.BoduButton_loc=(By.XPATH, self.BodyButton_path %(index1,index2))
        self.find_element(*self.BoduButton_loc).click()
    def get_BodyButtonStatus(self,index1,index2):
        self.BoduButton_loc=(By.XPATH, self.BodyButton_path %(index1,index2))
        return self.find_element(*self.BoduButton_loc).get_attribute("class")
    
    def input_BodyComments(self,index,text):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        self.find_element(*self.BodyComments_loc).clear()
        self.find_element(*self.BodyComments_loc).send_keys(text)
    def get_BodyComments(self,index):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        return self.find_element(*self.BodyComments_loc).get_attribute("value")
    def BodyComments_disabled(self,index):
        self.BodyComments_loc=(By.XPATH, self.BodyComments_path %index)
        flag=self.find_element(*self.BodyComments_loc).get_attribute("disabled")
        return flag
        