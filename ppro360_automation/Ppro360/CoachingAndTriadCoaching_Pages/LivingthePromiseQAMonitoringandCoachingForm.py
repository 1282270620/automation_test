'''
Created on 20170703

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from cgitb import text

class LivingthePromiseQAMonitoringandCoachingForm(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.vgm_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/input")
        self.callid_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/input")
        self.notes_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.threechooseclick_path="//*[@id='container']/div/section/div/form/div[2]/table[%d]/tr[%d]/td[2]/div/div[%d]/i"
        self.fourchooseclick_path="//*[@id='container']/div/section/div/form/div[2]/table[%d]/tr[%d]/td[2]/div/div[%d]/i"
    
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, self.KPIcheckbox_path %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
        
    def input_vgm (self,text):
        self.find_element(*self.vgm_loc).send_keys(text);
        
    def input_callid (self,text):
        self.find_element(*self.callid_loc).send_keys(text);
        
    def click_threechooseclick (self,moduleindex,lineindex,columnindex):
        self.threechooseclick_loc=(By.XPATH,self.threechooseclick_path %(moduleindex,lineindex,columnindex))
        self.find_element(*self.threechooseclick_loc).click()
        
    def click_fourchooseclick (self,moduleindex2,lineindex2,columnindex2):
        self.fourchooseclick_loc=(By.XPATH,self.fourchooseclick_path %(moduleindex2,lineindex2,columnindex2))
        self.find_element(*self.fourchooseclick_loc).click()
        
    def input_notes (self,text):
        self.find_element(*self.notes_loc).send_keys(text);