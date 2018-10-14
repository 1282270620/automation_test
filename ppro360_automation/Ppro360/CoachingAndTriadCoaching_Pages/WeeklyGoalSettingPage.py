'''
Created on 2017.6.26

@author: yalan.yin
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class WeeklyGoalSettingPage(BasePage):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
     
        self.ActionPlanning_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/textarea')
        self.AgentCommitment_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[2]/div/div/textarea')
        self.TLCommitment_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[3]/div/div/textarea')
        
     
        
    def click_KPIcheckbox (self, checkboxorder):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorder)
        self.find_element (*self.KPIcheckbox_loc).click()  
        
        
        #WGIndex(1, 6)
    def input_weeklyGoal (self, WGIndex, inputtext):
        self.WeeklyGoal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[2]/input' %WGIndex)
        self.find_element(*self.WeeklyGoal_loc).clear()
        self.find_element(*self.WeeklyGoal_loc).send_keys(inputtext)
        
        #IDIndex(1, 6)
    def input_ImprovementOrDecline (self, IDIndex, inputtext):
        self.ImprovementOrDecline_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[3]/input' %IDIndex)
        self.find_element(*self.ImprovementOrDecline_loc).clear()
        self.find_element(*self.ImprovementOrDecline_loc).send_keys(inputtext)
        
        #RIndex(1, 6)
        
    def input_Reason (self, RIndex, inputtext):
        self.Reason_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[4]/input' %RIndex)
        self.find_element(*self.Reason_loc).clear()
        self.find_element(*self.Reason_loc).send_keys(inputtext)
        
        #PGIndex(1, 6)
    def input_PersonalGoal (self, PGIndex, inputtext):
        self.PersonalGoal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[5]/input' %PGIndex)
        self.find_element(*self.PersonalGoal_loc).clear()
        self.find_element(*self.PersonalGoal_loc).send_keys(inputtext)
        
    def input_ActionPlanning (self, inputtext):
        self.find_element(*self.ActionPlanning_loc).clear()
        self.find_element(*self.ActionPlanning_loc).send_keys(inputtext)
        
    def input_AgentCommitment (self, inputtext):
        self.find_element(*self.AgentCommitment_loc).clear()
        self.find_element(*self.AgentCommitment_loc).send_keys(inputtext)
        
    def input_TLCommitment (self, inputtext):
        self.find_element(*self.TLCommitment_loc).clear()
        self.find_element(*self.TLCommitment_loc).send_keys(inputtext)
        
        
        
        