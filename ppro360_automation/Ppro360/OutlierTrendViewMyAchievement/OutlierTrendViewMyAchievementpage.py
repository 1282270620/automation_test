'''
Created on 20180227

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from selenium import webdriver

class OutlierTrendViewMyAchievementpage(BasePage.Action):
    
    
    def __init__(self):
        self.formtitle_loc=(By.XPATH,"//*[@id='container']/div/nav/div/span")
        self.sn_loc=(By.XPATH,"//*[@id='sn']")
        self.employeeName_loc=(By.XPATH,"//*[@id='employee_Name']")
        self.coachname_loc=(By.XPATH,'//*[@id="coach_title"]')
        self.completeddate_loc=(By.XPATH,'//*[@id="date"]')
        self.callRecordingNumber_loc=(By.XPATH,'//*[@id="callRecordingNumber"]')
        self.get_backbutton_loc=(By.XPATH,'//*[@id="container"]/div/nav/a/div/div')
        self.loginrole_loc=(By.XPATH,'//*[@id="container"]/div/nav/ul/li/a/div/div/dl/dt')
        self.loginlobandsite_loc=(By.XPATH,'//*[@id="container"]/div/nav/ul/li/a/div/div/dl/dd')
        self.threebutton_path='//*[@id="container"]/div/section/div/div[2]/a[%d]'
        self.backbutton_loc=(By.XPATH,'//*[@id="container"]/div/nav/a/div/div')
        self.warnmessage_path='//*[@id="container"]/div/div[2]/div/p[%d]'
        self.Confirmation_path='//*[@id="add-qa-coaching-modal"]/section/p[%d]'
        self.yesorno_path='//*[@id="add-qa-coaching-modal"]/footer/ul/li[%d]/a'
        self.typeandstatusclick_path='//*[@id="container"]/div/section/div/div[1]/div/div[%d]/div[3]/div/span'
        self.typeandstatuschoose_path='//*[@id="container"]/div/section/div/div[1]/div/div[%d]/div[3]/div/ul/li[%d]/a'
        self.fillter_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[1]/div/div[4]/button[1]')
        

    def get_formtitle(self):
        return self.find_element(*self.formtitle_loc).text
    
    def get_sn(self):
        return self.find_element(*self.sn_loc).get_attribute("value")
    
    def input_sn(self,text):
        self.Input_text(text,*self.sn_loc)
        
    def get_employeeName(self):
        return self.find_element(*self.employeeName_loc).get_attribute("value")
        
    def get_coachname(self):
        return self.find_element(*self.coachname_loc).get_attribute("value")
        
    def get_completeddate(self):
        return self.find_element(*self.completeddate_loc).get_attribute("value")
    
    def get_callRecordingNumber(self):
        return self.find_element(*self.callRecordingNumber_loc).get_attribute("value")
    
    def input_callRecordingNumber(self,text):
        self.Input_text(text,*self.callRecordingNumber_loc)
        
    def get_backbutton(self):
        return self.find_element(*self.backbutton_loc).text
        
    def click_backbutton(self):
        self.find_element(*self.backbutton_loc).click()
        
    def get_loginrole(self):
        return self.find_element(*self.loginrole_loc).text
        
    def get_loginlobandsite(self):
        return self.find_element(*self.loginlobandsite_loc).text
    def get_threebutton(self,index):
        self.threebutton_loc=(By.XPATH,self.threebutton_path %index)  
        return self.find_element(*self.threebutton_loc).text
            
    def click_threebutton(self,index):
        self.threebutton_loc=(By.XPATH,self.threebutton_path %index)  
        self.find_element(*self.threebutton_loc).click()
    
    def get_warnmessage(self,index):
        self.warnmessage_loc=(By.XPATH,self.warnmessage_path %index)
        return self.find_element(*self.warnmessage_loc).text
    
    def get_Confirmation(self,index):
        self.Confirmation_loc=(By.XPATH,self.Confirmation_path %index)
        return self.find_element(*self.Confirmation_loc).text
    
    def click_yesorno(self,index):
        self.yesorno_loc=(By.XPATH,self.yesorno_path %index)
        self.find_element(*self.yesorno_loc).click()
    
    def click_typeandstatusclick(self,index):
        self.typeandstatusclick_loc=(By.XPATH,self.typeandstatusclick_path %index)
        self.find_element(*self.typeandstatusclick_loc).click()
        
    def click_typeandstatuschoose(self,index,index2):
        self.typeandstatuschoose_loc=(By.XPATH,self.typeandstatuschoose_path %(index,index2))
        self.find_element(*self.typeandstatuschoose_loc).click()
        
    def get_typeandstatuschoose(self,index,index2):
        self.typeandstatuschoose_loc=(By.XPATH,self.typeandstatuschoose_path %(index,index2))
        return self.find_element(*self.typeandstatuschoose_loc).text
        
    def click_fillter(self):
        self.find_element(*self.fillter_loc).click()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        