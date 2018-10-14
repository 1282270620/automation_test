'''
Created on 20170710

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class VO6CerfificationForm(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.btn_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/input")
        self.brsid_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/div/input")
        self.auditor_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/input")
        self.verbatim_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/div/input")
        self.name_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.reasonforcallingclick_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/div/span")
        self.reasonforcallingchoose_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/div/div/ul/li[%d]/a"
        self.detractor_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div/span")
        self.detractorchoose_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div/ul/li[%d]/a"
        self.calldispositionclick_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[2]/div/span")
        self.calldispositionchoose_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[2]/div/ul/li[%d]/a"
        self.chooseclick_path="//*[@id='container']/div/section/div/form/div[2]/div[7]/div/div[%d]/div/div[%d]/div[2]/div[%d]/i"
        self.accounttype_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/div[9]/div/div/div[2]/div/span")
        self.accounttypechoose_path="//*[@id='container']/div/section/div/form/div[2]/div[7]/div/div[9]/div/div/div[2]/div/ul/li[%d]/a"
        self.vocprojectionclick_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/div[9]/div/div[6]/div[2]/div/span")
        self.vocprojectionchoose_path="//*[@id='container']/div/section/div/form/div[2]/div[7]/div/div[9]/div/div[6]/div[2]/div/ul/li[%d]/a"
        self.timebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/span/span")
        self.dayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.bigleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th/span")
        self.bigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.monthandyearbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]")
        self.yearclick_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.monthclick_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.smallleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th")
        self.smallrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]")
        self.auditpurpose_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/span")
        self.auditpurposechoose_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/ul/li[%d]/a"
        self.coachingcomments_path="//*[@id='container']/div/section/div/form/div[2]/div[7]/div/div[10]/div/div[%d]/div[2]/input"
         
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex)
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text); 
        
    def input_btn (self,text):
        self.find_element(*self.btn_loc).send_keys(text); 
        
    def input_brsid (self,text):
        self.find_element(*self.brsid_loc).send_keys(text); 
        
    def inpt_auditor (self,text):
        self.find_element(*self.auditor_loc).send_keys(text);
        
    def input_verbatim (self,text):
        self.find_element(*self.verbatim_loc).send_keys(text);

    def input_name (self,text):
        self.find_element(*self.name_loc).send_keys(text);
        
    def input_coachingcomments(self,text,lineindex11):
        self.coachingcomments_loc=(By.XPATH,self.coachingcomments_path %lineindex11)
        self.find_element(*self.coachingcomments_loc).send_keys(text)
        
    def click_auditpurpose(self):
        self.find_element(*self.auditpurpose_loc).click()
        
    def click_auditpurposechoose(self,lineindex10):
        self.auditpurposechoose_loc=(By.XPATH,self.auditpurposechoose_path %lineindex10)
   
    def click_reasonforcallingclick (self):
        self.find_element(*self.reasonforcallingclick_loc).click()
        
    def click_reasonforcallingchoose (self,lineindex):
        self.reasonforcallingchoose_loc=(By.XPATH,self.reasonforcallingchoose_path %lineindex)
        self.find_element(*self.reasonforcallingchoose_loc).click()
        
    def click_detractor (self):
        self.find_element(*self.detractor_loc).click()
        
    def click_detractorchoose (self,lineindex2):
        self.detractorchoose_loc=(By.XPATH,self.detractorchoose_path %lineindex2)
        self.find_element(*self.detractorchoose_loc).click()
        
    def click_calldispositionclick (self):
        self.find_element(*self.calldispositionclick_loc).click()
        
    def click_calldispositionchoose (self,lineindex3):
        self.calldispositionchoose_loc=(By.XPATH,self.calldispositionchoose_path %lineindex3)
        self.find_element(*self.calldispositionchoose_loc).click()
        
    def click_chooseclick (self,moduleindex,lineindex4,columnindex):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(moduleindex,lineindex4,columnindex))
        self.find_element(*self.chooseclick_loc).click()
    
    def click_accounttype (self):
        self.find_element(*self.accounttype_loc).click()
        
    def click_accounttypechoose (self,lineindex5):
        self.accounttypechoose_loc=(By.XPATH,self.accounttypechoose_path %lineindex5)
        self.find_element(*self.accounttypechoose_loc).click()
        
    def click_vocprojectionclick (self):
        self.find_element(*self.vocprojectionclick_loc).click()
        
    def click_vocprojectionchoose (self,lineindex6):
        self.vocprojectionchoose_loc=(By.XPATH,self.vocprojectionchoose_path %lineindex6)
        self.find_element(*self.vocprojectionchoose_loc).click()
        
    def click_timebutton (self):
        self.find_element(*self.timebutton_loc).click()
        
    def click_dayclick (self,lineindex7,columnindex2):
        self.dayclick_loc=(By.XPATH,self.dayclick_path %(lineindex7,columnindex2))    
        self.find_element(*self.dayclick_loc).click()
        
    def click_bigleftarrow (self):
        self.find_element(*self.bigleftarrow_loc).click()
    
    def click_bigrightarrow (self):
        self.find_element(*self.bigrightarrow_loc).click()
    
    def click_monthandyearbutton (self):
        self.find_element(*self.monthandyearbutton_loc).click()
        
    def click_yearclick (self,lineindex8):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %lineindex8)
        self.find_element(*self.yearclick_loc).click()
    
    def click_monthclick (self,lineindex9):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %lineindex9)
        self.find_element(*self.monthclick_loc).click()
        
        
    def click_smallleftarrow (self):
        self.find_element(*self.smallleftarrow_loc).click()
        
    def click_smallrightarrow (self):
        self.find_element(*self.smallrightarrow_loc).click()
        
    
    
        

    
    
