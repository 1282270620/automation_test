'''
Created on 2017.6.23

@author: yalan.yin
'''


from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class SalesTriLevelFormPage(BasePage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CallRecordingNumber_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        self.TeamManager_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[1]/input')
        self.Evaluator_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[2]/input')
        self.DateTimeSelector_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/span/span')
        self.CIDMediaTactic_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[2]/input')
        self.KeyStrengthsObserved_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/textarea')
        self.KeyDevelopmentOpportunities_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div/textarea')
        self.ActionPlanForImprovement1_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[2]/tbody/tr[2]/td[2]/div/textarea')
        self.ActionPlanForImprovement2_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[2]/tbody/tr[3]/td[2]/div/textarea')
        self.TeamManagerCommitment1_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[2]/tbody/tr[5]/td[2]/div/textarea')
        self.TeamManagerCommitment2_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[2]/tbody/tr[6]/td[2]/div/textarea')
        self.SeniorManagerCommitment_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/div/textarea') 
        
        
    def input_CallRecordingNumber (self, CallRecordingNumber):
        self.find_element(*self.CallRecordingNumber_loc).clear()
        self.find_element(*self.CallRecordingNumber_loc).send_keys(CallRecordingNumber)
        
    def input_TeamManager (self, inputtext):
        self.find_element(*self.TeamManager_loc).clear()
        self.find_element(*self.TeamManager_loc).send_keys(inputtext)
    
    def input_Evaluator (self, inputtext):
        self.find_element(*self.Evaluator_loc).clear()
        self.find_element(*self.Evaluator_loc).send_keys(inputtext)
        
    def click_DateTimeSelector (self):
        self.find_element(*self.DateTimeSelector_loc).click()
    
    def input_CIDMediaTactic (self, inputtext):
        self.find_element(*self.CIDMediaTactic_loc).clear()
        self.find_element(*self.CIDMediaTactic_loc).send_keys(inputtext)
        
    def input_TeamManagerDevelopment (self, TeamManagerSectionIndex, inputtext):
        self.TeamManagerDevelopment_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[%d]/td[2]/div/textarea' %TeamManagerSectionIndex)
        self.find_element(*self.TeamManagerDevelopment_loc).clear()
        self.find_element(*self.TeamManagerDevelopment_loc).send_keys(inputtext)
        
    def input_KeyElementSection (self, KeyElementSectionIndex, inputtext):
        self.KeyElementSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[%d]/td/div/textarea' %KeyElementSectionIndex)
        self.find_element(*self.KeyElementSection_loc).clear()
        self.find_element(*self.KeyElementSection_loc).send_keys(inputtext)
        
    def click_RadioButtonYes (self, YesIndex):
        self.RadioButtonYes_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[%d]/td/label/div/div[1]/label' %YesIndex)
        self.find_element(*self.RadioButtonYes_loc).click()
        
    def click_RadioButtonNo (self, NoIndex):
        self.RadioButtonNo_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[%d]/td/label/div/div[2]/label' %NoIndex)
        self.find_element(self.RadioButtonNo_loc).click()
        
    def input_KeyStrengthsObserved (self, inputtext):
        self.find_element(*self.KeyStrengthsObserved_loc).clear()
        self.find_element(*self.KeyStrengthsObserved_loc).send_keys(inputtext)
        
    def input_KeyDevelopmentOpportunities (self, inputtext):
        self.find_element(*self.KeyDevelopmentOpportunities_loc).clear()
        self.find_element(*self.KeyDevelopmentOpportunities_loc).send_keys(inputtext)
        
    def input_ActionPlanForImprovement1 (self, inputtext):
        self.find_element(*self.ActionPlanForImprovement1_loc).clear()
        self.find_element(*self.ActionPlanForImprovement1_loc).send_keys(inputtext)
        
    def input_ActionPlanForImprovement2 (self, inputtext):
        self.find_element(*self.ActionPlanForImprovement2_loc).clear()
        self.find_element(*self.ActionPlanForImprovement2_loc).send_keys(inputtext)
        
    def input_TeamManagerCommitment1 (self, inputtext):
        self.find_element(*self.TeamManagerCommitment1_loc).clear()
        self.find_element(*self.TeamManagerCommitment1_loc).send_keys(inputtext)
        
    def input_TeamManagerCommitment2 (self, inputtext):
        self.find_element(*self.TeamManagerCommitment2_loc).clear()
        self.find_element(*self.TeamManagerCommitment2_loc).send_keys(inputtext)   
        
    def input_SeniorManagerCommitment (self, inputtext):
        self.find_element(*self.SeniorManagerCommitment_loc).clear()
        self.find_element(*self.SeniorManagerCommitment_loc).send_keys(inputtext) 
        
         
        
        
        
        
        
        
        