'''
Created on 20170721

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class DirectModelFeedbackProcessConfirmation(BasePage.Action):
    
    
    def __init__(self):
         
        
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div/div/table/tbody/tr[4]/td[%d]/i"
        self.comments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.TextboxTitle_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def get_TextboxTitle(self, boxindex):#boxindex(3, 5, 7, 9, 11, 13, 14)
        TextboxTitle_loc=(By.XPATH, self.TextboxTitle_path %boxindex)
        return self.find_element(*TextboxTitle_loc).text
    
   
    def input_comments(self,text,lineindex): #(lineindex: 3, 5, 7, 9, 11, 13, 14)
        comments_loc=(By.XPATH,self.comments_path %lineindex)
        self.find_element(*comments_loc).clear()
        self.find_element(*comments_loc).send_keys(text)
        
    def get_comments(self,lineindex):
        comments_loc=(By.XPATH,self.comments_path %lineindex)
        return self.find_element(*comments_loc).text
    
    def Comments_disabled(self, lineindex):
        comments_loc=(By.XPATH,self.comments_path %lineindex)
        flag=self.find_element(*comments_loc).get_attribute("disabled")
        return flag
        
        