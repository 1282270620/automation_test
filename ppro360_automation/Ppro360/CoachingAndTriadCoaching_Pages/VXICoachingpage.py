'''
Created on 2017/3/6

@author: luming.zhao
'''


from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class VXICoachingpage(BasePage.Action):
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
        self.leaderCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[3]/div/div/textarea")
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")
        
    def input_strength(self,text):
        self.find_element(*self.strength_loc).send_keys(text)
       
    def input_opportunity(self,text):
        self.find_element(*self.opportunity_loc).send_keys(text) 
        
    def input_kpiRelation(self,text):
        self.find_element(*self.kpiRelation_loc).send_keys(text)
        
    def input_rootCauseAnalysis(self,text):
        self.find_element(*self.rootCauseAnalysis_loc).send_keys(text)
        
    def input_rcaCategory(self,text):
        self.find_element(*self.rcaCategory_loc).send_keys(text)
        
    def input_actionPlanning(self,text):
        self.find_element(*self.actionPlanning_loc).send_keys(text)
        
    def input_agentCommitment(self,text):
        self.find_element(*self.agentCommitment_loc).send_keys(text)   
        
    def input_leaderComitment(self,text):
        self.find_element(*self.leaderCommitment_loc).send_keys(text)
        
    def click_savebutton(self):
        self.find_element(*self.savebutton_loc).click()
        
        
        
        