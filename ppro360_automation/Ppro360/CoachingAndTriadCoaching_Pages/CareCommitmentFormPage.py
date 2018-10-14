'''
Created on 2018.1.12

@author: haodong.liu
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class CareCommitmentFormPage(BasePage.Action):
    
    def __init__(self):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[3]/td[%d]/i'
        self.FirstLongComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/textarea')
        self.SecondLongComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[11]/div/textarea')
        self.LastLongComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[12]/div/textarea')
        self.BodyShortComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/div[%d]/div/div[%d]/textarea'
        self.LongTextboxTitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label'
        self.ShortTextboxTitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/div[%d]/div/div[%d]/label'
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def get_LongTextboxTitle_loc(self,boxindex):
        LongTextboxTitle_loc=(By.XPATH, self.LongTextboxTitle_path %boxindex)
        return self.find_element(*LongTextboxTitle_loc).text
    def get_ShortTextboxTitle_loc(self,lineindex,moduleindex,columnindex):
        LongTextboxTitle_loc=(By.XPATH, self.ShortTextboxTitle_path %(lineindex,moduleindex,columnindex))
        return self.find_element(*LongTextboxTitle_loc).text
        
    def input_FirstLongComments(self,inputtext):
        self.find_element(*self.FirstLongComments_loc).clear()
        self.find_element(*self.FirstLongComments_loc).send_keys(inputtext)
    def getFirstLongComments_loc(self):
        return self.find_element(*self.FirstLongComments_loc).text
    def FirstLongComments_disabled(self):
        flag=self.find_element(*self.FirstLongComments_loc).get_attribute("disabled")
        return flag
    
    def input_SecondLongComments(self,inputtext):
        self.find_element(*self.SecondLongComments_loc).clear()
        self.find_element(*self.SecondLongComments_loc).send_keys(inputtext)
    def getSecondLongComments_loc(self):
        return self.find_element(*self.SecondLongComments_loc).text
    def SecondLongComments_disabled(self):
        flag=self.find_element(*self.SecondLongComments_loc).get_attribute("disabled")
        return flag
    
    def input_LastLongComments(self,inputtext):
        self.find_element(*self.LastLongComments_loc).clear()
        self.find_element(*self.LastLongComments_loc).send_keys(inputtext)
    def getLastLongComments_loc(self):
        return self.find_element(*self.LastLongComments_loc).text
    def LastLongComments_disabled(self):
        flag=self.find_element(*self.LastLongComments_loc).get_attribute("disabled")
        return flag
    
    def input_BodyShortComments(self,lineindex,moduleindex,columnindex,inputtext):
        self.BodyShortComments_loc=(By.XPATH,self.BodyShortComments_path %(lineindex,moduleindex,columnindex))
        self.find_element(*self.BodyShortComments_loc).clear()
        self.find_element(*self.BodyShortComments_loc).send_keys(inputtext)
    def getBodyShortComments_loc(self,lineindex,moduleindex,columnindex):
        self.BodyShortComments_loc=(By.XPATH,self.BodyShortComments_path %(lineindex,moduleindex,columnindex))
        return self.find_element(*self.BodyShortComments_loc).text
    def BodyShortComments_disabled(self,lineindex,moduleindex,columnindex):
        self.BodyShortComments_loc=(By.XPATH,self.BodyShortComments_path %(lineindex,moduleindex,columnindex))
        flag=self.find_element(*self.BodyShortComments_loc).get_attribute("disabled")
        return flag
        