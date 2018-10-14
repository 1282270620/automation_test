'''
Created on 2017.7.5

@author: yalan.yin
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage



class CustomerBeforeCompanyPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CallRecordingNumber_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        self.AuditPurposeDropdownDefault_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[2]/div/span')
        self.DetractorRCADropdownDefault_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[2]/div/span')
        self.CallDispositionDropdownDefault_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div[2]/div/span')
        self.ReasonForCallingDropdownDefault_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[2]/div/span')
        self.Dropdown1Default_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[13]/td/label/div/div/span')
        self.Dropdown2Default_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[15]/td/label/div/div/span')
        self.Dropdown3Default_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[17]/td/label/div/div/span')
        self.Dropdown4Default_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[18]/td/label/div/div/span')
        self.Dropdown5Default_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[22]/td/label/div/div/span')
        self.Dropdown6Default_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[23]/td/label/div/div/span')
        
        
    def click_KPIcheckbox (self, checkboxorder):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorder)
        self.find_element (*self.KPIcheckbox_loc).click()  
    
    def input_CallRecordingNumber (self, CallRecordingNumber):
        self.find_element(*self.CallRecordingNumber_loc).clear()
        self.find_element(*self.CallRecordingNumber_loc).send_keys(CallRecordingNumber)
        
    def click_AuditPurposeDropdownDefault (self):
        self.find_element(*self.AuditPurposeDropdownDefault_loc).click()
    
    def get_AuditPurposeDropdownDefault (self):
        return self.find_element(*self.AuditPurposeDropdownDefault_loc).text
    
    def click_DetractorRCADropdownDefault (self):
        self.find_element(*self.DetractorRCADropdownDefault_loc).click()
    def get_DetractorRCADropdownDefault (self):
        return self.find_element(*self.DetractorRCADropdownDefault_loc).text
    
    def click_CallDispositionDropdownDefault (self):
        self.find_element(*self.CallDispositionDropdownDefault_loc).click()
    def get_CallDispositionDropdownDefault (self):
        return self.find_element(*self.CallDispositionDropdownDefault_loc).text
    
    def click_ReasonForCallingDropdownDefault (self):
        self.find_element(*self.ReasonForCallingDropdownDefault_loc).click()
    def get_ReasonForCallingDropdownDefault (self):
        return self.find_element(*self.ReasonForCallingDropdownDefault_loc).text
        #APIndex (1, 4)
    def click_AuditPurposeDropdownList (self, APIndex):
        self.AuditPurposeDropdownList_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[2]/div/ul/li[%d]/a' %APIndex)
        self.find_element(*self.AuditPurposeDropdownList_loc).click()
    def get_AuditPurposeDropdownList (self):
        return self.find_element(*self.AuditPurposeDropdownList_loc).text
        #DRIndex(1, 27)
    def click_DetractorRCADropdownList (self, DRIndex):
        self.DetractorRCADropdownList_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[2]/div/ul/li[%d]/a' %DRIndex)
        self.find_element(*self.DetractorRCADropdownList_loc).click()
    def get_DetractorRCADropdownList (self):
        return self.find_element(*self.DetractorRCADropdownList_loc).text
        #CDIndex(1, 7)
    def click_CallDispositionDropdownList (self, CDIndex):
        self.CallDispositionDropdownList_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div[2]/div/ul/li[%d]/a' %CDIndex)
        self.find_element(*self.CallDispositionDropdownList_loc).click()
    def get_CallDispositionDropdownList (self):
        return self.find_element(*self.CallDispositionDropdownList_loc).text
        #RCIndex(1, 29)
    def click_ReasonForCallingDropdownList (self, RCIndex):
        self.ReasonForCallingDropdownList_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[2]/div/ul/li[%d]/a' %RCIndex)
        self.find_element(*self.ReasonForCallingDropdownList_loc).click()
    def get_ReasonForCallingDropdownList (self):
        return self.find_element(*self.ReasonForCallingDropdownList_loc).text
    
    def click_Dropdown1Default (self):
        self.find_element(*self.Dropdown1Default_loc).click() 
    def get_Dropdown1Default (self):
        return self.find_element(*self.Dropdown1Default_loc).text
    
    def click_Dropdown2Default (self):
        self.find_element(*self.Dropdown2Default_loc).click()
    def get_Dropdown2Default (self):
        return self.find_element(*self.Dropdown2Default_loc).text
    
    def click_Dropdown3Default (self):
        self.find_element(*self.Dropdown3Default_loc).click()
    def get_Dropdown3Default (self):
        return self.find_element(*self.Dropdown3Default_loc).text
    
    def click_Dropdown4Default (self):
        self.find_element(*self.Dropdown4Default_loc).click()
    def get_Dropdown4Default (self):
        return self.find_element(*self.Dropdown4Default_loc).text
    
    def click_Dropdown5Default (self):
        self.find_element(*self.Dropdown5Default_loc).click()
    def get_Dropdown5Default (self):
        return self.find_element(*self.Dropdown5Default_loc).text
    
    def click_Dropdown6Default (self):
        self.find_element(*self.Dropdown6Default_loc).click()
    def get_Dropdown6Default (self):
        return self.find_element(*self.Dropdown6Default_loc).text
        #D1Index(1, 11)
    def click_Dropdown1List (self, D1index): 
        self.Dropdown1List_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[13]/td/label/div/div/ul/li[%d]/a' %D1index) 
        self.find_element(*self.Dropdown1List_loc).click()
    def get_Dropdown1List (self):
        return self.find_element(*self.Dropdown1List_loc).text
        #D2Index(1, 11)
    def click_Dropdown2List (self, D2index): 
        self.Dropdown2List_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[15]/td/label/div/div/ul/li[%d]/a' %D2index)
        self.find_element(*self.Dropdown2List_loc).click()
    def get_Dropdown2List (self):
        return self.find_element(*self.Dropdown2List_loc).text
    
        #D3Index(1, 4)
    def click_Dropdown3List (self, D3index): 
        self.Dropdown3List_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[17]/td/label/div/div/ul/li[%d]/a' %D3index)
        self.find_element(*self.Dropdown3List_loc).click()
    def get_Dropdown3List (self):
        return self.find_element(*self.Dropdown3List_loc).text
    
        #D4Index(1, 3)
    def click_Dropdown4List (self, D4index): 
        self.Dropdown4List_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[18]/td/label/div/div/ul/li[%d]/a' %D4index)
        self.find_element(*self.Dropdown4List_loc).click()
    def get_Dropdown4List (self):
        return self.find_element(*self.Dropdown4List_loc).text
    
        #D5Index(1, 3)
    def click_Dropdown5List (self, D5index): 
        self.Dropdown5List_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[22]/td/label/div/div/ul/li[%d]/a' %D5index)
        self.find_element(*self.Dropdown5List_loc).click()
    def get_Dropdown5List (self):
        return self.find_element(*self.Dropdown5List_loc).text
    
        #D6Index(1, 5)
    def click_Dropdown6List (self, D6index): 
        self.Dropdown6List_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[23]/td/label/div/div/ul/li[%d]/a' %D6index)
        self.find_element(*self.Dropdown6List_loc).click()
    def get_Dropdown6List (self):
        return self.find_element(*self.Dropdown6List_loc).text
    
        
        #TextboxIndex(2, 4)
    def input_TextBoxesUnderCoachingKPIs (self, TextboxIndex, inputtext):
        self.TextBoxesUnderCoachingKPIs_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[1]/div/input' %TextboxIndex)
        self.find_element(*self.TextBoxesUnderCoachingKPIs_loc).clear()
        self.find_element(*self.TextBoxesUnderCoachingKPIs_loc).send_keys(inputtext)
    def get_TextBoxesUnderCoachingKPIs(self,TextboxIndex):
        self.TextBoxesUnderCoachingKPIs_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[1]/div/input' %TextboxIndex)
        return self.find_element(*self.TextBoxesUnderCoachingKPIs_loc).get_attribute("value")
    def TextBoxesUnderCoachingKPIs_disabled(self,TextboxIndex):
        self.TextBoxesUnderCoachingKPIs_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[1]/div/input' %TextboxIndex)
        self.find_element(*self.TextBoxesUnderCoachingKPIs_loc).get_attribute("disabled")
        
    def click_DateTimePicker (self):
        self.DateTimePicker_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[1]/div/div/div[2]/span')
        self.find_element(*self.DateTimePicker_loc).click()
    def click_Date(self):
        self.Date_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[1]/div/div/div[2]/ul/li/div/div/table/tbody/tr[1]/td[1]')
        self.find_element(*self.Date_loc).click()
    def get_DateComments(self):
        self.DateComments_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[1]/div/div/div[2]/input')
        return self.find_element(*self.DateComments_loc).get_attribute("value")
    
        #BoxesIndex(1, 25)
    def input_TextBoxesUnderCustomerBeforeCompany (self, BoxesIndex, inputtext):
        self.TextBoxesUnderCustomerBeforeCompany_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/div/textarea' %BoxesIndex)
        self.find_element(*self.TextBoxesUnderCustomerBeforeCompany_loc).clear()
        self.find_element(*self.TextBoxesUnderCustomerBeforeCompany_loc).send_keys(inputtext)
    def get_TextBoxesUnderCustomerBeforeCompany(self,BoxesIndex):
        self.TextBoxesUnderCustomerBeforeCompany_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/div/textarea' %BoxesIndex)
        return self.find_element(*self.TextBoxesUnderCustomerBeforeCompany_loc).text
    def TextBoxesUnderCustomerBeforeCompany_disabled(self,BoxesIndex):
        self.TextBoxesUnderCustomerBeforeCompany_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/div/textarea' %BoxesIndex)
        flag=self.find_element(*self.TextBoxesUnderCustomerBeforeCompany_loc).get_attribute("disabled")
        return flag
        
        #YesButtonIndex(1, 12) (14, 16, 19, 20, 21, 24, 25)
    def click_YesButton (self, YesButtonIndex):
        self.YesButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/label/div/div[1]/i' %YesButtonIndex)
        self.find_element(*self.YesButton_loc).click()
    def get_YesButtonStatus(self,YesButtonIndex):
        self.YesButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/label/div/div[1]/i' %YesButtonIndex)
        return self.find_element(*self.YesButton_loc).get_attribute("class")
        
        #NoButtonIndex(1, 12) (14, 16, 19, 20, 21, 24, 25)
    def click_NoButton (self, NoButtonIndex):
        self.NoButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/label/div/div[2]/i' %NoButtonIndex)
        self.find_element(*self.NoButton_loc).click()
    def get_NoButtonStatus(self,NoButtonIndex):
        self.NoButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/label/div/div[2]/i' %NoButtonIndex)
        return self.find_element(*self.NoButton_loc).get_attribute("class")
    
        #NAButtonIndex(1, 12) (14, 16, 19, 20, 21, 24, 25)
    def click_NAButton (self, NAButtonIndex):
        self.NAButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/label/div/div[3]/i' %NAButtonIndex)
        self.find_element(*self.NAButton_loc).click()
    def get_NAButtonStatus(self,NAButtonIndex):
        self.NAButton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td/label/div/div[3]/i' %NAButtonIndex)
        return self.find_element(*self.NAButton_loc).get_attribute("class")
        
    def get_Title(self,index):
        self.Title_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[1]/td/label/p' %index)
        return self.find_element(*self.Title_loc).text 
        
        
        