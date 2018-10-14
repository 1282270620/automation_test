'''
Created on 2018.3.1

@author: haodong.liu
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class PerformanceDailyCoachingPage(BasePage.Action):
    
    def __init__(self):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i'
        self.Long1Comments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea'
        self.Long2Comments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/div[%d]/div[2]/textarea'
        self.Title_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label'
        self.LastKpi_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[9]/i')
  
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def click_LastKpi(self):
        self.find_element(*self.LastKpi_loc).click()
    def get_LastKpiStatus(self):
        return self.find_element(*self.LastKpi_loc).get_attribute("class")
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
    
    def input_Long1Comments(self,index,text):
        self.Long1Comments_loc=(By.XPATH,self.Long1Comments_path %index)
        self.find_element(*self.Long1Comments_loc).send_keys(text)
    def get_Long1Comments(self,index):
        self.Long1Comments_loc=(By.XPATH,self.Long1Comments_path %index)
        return self.find_element(*self.Long1Comments_loc).text
    def Long1Comments_disabled(self,index):
        self.Long1Comments_loc=(By.XPATH,self.Long1Comments_path %index)
        flag=self.find_element(*self.Long1Comments_loc).get_attribute("disabled")
        return flag
    
    def input_Long2Comments(self,index1,index2,text):
        self.Long2Comments_loc=(By.XPATH,self.Long2Comments_path %(index1,index2))
        self.find_element(*self.Long2Comments_loc).send_keys(text)
    def get_Long2Comments(self,index1,index2):
        self.Long2Comments_loc=(By.XPATH,self.Long2Comments_path %(index1,index2))
        return self.find_element(*self.Long2Comments_loc).text
    def Long2Comments_disabled(self,index1,index2):
        self.Long2Comments_loc=(By.XPATH,self.Long2Comments_path %(index1,index2))
        flag=self.find_element(*self.Long2Comments_loc).get_attribute("disabled")
        return flag
    
    def get_TitleComments(self,index):
        self.Tile_loc=(By.XPATH,self.Title_path %index)
        return self.find_element(*self.Tile_loc).text