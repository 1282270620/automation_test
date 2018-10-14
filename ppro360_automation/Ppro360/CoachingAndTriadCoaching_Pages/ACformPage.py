'''
Created on 2017.3.2

@author: yalan.yin
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
class ACformPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
        self.FisrtTL_loc=(By.CSS_SELECTOR,"i.icon-arrow-up")
        self.FirstTL_loc=(By.XPATH, '//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[1]/td[1]')
        self.evaluate_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div/textarea')
        self.checkForunderstanding_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/textarea')
        self.identifyAndRemove_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/textarea')
        self.setEandC_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div/textarea')
        self.reconfirm_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/div/textarea')
        self.otherNandR_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[7]/div/textarea')
    
    def click_KPIcheckbox (self, checkboxorder):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorder)
        self.find_element (*self.KPIcheckbox_loc).click()  

    def input_identifyAndRemove (self, inputtext):
        self.find_element (*self.identifyAndRemove_loc).clear()
        self.find_element (*self.identifyAndRemove_loc).click()
    
        
    def input_evaluate (self, inputtext):
        self.find_element(*self.evaluate_loc).clear()
        self.find_element(*self.evaluate_loc).send_keys(inputtext)
        
    def input_checkForunderstanding (self, inputtext):
        self.find_element(*self.checkForunderstanding_loc).clear()
        self.find_element(*self.checkForunderstanding_loc).send_keys(inputtext)
        
    def input_setEandC (self, inputtext):
        self.find_element(*self.setEandC_loc).clear()
        self.find_element(*self.setEandC_loc).send_keys(inputtext)
        
    def input_reconfirm (self, inputtext):
        self.find_element(*self.reconfirm_loc).clear()
        self.find_element(*self.reconfirm_loc).send_keys(inputtext)
        
    def input_OtherNandR (self, inputtext):
        self.find_element(*self.otherNandR_loc).clear()
        self.find_element(*self.otherNandR_loc).send_keys(inputtext)
        
        
        