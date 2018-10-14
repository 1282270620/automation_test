'''
Created on 2017.2.24

@author: yalan.yin
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
class WeeklyGSformPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self, params1, params2, params3, params4, params5):
        '''
        Constructor
        '''     
        
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %params1)
        
        self.WeeklyGoal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[2]/input' %params2)

        self.ImproveOrDcline_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[3]/input" %params3)
        
        self.Reason_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[4]/input" %params4 )
        
        self.PersonalGoal_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[5]/input" %params5)
        self.actionplan_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[3]/div[1]/textarea")
        self.agentcommitment_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/div/textarea")
        self.TLcommitment_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[3]/div[3]/div/div/textarea")
    
    def click_KPIcheckbox (self):
        self.find_element (*self.KPIcheckbox_loc).click()
    
    def input_WeeklyGoal (self,kpivalue):
        self.find_element(*self.WeeklyGoal_loc).clear()
        self.find_element(*self.WeeklyGoal_loc).send_keys(kpivalue)
        
    def input_ImproveOrDcline (self,kpivalue):
        self.find_element(*self.ImproveOrDcline_loc).clear()
        self.find_element(*self.ImproveOrDcline_loc).send_keys(kpivalue)
        
    def input_Reason (self,kpivalue):
        self.find_element(*self.Reason_loc).clear()
        self.find_element(*self.Reason_loc).send_keys(kpivalue)
        
    def input_PersonalGoal (self,kpivalue):
        self.find_element(*self.PersonalGoal_loc).clear()
        self.find_element(*self.PersonalGoal_loc).send_keys(kpivalue)
    
    def input_actionplan (self,inputtext):
        self.find_element(*self.actionplan_loc).clear()
        self.find_element(*self.actionplan_loc).send_keys(inputtext)
        
    def input_agentcommitment (self, inputtext):
        self.find_element(*self.agentcommitment_loc).clear()
        self.find_element(*self.agentcommitment_loc).send_keys(inputtext)
    
    def input_TLcommitment (self,inputtext):
        self.find_element(*self.TLcommitment_loc).clear()
        self.find_element(*self.TLcommitment_loc).send_keys(inputtext)
        
        
     
    