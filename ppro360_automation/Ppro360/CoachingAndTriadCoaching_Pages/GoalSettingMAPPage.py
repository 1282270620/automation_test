'''
Created on 2017.6.22

@author: yalan.yin
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class GoalSettingMAPPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CallRecordingNumber_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        self.WerePreviousMapSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/textarea')
        self.BasedOnTheScorecardSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/textarea')
        self.IfApplicableSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/textarea')
        self.WhatAreTheCurrentMapSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div/textarea')
        self.WhatExamplesSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/div/textarea')
        self.WasASkillTransferSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[7]/div/textarea')
        self.WerePerformanceCommitmentSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[8]/div/textarea')
        self.KeyStrengthsSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[9]/div/textarea')
        self.KeyOpportunitiesSection_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[10]/div/textarea')
        
        
    def click_KPIcheckbox (self, checkboxorder):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorder)
        self.find_element (*self.KPIcheckbox_loc).click()  
        
    def input_CallRecordingNumber (self, CallRecordingNumber): 
        
        self.find_element(*self.CallRecordingNumber_loc).clear()
        self.find_element(*self.CallRecordingNumber_loc).send_keys(CallRecordingNumber)
    
    def input_WerePreviousMapSection (self, inputtext):
        self.find_element(*self.WerePreviousMapSection_loc).clear()
        self.find_element(*self.WerePreviousMapSection_loc).send_keys(inputtext)
        
    def input_BasedOnTheScorecardSection (self, inputtext):
        self.find_element(*self.BasedOnTheScorecardSection_loc).clear()
        self.find_element(*self.BasedOnTheScorecardSection_loc).send_keys(inputtext)
    
    def input_IfApplicableSection (self, inputtext):
        self.find_element(*self.IfApplicableSection_loc).clear()
        self.find_element(*self.IfApplicableSection_loc).send_keys(inputtext)
        
    def input_WhatAreTheCurrentMapSection (self, inputtext):
        self.find_element(*self.WhatAreTheCurrentMapSection_loc).clear()
        self.find_element(*self.WhatAreTheCurrentMapSection_loc).send_keys(inputtext)
        
    def input_WhatExamplesSection (self, inputtext):
        self.find_element(*self.WhatExamplesSection_loc).clear()
        self.find_element(*self.WhatExamplesSection_loc).send_keys(inputtext)
        
    def input_WasASkillTransferSection (self, inputtext):
        self.find_element(*self.WasASkillTransferSection_loc).clear()
        self.find_element(*self.WasASkillTransferSection_loc).send_keys(inputtext)
        
    def input_WerePerformanceCommitmentSection (self, inputtext):
        self.find_element(*self.WerePerformanceCommitmentSection_loc).clear()
        self.find_element(*self.WerePerformanceCommitmentSection_loc).send_keys(inputtext)
        
    def input_KeyStrengthsSection (self, inputtext):
        self.find_element(*self.KeyStrengthsSection_loc).clear()
        self.find_element(*self.KeyStrengthsSection_loc).send_keys(inputtext)
        
    def input_KeyOpportunitiesSection (self, inputtext):
        self.find_element(*self.KeyOpportunitiesSection_loc).clear()
        self.find_element(*self.KeyOpportunitiesSection_loc).send_keys(inputtext)
        
        
        