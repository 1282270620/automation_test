'''
Created on 20170703

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from cgitb import text

class TriLevelForm(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.seniorManagerCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.evaluator_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr/td/div/div/input")
        self.ani_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr/td/div/div[2]/input")
        self.keyStrengths_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.keyOpportunities_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.developmentGoals_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/div/textarea"
        self.keyelement_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td/div/textarea "
        self.teamManagerCommitment_path="//*[@id='container']/div/section/div/form/div[2]/table[2]/tbody/tr[%d]/td[2]/div/textarea"
        self.actionPlan_path="//*[@id='container']/div/section/div/form/div[2]/table[2]/tbody/tr[%d]/td[2]/div/textarea"
        self.chooseclick_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td/label/div/div[%d]/i " 
        
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
        
    def input_seniorManagerCommitment (self,text):
        self.find_element(*self.seniorManagerCommitment_loc).send_keys(text);
    
    def input_evaluator (self,text):
        self.find_element(*self.evaluator_loc).send_keys(text);
        
    def input_ani (self,text):
        self.find_element(*self.ani_loc).send_keys(text);
    
    def input_developmentGoals (self,text,lineindex):
        self.developmentGoals_loc=(By.XPATH,self.developmentGoals_path %lineindex)
        self.find_element(*self.developmentGoals_loc).send_keys(text);
    
    def input_keyelement (self,text,lineindex2):
        self.keyelement_loc=(By.XPATH,self.keyelement_path %lineindex2)
        self.find_element(*self.keyelement_loc).send_keys(text);
    
    def input_keyStrengths (self,text):
        self.find_element(*self.keyStrengths_loc).send_keys(text); 
        
    def input_keyOpportunities (self,text):
        self.find_element(*self.keyOpportunities_loc).send_keys(text); 
        
    def input_teamManagerCommitment (self,text,lineindex3):
        self.teamManagerCommitment_loc=(By.XPATH,self.teamManagerCommitment_path %lineindex3) 
        self.find_element(*self.teamManagerCommitment_loc).send_keys(text); 
        
    def input_actionPlan (self,text,lineindex4):
        self.actionPlan_loc=(By.XPATH,self.actionPlan_path %lineindex4) 
        self.find_element(*self.actionPlan_loc).send_keys(text); 
        
    def click_chooseclick (self,lineindex5,columnindex):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(lineindex5,columnindex))
        self.find_element(*self.chooseclick_loc).click()
        
        
        
        
        
        
        
        
        
         
        
        
        
        
