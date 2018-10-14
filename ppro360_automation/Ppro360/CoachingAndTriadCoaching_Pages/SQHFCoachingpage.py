'''
Created on 2017/03/17

@author: luming.zhao
'''


from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class SQHFCoachingpage(BasePage.Action):


    def __init__(self):
       
        self.calendar_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/span/span")
        self.date_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td[3]")
        self.tactic_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/input")
        self.reason_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/div/div[3]/i")
        self.beginText_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/table/tbody/tr[13]/td/div/textarea")
        self.earnText_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/table/tbody/tr[13]/td/div/textarea")
        self.sellText_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/table/tbody/tr[13]/td/div/textarea")
        self.turnText_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/table/tbody/tr[5]/td/div/textarea")
        self.exceedText_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[8]/table/tbody/tr[4]/td/div/textarea")
        self.standardText_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[9]/table/tbody/tr[8]/td/div/textarea")
        self.strengths_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[10]/div/textarea")
        self.opportunities1_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[2]/td[2]/div/textarea")
        self.opportunities2_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[3]/td[2]/div/textarea")
        self.plan1_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[5]/td[2]/div/textarea")
        self.plan2_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[6]/td[2]/div/textarea")
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")
        self.eachRadio_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/table/tbody/tr[2]/td[2]/div/div[1]/i")
        
        
    def click_calendar(self):
        self.find_element(*self.calendar_loc).click()
    
    def click_date(self):
        self.find_element(*self.date_loc).click()
    
    def select_eachRadio(self,moduleindex,lineindex,radioindex):
        eachRadio_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[%d]/table/tbody/tr[%d]/td[2]/div/div[%d]/i" %(moduleindex,lineindex,radioindex))
        self.find_element(*self.eachRadio_loc).click()
       
    def input_tactic(self,text):
        self.find_element(*self.tactic_loc).send_keys(text)
    
    def click_reason(self):
        self.find_element(*self.reason_loc).click()
        
    def input_beginText(self,text):
        self.find_element(*self.beginText_loc).send_keys(text)
        
    def input_earnText(self,text):
        self.find_element(*self.earnText_loc).send_keys(text)
        
    def input_sellText(self,text):
        self.find_element(*self.sellText_loc).send_keys(text)
        
    def input_turnText(self,text):
        self.find_element(*self.turnText_loc).send_keys(text)
        
    def input_exceedText(self,text):
        self.find_element(*self.beginText_loc).send_keys(text)
        
    def input_standardText(self,text):
        self.find_element(*self.standardText_loc).send_keys(text)
        
    def input_strengths(self,text):
        self.find_element(*self.strengths_loc).send_keys(text)
        
    def input_opportunities1(self,text):
        self.find_element(*self.opportunities1_loc).send_keys(text)
        
    def input_opportunities2(self,text):
        self.find_element(*self.opportunities2_loc).send_keys(text)
        
    def input_plan1(self,text):
        self.find_element(*self.plan1_loc).send_keys(text)
        
    def input_plan2(self,text):
        self.find_element(*self.plan2_loc).send_keys(text)
        
       
    def click_savebutton(self):
        self.find_element(*self.savebutton_loc).click() 