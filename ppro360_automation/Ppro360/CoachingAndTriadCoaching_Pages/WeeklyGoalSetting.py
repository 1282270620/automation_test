'''
Created on 2017.2.24

@author: yalan.yin
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
class  WeeklyGoalSetting(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''     
        
        self.KPIcheckbox_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i" )
        self.PerformanceReview_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[%d]/input"
        self.actionplan_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[1]/textarea")
        self.actionplan_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/label")
        self.agentcommitment_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/div/textarea")
        self.agentcommitment_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/label")
        self.TLcommitment_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[3]/div[3]/div/div/textarea")
        self.TLcommitment_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[3]/div/label")
            
    def click_KPIcheckbox (self):
        self.find_element (*self.KPIcheckbox_loc).click()
    
    def input_PerformanceReview (self,columnindex,lineindex,text):
        self.PerformanceReview_loc=(By.XPATH,self.PerformanceReview_path %(columnindex,lineindex))
        self.Input_text(text,*self.PerformanceReview_loc)
        
    def get_PerformanceReview(self,columnindex,lineindex):
        self.PerformanceReview_loc=(By.XPATH,self.PerformanceReview_path %(columnindex,lineindex))
        return self.find_element(*self.PerformanceReview_loc).get_attribute("value")
    
    def PerformanceReview_disabled(self,columnindex,lineindex):
        self.PerformanceReview_loc=(By.XPATH,self.PerformanceReview_path %(columnindex,lineindex))
        flag=self.find_element(*self.PerformanceReview_loc).get_attribute("disabled")
        return flag
    
    def input_actionplan (self,text):
        self.Input_text(text,*self.actionplan_loc)
        
    def get_actionplan(self):
        return self.find_element(*self.actionplan_loc).get_attribute("value")
    
    def actionplan_disabled(self):
        flag=self.find_element(*self.actionplan_loc).get_attribute("disabled")
        return flag 
    
    def get_actionplanBoxTitle(self):
        return self.find_element(*self.actionplan_title_loc).text
        
    def input_agentcommitment (self,text):
        self.Input_text(text,*self.agentcommitment_loc)
    
    def get_agentcommitment(self):
        return self.find_element(*self.agentcommitment_loc).get_attribute("value")
    
    def agentcommitment_disabled(self):
        flag=self.find_element(*self.agentcommitment_loc).get_attribute("disabled")
        return flag 
    
    def get_agentcommitmentBoxTitle(self):
        return self.find_element(*self.agentcommitment_title_loc).text
    
    def input_TLcommitment (self,text):
        self.Input_text(text,*self.TLcommitment_loc)
    
    def get_TLcommitment(self):
        return self.find_element(*self.TLcommitment_loc).get_attribute("value")
    
    def TLcommitment_disabled(self):
        flag=self.find_element(*self.TLcommitment_loc).get_attribute("disabled")
        return flag 
    
    def get_TLcommitmentBoxTitle(self):
        return self.find_element(*self.TLcommitment_title_loc).text
        
     
    