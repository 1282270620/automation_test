'''
Created on 20170228

@author: luming.zhao
'''



from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class DFMCoachingpage(BasePage.Action):
    '''
    classdocs
    '''
   
    def __init__(self):
        '''
        Constructor
        '''

        self.agentOpinion_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.leaderSuggestion_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.agentImprovement_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.improvementSuggestion_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        self.actionDetail_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/textarea")
        self.addtionalComments_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/textarea")
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")
        self.backhomepage_loc=(By.XPATH,"//*[@id='container']/div/nav/a")
        self.TextboxTitle_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        
    def get_TextboxTitle(self, boxindex):#boxindex(2, 7)
        TextboxTitle_loc=(By.XPATH, self.TextboxTitle_path %boxindex)
        return self.find_element(*TextboxTitle_loc).text
        
    def input_agentOpinion(self,text):
        self.find_element(*self.agentOpinion_loc).clear()
        self.find_element(*self.agentOpinion_loc).send_keys(text)
    def get_agentOpinion(self):
        return self.find_element(*self.agentOpinion_loc).text
    def agentOpinion_disabled(self):
        flag=self.find_element(*self.agentOpinion_loc).get_attribute("disabled")
        return flag
        
    def input_leaderSuggestion(self,text):
        self.find_element(*self.leaderSuggestion_loc).clear()
        self.find_element(*self.leaderSuggestion_loc).send_keys(text)
    def get_leaderSuggestion(self):
        return self.find_element(*self.leaderSuggestion_loc).text
    def leaderSuggestion_disabled(self):
        flag=self.find_element(*self.leaderSuggestion_loc).get_attribute("disabled")
        return flag
        
    def input_agentImprovement(self,text):
        self.find_element(*self.agentImprovement_loc).clear()
        self.find_element(*self.agentImprovement_loc).send_keys(text)
    def get_agentImprovement(self):
        return self.find_element(*self.agentImprovement_loc).text
    def agentImprovement_disabled(self):
        flag=self.find_element(*self.agentImprovement_loc).get_attribute("disabled")
        return flag
          
        
    def input_improvementSuggestion(self,text):
        self.find_element(*self.improvementSuggestion_loc).clear()
        self.find_element(*self.improvementSuggestion_loc).send_keys(text)
    def get_improvementSuggestion(self):
        return self.find_element(*self.improvementSuggestion_loc).text
    def improvementSuggestion_disabled(self):
        flag=self.find_element(*self.improvementSuggestion_loc).get_attribute("disabled")
        return flag
        
    def input_actionDetail(self,text):
        self.find_element(*self.actionDetail_loc).clear()
        self.find_element(*self.actionDetail_loc).send_keys(text)
        
    def get_actionDetail(self):
        return self.find_element(*self.actionDetail_loc).text
    def actionDetail_disabled(self):
        flag=self.find_element(*self.actionDetail_loc).get_attribute("disabled")
        return flag
        
    def input_addtionalComments(self,text):
        self.find_element(*self.addtionalComments_loc).clear()
        self.find_element(*self.addtionalComments_loc).send_keys(text) 
    def get_addtionalComments(self):
        return self.find_element(*self.addtionalComments_loc).text
    def addtionalComments_disabled(self):    
        flag=self.find_element(*self.addtionalComments_loc).get_attribute("disabled")
        return flag
           
    def click_savebutton(self):
        self.find_element(*self.savebutton_loc).click()
        
    def backhomepage(self):
        self.backhomepage(*self.backhomepage_loc).click()
        
    
        
            