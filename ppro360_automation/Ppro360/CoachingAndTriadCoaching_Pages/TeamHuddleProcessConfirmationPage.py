'''
Created on 20170626

@author: luming.zhao
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By



class TeamHuddleProcessConfirmationPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        
        # Here is lack of datepicker
        
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.focus_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/input")
        self.goal_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/input")
        self.topic_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/input")
        self.strengths_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        self.opportunities_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/textarea")
        self.commitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/textarea")
        
        
        
    def input_click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorderindex) 
    
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);      
    
    def input_focus(self,text):
        self.find_element(*self.focus_loc).send_keys(text);
        
    def input_goal(self,text):
        self.find_element(*self.goal_loc).send_keys(text);
        
    def input_topic(self,text):
        self.find_element(*self.topic_loc).send_keys(text);
        
    def input_fundamentals(self,text,module1index):
        
        #module1index can only be 3 or 5 or 7 or 9
        self.fundamentals_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/textarea" %module1index)
        self.find_element(*self.fundamentals_loc).send_keys(text);
        
    def input_execution(self,text,module2index):
        
        #module1index can only be 12 or 14 or 16 or 18
        self.execution_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/textarea" %module2index) 
        self.find_element(*self.execution_loc).send_keys(text);
        
    def input_specialtopic(self,text,module3index):
        
        #module1index can only be 21 or 23
        self.specialtopic_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/textarea" %module3index) 
        self.find_element(*self.specialtopic_loc).send_keys(text);
        
    def input_blankname(self,text,module4index):
        
        #module1index can only be 26 or 28 or 30 or 32 or 34 or 36 or 38
        self.blankname_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/textarea" %module4index) 
        self.find_element(*self.blankname_loc).send_keys(text); 
        
    def input_strengths(self,text):
        self.find_element(*self.strengths_loc).send_keys(text);
        
    def input_opportunities(self,text):
        self.find_element(*self.opportunities_loc).send_keys(text);
        
    def input_commitment(self,text):
        self.find_element(*self.commitment_loc).send_keys(text);
        
    def select_eachRadio1(self,line1index,radioindex):
        
        #line1index can only be 2 ro 4 or 6 or 8
        #radioinde can only be 1 or 2
        self.eachRadio1_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/tble/tbody/tr[%d]/td[3]/div[%d]/i" %(line1index,radioindex));
        self.find_element(*self.eachRadio1_loc).click()
        
    def select_eachRadio2(self,line2index,radioindex):
        
        #line2index can only be 11 ro 13 or 15 or 17
        #radioinde can only be 1 or 2
        self.eachRadio2_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/tble/tbody/tr[%d]/td[3]/div[%d]/i" %(line2index,radioindex));
        self.find_element(*self.eachRadio2_loc).click()
        
    def select_eachRadio3(self,line3index,radioindex):
        
        #line3index can only be 20 ro 22
        #radioinde can only be 1 or 2
        self.eachRadio3_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/tble/tbody/tr[%d]/td[3]/div[%d]/i" %(line3index,radioindex));
        self.find_element(*self.eachRadio3_loc).click()
        
    def select_eachRadio4(self,line4index,radioindex):
        
        #line4index can only be 25 ro 27 or 29 or 31 or 33 or 35 or 37
        #radioinde can only be 1 or 2
        self.eachRadio4_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/tble/tbody/tr[%d]/td[3]/div[%d]/i" %(line4index,radioindex));
        self.find_element(*self.eachRadio4_loc).click()