'''
Created on 2017.8.4

@author: yalan.yin
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class CoachingLoopProcessConfirmationPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CallRecordingNumber_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        self.ActionOneComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/textarea')
        self.ActionTwoComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div/textarea')
        self.ActionThreeComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[7]/div/textarea')
        self.ActionFourComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[9]/div/textarea')
        self.ActionFiveComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[11]/div/textarea')
        self.Recommendations_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[12]/div/textarea')
        self.TextboxTitle_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        
        #checkboxorder(2, ##)
    def click_KPIcheckbox (self, checkboxorder):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorder)
        self.find_element (*self.KPIcheckbox_loc).click()  
        
    def get_TextboxTitle(self, boxindex):#boxindex(3, 5, 7, 9, 11, 12)
        TextboxTitle_loc=(By.XPATH, self.TextboxTitle_path %boxindex)
        return self.find_element(*TextboxTitle_loc).text
        
    def input_ActionOneComments (self, inputtext):
        self.find_element(*self.ActionOneComments_loc).clear()
        self.find_element(*self.ActionOneComments_loc).send_keys(inputtext)
    def get_ActionOneComments(self):
        return self.find_element(*self.ActionOneComments_loc).text
    def ActionOneComments_disabled(self):
        flag=self.find_element(*self.ActionOneComments_loc).get_attribute("disabled")
        return flag
    
    def input_ActionTwoComments (self, inputtext):
        self.find_element(*self.ActionTwoComments_loc).clear()
        self.find_element(*self.ActionTwoComments_loc).send_keys(inputtext)
    def get_ActionTwoComments(self):
        return self.find_element(*self.ActionTwoComments_loc).text
    def ActionTwoComments_disabled(self):
        flag=self.find_element(*self.ActionTwoComments_loc).get_attribute("disabled")
        return flag    
    
        
    def input_ActionThreeComments (self, inputtext):
        self.find_element(*self.ActionThreeComments_loc).clear()
        self.find_element(*self.ActionThreeComments_loc).send_keys(inputtext)
    def get_ActionThreeComments(self):
        return self.find_element(*self.ActionThreeComments_loc).text
    def ActionThreeComments_disabled(self):
        flag=self.find_element(*self.ActionThreeComments_loc).get_attribute("disabled")
        return flag    
        
        
    def input_ActionFourComments (self, inputtext):
        self.find_element(*self.ActionFourComments_loc).clear()
        self.find_element(*self.ActionFourComments_loc).send_keys(inputtext)
    def get_ActionFourComments(self):
        return self.find_element(*self.ActionFourComments_loc).text
    def ActionFourComments_disabled(self):
        flag=self.find_element(*self.ActionFourComments_loc).get_attribute("disabled")
        return flag
        
    def input_ActionFiveComments (self, inputtext):
        self.find_element(*self.ActionFiveComments_loc).clear()
        self.find_element(*self.ActionFiveComments_loc).send_keys(inputtext)
    def get_ActionFiveComments(self):
        return self.find_element(*self.ActionFiveComments_loc).text
    def ActionFiveComments_disabled(self):
        flag=self.find_element(*self.ActionFiveComments_loc).get_attribute("disabled")
        return flag    
        
        
    def input_Recommendations(self, inputtext):
        self.find_element(*self.Recommendations_loc).clear()
        self.find_element(*self.Recommendations_loc).send_keys(inputtext)
    def get_Recommendations(self):
        return self.find_element(*self.Recommendations_loc).text
    def Recommendations_disabled(self):
        flag=self.find_element(*self.Recommendations_loc).get_attribute("disabled")
        return flag
        
        
        
        