'''
Created on 20170703

@author: haodong.liu
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class GoalSettingPlanandNotesFormPage(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        self.KPIcheckbox_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.ActionOneComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[2]/td/textarea')
        self.ActionTwoComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[4]/td/textarea')
        self.ActionThreeComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[6]/td/textarea')
        self.ActionFourComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[8]/td/textarea')
        self.ActionFiveComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[10]/td/textarea')
        self.ActionSixComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[12]/td/textarea')
        self.ActionSevenComments_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[14]/td/textarea')
        self.TextboxTitle_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[%d]/td/label"
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
        
    def click_KPIcheckbox (self, checkboxorderindex):
        self.KPIcheckbox_loc=(By.XPATH,self.KPIcheckbox_path  %checkboxorderindex) 
        self.find_element(*self.KPIcheckbox_loc).click()
    
    def get_TextboxTitle(self, boxindex):#boxindex(1, 3, 5, 7, 9, 11, 13)
        TextboxTitle_loc=(By.XPATH, self.TextboxTitle_path %boxindex)
        return self.find_element(*TextboxTitle_loc).text
        
    def input_callRecordingNumber (self,text):
        self.find_element(*self.callRecordingNumber_loc).send_keys(text);
    
    def input_ActionOneComments(self,inputtext):
        self.find_element(*self.ActionOneComments_loc).clear()
        self.find_element(*self.ActionOneComments_loc).send_keys(inputtext)
    def get_ActionOneComments(self):
        return self.find_element(*self.ActionOneComments_loc).text
    def ActionOneComments_disabled(self):
        flag=self.find_element(*self.ActionOneComments_loc).get_attribute("disabled")
        return flag
    
    def input_ActionTwoComments(self,inputtext):
        self.find_element(*self.ActionTwoComments_loc).clear()
        self.find_element(*self.ActionTwoComments_loc).send_keys(inputtext)
    def get_ActionTwoComments(self):
        return self.find_element(*self.ActionTwoComments_loc).text
    def ActionTwoComments_disabled(self):
        flag=self.find_element(*self.ActionTwoComments_loc).get_attribute("disabled")
        return flag
    
    def input_ActionThreeComments(self,inputtext):
        self.find_element(*self.ActionThreeComments_loc).clear()
        self.find_element(*self.ActionThreeComments_loc).send_keys(inputtext)
    def get_ActionThreeComments(self):
        return self.find_element(*self.ActionThreeComments_loc).text
    def ActionThreeComments_disabled(self):
        flag=self.find_element(*self.ActionThreeComments_loc).get_attribute("disabled")
        return flag
    
    def input_ActionFourComments(self,inputtext):
        self.find_element(*self.ActionFourComments_loc).clear()
        self.find_element(*self.ActionFourComments_loc).send_keys(inputtext)
    def get_ActionFourComments(self):
        return self.find_element(*self.ActionFourComments_loc).text
    def ActionFourComments_disabled(self):
        flag=self.find_element(*self.ActionFourComments_loc).get_attribute("disabled")
        return flag
    
    def input_ActionFiveComments(self,inputtext):
        self.find_element(*self.ActionFiveComments_loc).clear()
        self.find_element(*self.ActionFiveComments_loc).send_keys(inputtext)
    def get_ActionFiveComments(self):
        return self.find_element(*self.ActionFiveComments_loc).text
    def ActionFiveComments_disabled(self):
        flag=self.find_element(*self.ActionFiveComments_loc).get_attribute("disabled")
        return flag
    
    def input_ActionSixComments(self,inputtext):
        self.find_element(*self.ActionSixComments_loc).clear()
        self.find_element(*self.ActionSixComments_loc).send_keys(inputtext)
    def get_ActionSixComments(self):
        return self.find_element(*self.ActionSixComments_loc).text
    def ActionSixComments_disabled(self):
        flag=self.find_element(*self.ActionSixComments_loc).get_attribute("disabled")
        return flag
    
    def input_ActionSevenComments(self,inputtext):
        self.find_element(*self.ActionSevenComments_loc).clear()
        self.find_element(*self.ActionSevenComments_loc).send_keys(inputtext)
    def get_ActionSevenComments(self):
        return self.find_element(*self.ActionSevenComments_loc).text
    def ActionSevenComments_disabled(self):
        flag=self.find_element(*self.ActionSevenComments_loc).get_attribute("disabled")
        return flag
    
        