'''
Created on 2018.2.6

@author: haodong.liu
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class TriLevelFormPage(BasePage.Action):
    

    def __init__(self):
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i'
        self.ShortComments_path='//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[1]/td/div/div[%d]/input'
        self.GoalsImprovementCommitmentComments_path='//*[@id="container"]/div/section/div/form/div[2]/table[%d]/tbody/tr[%d]/td[2]/div/textarea'
        self.KeyElementComments_path='//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[%d]/td/div/textarea'
        self.RadioButton_path='//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[%d]/td/label/div/div[%d]/i'
        self.LastComments_path=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/textarea')
        self.KeyTitle_path='//*[@id="container"]/div/section/div/form/div[2]/table[1]/tbody/tr[%d]/td/label/p'
        self.LastTitle_path=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[4]/label')
        self.GoalsImprovementCommitmentTile_path='//*[@id="container"]/div/section/div/form/div[2]/table[%d]/tbody/tr[%d]/th/label'
        self.acknowledgedDate_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div')
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def get_acknowledgedDate(self):
        acknowledagedDate=self.find_element(*self.acknowledgedDate_loc).text
        return acknowledagedDate
    
    def ClickKpiBox(self,index):
        self.ClickKpiBox_loc=(By.XPATH,self.KPIcheckbox_path %index)
        self.find_element(*self.ClickKpiBox_loc).click()
    
    def getKeyTitle(self,index):
        self.KeyTitle_loc=(By.XPATH,self.KeyTitle_path %index)
        return self.find_element(*self.KeyTitle_loc).text
    def getLastTitle(self):
        return self.find_element(*self.LastTitle_path).text
    def getGoalsImprovementCommitmentTitle(self,index1,index2):
        self.GoalsImprovementCommitment_loc=(By.XPATH,self.GoalsImprovementCommitmentTile_path %(index1,index2))
        return self.find_element(*self.GoalsImprovementCommitment_loc).text
    
    def click_RadioButton(self,index1,index2):
        self.RadioButton_loc=(By.XPATH,self.RadioButton_path %(index1,index2))
        self.find_element(*self.RadioButton_loc).click()
    def get_RadioButtonStatus(self,index1,index2):
        self.RadioButton_loc=(By.XPATH,self.RadioButton_path %(index1,index2))
        return self.find_element(*self.RadioButton_loc).get_attribute('class')
    
    def InputShortComments(self,index,text):
        self.InputShortComments_loc=(By.XPATH,self.ShortComments_path %index)
        self.find_element(*self.InputShortComments_loc).clear()
        self.find_element(*self.InputShortComments_loc).send_keys(text)
    def get_ShortComments(self,index):
        self.ShortComments_loc=(By.XPATH,self.ShortComments_path %index)
        return self.find_element(*self.ShortComments_loc).get_attribute('value')
    def ShortComments_disabled(self,index):
        self.ShortComments_loc=(By.XPATH,self.ShortComments_path %index)
        flag=self.find_element(*self.ShortComments_loc).get_attribute('disabled')
        return flag
    
    def InputKeyElementComments(self,index,text):
        self.InputKeyElementComments_loc=(By.XPATH,self.KeyElementComments_path %index)
        self.find_element(*self.InputKeyElementComments_loc).clear()
        self.find_element(*self.InputKeyElementComments_loc).send_keys(text)
    def get_KeyElementComments(self,index):
        self.KeyElementComments_loc=(By.XPATH,self.KeyElementComments_path %index)
        return self.find_element(*self.KeyElementComments_loc).text
    def KeyElementComments_disabled(self,index):
        self.KeyElementComments_loc=(By.XPATH,self.KeyElementComments_path %index)
        flag=self.find_element(*self.KeyElementComments_loc).get_attribute('disabled')
        return flag
    
    def InputGoalsImprovementCommitmentComments(self,index1,index2,text):
        self.InputGoalsImprovementCommitmentComments_loc=(By.XPATH,self.GoalsImprovementCommitmentComments_path %(index1,index2))
        self.find_element(*self.InputGoalsImprovementCommitmentComments_loc).clear()
        self.find_element(*self.InputGoalsImprovementCommitmentComments_loc).send_keys(text)
    def get_GoalsImprovementCommitmentComments(self,index1,index2):
        self.GoalsImprovementCommitmentComments_loc=(By.XPATH,self.GoalsImprovementCommitmentComments_path %(index1,index2))
        return self.find_element(*self.GoalsImprovementCommitmentComments_loc).text
    def GoalsImprovementCommitmentComments_disabled(self,index1,index2):
        self.GoalsImprovementCommitmentComments_loc=(By.XPATH,self.GoalsImprovementCommitmentComments_path %(index1,index2))
        flag=self.find_element(*self.GoalsImprovementCommitmentComments_loc).get_attribute('disabled')
        return flag
    
    def InputLastComments(self,text):
        self.find_element(*self.LastComments_path).clear()
        self.find_element(*self.LastComments_path).send_keys(text)
    def get_LastComments(self):
        return self.find_element(*self.LastComments_path).text
    def LastComments_disabled(self):
        flag=self.find_element(*self.LastComments_path).get_attribute('disabled')
        return flag
    
    
    