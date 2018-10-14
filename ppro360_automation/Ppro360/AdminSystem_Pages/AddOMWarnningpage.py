'''
Created on Mar 1, 2017

@author: symbio
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
class AddOMWarningpage(BasePage.Action):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.warningtittle_loc=(By.XPATH,"/html/body/div[4]/div/div/div[1]/h4")
        self.warningmessage_loc=(By.XPATH,"/html/body/div[4]/div/div/div[2]")
        self.warningOKbutton_loc=(By.XPATH,"/html/body/div[4]/div/div/div[3]/ul/li[1]/a")
        
    def click_OK(self):
        self.find_element(*self.warningOKbutton_loc).click()
    
    def get_warningtittle(self):
        return self.find_element(*self.warningtittle_loc).text
    
    def get_warningmessage(self):
        return self.find_element(*self.warningmessage_loc).text
        