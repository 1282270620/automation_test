'''
Created on 20170626

@author: luming.zhao
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By


class OneToOneCoachingLoopPage(BasePage.Action):
  
   
        
     
    def __init__(self):
        '''
        Constructor
        '''
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.agent_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr/td/div/div/input")
        self.interaction_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr/td/div/div[2]/input")
        self.strengths_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.opportunities_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.commitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.feedback_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        
    def click_KPIcheckbox (self,checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorderindex) 
        
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
        
    def input_agent(self,text):
        self.find_element(*self.agent_loc).send_keys(text);
        
    def input_interaction(self,text):
        self.find_element(*self.interaction_loc).send_keys(text);
        
    def input_textbody(self,text,lineindex):
        self.textbody_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td/div/textarea" %lineindex)
        self.find_element(*self.textbody_loc).send_keys(text);
        
    def input_strengths(self,text):
        self.find_element(*self.strengths_loc).send_keys(text);
        
    def input_opportunities(self,text):
        self.find_element(*self.opportunities_loc).send_keys(text);
    
    def input_commitment(self,text):
        self.find_element(*self.commitment_loc).send_keys(text);
    
    
    def input_feedback(self,text):
        self.find_element(*self.feedback_loc).send_keys(text);
        
    def select_eachRadio(self,lineindex,radioindex):
        self.eachRadio_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td/label/div/div[%d]/i" %(lineindex,radioindex));
        self.find_element(*self.eachRadio_loc).click()