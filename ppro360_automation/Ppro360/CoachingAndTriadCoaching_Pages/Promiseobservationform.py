'''
Created on 20170707

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class Promiseobservationform(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div/div/table/tbody/tr[4]/td[%d]/i"
        self.interactionType_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/input")
        self.observationnotes_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.chooseclick_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/div/div/div[%d]/div[2]/div[%d]/i" 
        self.standardlegalcompliancechooseclick_path="//*[@id='container']/div/section/div/form/div[2]/div[15]/div/div[%d]/div[%d]/div/div[2]/div[%d]/i"
        self.timebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/span/span")
        self.dayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.bigleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th/span")
        self.bigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.bigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.monthandyearbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]")
        self.yearclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.monthclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.smallleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th")
        self.smallrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]")
        self.hourbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/span/span")
        self.hourbackbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/span/span")
        self.ampmbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[2]/td[5]/button")
        self.houruparrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr/td/a/span")
        self.hourdownarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[3]/td/a/span")
        self.minuteuparrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr/td[3]/a/span")
        self.minutedownarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[3]/td[3]/a/span")
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
        
    def input_interactionType (self,text):
        self.find_element(*self.interactionType_loc).send_keys(text);
        
    def input_observationnotes (self,text,lineindex):
        self.observationnotes_loc=(By.XPATH,self.observationnotes_path %lineindex)
        self.find_element(*self.observationnotes_loc).send_keys(text);
        
    def click_chooseclick (self,moduleindex,columnindex,lineindex2):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(moduleindex,columnindex,lineindex2))
        self.find_element(*self.chooseclick_loc).click()
        
    def click_standardlegalcompliancechooseclick (self,lineindex3,moduleindex2,columnindex2):
        self.standardlegalcompliancechooseclick_loc=(By.XPATH,self.standardlegalcompliancechooseclick_path %(lineindex3,moduleindex2,columnindex2))
        self.find_element(*self.standardlegalcompliancechooseclick_loc).click()
    
    def click_timebutton (self):
        self.find_element(*self.timebutton_loc).click()
        
    def click_dayclick (self,lineindex4,columnindex3):
        self.dayclick_loc=(By.XPATH,self.dayclick_path %(lineindex4,columnindex3))    
        self.find_element(*self.dayclick_loc).click()
        
    def click_bigleftarrow (self):
        self.find_element(*self.bigleftarrow_loc).click()
        
    def click_bigrightarrow (self):
        self.find_element(*self.bigrightarrow_loc).click()
    
    def click_monthandyearbutton (self):
        self.find_element(*self.monthandyearbutton_loc).click()

    def click_yearclick (self,lineindex5):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %lineindex5)
        self.find_element(*self.yearclick_loc).click()
    
    def click_monthclick (self,lineindex6):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %lineindex6)
        self.find_element(*self.monthclick_loc).click()
        
        
    def click_smallleftarrow (self):
        self.find_element(*self.smallleftarrow_loc).click()
        
    def click_smallrightarrow (self):
        self.find_element(*self.smallrightarrow_loc).click()
        
    def click_hourbutton (self):
        self.find_element(*self.hourbutton_loc).click()
        
    def click_hourbackbutton (self):
        self.find_element(*self.hourbackbutton_loc).click()        
        
    def click_ampmbutton (self):
        self.find_element(*self.ampmbutton_loc).click()
    
    def click_houruparrow (self):
        self.find_element(*self.houruparrow_loc).click()
        
    def click_hourdownarrow (self):
        self.find_element(*self.hourdownarrow_loc).click()
        
    def click_minuteuparrow (self):
        self.find_element(*self.minuteuparrow_loc).click()
        
    def click_minutedownarrow (self):
        self.find_element(*self.minutedownarrow_loc).click()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
          
        
        
        
        
        
        
        
        
        
        
    
    