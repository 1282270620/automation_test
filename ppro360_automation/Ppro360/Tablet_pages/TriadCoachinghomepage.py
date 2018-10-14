'''
Created on Mar 06, 2017

@author: Sabrina Guo
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
class TriadCoachinghomepage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.SN_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[1]/div[1]/input")
        self.CoachName_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[1]/div[2]/div/span")
        self.EmployeeName_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[2]/div[2]/div/span")
        self.coachnameselect_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[1]/div[2]/div/span/span")
        self.statusselect_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[2]/div[2]/div/span/span")
        self.filterbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[4]/button")
        self.exportbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[2]/div[4]/button")
        self.type_loc=(By.XPATH,"(//span[@type='button'])[3]")
        
    def input_SN(self,SNnumber):
        self.find_element(*self.SN_loc).send_keys(SNnumber)    
        
    def select_coachname(self,coachname):
        coachname_loc=(By.LINK_TEXT,coachname)
        self.find_element(*self.coachnameselect_loc).click()
        self.find_element(*coachname_loc).click()
        
    def click_type(self):
        self.find_element(*self.type_loc).click()
    
    def get_CoachName(self):
        coachname=self.find_element(*self.CoachName_loc).text
        return coachname
        
    
    def get_EmployeeName(self):
        employeename=self.find_element(*self.EmployeeName_loc).text    
        return employeename
        
        
    def get_typename(self,coachname_path):
        coachname_loc=(By.XPATH,coachname_path)
        coachformname = self.find_element(*coachname_loc).text
        return coachformname
    
    def select_status(self,status):
        status_loc=(By.LINK_TEXT,status)
        self.find_element(*self.statusselect_loc).click()
        self.find_element(*status_loc).click()
    
    def click_filterbutton(self):
        self.find_element(*self.filterbutton_loc).click()
    
    def click_exportbutton(self):
        self.find_element(*self.exportbutton_loc).click()
        
    def click_eachcoach(self,eachcoach_loc):
        self.find_element(*(By.XPATH,eachcoach_loc)).click()
    
    