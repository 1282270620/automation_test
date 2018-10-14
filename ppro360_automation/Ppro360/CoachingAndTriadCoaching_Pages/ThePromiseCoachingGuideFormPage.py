'''
Created on 20170626

@author: luming.zhao
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class ThePromiseCoachingGuideFormPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.customer_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/input")
        self.session_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.opportunity_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[10]/div/textarea")
        self.agentCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[11]/div/textarea")
    
    
    
    
    
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorderindex) 
        
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);   
        
    def input_customer(self,text):
        self.find_element(*self.customer_loc).send_keys(text);
        
    def input_session(self,text):
        self.find_element(*self.session_loc).send_keys(text);
        
#   def input_welcome(self,textarea,text):
#         self.welcome_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[3]/div[%d]/textarea" %textarea);
#         self.find_element(*self.welcome_loc).send_keys(text);    
#         
#   def input_need(self,textarea,text):
#         self.need_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[3]/div[%d]/textarea" %textarea);
#         self.find_element(*self.need_loc).send_keys(text); 
#         
#   def input_solution(self,textarea,text):
#         self.soulution_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[3]/div[%d]/textarea"%textarea)

        
    def input_bodybox(self,textareaindex,text,moduleindex):
        self.bodybox_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[3]/div[%d]/textarea" %(moduleindex,textareaindex));
        self.find_element(*self.bodybox_loc).send_keys(text);
      
    def input_opportunity(self,text):
        self.find_element(*self.opportunity_loc).send_keys(text);
      
    def input_agentCommitment(self,text):
        self.find_element(*self.agentCommitment_loc).send_keys(text);  
    
        
        
        
        