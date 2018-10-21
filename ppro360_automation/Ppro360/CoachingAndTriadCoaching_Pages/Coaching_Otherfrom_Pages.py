'''
Created on 2018/8/3

@author: hanyang.dong
'''
import xlrd
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
from public_method.Get_configration_data_OtherAccount import Get_configration_data_OtherAccount
import pyautogui


class Coaching_Otherfrom_Pages(BasePage.Action):
    def __init__(self):
        #//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[1]/td[2]
        self.Performance_loc=(By.XPATH,'//*[@id="container"]/div/section/section/a[1]/p')
        self.TL2Testerlist_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[1]/td[1]')
        self.FirstAgent_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]')
        #
        self.FirstAgent_L1_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[1]')
        self.AgentFirstKPI_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]')
        self.AgentFirstKPI_L1_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[1]/td[2]/span')
        self.AddCoachingForm_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[14]/div/a')
        
        
        #self.Otherform_loc = (By.LINK_TEXT,"Other")
        self.Formlists_path='//*[@id="add-coaching-modal"]/section/ul/li[%d]'
        self.lenKPIlists_path='//*[@id="container"]/div/section/div/form/div[2]/div/div[1]/table/tbody/tr[1]/td[%d]'
        
        self.AddCoachingFormButton_loc=(By.XPATH,'//*[@id="add-coaching-modal"]/footer/ul/li[1]/a')
        self.SuccessfullyAddedMessage_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div/p[1]')
        self.BackButton_loc=(By.XPATH,'//*[@id="container"]/div/nav/a/div/div')
        self.Coaching_loc=(By.LINK_TEXT,"Coaching")
        self.ThisCoaching_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[1]')
        self.title_loc=(By.XPATH,'//*[@id="container"]/div/nav/div/span')
        self.CompleteCoachingButton=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[3]/a[3]')
        
        #
        self.CallRecordingNumber_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        self.CompletedDate_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[1]/div[2]/div[3]/div/div/input')
        self.AcknowledgedDate_loc = (By.XPATH,'//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[3]/div/div/input')
        self.shortinput_path='//*[@id="container"]/div/section/div/form/div[1]/div[%d]/div[%d]/div/div/input'
        #
        #
        
        #self.KPIlists_agent_path='//*[@id="container"]/div/section/div/form/div[2]/div/div[1]/table/tbody/tr[5]/td[%d]/i'
        self.KPIlists_path='//*[@id="container"]/div/section/div/form/div[2]/div/div[1]/table/tbody/tr[%d]/td[%d]/i'
        
        
        
        self.BrowseFile_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div/div[2]/div/div/p/span')
        self.Uploadsuccess_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div/p[1]')
        self.UpdateAttachment_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div/a[2]')
        self.Coachstatus_loc=(By.XPATH,'//*[@id="coach_status"]')
        self.BrowseFile_popup_loc=(By.XPATH,'//*[@id="attachment-modal"]/section/p/span')
        self.Nowfilename_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div/a[1]')
        self.CompleteCoaching_button_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[3]/a[3]')
        self.CompleteCoaching_yse_button_loc=(By.LINK_TEXT,"Yes")
        #
        self.SearchStatus_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div[1]/div/div[2]/div[3]/div/span')
        self.SearchCompleted_loc = (By.LINK_TEXT,"Completed")
        self.Filter_button_loc = (By.XPATH,'//*[@id="container"]/div/section/div/div[1]/div/div[4]/button[1]')
        self.CoachingPlannedSN_loc = (By.XPATH,'//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[1]/td[1]')
        self.CoachingCompletedSN_loc = (By.XPATH,'//*[@id="container"]/div/section/div/div[2]/table/tbody/tr/td[1]')
        self.CoachingCompletedStatus_loc = (By.XPATH,'//*[@id="container"]/div/section/div/div[2]/table/tbody/tr/td[6]')
        self.printbutton_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[3]/a[1]')
        self.backbutton_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[3]/a[2]')
        #
        
    
        self._loc = (By.XPATH,'')
        self._loc = (By.LINK_TEXT,"")
    
        
    def click_(self):
        self.find_element(*self._loc).click()
        time.sleep(Gl.waittime)
        
    def get_(self):
        return self.find_element(*self._loc).text        
        
    
    def click_BrowseFile(self):
        self.find_element(*self.BrowseFile_loc).click()
        time.sleep(Gl.waittime)
    def input_CallRecordingNumber(self,text):
        self.find_element(*self.CallRecordingNumber_loc).send_keys(text);
        time.sleep(2)    
    def get_CallRecordingNumberValue(self):
        return self.find_element(*self.CallRecordingNumber_loc).text 
    def get_CallRecordingNumber(self):
        return self.find_element(*self.CallRecordingNumber_loc).get_attribute("disabled")
    def get_CompletedDate(self):
        return self.find_element(*self.CompletedDate_loc).get_attribute("disabled")
    def get_AcknowledgedDate(self):
        return self.find_element(*self.AcknowledgedDate_loc).get_attribute("disabled")
    def get_AcknowledgedDateValue(self):
        return self.find_element(*self.AcknowledgedDate_loc).text
    

    def click_KPIlists(self,index1,index2):
        self.KPIlists_loc=(By.XPATH,self.KPIlists_path % (index1,index2))
        self.find_element(*self.KPIlists_loc).click()
        time.sleep(Gl.waittime)

    def get_KPIlists(self,lineindex1,lineindex2):
        self.KPIlists_loc=(By.XPATH,self.KPIlists_path %(lineindex1,lineindex2))
        return self.find_element(*self.KPIlists_loc).get_attribute("class")
    #
    def KPIlists_disabled(self,lineindex,mid):
        self.KPIlists_loc=(By.XPATH,self.KPIlists_path %(lineindex,mid))
        flag=self.find_element(*self.KPIlists_loc).get_attribute("disabled")
        return flag
        
        
    def get_allformlist(self):
        Get_Text=Get_AnyText_ForNormal()
        Any_path=self.Formlists_path
        lobs_list=Get_Text.Get_Text_ForLoop(1, Any_path)
        return lobs_list
        time.sleep(Gl.waittime)
    def get_lenKPIlist(self):
        Get_Text=Get_AnyText_ForNormal()
        Any_path=self.lenKPIlists_path
        lobs_list=Get_Text.Get_Text_ForLoop(1, Any_path)
        return lobs_list
        time.sleep(Gl.waittime)
        
    def click_needclicktheform(self,index):
        needclicktheform_loc=(By.XPATH,self.Formlists_path % index)
        self.find_element(*needclicktheform_loc).click()
        time.sleep(Gl.waittime)
        
        
        
    def click_Performance(self):
        self.smart_click(*self.Performance_loc)
