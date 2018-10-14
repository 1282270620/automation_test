'''
Created on 2017/3/6

@author: luming.zhao
'''


from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class VXIDevelopmental(BasePage.Action):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.strength_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr/td/div/textarea")
        self.opportunity_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr/td[2]/div/textarea")
        self.kpiRelation_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr/td[3]/div/textarea")
        self.rootCauseAnalysis_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.rcaCategory_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/div/input")
        self.actionPlanning_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.agentCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/div/div/textarea")
        self.leaderComitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[3]/div/div/textarea")
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")
        self.callRecordingID_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.strength_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/thead/tr/th")
        self.opportunity_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/thead/tr/th[2]")
        self.kpiRelation_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/thead/tr/th[3]")
        self.rootCauseAnalysis_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/label")
        self.rcaCategory_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/label")
        self.actionPlanning_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/label")
        self.agentCommitment_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/div/label")
        self.leaderComitment_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[3]/div/label")
        
        
        
        
        
        
    def input_strength(self,text):
        self.Input_text(text,*self.strength_loc)
        
    def get_strength(self):
        return self.find_element(*self.strength_loc).get_attribute("value")
    
    def strength_disabled(self):
        flag=self.find_element(*self.strength_loc).get_attribute("disabled")
        return flag 
    def get_strengthBoxTitle(self):
        return self.find_element(*self.strength_title_loc).text 

    def input_callRecordingID(self,text):
        self.Input_text(text,*self.callRecordingID_loc)

    def get_callRecordingID(self):
        return self.find_element(*self.callRecordingID_loc).get_attribute("value")
            
    def callRecordingID_disabled(self):
        flag=self.find_element(*self.callRecordingID_loc).get_attribute("disabled")
        return flag   
     
    def input_opportunity(self,text):
        self.Input_text(text,*self.opportunity_loc)
        
    def get_opportunity(self):
        return self.find_element(*self.opportunity_loc).get_attribute("value")
        
    def opportunity_disabled(self):
        flag=self.find_element(*self.opportunity_loc).get_attribute("disabled")
        return flag
    
    def get_opportunityBoxTitle(self):
        return self.find_element(*self.opportunity_title_loc).text
        
    def input_kpiRelation(self,text):
        self.Input_text(text,*self.kpiRelation_loc)
        
    def get_kpiRelation(self):
        return self.find_element(*self.kpiRelation_loc).get_attribute("value")

    def kpiRelation_disabled(self):
        flag=self.find_element(*self.kpiRelation_loc).get_attribute("disabled")
        return flag
    
    def get_kpiRelationBoxTitle(self):
        return self.find_element(*self.kpiRelation_title_loc).text
        
    def input_rootCauseAnalysis(self,text):
        self.Input_text(text,*self.rootCauseAnalysis_loc)
        
    def get_rootCauseAnalysis(self):
        return self.find_element(*self.rootCauseAnalysis_loc).get_attribute("value")

    def rootCauseAnalysis_disabled(self):
        flag=self.find_element(*self.rootCauseAnalysis_loc).get_attribute("disabled")
        return flag
    
    def get_rootCauseAnalysisBoxTitle(self):
        return self.find_element(*self.rootCauseAnalysis_title_loc).text
        
    def input_rcaCategory(self,text):
        self.Input_text(text,*self.rcaCategory_loc)
        
    def get_rcaCategory(self):
        return self.find_element(*self.rcaCategory_loc).get_attribute("value")
    
    def rcaCategory_disabled(self):
        flag=self.find_element(*self.rcaCategory_loc).get_attribute("disabled")
        return flag
    
    def get_rcaCategoryBoxTitle(self):
        return self.find_element(*self.rcaCategory_title_loc).text
        
    def input_actionPlanning(self,text):
        self.Input_text(text,*self.actionPlanning_loc)
        
    def get_actionPlanning(self):
        return self.find_element(*self.actionPlanning_loc).get_attribute("value")
        
    def actionPlanning_disabled(self):
        flag=self.find_element(*self.actionPlanning_loc).get_attribute("disabled")
        return flag
    
    def get_actionPlanningBoxTitle(self):
        return self.find_element(*self.actionPlanning_title_loc).text
        
    def input_agentCommitment(self,text):
        self.Input_text(text,*self.agentCommitment_loc)
        
    def get_agentCommitment(self):
        return self.find_element(*self.agentCommitment_loc).get_attribute("value")
        
    def agentCommitment_disabled(self):
        flag=self.find_element(*self.agentCommitment_loc).get_attribute("disabled")
        return flag
    
    def get_agentCommitmentBoxTitle(self):
        return self.find_element(*self.agentCommitment_title_loc).text
        
    def input_leaderComitment(self,text):
        self.Input_text(text,*self.leaderComitment_loc)
        
    def get_leaderComitment(self):
        return self.find_element(*self.leaderComitment_loc).get_attribute("value")
        
    def leaderComitment_disabled(self):
        flag=self.find_element(*self.leaderComitment_loc).get_attribute("disabled")
        return flag
    
    def get_leaderComitmentBoxTitle(self):
        return self.find_element(*self.leaderComitment_title_loc).text
        

        
        
        
        