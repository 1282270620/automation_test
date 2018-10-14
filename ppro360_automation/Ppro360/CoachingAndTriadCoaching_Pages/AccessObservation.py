'''
Created on 20170627

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class AccessObservation(BasePage.Action):
    
    
    def __init__(self):
         
        self.callRecordingNumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div/div[3]/div[2]/div/div/input")
        self.associateCommitment_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[3]/div/textarea")
        self.RadioButtonStatus_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[2]/div[%d]/i "
        self.RadioButton_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[2]/div[%d]/label"
        self.KPIcheckbox_Path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.associateCommitmentTitle_path='//*[@id="container"]/div/section/div/form/div[2]/div[3]/label'
    
    def click_RadioButton (self,lineindex,buttontypeindex): #columnindex (1, 14)  buttontypeindex 1=yes   2=no 3=n/a
        RadioButton_loc=(By.XPATH,self.RadioButton_path %(lineindex,buttontypeindex))
        self.find_element(*RadioButton_loc).click()
    def get_RadioButtonStatus(self,lineindex,buttontypeindex): #columnindex (1, 14)  buttontypeindex 1=yes   2=no 3=n/a
        RadioButtonStatus_loc=(By.XPATH, self.RadioButtonStatus_path %(lineindex,buttontypeindex))
        return self.find_element(*RadioButtonStatus_loc).get_attribute('class')
    
    def input_associateCommitment (self,text):
        self.find_element(*self.associateCommitment_loc).clear()
        self.find_element(*self.associateCommitment_loc).send_keys(text); 
    def get_associateCommitment(self):
        return self.find_element(*self.associateCommitment_loc).text
    def associateCommitment_disabled(self):
        flag=self.find_element(*self.associateCommitment_loc).get_attribute('disabled')
        return flag
    def get_associateCommitmentTitle(self):
        associateCommitmentTitle_loc=(By.XPATH, self.associateCommitmentTitle_path)
        return self.find_element(*associateCommitmentTitle_loc).text
    
        