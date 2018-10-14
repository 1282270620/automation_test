'''
Created on 2018.2.11

@author: haodong.liu
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class TeamHuddleProcessConfirmationFormPage(BasePage.Action):
    

    def __init__(self):
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i'
        self.TimeButton_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div/div/div[2]/span/span'
        self.DayButton_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[%d]/td[%d]'
        self.DateComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div/div/div[2]/input'
        self.KpiComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[%d]/input'
        self.TopicComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/input')
        self.LongComments_path='//*[@id="container"]/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/textarea'
        self.LastLongComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea'
        self.RadioButton_path='//*[@id="container"]/div/section/div/form/div[2]/table/tbody/tr[%d]/td[3]/div[%d]/i'
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
    
    def Click_TimeButton(self,index):
        self.TimeButton_loc=(By.XPATH,self.TimeButton_path %index)
        self.find_element(*self.TimeButton_loc).click()
    def TimeButton_disabled(self,index):
        self.TimeButton_loc=(By.XPATH,self.TimeButton_path %index)
        flag=self.find_element(*self.TimeButton_loc).get_attribute('disabled')
        return flag
    
    def Click_DayButton(self,index1,index2,index3):
        self.DayButton=(By.XPATH,self.DayButton_path %(index1,index2,index3))
        self.find_element(*self.DayButton).click()
        
    def click_RadioButton(self,index1,index2):
        self.RadioButton_loc=(By.XPATH,self.RadioButton_path %(index1,index2))
        self.find_element(*self.RadioButton_loc).click()
    def get_RadioButtonStatus(self,index1,index2):
        self.RadioButton_loc=(By.XPATH,self.RadioButton_path %(index1,index2))
        return self.find_element(*self.RadioButton_loc).get_attribute('class')
    
    def Input_KpiComments(self,index,text):
        self.KpiComments_loc=(By.XPATH,self.KpiComments_path %index)
        self.find_element(*self.KpiComments_loc).clear()
        self.find_element(*self.KpiComments_loc).send_keys(text)
    def get_KpiComments(self,index):
        self.KpiComments_loc=(By.XPATH,self.KpiComments_path %index)
        return self.find_element(*self.KpiComments_loc).get_attribute('value')
    def KpiComments_disabled(self,index):
        self.KpiComments_loc=(By.XPATH,self.KpiComments_path %index)
        flag=self.find_element(*self.KpiComments_loc).get_attribute('disabled')
        return flag
    
    def Input_DateComments(self,index,text):
        self.DateComments_loc=(By.XPATH,self.DateComments_path %index)
        self.find_element(*self.DateComments_loc).clear()
        self.find_element(*self.DateComments_loc).send_keys(text)
    def get_DateComments(self,index):
        self.DateComments_loc=(By.XPATH,self.DateComments_path %index)
        return self.find_element(*self.DateComments_loc).get_attribute('value')
    def DateComments_disabled(self,index):
        self.DateComments_loc=(By.XPATH,self.DateComments_path %index)
        flag=self.find_element(*self.DateComments_loc).get_attribute('disabled')
        return flag
    
    def Input_TopicComments(self,text):
        self.find_element(*self.TopicComments_loc).clear()
        self.find_element(*self.TopicComments_loc).send_keys(text)
    def get_TopicComments(self):
        return self.find_element(*self.TopicComments_loc).get_attribute('value')
    def TopicComments_disabled(self):
        flag=self.find_element(*self.TopicComments_loc).get_attribute('disabled')
        return flag
    
    def Input_LongComments(self,index,text):
        self.LongComments_loc=(By.XPATH,self.LongComments_path %index)
        self.find_element(*self.LongComments_loc).clear()
        self.find_element(*self.LongComments_loc).send_keys(text)
    def get_LongComments(self,index):
        self.LongComments_loc=(By.XPATH,self.LongComments_path %index)
        return self.find_element(*self.LongComments_loc).text
    def LongComments_disabled(self,index):
        self.LongComments_loc=(By.XPATH,self.LongComments_path %index)
        flag=self.find_element(*self.LongComments_loc).get_attribute('disabled')
        return flag
    
    def Input_LastLongComments(self,index,text):
        self.LastLongComments_loc=(By.XPATH,self.LastLongComments_path %index)
        self.find_element(*self.LastLongComments_loc).clear()
        self.find_element(*self.LastLongComments_loc).send_keys(text)
    def get_LastLongComments(self,index):
        self.LastLongComments_loc=(By.XPATH,self.LastLongComments_path %index)
        return self.find_element(*self.LastLongComments_loc).text
    def LastLongComments_disabled(self,index):
        self.LastLongComments_loc=(By.XPATH,self.LastLongComments_path %index)
        flag=self.find_element(*self.LastLongComments_loc).get_attribute('disabled')
        return flag
    
    
    
    
    
    
