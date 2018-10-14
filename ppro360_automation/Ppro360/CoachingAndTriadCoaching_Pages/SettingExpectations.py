'''
Created on 2017/3/7

@author: luming.zhao
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By


class SettingExpectations(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.establishExpectation_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.reason_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.resources_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.verifyUnderstanding_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        self.verifyCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/textarea")
        self.confidenceBuilder_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/textarea")
        self.otherNotesAndRemarks_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[8]/div/textarea")
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")
        
    def input_establishExpectation(self,text):
        self.Input_text(text,*self.establishExpectation_loc)
    def get_establishExpectation(self):
        return self.find_element(*self.establishExpectation_loc).get_attribute("value")
    def establishExpectation__disabled(self):
        flag=self.find_element(*self.establishExpectation_loc).get_attribute("disabled")
        return flag
    def get_establishExpectationBoxTitle(self):
        return self.find_element(*self.establishExpectation_loc).text
        
        
        
    def input_reason(self,text):
        self.Input_text(text,*self.reason_loc)
    def get_reason(self):
        return self.find_element(*self.reason_loc).get_attribute("value")
    def reason__disabled(self):
        flag=self.find_element(*self.reason_loc).get_attribute("disabled")
        return flag
    def get_reasonBoxTitle(self):
        return self.find_element(*self.reason_loc).text
    
    
        
    def input_resources(self,text):
        self.Input_text(text,*self.resources_loc)
    def get_resources(self):
        return self.find_element(*self.resources_loc).get_attribute("value")
    def resources__disabled(self):
        flag=self.find_element(*self.resources_loc).get_attribute("disabled")
        return flag
    def get_resourcesBoxTitle(self):
        return self.find_element(*self.resources_loc).text        
        
        
        
    def input_verifyUnderstanding(self,text):
        self.Input_text(text,*self.verifyUnderstanding_loc)
    def get_verifyUnderstanding(self):
        return self.find_element(*self.verifyUnderstanding_loc).get_attribute("value")
    def verifyUnderstanding__disabled(self):
        flag=self.find_element(*self.verifyUnderstanding_loc).get_attribute("disabled")
        return flag
    def get_verifyUnderstandingBoxTitle(self):
        return self.find_element(*self.verifyUnderstanding_loc).text         
        
        
        
    def input_verifyCommitment(self,text):
        self.Input_text(text,*self.verifyCommitment_loc)
    def get_verifyCommitment(self):
        return self.find_element(*self.verifyCommitment_loc).get_attribute("value")
    def verifyCommitment__disabled(self):
        flag=self.find_element(*self.verifyCommitment_loc).get_attribute("disabled")
        return flag
    def get_verifyCommitmentBoxTitle(self):
        return self.find_element(*self.verifyCommitment_loc).text     
        
        
        
    def input_confidenceBuilder(self,text):
        self.Input_text(text,*self.confidenceBuilder_loc)
    def get_confidenceBuilder(self):
        return self.find_element(*self.confidenceBuilder_loc).get_attribute("value")
    def confidenceBuilder__disabled(self):
        flag=self.find_element(*self.confidenceBuilder_loc).get_attribute("disabled")
        return flag
    def get_confidenceBuilderBoxTitle(self):
        return self.find_element(*self.confidenceBuilder_loc).text          
        
        
    def input_otherNotesAndRemarks(self,text):
        self.Input_text(text,*self.otherNotesAndRemarks_loc)
    def get_otherNotesAndRemarks(self):
        return self.find_element(*self.otherNotesAndRemarks_loc).get_attribute("value")
    def otherNotesAndRemarks__disabled(self):
        flag=self.find_element(*self.otherNotesAndRemarks_loc).get_attribute("disabled")
        return flag
    def get_otherNotesAndRemarksBoxTitle(self):
        return self.find_element(*self.otherNotesAndRemarks_loc).text            
        
        
        
    def click_savebutton(self):
        self.find_element(*self.savebutton_loc).click()