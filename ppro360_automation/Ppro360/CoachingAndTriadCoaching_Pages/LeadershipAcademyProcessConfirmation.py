'''
Created on 20170630

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class LeadershipAcademyProcessConfirmation(BasePage.Action):
    
    
    def __init__(self):
         
       
        self.samGoal_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr/td[2]/input")
        self.samGoalTitle_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr/td[1]/label')
        self.firstthreeinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.firstthreeinputtitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label'
        self.comments_path="//*[@id='container']/div/section/div/form/div[2]/table[2]/tbody/tr[%d]/td[2]/textarea" 
        self.commentsTitle_path='//*[@id="container"]/div/section/div/form/div[2]/table[2]/tbody/tr[%d]/td[1]'
    
    
    
    def input_samGoal (self,text):
        self.find_element(*self.samGoal_loc).clear()
        self.find_element(*self.samGoal_loc).send_keys(text);
    def get_samGoal(self):
        return self.find_element(*self.samGoal_loc).get_attribute('value')
    def samGoal_disabled(self):
        samGoalStatus=self.find_element(*self.samGoal_loc).get_attribute('disabled')
        return samGoalStatus
    def get_samGoalTitle(self):
        return self.find_element(*self.samGoalTitle_loc).text
        
        
    
    def input_firstthreeinput (self,lineindex,text):  #lineindex=(2,4)
        firstthreeinput_loc=(By.XPATH,self.firstthreeinput_path %lineindex)
        self.find_element(*firstthreeinput_loc).clear()
        self.find_element(*firstthreeinput_loc).send_keys(text);
    def get_firstthreeinput(self,lineindex):
        firstthreeinput_loc=(By.XPATH,self.firstthreeinput_path %lineindex)
        return self.find_element(*firstthreeinput_loc).text
    def firstthreeinput_disabled(self,lineindex):
        firstthreeinput_loc=(By.XPATH,self.firstthreeinput_path %lineindex)
        firstthreeinputstatus=self.find_element(*firstthreeinput_loc).get_attribute('disabled')
        return firstthreeinputstatus
    def get_firstthreeinputtitle(self,lineindex):
        firstthreeinputtitle_loc=(By.XPATH, self.firstthreeinputtitle_path %lineindex)
        return self.find_element(*firstthreeinputtitle_loc).text
        
    def input_comments (self,lineindex2,text): #lineindex2=3, 5, 7, 9, 11
        comments_loc=(By.XPATH,self.comments_path %lineindex2)
        self.find_element(*comments_loc).clear()
        self.find_element(*comments_loc).send_keys(text);
    def get_connments(self,lineindex2):
        comments_loc=(By.XPATH,self.comments_path %lineindex2)
        return self.find_element(*comments_loc).text
    def comments_disabled(self,lineindex2):
        comments_loc=(By.XPATH,self.comments_path %lineindex2)
        commentsstatus=self.find_element(*comments_loc).get_attribute('disabled')
        return commentsstatus
    def get_commentsTitle(self,lineindex2):
        commentsTitle_loc=(By.XPATH, self.commentsTitle_path %lineindex2)
        return self.find_element(*commentsTitle_loc).text
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        