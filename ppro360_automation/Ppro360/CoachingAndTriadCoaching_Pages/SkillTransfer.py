'''
Created on 20170307

@author: luming.zhao
'''

from Tablet_pages import BasePage
from selenium.webdriver.common.by import By


class SkillTransfer(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.focus_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.focus_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/label")
        self.importance_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.importance_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/label")
        self.how_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.how_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/label")
        self.achieve_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        self.achieve_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/label")
        self.explain_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[%d]/i"
        self.show_path="//*[@id='container']/div/section/div/form/div[2]/div[7]/div[%d]/i"
        self.practice_path="//*[@id='container']/div/section/div/form/div[2]/div[8]/div[%d]/i"
        self.completebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[3]")
            
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path % checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.Input_text(text,*self.callRecordingNumber_loc)
        
    def get_callRecordingNumber(self):
        return self.find_element(*self.callRecordingNumber_loc).get_attribute("value")
            
    def callRecordingNumber_disabled(self):
        flag=self.find_element(*self.callRecordingNumber_loc).get_attribute("disabled")    
    

    def input_focus (self,text):
        self.Input_text(text,*self.focus_loc)
    
    def get_focus(self):
        return self.find_element(*self.focus_loc).get_attribute("value")
    
    def focus_disabled(self):
        flag=self.find_element(*self.focus_loc).get_attribute("disabled")
        return flag 
    
    def get_focusBoxTitle(self):
        return self.find_element(*self.focus_title_loc).text
     
    def input_importance (self,text):
        self.Input_text(text,*self.importance_loc)
    
    def get_importance(self):
        return self.find_element(*self.importance_loc).get_attribute("value")
    
    def importance_disabled(self):
        flag=self.find_element(*self.importance_loc).get_attribute("disabled")
        return flag
    
    def get_importanceBoxTitle(self):
        return self.find_element(*self.importance_title_loc).text
             
    def input_how (self,text):
        self.Input_text(text,*self.how_loc)
    
    def get_how(self):
        return self.find_element(*self.how_loc).get_attribute("value")
    
    def how_disabled(self):
        flag=self.find_element(*self.how_loc).get_attribute("disabled")
        return flag 
    
    def get_howBoxTitle(self):
        return self.find_element(*self.how_title_loc).text
    

    def input_achieve (self,text):
        self.Input_text(text,*self.achieve_loc)
    
    def get_achieve(self):
        return self.find_element(*self.achieve_loc).get_attribute("value")
    
    def achieve_disabled(self):
        flag=self.find_element(*self.achieve_loc).get_attribute("disabled")
        return flag 
    
    def get_achieveBoxTitle(self):
        return self.find_element(*self.achieve_title_loc).text
        
    def click_explain(self,lineindex):
        self.explain_loc=(By.XPATH,self.explain_path %lineindex)
        self.find_element(*self.explain_yes).click()
        
    def get_explainBoxStatus(self,lineindex):
        explainBoxStatus_loc=(By.XPATH,self.explain_path % lineindex)
        explainBoxStatus=self.find_element(*explainBoxStatus_loc).get_attribute("class")
        return explainBoxStatus
      
    def click_show(self,lineindex):
        self.show_loc=(By.XPATH,self.show_path %lineindex)
        self.find_element(*self.show_loc).click()

    def get_showBoxStatus(self,lineindex):
        showBoxStatus_loc=(By.XPATH,self.show_path % lineindex)
        showBoxStatus=self.find_element(*showBoxStatus_loc).get_attribute("class")
        return showBoxStatus
    
    def click_practice(self,lineindex):
        self.practice_loc=(By.XPATH,self.practice_path %lineindex)
        self.find_element(*self.practice_loc).click()
        
    def get_practiceBoxStatus(self,lineindex):
        practiceBoxStatus_loc=(By.XPATH,self.practice_path % lineindex)
        practiceBoxStatus=self.find_element(*practiceBoxStatus_loc).get_attribute("class")
        return practiceBoxStatus
        
    def click_completebutton(self):
        self.find_element(*self.completebutton_loc).click()
        
        
        
        