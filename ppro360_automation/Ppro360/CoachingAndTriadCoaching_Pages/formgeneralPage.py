'''
Created on 2017.3.1

@author: yalan.yin
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
class formgeneralPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
        
        self.SaveandContinueLater_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[3]/a[2]")
   
        self.Print_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[3]/a[1]')
        self.CompleteCoach_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[3]/a[3]')
        self.CancelCoach_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[3]/a[4]')
        self.QuitwithoutSave_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[3]/a[5]')
        self.coachtitle_loc=(By.CSS_SELECTOR,"#container > div > nav > div > span")
    
        
    def get_CoachingTitle(self):
        return self.find_element(*self.coachtitle_loc).text
        
    def click_SaveandContinueLater (self):
        self.find_element (*self.SaveandContinueLater_loc).click()

    
    def click_Print (self):
        self.find_element (*self.Print_loc).click()  
    
    def click_CompleteCoach (self):
        self.find_element (*self.CompleteCoach_loc).click()
    
    def click_CancelCoach (self):
        self.find_element (*self.CancelCoach_loc).click ()
        
    def click_QuitwithoutSave (self):
        self.find_element (*self.QuitwithoutSave_loc).click()