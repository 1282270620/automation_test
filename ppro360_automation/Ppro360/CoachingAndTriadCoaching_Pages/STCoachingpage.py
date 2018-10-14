'''
Created on 20170307

@author: luming.zhao
'''


from Tablet_pages import BasePage
from selenium.webdriver.common.by import By


class STCoachingpage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.focus_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/textarea")
        self.importance_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.how_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.achieve_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        self.explain_yes=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/i")
        self.show_no=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div[2]/i")
        self.practice_yes=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[8]/div/i")
        self.completebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[3]")
        
        
    def input_focus(self,text):
        self.find_element(*self.focus_loc).send_keys(text)
        
    def input_importance(self,text):
        self.find_element(*self.importance_loc).send_keys(text)
        
    def input_how(self,text):
        self.find_element(*self.how_loc).send_keys(text)
    
    def input_achieve(self,text):
        self.find_element(*self.achieve_loc).send_keys(text)
        
    def click_explain(self):
        self.find_element(*self.explain_yes).click()
        
    def click_show(self):
        self.find_element(*self.show_no).click()
        
    def click_practice(self):
        self.find_element(*self.practice_yes).click()
        
    def click_completebutton(self):
        self.find_element(*self.completebutton_loc).click()
        
        
        
        