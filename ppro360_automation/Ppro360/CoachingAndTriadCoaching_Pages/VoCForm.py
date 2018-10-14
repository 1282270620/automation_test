'''
Created on 20171227

@author: luming.zhao
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from MySQLdb.constants import FLAG
from operator import index
from __builtin__ import True
from pip._vendor.pyparsing import line


class VoCForm(BasePage.Action):

    def __init__(self):
        
        self.Auditors_hird_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div/input")
        self.Auditors_hird_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/label")
        self.AvayaDRS_ID_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[1]/div/input")
        self.AvayaDRS_ID_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[1]/label")
        self.Ban_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/div/input")
        self.Ban_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div[2]/label")
        self.Remarks_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/textarea")
        self.Remarks_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/label")
        
        self.calldate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/input")
        self.dayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.bigleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th/span")
        self.bigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.monthandyearbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]")
        self.yearclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.monthclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        
        self.AuditPurpose_click_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[1]/div/span")
        self.AuditPurpose_path="//*[@id='container']/div/section/div/form/div[2]/div[4]/div[1]/div/ul/li[%d]/a" #%d just 1-5
        self.CallDisposition_click_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[5]/div/div/span")
        self.CallDisposition_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/div/div/ul/li[%d]/a" #%d just 1-7
        self.DetractorRCA_click_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/div/span")
        self.DetractorRCA_path="//*[@id='container]/div/section/div/form/div[2]/div[4]/div[2]/div/ul/li[%d]/a" #%d just 1-27
        self.CoachingMethodology_click_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[8]/div/div/div[2]/div/span")
        self.CoachingMethodology_path="//*[@id='container']/div/section/div/form/div[2]/div[8]/div/div/div[2]/div/ul/li[%d]/a" #%d just 1-3
        
        self.WarmlyWelcome_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div[1]/div/div[%d]/div[2]/div[%d]/label"
        self.UncoverNeeds_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div[2]/div/div[%d]/div[2]/div[%d]/label"
        self.PersonalizeSolution_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div[3]/div/div[%d]/div[2]/div[%d]/label"
        self.GainAgreement_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div[4]/div/div[2]/div[2]/div[%d]/label"
        self.ThoroughlyEducate_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div[5]/div/div[%d]/div[2]/div[%d]/label"
        self.SincerelyThanks_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div[6]/div/div[%d]/div[2]/div[%d]/label"
        self.Survey_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div/div[7]/div/div[%d]/div[2]/div[%d]/label"
        
    def input_Auditors_hird(self,text):
        self.Input_text(text,*self.Auditors_hird_loc)
    def get_Auditors_hird(self):
        return self.find_element(*self.Auditors_hird_loc).get_attribute("value")
    def Auditors_hird_disabled(self):
        flag=self.find_element(*self.Auditors_hird_loc).get_attribute("disabled")
        return flag
    def get_Auditors_hirdBoxTitle(self):
        return self.find_element(*self.Auditors_hird_title_loc).text
        
        
    def input_AvayaDRS_ID(self,text):
        self.Input_text(text,*self.AvayaDRS_ID_loc)
    def get_AvayaDRS_ID(self):
        return self.find_element(*self.AvayaDRS_ID_loc).get_attribute("value")
    def AvayaDRS_ID_disabled(self):
        flag=self.find_element(*self.AvayaDRS_ID_loc).get_attribute("disabled")
        return flag
    def get_AvayaDRS_IDBoxTitle(self):
        return self.find_element(*self.AvayaDRS_ID_title_loc).text
        
        
    def input_Ban(self,text):
        self.Input_text(text,*self.Ban_loc)
    def get_Ban(self):
        return self.find_element(*self.Ban_loc).get_attribute("value")
    def Ban_disabled(self):
        flag=self.find_element(*self.Ban_loc).get_attribute("disabled")
        return flag
    def get_BanBoxTitle(self):
        return self.find_element(*self.Ban_title_loc).text
        
        
    def input_Remarks(self,text):
        self.Input_text(text,*self.Remarks_loc)
    def get_Remarks(self):
        return self.find_element(*self.Remarks_loc).get_attribute("value")
    def Remarks_disabled(self):
        flag=self.find_element(*self.Remarks_loc).get_attribute("disabled")
        return flag
    def get_RemarksBoxTitle(self):
        return self.find_element(*self.Remarks_title_loc).text
        
    def get_calldate(self):
        return self.find_element(*self.calldate_loc).get_attribute("value")
    def calldate_disabled(self):
        flag=self.find_element(*self.calldate_loc).get_attribute("disabled")
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
        
        
        
        
        
        
        