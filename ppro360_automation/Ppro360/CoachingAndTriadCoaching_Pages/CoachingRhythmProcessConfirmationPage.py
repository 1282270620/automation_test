'''
Created on 2018.2.1

@author: haodong.liu
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class CoachingRhythmProcessConfirmationPage(BasePage.Action):
    
    
    def __init__(self):
        self.callRecordingNumber_path=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[3]/td[%d]/i'
        self.LongComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea'
        self.shortComments_path='//*[@id="container"]/div/section/div/form/div[2]/table/tbody/tr[%d]/td[%d]/textarea'
        self.RadioButton_path='//*[@id="container"]/div/section/div/form/div[2]/table/tbody/tr[%d]/td[%d]/div[%d]/i'
        self.LongTiltle_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label'
        self.ShortTiltle_path='//*[@id="container"]/div/section/div/form/div[2]/table/tbody/tr[%d]/td[%d]'
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def click_RadioButton(self,index1,index2,index3):
        self.RadioButton_loc=(By.XPATH,self.RadioButton_path %(index1,index2,index3))
        self.find_element(*self.RadioButton_loc).click()
    def get_RadioButtonStatus(self,index1,index2,index3):
        self.RadioButton_loc=(By.XPATH,self.RadioButton_path %(index1,index2,index3))
        return self.find_element(*self.RadioButton_loc).get_attribute('class')
    
    def Yes_disabled(self,index1,index2):
        self.Yes_loc=(By.XPATH,self.Yes_path %(index1,index2))
        self.find_element(*self.Yes_loc).get_attribute('disabled')
    
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_path).send_keys(text);
    
    def getLongTiltle(self,index):
        self.LongTiltle_loc=(By.XPATH,self.LongTiltle_path %index)
        return self.find_element(*self.LongTiltle_loc).text
    def getShortTiltle(self,index1,index2):
        self.ShortTiltle_loc=(By.XPATH,self.ShortTiltle_path %(index1,index2))
        return self.find_element(*self.ShortTiltle_loc).text
    
    def input_LongComments(self,index,inputtext):
        self.LongComments_loc=(By.XPATH,self.LongComments_path %index)
        self.find_element(*self.LongComments_loc).clear()
        self.find_element(*self.LongComments_loc).send_keys(inputtext)
    def get_LongComments(self,index):
        self.LongComments_loc=(By.XPATH,self.LongComments_path %index)
        return self.find_element(*self.LongComments_loc).text
    def LongComments_disable(self,index):
        self.LongComments_loc=(By.XPATH,self.LongComments_path %index)
        flag=self.find_element(*self.LongComments_loc).get_attribute('disabled')
        return flag
    
    def Input_ShortComments(self,index1,index2,inputtext):
        self.shortComments_loc=(By.XPATH,self.shortComments_path %(index1,index2))
        self.find_element(*self.shortComments_loc).clear()
        self.find_element(*self.shortComments_loc).send_keys(inputtext)
    def get_ShortComments(self,index1,index2):
        self.shortComments_loc=(By.XPATH,self.shortComments_path %(index1,index2))
        return self.find_element(*self.shortComments_loc).text
    def ShortComments_disable(self,index1,index2):
        self.shortComments_loc=(By.XPATH,self.shortComments_path %(index1,index2))
        flag=self.find_element(*self.shortComments_loc).get_attribute('disabled')
        return flag
    
    