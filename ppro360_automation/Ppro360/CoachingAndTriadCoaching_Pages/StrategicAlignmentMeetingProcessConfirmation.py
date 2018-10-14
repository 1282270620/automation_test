'''
Created on 20170629

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class StrategicAlignmentMeetingProcessConfirmation(BasePage.Action):
    
    
    def __init__(self):
         
       
        self.TextBox_Path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/div[1]/textarea'
        self.TextBoxTitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label/div[1]'
        self.KEYSTRENGTHSAndOPPORTUNITIES_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/textarea' 
        self.KEYSTRENGTHSAndOPPORTUNITIESTitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label'
        self.ScoreInput_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/div[2]/input'
        self.OverallScore_path='//*[@id="container"]/div/section/div/form/div[2]/label/div[2]/input'
        self.ScoreBall_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div/div[2]/i'
        self.OverallScoreBall_path='//*[@id="container"]/div/section/div/form/div[2]/label/div[2]/i'
        
        
    
        
    def input_TextBox(self,index,text): #index (2, 8)
        TextBox_loc=(By.XPATH,self.TextBox_Path %index)
        self.find_element(*TextBox_loc).clear()
        self.find_element(*TextBox_loc).send_keys(text);
    def get_TextBox(self,index): #index (2, 8)
        TextBox_loc=(By.XPATH,self.TextBox_Path %index)
        return self.find_element(*TextBox_loc).text
    def TextBox_disabled(self,index): #index (2, 8)
        TextBox_loc=(By.XPATH,self.TextBox_Path %index)
        flag=self.find_element(*TextBox_loc).get_attribute('disabled')
        return flag
    def get_TextBoxTitle(self,index): #index (2, 8)
        TextBoxTitle_loc=(By.XPATH, self.TextBoxTitle_path %index)
        return self.find_element(*TextBoxTitle_loc).text
    
    def input_KEYSTRENGTHSAndOPPORTUNITIES(self,boxindex,text): #boxindex=9, 10
        KEYSTRENGTHSAndOPPORTUNITIES_loc=(By.XPATH, self.KEYSTRENGTHSAndOPPORTUNITIES_path %boxindex)
        self.find_element(*KEYSTRENGTHSAndOPPORTUNITIES_loc).clear()
        self.find_element(*KEYSTRENGTHSAndOPPORTUNITIES_loc).send_keys(text)
    def get_KEYSTRENGTHSAndOPPORTUNITIES(self,boxindex): #boxindex=9, 10
        KEYSTRENGTHSAndOPPORTUNITIES_loc=(By.XPATH, self.KEYSTRENGTHSAndOPPORTUNITIES_path %boxindex)
        return self.find_element(*KEYSTRENGTHSAndOPPORTUNITIES_loc).text
    def KEYSTRENGTHSAndOPPORTUNITIES_disabled(self,boxindex):  #boxindex=9, 10
        KEYSTRENGTHSAndOPPORTUNITIES_loc=(By.XPATH, self.KEYSTRENGTHSAndOPPORTUNITIES_path %boxindex)
        flag=self.find_element(*KEYSTRENGTHSAndOPPORTUNITIES_loc).get_attribute('disabled')
        return flag
    def get_KEYSTRENGTHSAndOPPORTUNITIESTitle(self,boxindex): #boxindex=9, 10
        KEYSTRENGTHSAndOPPORTUNITIESTitle_loc=(By.XPATH, self.KEYSTRENGTHSAndOPPORTUNITIESTitle_path %boxindex)
        return self.find_element(*KEYSTRENGTHSAndOPPORTUNITIESTitle_loc).text
    
    def input_Score(self,index,score): #index(2,8)
        ScoreInput_loc=(By.XPATH, self.ScoreInput_path %index)
        self.find_element(*ScoreInput_loc).clear()
        self.find_element(*ScoreInput_loc).send_keys(score)
    def get_Score(self,index):
        ScoreInput_loc=(By.XPATH, self.ScoreInput_path %index)
        return self.find_element(*ScoreInput_loc).get_attribute('value')
    def Score_disabled(self,index):
        ScoreInput_loc=(By.XPATH, self.ScoreInput_path %index)
        flag=self.find_element(*ScoreInput_loc).get_attribute('disabled')
        return flag
    def get_ScoreBallStatus(self,index):  #index(2,8)
        ScoreBall_loc=(By.XPATH, self.ScoreBall_path %index)
        return self.find_element(*ScoreBall_loc).get_attribute('class')
    def input_OverallScore(self,score):
        OverallScore_loc=(By.XPATH, self.OverallScore_path)
        self.find_element(*OverallScore_loc).send_keys(score)
    def get_OverallScore(self):
        OverallScore_loc=(By.XPATH, self.OverallScore_path)
        return self.find_element(*OverallScore_loc).get_attribute('value')
    def get_OverallScoreBallStatus(self): 
        OverallScoreBallStatus_loc=(By.XPATH, self.OverallScoreBall_path)
        return self.find_element(*OverallScoreBallStatus_loc).get_attribute('class')
        
    def OverallScore_disabled(self):
        OverallScoreStatus_loc=(By.XPATH, self.OverallScore_path)
        flag=self.find_element(*OverallScoreStatus_loc).get_attribute('disabled')
        return flag
        
        
        
        
        
        
        
        
    
    
    