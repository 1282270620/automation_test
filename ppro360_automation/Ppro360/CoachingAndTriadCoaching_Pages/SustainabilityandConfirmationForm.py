'''
Created on 20170707

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class SustainabilityandConfirmationForm(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.input_lastonecomment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/textarea")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div/div/table/tbody/tr[4]/td[%d]/i"
        self.scoring_path="//div[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/div[2]/div[%d]/div[%d]/input"
        self.tlcomments_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[%d]/td[2]/textarea"
        self.trendingfeedback_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/div/table/tbody/tr[%d]/td[2]/textarea"
        self.startdatebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/span/span")
        self.startdayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.startbigleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th/span")
        self.startbigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.startmonthandyearbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]")
        self.startyearclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.startmonthclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.startsmallleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th")
        self.startsmallrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]")
        self.enddatebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/span/span")
        self.enddayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.endbigleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th/span")
        self.endbigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.endmonthandyearbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]")
        self.endyearclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.endmonthclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.endsmallleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th")
        self.endsmallrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]")
        
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
        
    def input_scoring (self,columnindex,lineindex,text2):
        self.scoring_loc=(By.XPATH,self.scoring_path %(columnindex,lineindex))
        self.find_element(*self.scoring_loc).send_keys(text2);
        
    def input_tlcomments (self,lineindex2,text):
        self.tlcomments_loc=(By.XPATH,self.tlcomments_path %lineindex2)
        self.find_element(*self.tlcomments_loc).send_keys(text);
        
    def input_trendingfeedback (self,lineindex3,text):
        self.trendingfeedback_loc=(By.XPATH,self.trendingfeedback_path %lineindex3)
        self.find_element(*self.trendingfeedback_loc).send_keys(text);
      
    def input_lastonecomment (self,text):
        self.find_element(*self.input_lastonecomment_loc).send_keys(text);
        
    def click_startdatebutton (self):
        self.find_element(*self.startdatebutton_loc).click()
    
    def click_startdayclick (self,lineindex6,columnindex2):
        self.startdayclick_loc=(By.XPATH,self.startdayclick_path %(lineindex6,columnindex2))    
        self.find_element(*self.startdayclick_loc).click()
        
    def click_startbigleftarrow (self):
        self.find_element(*self.startbigleftarrow_loc).click()
        
    def click_startbigrightarrow (self):
        self.find_element(*self.startbigrightarrow_loc).click()
    
    def click_startmonthandyearbutton (self):
        self.find_element(*self.startmonthandyearbutton_loc).click()

    def click_startyearclick (self,lineindex4):
        self.startyearclick_loc=(By.XPATH,self.startyearclick_path %lineindex4)
        self.find_element(*self.startyearclick_loc).click()
    
    def click_startmonthclick (self,lineindex5):
        self.startmonthclick_loc=(By.XPATH,self.startmonthclick_path %lineindex5)
        self.find_element(*self.startmonthclick_loc).click()
        
        
    def click_startsmallleftarrow (self):
        self.find_element(*self.startsmallleftarrow_loc).click()
        
    def click_startsmallrightarrow (self):
        self.find_element(*self.startsmallrightarrow_loc).click()
        
    def click_enddatebutton (self):
        self.find_element(*self.enddatebutton_loc).click()
    
    def click_enddayclick (self,lineindex9,columnindex3):
        self.enddayclick_loc=(By.XPATH,self.enddayclick_path %(lineindex9,columnindex3))    
        self.find_element(*self.enddayclick_loc).click()
        
    def click_endbigleftarrow (self):
        self.find_element(*self.endbigleftarrow_loc).click()
        
    def click_endbigrightarrow (self):
        self.find_element(*self.endbigrightarrow_loc).click()
    
    def click_endmonthandyearbutton (self):
        self.find_element(*self.endmonthandyearbutton_loc).click()
        
    def click_endyearclick (self,lineindex7):
        self.endyearclick_loc=(By.XPATH,self.endyearclick_path %lineindex7)
        self.find_element(*self.endyearclick_loc).click()
    
    def click_endmonthclick (self,lineindex8):
        self.endmonthclick_loc=(By.XPATH,self.endmonthclick_path %lineindex8)
        self.find_element(*self.endmonthclick_loc).click()
        
        
    def click_endsmallleftarrow (self):
        self.find_element(*self.endsmallleftarrow_loc).click()
        
    def click_endsmallrightarrow (self):
        
        self.find_element(*self.endsmallrightarrow_loc).click()
        
        
        
        
        
    