#         self.find_element(*self.Performance_loc).click()
#         time.sleep(Gl.waittime)
    def click_TL2Testerlist(self):
        self.find_element(*self.TL2Testerlist_loc).click()
        time.sleep(Gl.waittime)
    def get_FirstAgentuserid(self):
        return self.find_element(*self.FirstAgent_loc).get_attribute("data-id")
    #
    def get_FirstAgentuserid_L1(self):
        return self.find_element(*self.FirstAgent_L1_loc).get_attribute("data-id")
    def click_AgentFirstKPI(self):
        self.find_element(*self.AgentFirstKPI_loc).click()
        time.sleep(Gl.waittime)
    def click_AgentFirstKPI_L1(self):
        self.find_element(*self.AgentFirstKPI_L1_loc).click()
        time.sleep(Gl.waittime)    
        
    def click_AddCoachingForm(self):
        self.find_element(*self.AddCoachingForm_loc).click()
        time.sleep(Gl.waittime)
    #def click_Otherform(self):
        #self.find_element(*self.Otherform_loc).click()
        time.sleep(Gl.waittime)
    def click_AddButton(self):
        self.find_element(*self.AddCoachingFormButton_loc).click()
        #time.sleep(Gl.waittime*3)
    def get_SuccessfullyAddedMessage(self):
        return self.find_element(*self.SuccessfullyAddedMessage_loc).text
        #Coaching Added
    def click_BackButton(self):
        self.find_element(*self.BackButton_loc).click()
        time.sleep(Gl.waittime)
    def click_Coaching(self):
        self.smart_click(*self.Coaching_loc)
        time.sleep(Gl.waittime)
