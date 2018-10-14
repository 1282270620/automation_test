'''
Created on 20170706

@author: luming.zhao
'''


from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class SalesSupporSideBySideFormPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.calendar_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/span/span")#Click calendar button
        self.date_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td")#choose date default first line first date
        self.mediaTactic_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/input")
        
        
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, "//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i" %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
        
    def input_callRecordingNumber(self,text):
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);   
    
    def click_calendar(self):
        self.find_element(*self.calendar_loc).click()
        
    def click_date(self):
        self.find_element(*self.date_loc).click()
    
    def click_checkbox(self,checkboxindex):
        self.checkbox_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/div[%d]/i" %checkboxindex)
        self.find_element(*self.checkbox_loc).click()
        
    def input_callbehavior(self,text,callbehaviorindex):
        self.callbehavior_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[4]/div[%d]/div/textarea" %callbehaviorindex)
        self.find_element(*self.callbehavior_loc).send_keys(text)
        
    def input_kpibehavior(self,text,behaviorindex):
        self.kpibehavior_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[%d]/div[2]/input" %behaviorindex)
        self.find_element(*self.kpibehavior_loc).send_keys(text)
        
    def input_goalbehavior(self,text,behaviorindex):
        self.goalbehavior_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[%d]/div[2]/input[2]" %behaviorindex)
        self.find_element(*self.goalbehavior_loc).send_keys(text)   
        
    def click_calendarbehavior(self,behaviorindex):
        self.calendarbehavior_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[%d]/div[2]/div/div/div[2]/span/span" %behaviorindex)#Click  PERFORMANCE TO DATE calendar
        self.find_element(*self.calendarbehavior_loc).click()
        
    def click_datebehavior(self,behaviorindex):
        self.datebehavior_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[%d]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td" %behaviorindex)
        self.find_element(*self.datebehavior_loc).click()
        
    def input_notesbox(self,text,notesindex):
        #notesindex can be only 1 or 7 or 14 or 21 or 25
        self.notesbox_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[4]/textarea" %notesindex)
        self.find_element(*self.notesbox_loc).send_keys(text)
        
    def input_firstlineofmodulebox(self,text,moduleindex):
        #moduleindex can only be 1 or 7 or 14 or 21 or 25
        self.firstlineofmodulebox_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[3]" %moduleindex)
        self.find_element(*self.firstlineofmodulebox_loc).send_keys(text) 
        
    def input_otherlineofmodulebox(self,text,lineindex):       
        #lineindex can only be 2 to 31,except 1 or 7 or 14 or 21 or 25
        self.otherlineofmodulebox_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]" %lineindex)
        self.find_element(*self.otherlineofmodulebox_loc).send_keys(text)
        
    def input_strengthsobserved(self,text):
        self.strengthsobserved_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[33]/td/textarea")
        self.find_element(*self.strengthsobserved_loc).send_keys(text)
        
    def input_developmentopportunities(self,text):
        self.developmentopportunities_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[35]/td/textarea")
        self.find_element(*self.developmentopportunities_loc).send_keys(text)
        
    def input_improvement(self,text,improvementindex):
        self.improvement_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[37]/td/div[%d]/textarea" %improvementindex)
        self.find_element(*self.improvement_loc).send_keys(text)
        
    def input_agentcommitment(self,text,agentindex):
        self.agentcommitment_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/table/tbody/tr[39]/td/div[%d]/textarea" %agentindex)
        self.find_element(*self.agentcommitment_loc).send_keys(text)
        
    def input_teamManagerCommitment(self,text):
        self.teammanagercommitment_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/table/tbody/tr[41]/td/textarea")
        self.find_element(*self.teammanagercommitment_loc).send_keys(text)
 
 
        
        
        
        
        
        
        