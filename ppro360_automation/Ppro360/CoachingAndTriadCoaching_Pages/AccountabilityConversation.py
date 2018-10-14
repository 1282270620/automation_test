# -*- coding: utf-8 -*
'''
Created on 2017/3/6

@author: luming.zhao
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By


class AccountabilityConversation(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.evaluate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.checkfu_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.iarar_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.seac_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        self.reconfirmUnderstanding_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/textarea")
        self.otherNotesAndRemarks_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/textarea")
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")
        self.evaluate_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/label")
        self.checkfu_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/label")
        self.iarar_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/label")
        self.seac_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/label")
        self.reconfirmUnderstanding_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/label")
        self.otherNotesAndRemarks_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/label")
        
        
        
        
    def input_evaluate(self,text):
        self.Input_text(text,*self.evaluate_loc)
    def get_evaluate(self):
        return self.find_element(*self.evaluate_loc).get_attribute("value")
    def evaluate__disabled(self):
        flag=self.find_element(*self.evaluate_loc).get_attribute("disabled")
        return flag
    def get_evaulateBoxTitle(self):
        return self.find_element(*self.evaluate_title_loc).text
    
    
    def input_checkfu(self,text):
        self.Input_text(text,*self.checkfu_loc)
    def get_checkfu(self):
        return self.find_element(*self.checkfu_loc).get_attribute("value")
    def checkfu__disabled(self):
        flag=self.find_element(*self.checkfu_loc).get_attribute("disabled")
        return flag    
    def get_checkfuBoxTitle(self):
        return self.find_element(*self.checkfu_title_loc).text
    
        
    def input_iarar(self,text):
        self.Input_text(text,*self.iarar_loc)
    def get_iarar(self):
        return self.find_element(*self.iarar_loc).get_attribute("value")  
    def iarar__disabled(self):
        flag=self.find_element(*self.iarar_loc).get_attribute("disabled")
        return flag
    def get_iararBoxTitle(self):
        return self.find_element(*self.iarar_title_loc).text
     
        
    def input_seac(self,text):
        self.Input_text(text,*self.seac_loc)
    def get_seac(self):
        return self.find_element(*self.seac_loc).get_attribute("value")   
    def seac__disabled(self):
        flag=self.find_element(*self.seac_loc).get_attribute("disabled")
        return flag
    def get_seacBoxTitle(self):
        return self.find_element(*self.seac_title_loc).text
    
    
        
    def input_reconfirmUnderstanding(self,text):
        self.Input_text(text,*self.reconfirmUnderstanding_loc)
    def get_reconfirmUnderstanding(self):
        return self.find_element(*self.reconfirmUnderstanding_loc).get_attribute("value")   
    def reconfirmUnderstanding__disabled(self):
        flag=self.find_element(*self.reconfirmUnderstanding_loc).get_attribute("disabled")
        return flag
    def get_reconfirmUnderstandingBoxTitle(self):
        return self.find_element(*self.reconfirmUnderstanding_title_loc).text
    
    
        
    def input_otherNotesAndRemarks(self,text):
        self.Input_text(text,*self.otherNotesAndRemarks_loc)
    def get_otherNotesAndRemarks(self):
        return self.find_element(*self.otherNotesAndRemarks_loc).get_attribute("value") 
    def otherNotesAndRemarks__disabled(self):
        flag=self.find_element(*self.otherNotesAndRemarks_loc).get_attribute("disabled")
        return flag
    def get_otherNotesAndRemarksBoxTitle(self):
        return self.find_element(*self.otherNotesAndRemarks_title_loc).text  
      
      
        
    def click_savebutton(self):
        self.find_element(*self.savebutton_loc).click()
        
    