#         self.find_element(*self.Coaching_loc).click()
         
    def click_ThisCoaching(self):
        self.find_element(*self.ThisCoaching_loc).click()
        time.sleep(Gl.waittime)
    def get_title(self):
        return self.find_element(*self.title_loc).text
        #Coaching - Other
    def get_CompleteCoachingButton(self):
        return self.find_element(*self.CompleteCoachingButton).get_attribute("disabled")
        
    def click_Setbutton(self):
        self.find_element(*self.Setbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def get_list(self,role):
        Get_Text=Get_AnyText_ForNormal()
        if role=="VP" or role=="SVP":
            Any_path=self.Switchlists_svpAndvpRole_path
        else:
            Any_path=self.Switchlists_otherrole_path
        lobs_list=Get_Text.Get_Text_ForLoop(1, Any_path)
        return lobs_list   
    
    def uploadfile_loc_1(self):
        GetDataOA=Get_configration_data_OtherAccount()
        upload_file_name_1=GetDataOA.get_upload_file_name_1()
        upload_file_path=GetDataOA.get_upload_file_path()
        pyautogui.typewrite(upload_file_path+upload_file_name_1)
        pyautogui.press('enter')
        
        
        #
    def uploadfile_loc_2(self):
        GetDataOA=Get_configration_data_OtherAccount()
        upload_file_name_2=GetDataOA.get_upload_file_name_2()
        upload_file_path=GetDataOA.get_upload_file_path()
        pyautogui.typewrite(upload_file_path+upload_file_name_2)
        pyautogui.press('enter')
        
    def get_Uploadsuccess(self):
        return self.find_element(*self.Uploadsuccess_loc).text
    
    def get_UpdateAttachment(self):
        return self.find_element(*self.UpdateAttachment_loc).text
    def click_UpdateAttachment(self):
        self.find_element(*self.UpdateAttachment_loc).click()
        time.sleep(Gl.waittime)
    def get_Coachstatus(self):
        return self.find_element(*self.Coachstatus_loc).get_attribute("value")
    
    def click_BrowseFile_popup(self):
        self.find_element(*self.BrowseFile_popup_loc).click()
    def click_CompleteCoaching_button(self):
        self.find_element(*self.CompleteCoaching_button_loc).click()
    #
    def get_Nowfilename(self):
        return self.find_element(*self.Nowfilename_loc).text
    def click_downloadfile(self):
        self.find_element(*self.Nowfilename_loc).click()
        #pyautogui.press('enter')
        time.sleep(Gl.waittime)
        
    def click_CompleteCoaching_yse_button_loc(self):
        self.find_element(*self.CompleteCoaching_yse_button_loc).click()
        time.sleep(Gl.waittime*3)  
    def click_SearchStatus(self):
        self.find_element(*self.SearchStatus_loc).click()
    def click_SearchCompleted(self):
        self.find_element(*self.SearchCompleted_loc).click()
    def click_Filter_button(self):
        self.find_element(*self.Filter_button_loc).click()
    def get_CoachingPlannedSN(self):
        return self.find_element(*self.CoachingPlannedSN_loc).text 
    def get_CoachingCompletedSN(self):
        return self.find_element(*self.CoachingCompletedSN_loc).text
    def get_CoachingCompletedStatus(self):
        return self.find_element(*self.CoachingCompletedStatus_loc).text 
    def get_printbutton(self):
        return self.find_element(*self.printbutton_loc).text
    def get_backbutton(self):
        return self.find_element(*self.backbutton_loc).text
    
    def input_shortinput (self,lineindex,mid,text):
        self.shortinput_loc=(By.XPATH,self.shortinput_path %(lineindex,mid))
        self.Input_text(text,*self.shortinput_loc)
        
    def get_shortinput(self,lineindex,mid):
        self.shortinput_loc=(By.XPATH,self.shortinput_path %(lineindex,mid))
        return self.find_element(*self.shortinput_loc).get_attribute("value")
    
    def shortinput_disabled(self,lineindex,mid):
        self.shortinput_loc=(By.XPATH,self.shortinput_path %(lineindex,mid))
        flag=self.find_element(*self.shortinput_loc).get_attribute("disabled")
        return flag
    
    def get_shortinput_text(self,lineindex,mid):
        self.shortinput_loc=(By.XPATH,self.shortinput_path %(lineindex,mid))
        return self.find_element(*self.shortinput_loc).text
    
    
    #
        
        
