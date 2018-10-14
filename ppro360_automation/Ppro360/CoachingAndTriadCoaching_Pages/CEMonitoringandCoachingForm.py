'''
Created on 20170703

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from cgitb import text

class CEMonitoringandCoachingForm(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.immediateSupervisor_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[2]/div/input")
        self.operationsManager_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[3]/div/input")
        self.btn_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[4]/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.MonitoringType_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/span/span")
        self.CustomerType_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/span")
        self.MonitoringTypechoose_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/ul/li[%d]/a"
        self.CustomerTypechoose_path="//div[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/ul/li[%d]/a" 
        self.AgentbehaviorsaffectsCE_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/table/tbody/tr[%d]/td[2]/div/span"
        self.AgentbehaviorsaffectsCEchoose_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/table/tbody/tr[%d]/td[2]/div/ul/li[%d]/a"
        self.comments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def input_immediateSupervisor (self,text):
        self.find_element(*self.immediateSupervisor_loc).send_keys(text);
        
    def input_operationsManager (self,text):
        self.find_element(*self.operationsManager_loc).send_keys(text);
                
    def input_btn (self,text):
        self.find_element(*self.btn_loc).send_keys(text);
    
    def click_MonitoringType (self):
        self.find_element(*self.MonitoringType_loc).click()
        
    def click_MonitoringTypechoose (self,lineindex):
        self.MonitoringTypechoose_loc=(By.XPATH,self.MonitoringTypechoose_path %lineindex)
        self.find_element(*self.MonitoringTypechoose_loc).click()
    
    def click_CustomerType (self):
        self.find_element(*self.CustomerType_loc).click()
        
    def click_CustomerTypechoose (self,lineindex2):
        self.CustomerTypechoose_loc=(By.XPATH,self.CustomerTypechoose_path %lineindex2)
        self.find_element(*self.CustomerTypechoose_loc).click()
        
    def click_AgentbehaviorsaffectsCE (self,moduleindex):
        self.AgentbehaviorsaffectsCE_loc=(By.XPATH,self.AgentbehaviorsaffectsCE_path %moduleindex)
        self.find_element(*self.AgentbehaviorsaffectsCE_loc).click()
        
    def click_AgentbehaviorsaffectsCEchoose (self,moduleindex,lineindex3):
        self.AgentbehaviorsaffectsCEchoose_loc=(By.XPATH,self.AgentbehaviorsaffectsCEchoose_path %(moduleindex,lineindex3))
        self.find_element(*self.AgentbehaviorsaffectsCEchoose_loc).click()
    
    def input_comments (self,text,lineindex4):
        self.comments_loc=(By.XPATH,self.comments_path %lineindex4)
        self.find_element(*self.comments_loc).send_keys(text);
    
        
        

        
        