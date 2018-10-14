'''
Created on 20171102

@author: luming.zhao
'''

from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from MySQLdb.constants import FLAG

class MonthlyGoalSettingAgent(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #'Goal Period' section on the page
        self.GoalPeriod_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div[1]/input")
        #'Goal #1 or #2' section on the page
        self.previousGoalText_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[%d]/div[1]/div[2]/input"
        self.previousGoalTextTitle_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[%d]/div[1]/div[1]"
        
        #'KPI' section on the page
        self.previousKpi_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[%d]/div[2]/div[1]/input"
        self.previousKpiTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]")
        
        #'GOAL' section on the page
        self.previousGoal_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[%d]/div[2]/div[2]/input"
        self.previousGoalTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]")
        self.scorecard_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
                                     
        self.scorecardBoxTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/label")
        self.described_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/textarea")
        self.mitigate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/textarea")
        self.currentGoalPeriod_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[1]/div[2]/div[1]/input")
        self.currentGoalPeriodTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[1]/div[2]/div[1]/div")
        self.currentGoalText_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[%d]/div[1]/div[2]/input"
        self.currentGoalTextTitle_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[%d]/div[1]/div[1]"
                                         
        
        self.currentKpi_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[%d]/div[2]/div[1]/input"
        self.currentKpiTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[1]/div[2]/div[2]/div[1]")
        self.currentGoal_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[%d]/div[2]/div[2]/input"
        self.currentGoalTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[1]/div[2]/div[2]/div[2]")
        self.important_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div[2]/textarea")
        self.importantTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div[1]")
        self.demonstrate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[8]/div[2]/textarea")
        self.demonstrateTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[8]/div[1]")
        self.agentGoal_path="//*[@id='container']/div/section/div/form/div[2]/div[10]/div[%d]/div[2]/input"
        self.agentGoalTitle_path="//*[@id='container']/div/section/div/form/div[2]/div[10]/div[%d]/div[1]"
        self.development_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[12]/div[2]/textarea")
        self.developmentTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[11]/label")
        self.supervisorCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[14]/div[2]/textarea")
        self.supervisorCommitmentTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[13]/label")
        
    def input_GoalPeriod(self,text):
        self.find_element(*self.GoalPeriod_loc).send_keys(text)
    def get_GoalPeriod(self):
        return self.find_element(*self.GoalPeriod_loc).get_attribute("value")
    def GoalPeriod_disabled(self):
        #flag=self.find_element(*self.GoalPeriod_loc).get_attribute("disabled")
        #return flag
        return self.find_element(*self.GoalPeriod_loc).get_attribute("disabled")
    def get_GoalPeriodBoxTitle(self):
        return self.find_element(*self.GoalPeriod_loc).text
    
    def input_previousGoalText(self,lineindex1,text):
        self.previousGoalText_loc=(By.XPATH,self.previousGoalText_path %lineindex1)
        self.find_element(*self.previousGoalText_loc).send_keys(text)
    def get_previousGoalText(self,lineindex1):
        self.previousGoalText_loc=(By.XPATH,self.previousGoalText_path %lineindex1)
        return self.find_element(*self.previousGoalText_loc).get_attribute("value")
    def previousGoalText_disabled(self,lineindex1):
        #flag=self.find_element(*self.previousGoalText_loc).get_attribute("disabled")
        self.previousGoalText_loc=(By.XPATH,self.previousGoalText_path %lineindex1)
        return self.find_element(*self.previousGoalText_loc).get_attribute("disabled")
    def get_previousGoalTextBoxTitle(self,lineindex1):
        self.previousGoalTextTitle_loc=(By.XPATH,self.previousGoalTextTitle_path %lineindex1)
        return self.find_element(*self.previousGoalTextTitle_loc).text
    
    
   
    def input_previousKpi(self,lineindex2,text):
        self.previousKpi_loc=(By.XPATH,self.previousKpi_path %lineindex2)
        self.find_element(*self.previousKpi_loc).send_keys(text)
    def get_previousKpi(self,lineindex2):
        self.previousKpi_loc=(By.XPATH,self.previousKpi_path %lineindex2)
        return self.find_element(*self.previousKpi_loc).get_attribute("value")
    def previousKpi_disabled(self,lineindex2):
        #flag=self.find_element(*self.previousKpi_loc).get_attribute("disabled")
        self.previousKpi_loc=(By.XPATH,self.previousKpi_path %lineindex2)
        return self.find_element(*self.previousKpi_loc).get_attribute("disabled")
    def get_previousKpiBoxTitle(self):
        #self.previousKpiTitle_loc=(By.XPATH,"//*[@id=container']/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]")
        return self.find_element(*self.previousKpiTitle_loc).text
    

    
    
    
    def input_previousGoal(self,lineindex3,text):
        self.previousGoal_loc=(By.XPATH,self.previousGoal_path %lineindex3)
        self.find_element(*self.previousGoal_loc).send_keys(text)
    def get_previousGoal(self,lineindex3):
        self.previousGoal_loc=(By.XPATH,self.previousGoal_path %lineindex3)
        return self.find_element(*self.previousGoal_loc).get_attribute("value")
    def previousGoal_disabled(self,lineindex3):
        #flag=self.find_element(*self.previousGoal_loc).get_attribute("disabled")
        self.previousGoal_loc=(By.XPATH,self.previousGoal_path %lineindex3)
        return self.find_element(*self.previousGoal_loc).get_attribute("disabled")
    def get_previousGoalBoxTitle(self):
        #self.previousGoalTitle_loc=(By.XPATH,self.previousGoalTitle_path %lineindex3)
        return self.find_element(*self.previousGoalTitle_loc).text
    
    
    
    def input_scorecard(self,text):
        self.find_element(*self.scorecard_loc).send_keys(text)
    def get_scorecard(self):
        return self.find_element(*self.scorecard_loc).get_attribute("value")
    def scorecard_disabled(self):
        #flag=self.find_element(*self.scorecard_loc).get_attribute("disabled")
        return self.find_element(*self.scorecard_loc).get_attribute("disabled")
    def get_scorecardBoxTitle(self):
        return self.find_element(*self.scorecardBoxTitle_loc).text
    
    
    def input_described(self,text):
        self.find_element(*self.described_loc).send_keys(text)
    def get_described(self):
        return self.find_element(*self.described_loc).get_attribute("value")
    def described_disabled(self):
        #flag=self.find_element(*self.described_loc).get_attribute("disabled")
        return self.find_element(*self.described_loc).get_attribute("disabled")
    def get_describedBoxTitle(self):
        return self.find_element(*self.scorecardBoxTitle_loc).text
    
    
    def input_mitigate(self,text):
        self.find_element(*self.mitigate_loc).send_keys(text)
    def get_mitigate(self):
        return self.find_element(*self.mitigate_loc).get_attribute("value")
    def mitigate_disabled(self):
        #flag=self.find_element(*self.mitigate_loc).get_attribute("disabled")
        return self.find_element(*self.mitigate_loc).get_attribute("disabled")
    def get_mitigateBoxTitle(self):
        return self.find_element(*self.scorecardBoxTitle_loc).text
    
    
        
    def input_currentGoalPeriod(self,text):
        self.find_element(*self.currentGoalPeriod_loc).send_keys(text)
    def get_currentGoalPeriod(self):
        return self.find_element(*self.currentGoalPeriod_loc).get_attribute("value")
    def currentGoalPeriod_disabled(self):
        #flag=self.find_element(*self.currentGoalPeriod_loc).get_attribute("disabled")
        return self.find_element(*self.currentGoalPeriod_loc).get_attribute("disabled")
    def get_currentGoalPeriodBoxTitle(self):
        
        return self.find_element(*self.currentGoalPeriodTitle_loc).text
    
        
    def input_currentGoalText(self,lineindex4,text):
        self.currentGoalText_loc=(By.XPATH,self.currentGoalText_path %lineindex4)
        self.find_element(*self.currentGoalText_loc).send_keys(text)
    def get_currentGoalText(self,lineindex4):
        self.currentGoalText_loc=(By.XPATH,self.currentGoalText_path %lineindex4)
        return self.find_element(*self.currentGoalText_loc).get_attribute("value")
    def currentGoalText_disabled(self,lineindex4):
        #flag=self.find_element(*self.currentGoalText_loc).get_attribute("disabled")
        self.currentGoalText_loc=(By.XPATH,self.currentGoalText_path %lineindex4)
        return self.find_element(*self.currentGoalText_loc).get_attribute("disabled")
    def get_currentGoalTextBoxTitle(self,lineindex4):
        self.currentGoalTextTitle_loc=(By.XPATH,self.currentGoalTextTitle_path %lineindex4)
        return self.find_element(*self.currentGoalTextTitle_loc).text
    
    
    def input_currentKpi(self,lineindex5,text):
        self.currentKpi_loc=(By.XPATH,self.currentKpi_path %lineindex5)
        self.find_element(*self.currentKpi_loc).send_keys(text)
    def get_currentKpi(self,lineindex5):
        self.currentKpi_loc=(By.XPATH,self.currentKpi_path %lineindex5)
        return self.find_element(*self.currentKpi_loc).get_attribute("value")
    def currentKpi_disabled(self,lineindex5):
        #flag=self.find_element(*self.currentKpi_loc).get_attribute("disabled")
        self.currentKpi_loc=(By.XPATH,self.currentKpi_path %lineindex5)
        return self.find_element(*self.currentKpi_loc).get_attribute("disabled")
    def get_currentKpiTextBoxTitle(self):
        
        return self.find_element(*self.currentKpiTitle_loc).text
    
    
    def input_currentGoal(self,lineindex6,text):
        self.currentGoal_loc=(By.XPATH,self.currentGoal_path %lineindex6)
        self.find_element(*self.currentGoal_loc).send_keys(text)
    def get_currentGoal(self,lineindex6):
        self.currentGoal_loc=(By.XPATH,self.currentGoal_path %lineindex6)
        return self.find_element(*self.currentGoal_loc).get_attribute("value")
    def currentGoal_disabled(self,lineindex6):
        #flag=self.find_element(*self.currentGoal_loc).get_attribute("disabled")
        self.currentGoal_loc=(By.XPATH,self.currentGoal_path %lineindex6)
        return self.find_element(*self.currentGoal_loc).get_attribute("disabled")
    def get_currentGoalBoxTitle(self):
        return self.find_element(*self.currentGoalTitle_loc).text
    
    
    def input_important(self,text):
        self.find_element(*self.important_loc).send_keys(text)
    def get_important(self):
        return self.find_element(*self.important_loc).get_attribute("value")
    def important_disabled(self):
        #flag=self.find_element(*self.important_loc).get_attribute("disabled")
        return self.find_element(*self.important_loc).get_attribute("disabled")
    def get_importantBoxTitle(self):
        return self.find_element(*self.importantTitle_loc).text
    
    
    def input_demonstrate(self,text):
        self.find_element(*self.demonstrate_loc).send_keys(text)
    def get_demonstrate(self):
        return self.find_element(*self.demonstrate_loc).get_attribute("value")
    def demonstrate_disabled(self):
        #flag=self.find_element(*self.demonstrate_loc).get_attribute("disabled")
        return self.find_element(*self.demonstrate_loc).get_attribute("disabled")
    def get_demonstrateBoxTitle(self):
        return self.find_element(*self.demonstrateTitle_loc).text
    
    
    
    def input_agentGoal(self,lineindex7,text):
        self.agentGoal_loc=(By.XPATH,self.agentGoal_path %lineindex7)
        self.find_element(*self.agentGoal_loc).send_keys(text)
    def get_agentGoal(self,lineindex7):
        self.agentGoal_loc=(By.XPATH,self.agentGoal_path %lineindex7)
        return self.find_element(*self.agentGoal_loc).get_attribute("value")
    def agentGoal_disabled(self,lineindex7):
        #flag=self.find_element(*self.agentGoalloc).get_attribute("disabled")
        self.agentGoal_loc=(By.XPATH,self.agentGoal_path %lineindex7)
        return self.find_element(*self.agentGoal_loc).get_attribute("disabled")
    def get_agentGoalBoxTitle(self,lineindex7):
        self.agentGoalTitle_loc=(By.XPATH,self.agentGoalTitle_path %lineindex7)
        return self.find_element(*self.agentGoalTitle_loc).text
    
    
        
    def input_development(self,text):
        self.find_element(*self.development_loc).send_keys(text)
    def get_development(self):
        return self.find_element(*self.development_loc).get_attribute("value")
    def development_disabled(self):
        #flag=self.find_element(*self.development_loc).get_attribute("disabled")
        return self.find_element(*self.development_loc).get_attribute("disabled")
    def get_developmentBoxTitle(self):
        return self.find_element(*self.developmentTitle_loc).text
    
            
    def input_supervisorCommitment(self,text):
        self.find_element(*self.supervisorCommitment_loc).send_keys(text)
    def get_supervisorCommitment(self):
        return self.find_element(*self.supervisorCommitment_loc).get_attribute("value")
    def supervisorCommitment_disabled(self):
        #flag=self.find_element(*self.supervisorCommitment_loc).get_attribute("disabled")
        return self.find_element(*self.supervisorCommitment_loc).get_attribute("disabled")
    def get_supervisorCommitmentBoxTitle(self):
        return self.find_element(*self.supervisorCommitmentTitle_loc).text
