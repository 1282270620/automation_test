'''
Created on 20170627

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class CustomerExperienceImprovementCalibration(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.selectbotton_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[2]/div/span" 
        self.scorechoose_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[2]/div/ul/li[%d]/a"
        self.lasttwoinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.midinput_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[%d]/textarea"
        self.midinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[1]"
        self.lasttwoinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        self.selectbottonvalue_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[2]/div/span"
        
              
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
        
    def click_selectbotton (self,moduleindex):
        self.selectbotton_loc=(By.XPATH,self.selectbotton_path %moduleindex)
        self.find_element(*self.selectbotton_loc).click()
    
    def get_selectbottonvalue(self,moduleindex):
        self.selectbottonvalue_loc=(By.XPATH,self.selectbottonvalue_path %moduleindex)
        flag=self.find_element(*self.selectbottonvalue_loc).text
        return flag
    
    def selectbotton_disabled(self,moduleindex):
        self.selectbotton_loc=(By.XPATH,self.selectbotton_path %moduleindex)
        flag=self.find_element(*self.selectbotton_loc).get_attribute("disabled")
        return flag
        
    def click_scorechoose (self,moduleindex,lineindex):
        self.scorechoose_loc=(By.XPATH,self.scorechoose_path %(moduleindex,lineindex))
        self.find_element(*self.scorechoose_loc).click()
        
    def input_midinput(self,moduleindex,lineindex,text):
        self.midinput_loc=(By.XPATH,self.midinput_path %(moduleindex,lineindex))
        self.Input_text(text,*self.midinput_loc)

    def get_midinput(self,moduleindex,lineindex):
        self.midinput_loc=(By.XPATH,self.midinput_path %(moduleindex,lineindex) )
        return self.find_element(*self.midinput_loc).get_attribute("value")

    def midinput_disabled(self,moduleindex,lineindex):
        self.midinput_loc=(By.XPATH,self.midinput_path %(moduleindex,lineindex) )
        flag=self.find_element(*self.midinput_loc).get_attribute("disabled")
        return flag 
        
    def get_midinputBoxtitle(self,lineindex):
        self.midinput_title_loc=(By.XPATH,self.midinput_title_path %lineindex)
        return self.find_element(*self.midinput_title_loc).text  
    
    def input_lasttwoinput (self,lineindex,text):
        self.lasttwoinput_loc=(By.XPATH,self.lasttwoinput_path %lineindex)
        self.Input_text(text,*self.lasttwoinput_loc)
        
    def get_lasttwoinput(self,lineindex):
        self.lasttwoinput_loc=(By.XPATH,self.lasttwoinput_path %lineindex )
        return self.find_element(*self.lasttwoinput_loc).get_attribute("value")

    def lasttwoinput_disabled(self,lineindex):
        self.lasttwoinput_loc=(By.XPATH,self.lasttwoinput_path %lineindex )
        flag=self.find_element(*self.lasttwoinput_loc).get_attribute("disabled")
        return flag 
        
    def get_lasttwoinputBoxtitle(self,lineindex):
        self.lasttwoinput_title_loc=(By.XPATH,self.lasttwoinput_title_path %lineindex)
        return self.find_element(*self.lasttwoinput_title_loc).text 
        
        
        
        