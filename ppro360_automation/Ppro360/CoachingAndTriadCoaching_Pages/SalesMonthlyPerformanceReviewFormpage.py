'''
Created on 20170622

@author: luming.zhao
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage



class SalesMonthlyPerformanceReviewFormpage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.lastMonthPerformance_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/thead/tr/th[4]/input")
        self.previousMonthPerformance_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/thead/tr/th[6]/input")
        self.summary_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.agentCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div/textarea")
        self.teamManagerCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/textarea")
        self.otherNotes_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div/textarea")
        
        self.monthlyPerformances_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/input")
        
        self.behaviorAndKpi_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[2]/td[2]/div/textarea")
        
        self.behavioradio_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[2]/td[3]/div[2]/div/div/i")
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorderindex)    
     
        
    def input_callRecordingNumber(self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
        
    def input_lastMonthPerformance(self,text):
        self.find_element(*self.lastMonthPerformance_loc).send_keys(text);
        
    def input_previousMonthPerformance(self,text):
        self.find_element(*self.previousMonthPerformance_loc).send_keys(text);
       
    def input_summary(self,text):
        self.find_element(*self.summary_loc).send_keys(text);
        
    def input_agentCommitment(self,text):
        self.find_element(*self.agentCommitment_loc).send_keys(text);
        
    def input_teamManagerCommitment(self,text):
        self.find_element(*self.teamManagerCommitment_loc).send_keys(text);
        
    def input_otherNotes(self,text):
        self.find_element(*self.otherNotes_loc).send_keys(text);
        
    def input_monthlyPerformances(self,text,lineindex,columnindex):
        monthlyPerformances_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[%d]/input"%(lineindex,columnindex));
        self.find_element(*monthlyPerformances_loc).send_keys(text);
    
    def input_behaviorAndKpi(self,text,behaviorindex):
        behaviorAndKpi_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/div/textarea"%(behaviorindex));
        self.find_element(*behaviorAndKpi_loc).send_keys(text);
    
    def input_behavioradio(self,text,moduleindex,behaciorindex,radioindex):
        behavioradio_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[%d]/td[3]/div[%d]/div/div[%d]/i"%(moduleindex,behaciorindex,radioindex))
        self.find_element(*behavioradio_loc).send_keys(text);
