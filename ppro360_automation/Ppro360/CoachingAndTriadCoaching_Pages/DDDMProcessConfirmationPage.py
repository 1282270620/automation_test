'''
Created on 2018.3.5

@author: haodong.liu
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class DDDMProcessConfirmationPage(BasePage.Action):
    
    def __init__(self):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i'
        self.BodyComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div[4]/textarea'
        self.LastComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea'
        self.GradeComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div[5]/input'
        self.GrageColor_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div[5]/i'
        self.OverallScoreComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[7]/div[2]/input')
        self.OverallScoreColor_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[7]/div[2]/i')
        self.BodyTitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[%d]/div[2]'
        self.LastTitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label'
        
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
    
    def get_GradeColor(self,index):
        self.GrageColor_loc=(By.XPATH,self.GrageColor_path %index)
        return self.find_element(*self.GrageColor_loc).get_attribute("class")
    
    def get_OverallScoreComments(self):
        return self.find_element(*self.OverallScoreComments_loc).get_attribute("value")
    def get_OverallScoreColor(self):
        return self.find_element(*self.OverallScoreColor_loc).get_attribute("class")
    def OverallScore_disabled(self):
        flag=self.find_element(*self.OverallScoreComments_loc).get_attribute("disabled")
        return flag
    
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
    
    def input_GradeComments(self,index,text):
        self.GradeComments_loc=(By.XPATH, self.GradeComments_path %index)
        self.find_element(*self.GradeComments_loc).clear()
        self.find_element(*self.GradeComments_loc).send_keys(text)
    def get_GradeComments(self,index):
        self.GradeComments_loc=(By.XPATH, self.GradeComments_path %index)
        return self.find_element(*self.GradeComments_loc).get_attribute("value")
    def GradeComments_disabled(self,index):
        self.GradeComments_loc=(By.XPATH, self.GradeComments_path %index)
        flag=self.find_element(*self.GradeComments_loc).get_attribute("disabled")
        return flag
    
    def get_BodyTitle(self,index):
        self.BodyTitle_loc=(By.XPATH, self.BodyTitle_path %index)
        return self.find_element(*self.BodyTitle_loc).text
    def get_LastTitle(self,index):
        self.LastTitle_loc=(By.XPATH, self.LastTitle_path %index)
        return self.find_element(*self.LastTitle_loc).text