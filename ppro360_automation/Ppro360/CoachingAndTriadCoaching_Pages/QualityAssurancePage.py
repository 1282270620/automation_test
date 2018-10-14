'''
Created on 20170710

@author: luming.zhao
'''



from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class QualityAssurancePage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.sn_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/div/div/div/div/input")
        self.callrecordingnumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/div[2]/div[2]/div/div/input")
        self.Button_path='//*[@id="container"]/div/section/div/div[2]/a[%d]'
        self.Button_path2='//*[@id="container"]/div/section/div/div[2]/a[%d]'
        self.Error_path='//*[@id="container"]/div/div[2]/div/p[%d]'
        self.Info_path='//*[@id="add-qa-coaching-modal"]/section/p[2]/text()[%d]'
        self.CoachingPageInfo_path='//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[1]/td[%d]'
        #self.TLInfo_path='//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[%d]'
        
    def click_CompletedSection(self):
        self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div[1]/div/div[2]/div[3]/div/ul/li[5]/a').click()
    
    def get_firstTLHRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    def get_firstAgentID(self):
        return self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/div/table[1]/tbody/tr[1]').get_attribute("data-id")
        
    def input_sn(self,text):
        self.find_element(*self.sn_loc).send_keys(text)
        
    def input_callrecordingnumber(self,text):
        self.find_element(*self.callrecordingnumber_loc).send_keys(text)
        
    def click_AddCoaching(self):
        self.AddCoaching_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[2]/a[2]")
        self.find_element(*self.AddCoaching_loc).click() 
    
    def click_yes(self):
        self.yes_loc=(By.XPATH,"//*[@id='add-qa-coaching-modal']/footer/ul/li/a")
        self.find_element(*self.yes_loc).click()
    
    def get_sn(self):
        SN_loc=(By.XPATH,'//*[@id="sn"]')
        return self.find_element(*SN_loc).get_attribute("value")
    def SN_disabled(self):
        SN_loc=(By.XPATH,'//*[@id="sn"]')
        flag=self.find_element(*SN_loc).get_attribute("disabled")
        return flag
    def get_EmployeeName(self):
        EmployeeName_loc=(By.XPATH,'//*[@id="employee_Name"]')
        return self.find_element(*EmployeeName_loc).get_attribute("value")
    def EmployeeName_disabled(self):
        EmployeeName_loc=(By.XPATH,'//*[@id="employee_Name"]')
        flag=self.find_element(*EmployeeName_loc).get_attribute("disabled")
        return flag
    def get_CoachName(self):
        CoachName_loc=(By.XPATH,'//*[@id="coach_title"]')
        return self.find_element(*CoachName_loc).get_attribute("value")
    def CoachName_disabled(self):
        CoachName_loc=(By.XPATH,'//*[@id="coach_title"]')
        flag=self.find_element(*CoachName_loc).get_attribute("disabled")
        return flag
    def get_CompletedDate(self):
        CompletedDate_loc=(By.XPATH,'//*[@id="date"]')
        return self.find_element(*CompletedDate_loc).get_attribute("value")
    def CompletedDate_disabled(self):
        CompletedDate_loc=(By.XPATH,'//*[@id="date"]')
        flag=self.find_element(*CompletedDate_loc).get_attribute("disabled")
        return flag
    def get_CallRecordingNumber(self):
        CallRecordingNumber_loc=(By.XPATH,'//*[@id="callRecordingNumber"]')
        return self.find_element(*CallRecordingNumber_loc).get_attribute("value")
    def CallRecordingNumber_disabled(self):
        CallRecordingNumber_loc=(By.XPATH,'//*[@id="callRecordingNumber"]')
        flag=self.find_element(*CallRecordingNumber_loc).get_attribute("disabled")
        return flag
    
    def get_Error1(self):
        Error_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div/p[1]')
        Error=self.find_element(*Error_loc).text
        return Error
    def get_Error2(self):
        Error_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div/p[2]')
        Error=self.find_element(*Error_loc).text
        return Error
    def get_AddSuccessInfo(self):
        SuccessInfo_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div/p[1]')
        return self.find_element(*SuccessInfo_loc).text
    
    def get_ButtonName(self,index):
        ButtonName_loc=(By.XPATH,self.Button_path %index)
        return self.find_element(*ButtonName_loc).text
    def get_ButtonName2(self,index):
        ButtonName_loc=(By.XPATH,self.Button_path2 %index)
        return self.find_element(*ButtonName_loc).text
        
    def Click_Button(self,index):
        Button_loc=(By.XPATH,self.Button_path %index)
        self.find_element(*Button_loc).click()
    def Close_ErrorButton(self):
        ErrorButton_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div/button/span')
        self.find_element(*ErrorButton_loc).click()
        
    
        
    def get_AddQACoachingInfoTitle(self):
        Tile_loc=(By.XPATH,'//*[@id="add-qa-coaching-modal"]/header')
        return self.find_element(*Tile_loc).text
    def get_AddQACoachingPromptInfo(self):
        Prompt_loc=(By.XPATH,'//*[@id="add-qa-coaching-modal"]/section/p[1]')
        return self.find_element(*Prompt_loc).text
    def get_AddQAInfo(self):
        Info_loc=(By.XPATH,'//*[@id="add-qa-coaching-modal"]/section/p[2]')
        return self.find_element(*Info_loc).text
    
    def get_CoachpageInfo(self,index):
        CoachingInfo_loc=(By.XPATH, self.CoachingPageInfo_path %index)
        return self.find_element(*CoachingInfo_loc).text
    
    