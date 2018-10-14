'''
Created on Jun 22, 2018

@author: symbio
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
class DatePickerPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #self.CurrentYearAndMonth=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[2]")
        #self.CurrentYearAndMonth=(By.CLASS_NAME,"switch")
        self.CurrentDate=(By.CLASS_NAME,"day active today")
        self.DisableDate=(By.CLASS_NAME,"day disabled")
    
    def select_currentDate(self):
        self.find_element(*self.CurrentDate).click()
        
