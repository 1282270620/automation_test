'''
Created on 2017.6.27

@author: yalan.yin
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class WeeklyAgentPerformanceReview(BasePage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CallRecordingNumber_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        
        
    def input_CallRecordingNumber (self, CallRecordingNumber):
        self.find_element(*self.CallRecordingNumber_loc).clear()
        self.find_element(*self.CallRecordingNumber_loc).send_keys(CallRecordingNumber)  
        
    def click_KPIcheckbox (self, checkboxorder):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorder)
        self.find_element (*self.KPIcheckbox_loc).click()  
    
    
    def input_Week1Goal (self, WGIndex, inputtext):   
        self.Week1Goal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[2]/input' %WGIndex)
        self.find_element(*self.Week1Goal_loc).clear()
        self.find_element(*self.Week1Goal_loc).send_keys(inputtext)
        
    def input_Week2Goal (self, WGIndex, inputtext):   
        self.Week2Goal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[4]/input' %WGIndex)
        self.find_element(*self.Week2Goal_loc).clear()
        self.find_element(*self.Week2Goal_loc).send_keys(inputtext)
        
    def input_Week3Goal (self, WGIndex, inputtext):   
        self.Week3Goal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[6]/input' %WGIndex)
        self.find_element(*self.Week3Goal_loc).clear()
        self.find_element(*self.Week3Goal_loc).send_keys(inputtext)
        
    def input_Week4Goal (self, WGIndex, inputtext):   
        self.Week4Goal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[8]/input' %WGIndex)
        self.find_element(*self.Week4Goal_loc).clear()
        self.find_element(*self.Week4Goal_loc).send_keys(inputtext)   
        
    def input_Week1Actual (self, WAIndex, inputtext):   
        self.Week1Actual_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[3]/input' %WAIndex)
        self.find_element(*self.Week1Actual_loc).clear()
        self.find_element(*self.Week1Actual_loc).send_keys(inputtext)
        
    def input_Week2Actual (self, WAIndex, inputtext):   
        self.Week2Actual_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[5]/input' %WAIndex)
        self.find_element(*self.Week2Actual_loc).clear()
        self.find_element(*self.Week2Actual_loc).send_keys(inputtext)
        
    def input_Week3Actual (self, WAIndex, inputtext):   
        self.Week3Actual_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[7]/input' %WAIndex)
        self.find_element(*self.Week3Actual_loc).clear()
        self.find_element(*self.Week3Actual_loc).send_keys(inputtext)   
        
    def input_Week4Actual (self, WAIndex, inputtext):   
        self.Week4Actual_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[9]/input' %WAIndex)
        self.find_element(*self.Week4Actual_loc).clear()
        self.find_element(*self.Week4Actual_loc).send_keys(inputtext) 
        
        #OIndex(1, 4)
    def input_Opportunities (self, OIndex, inputtext):
        self.Opportunities_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[%d]/div[1]/div[1]/div/textarea' %OIndex)
        self.find_element(*self.Opportunities_loc).clear()
        self.find_element(*self.Opportunities_loc).send_keys(inputtext)
        
        #TCIndex(1, 4)
    def input_TLCommitment (self, TCIndex, inputtext):
        self.TLCommitment_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[%d]/div[1]/div[2]/div/textarea' %TCIndex)
        self.find_element(*self.TLCommitment_loc).clear()
        self.find_element(*self.TLCommitment_loc).send_keys(inputtext)
        
        #ACIndex(1, 4)
    def input_AgentCommitment (self, ACIndex, inputtext):
        self.AgentCommitment_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[%d]/div[1]/div[3]/div/textarea' %ACIndex)
        self.find_element(*self.AgentCommitment_loc).clear()
        self.find_element(*self.AgentCommitment_loc).send_keys(inputtext)
        
        #SBIndex(1, 4)
    def click_SaveButton (self, SBIndex):
        self.SaveButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[%d]/div[2]/div/button[1]' %SBIndex)
        self.find_selement(*self.SaveButton_loc).click()
        
        #OBIndex(1, 4)
    def click_OMSignButton (self, OBIndex):
        self.OMSignButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/div[2]/div/button[2]' %OBIndex)
        self.find_element(*self.OMSignButton_loc).click()
        
    def click_AgentSignButton (self, ABIndex):
        self.AgentSignButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[%d]/div[2]/div[2]/button' %ABIndex)
        self.find_element (*self.AgentSignButton_loc).click()
        
        
        
        
        