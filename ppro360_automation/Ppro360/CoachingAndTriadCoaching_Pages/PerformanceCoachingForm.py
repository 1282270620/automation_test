'''
Created on 20170707

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class PerformanceCoachingForm(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.shortcomments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[%d]/div/input"
        self.shortcomments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[%d]/label"
        self.longcomments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.longcomments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        self.remarkscomments_path="//*[@id='container']/div/section/div/form/div[2]/div[11]/div[%d]/div[2]/input"
        self.remarkscomments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[11]/div[%d]/div[1]/div[1]"
        self.chooseclick_path="//*[@id='container']/div/section/div/form/div[2]/div[11]/div[%d]/div/div[2]/div[%d]/i"
        self.calldate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/input")
        self.timebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/span/span")
        self.dayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.bigleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th/span")
        self.bigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.monthandyearbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]")
        self.smallleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th")
        self.smallrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]")
        self.yearclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.monthclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
        
    def input_shortcomments (self,lineindex,columnindex,text):
        self.shortcomments_loc=(By.XPATH,self.shortcomments_path %(lineindex,columnindex) )
        self.Input_text(text,*self.shortcomments_loc)
        
    def get_shortcomments(self,lineindex,columnindex):
        self.shortcomments_loc=(By.XPATH,self.shortcomments_path %(lineindex,columnindex) )
        return self.find_element(*self.shortcomments_loc).get_attribute("value")

    def shortcomments_disabled(self,lineindex,columnindex):
        self.shortcomments_loc=(By.XPATH,self.shortcomments_path %(lineindex,columnindex))
        flag=self.find_element(*self.shortcomments_loc).get_attribute("disabled")
        return flag 
        
    def get_shortcommentsBoxtitle(self,lineindex,columnindex):
        self.shortcomments_title_loc=(By.XPATH,self.shortcomments_title_path %(lineindex,columnindex))
        return self.find_element(*self.shortcomments_title_loc).text
    
    def input_longcomments (self,lineindex,text):
        self.longcomments_loc=(By.XPATH,self.longcomments_path %lineindex )
        self.Input_text(text,*self.longcomments_loc)
        
    def get_longcomments(self,lineindex):
        self.longcomments_loc=(By.XPATH,self.longcomments_path %lineindex )
        return self.find_element(*self.longcomments_loc).get_attribute("value")

    def longcomments_disabled(self,lineindex):
        self.longcomments_loc=(By.XPATH,self.longcomments_path %lineindex )
        flag=self.find_element(*self.longcomments_loc).get_attribute("disabled")
        return flag 
        
    def get_longcommentsBoxtitle(self,lineindex):
        self.longcomments_title_loc=(By.XPATH,self.longcomments_title_path %lineindex)
        return self.find_element(*self.longcomments_title_loc).text

    def get_calldate(self):
        return self.find_element(*self.calldate_loc).get_attribute("value")
    
    def calldate_disabled(self):
        flag=self.find_element(*self.calldate_loc).get_attribute("disabled")
        return flag 
        
    def input_remarkscomments (self,lineindex,text):
        self.remarkscomments_loc=(By.XPATH,self.remarkscomments_path %lineindex )
        self.Input_text(text,*self.remarkscomments_loc)
        
    def get_remarkscomments(self,lineindex):
        self.remarkscomments_loc=(By.XPATH,self.remarkscomments_path %lineindex )
        return self.find_element(*self.remarkscomments_loc).get_attribute("value")

    def remarkscomments_disabled(self,lineindex):
        self.remarkscomments_loc=(By.XPATH,self.remarkscomments_path %lineindex )
        flag=self.find_element(*self.remarkscomments_loc).get_attribute("disabled")
        return flag 
        
    def get_remarkscommentsBoxtitle(self,lineindex):
        self.remarkscomments_title_loc=(By.XPATH,self.remarkscomments_title_path %lineindex)
        return self.find_element(*self.remarkscomments_title_loc).text
        
    def click_chooseclick (self,lineindex,columnindex):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(lineindex,columnindex))
        self.find_element(*self.chooseclick_loc).click()
        
    def chooseclick_disabled(self,lineindex,columnindex):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(lineindex,columnindex) )
        flag=self.find_element(*self.chooseclick_loc).get_attribute("disabled")
        return flag
    
    def get_chooseclicktatus(self,lineindex,columninde):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(lineindex,columninde))
        checkstataus=self.find_element(*self.chooseclick_loc).get_attribute("class")
        return checkstataus
    
    def click_timebutton (self):
        self.find_element(*self.timebutton_loc).click()
        
    def timebutton_disabled(self):
        flag=self.find_element(*self.timebutton_loc).get_attribute("disabled")
        return flag
        
    def click_dayclick (self,lineindex,columnindex):
        self.dayclick_loc=(By.XPATH,self.dayclick_path %(lineindex,columnindex))    
        self.find_element(*self.dayclick_loc).click()
        
    def click_bigleftarrow (self):
        self.find_element(*self.bigleftarrow_loc).click()
        
    def click_bigrightarrow (self):
        self.find_element(*self.bigrightarrow_loc).click()
    
    def click_monthandyearbutton (self):
        self.find_element(*self.monthandyearbutton_loc).click()
        
    def click_yearclick (self,lineindex):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %lineindex)
        self.find_element(*self.yearclick_loc).click()
    
    def click_monthclick (self,lineindex):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %lineindex)
        self.find_element(*self.monthclick_loc).click()
        
        
    def click_smallleftarrow (self):
        self.find_element(*self.smallleftarrow_loc).click()
        
    def click_smallrightarrow (self):
        self.find_element(*self.smallrightarrow_loc).click()
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
