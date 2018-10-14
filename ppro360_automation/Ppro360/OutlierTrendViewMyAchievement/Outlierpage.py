'''
Created on 20180227

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from selenium import webdriver

class Outlierpage(BasePage.Action):
    
    
    def __init__(self):
        self.selectagent_path="//*[@id='container']/div/section/div/div[2]/div/table[%d]/tbody/tr[%d]/td[2]/span"
        self.addCoachButton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[2]/div/table[1]/tbody/tr[1]/td[5]/div/a[2]")
        self.formname_path="//*[@id='container']/div/section/div/div[3]/div/div/section/ul/li[%d]"
        self.addorcancle_path='//*[@id="add-coaching-modal"]/footer/ul/li[%d]/a'
        self.warnmessage_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div/p[1]')
        self.AgentName_path='//*[@id="container"]/div/section/div/div[2]/div/table[%d]/tbody/tr[%d]/td[1]'
        
    def get_AgentName(self,index1,index2):    
        AgentName_loc=(By.XPATH, self.AgentName_path %(index1,index2))
        return self.find_element(*AgentName_loc).text
    
    def click_selectagent(self,index1,index2):
        self.selectagent_loc=(By.XPATH,self.selectagent_path %(index1,index2))
        self.find_element(*self.selectagent_loc).click()
    
    def click_addCoachButton(self):
        self.find_element(*self.addCoachButton_loc).click()
        
    def get_formname(self,index):
        self.formname_loc=(By.XPATH,self.formname_path %index)
        return self.find_element(*self.formname_loc).text
    
    def click_form(self,index):
        self.formname_loc=(By.XPATH,self.formname_path %index)
        self.find_element(*self.formname_loc).click()
        
    def click_addorcancle(self,index):
        self.addorcancle_loc=(By.XPATH,self.addorcancle_path %index)
        self.find_element(*self.addorcancle_loc).click()
        
    def get_addorcancle(self,index):
        self.addorcancle_loc=(By.XPATH,self.addorcancle_path %index)
        if self.Element_displayed(*self.addorcancle_loc)==False:
            x="window is closed"
            return x
        else:
            return self.find_element(*self.addorcancle_loc).text
        
    def get_warnmessage(self):
        if self.Element_displayed(*self.warnmessage_loc)==False:
            x="form is canceled"
            return x
        else:
            return self.find_element(*self.warnmessage_loc).text
    
    def get_addmessage(self):
        return self.find_element(*self.warnmessage_loc).text
        
        
        
        