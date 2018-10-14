'''
Created on 20170629

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class AgentHuddleProcessConfirmation(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.specialtopic_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr/td[2]/input")
        self.specialtopic_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[1]/td[1]")
        self.lastthreeinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.lastthreeinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        self.otherinput_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/textarea" 
        self.otherinput_title_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[1]"
        self.chooseclick_path="//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[3]/div[%d]/i" 
        
        
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path % checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.Input_text(text,*self.callRecordingNumber_loc)
               
    def input_specialtopic (self,text):
        self.Input_text(text,*self.specialtopic_loc)
    
    def get_specialtopic(self):
        return self.find_element(*self.specialtopic_loc).get_attribute("value")
    
    def specialtopic_disabled(self):
        flag=self.find_element(*self.specialtopic_loc).get_attribute("disabled")
        return flag 
    
    def get_specialtopicBoxTitle(self):
        return self.find_element(*self.specialtopic_title_loc).text
        
    def input_lastthreeinput (self,lineindex,text):
        self.lastthreeinput_loc=(By.XPATH,self.lastthreeinput_path %lineindex)
        self.Input_text(text,*self.lastthreeinput_loc)
          
    def get_lastthreeinput(self,lineindex):
        self.lastthreeinput_loc=(By.XPATH,self.lastthreeinput_path %lineindex)
        return self.find_element(*self.lastthreeinput_loc).get_attribute("value")
    
    def lastthreeinput_disabled(self,lineindex):
        self.lastthreeinput_loc=(By.XPATH,self.lastthreeinput_path %lineindex)
        flag=self.find_element(*self.lastthreeinput_loc).get_attribute("disabled")
        return flag 
    
    def get_lastthreeinputBoxTitle(self,lineindex):
        self.lastthreeinput_title_loc=(By.XPATH,self.lastthreeinput_title_path %lineindex)
        return self.find_element(*self.lastthreeinput_title_loc).text

    def input_otherinput(self,lineindex,text):
        self.otherinput_loc=(By.XPATH,self.otherinput_path %lineindex)
        self.Input_text(text,*self.otherinput_loc)
 
    def get_otherinput(self,lineindex):
        self.otherinput_loc=(By.XPATH,self.otherinput_path %lineindex)
        return self.find_element(*self.otherinput_loc).get_attribute("value")
    
    def otherinput_disabled(self,lineindex):
        self.otherinput_loc=(By.XPATH,self.otherinput_path %lineindex)
        flag=self.find_element(*self.lastthreeinput_loc).get_attribute("disabled")
        return flag 
    
    def get_otherinputBoxTitle(self,lineindex):
        self.otherinput_title_loc=(By.XPATH,self.otherinput_title_path %lineindex)
        return self.find_element(*self.otherinput_title_loc).text
    
    def click_chooseclick (self,moduleindex,lineindex):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(moduleindex,lineindex))
        self.find_element(*self.chooseclick_loc).click()
        
    def get_chooseclickStataus(self,moduleindex,lineindex):
        chooseclickStataus_loc=(By.XPATH,self.chooseclick_path %(moduleindex,lineindex))
        chooseclickStataus=self.find_element(*chooseclickStataus_loc).get_attribute("class")
        return chooseclickStataus
