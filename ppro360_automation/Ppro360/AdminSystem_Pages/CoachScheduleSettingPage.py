'''
Created on 2018-9-21

@author: Test.liu
'''
import time
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal

class CoachScheduleSettingPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CoachSchedule_loc = (By.LINK_TEXT,'Coach Schedule')
        self.CoachScheduleSetting_loc = (By.LINK_TEXT,"Setting")
        self.CoachSchedulePageTitle_loc = (By.CSS_SELECTOR,"body div.zone.ng-scope div div.page-title div h2")
        self.ClickCoachNameDropDown_loc = (By.CSS_SELECTOR,'#single-button')
        self.CoachName_DropDown_path = '/html/body/div[2]/div/div[2]/div[1]/div/div[1]/div/ul/li[%d]/a'
        self.StatusOption_loc = (By.CSS_SELECTOR,'body div.zone.ng-scope div div.page-content div:nth-child(1) div div:nth-child(2) div')
        self.StatusName_DropDown_path = '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/ul/li[%d]/a'
        self.StatusName_path = '//*[@data-name="%s"]'
        self.InputText_loc = (By.CSS_SELECTOR,'body div.zone.ng-scope div div.page-content div:nth-child(1) div div:nth-child(3) div div input')
        self.AddCoachSchedule_loc = (By.LINK_TEXT,'Add')
        self.CoachScheduleList_path = "/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[%d]/td[%d]"
        self.get_MessageDisplay_loc = (By.XPATH,"/html/body/div[2]/div/div[5]")
        self.get_MessageError_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/div/div[3]/span')
        self.CoachScheduleCount_path = '/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[%d]/td[1]'
        
        self.SettingDeleteButton_path = 'body div.zone.ng-scope div div.page-content div.table-view.row.table-heightL div table tbody tr:nth-child(%d) td.pointActions a'
        self.PopupWindowTitle_loc = (By.CSS_SELECTOR,'body div.zone.ng-scope div div.dialog.fade.in.delete-confirm div div.modal-header h3')
        self.PopupWindowMessage_loc = (By.CSS_SELECTOR,'body div.zone.ng-scope div div.dialog.fade.in.delete-confirm div div.modal-body div p')
        self.PopupWindowDelete_loc = (By.CSS_SELECTOR,'body div.zone.ng-scope div div.dialog.fade.in.delete-confirm div div.modal-footer a.btn.btn-warning')
        self.PopupWindowCancel_loc = (By.CSS_SELECTOR,'body div.zone.ng-scope div div.dialog.fade.in.delete-confirm div div.modal-footer a.btn.btn-cancel')
        
        self.SettingListDelete_loc = (By.XPATH,'/html/body/div[2]/div/div[5]/div/span')
        
    def click_CoachScheduleSetting(self):
        self.find_element(*self.CoachSchedule_loc).click()
        self.find_element(*self.CoachScheduleSetting_loc).click()
        
    def get_CoachSchedulePageTitle(self):
        pagetitle = self.find_element(*self.CoachSchedulePageTitle_loc).text
        return pagetitle
    
    def click_CoachNameDropDown(self):
        self.find_element(*self.ClickCoachNameDropDown_loc).click()
        
    def click_StatusOption(self):
        self.find_element(*self.StatusOption_loc).click()
    
    def select_CoachName(self,coachnameindex):
        self.click_CoachNameDropDown()
        CoachName_DropDown_loc = (By.XPATH, self.CoachName_DropDown_path % coachnameindex)
        coachname = self.find_element(*CoachName_DropDown_loc).text
        self.find_element(*CoachName_DropDown_loc).click()
        return coachname
        
    def select_status(self,status):
        self.click_StatusOption()
        StatusName_loc = (By.XPATH, self.StatusName_path % status)
        self.find_element(*StatusName_loc).click()
    
    def input_ScheduleTime(self,scheduletime):
        self.Input_text(str(scheduletime),*self.InputText_loc)
    
    def click_AddCoachSchedule(self):
        self.find_element(*self.AddCoachSchedule_loc).click()
    
    def get_MessageDisplay(self):
        return self.find_element(*self.get_MessageDisplay_loc).text
    
    def get_MessageError(self):
        return self.find_element(*self.get_MessageError_loc).text
        
    def get_SettingValue(self):
        rowindex = 1
        coluindex = 1
        contentlist = []
        CoachScheduleList_path = self.CoachScheduleList_path % (rowindex, coluindex)
        self.refresh_window()
        time.sleep(1)
        while self.isElementExist(CoachScheduleList_path):
            rowindex = rowindex + 1
            CoachScheduleList_path = self.CoachScheduleList_path % (rowindex, coluindex)
        rowindex = rowindex - 1
        while self.isElementExist(self.CoachScheduleList_path % (rowindex,coluindex)):
            CoachScheduleList_loc = (By.XPATH, self.CoachScheduleList_path % (rowindex,coluindex))
            contentlist.append(self.find_element(*CoachScheduleList_loc).text)
            CoachScheduleList_loc = (By.XPATH, self.CoachScheduleList_path % (rowindex,coluindex))
            coluindex = coluindex + 1
        return contentlist
    
    def get_CoachNameDropDown(self):
        index = 2#index 1 is the default
        coachnamelist = []
        CoachNameDropDown_path = self.CoachName_DropDown_path % index
        while self.isElementExist(CoachNameDropDown_path):
            CoachName_DropDown_loc = (By.XPATH,CoachNameDropDown_path)
            coachnamelist.append(self.find_element(*CoachName_DropDown_loc).text)
            index = index + 1
            CoachNameDropDown_path = self.CoachName_DropDown_path % index
        return coachnamelist
    
    def click_SettingDeleteButton(self,index):
        SettingDeleteButton_loc = (By.CSS_SELECTOR,self.SettingDeleteButton_path % index)
        self.find_element(*SettingDeleteButton_loc).click()
    
    def get_StatusOption(self):
        index = 2#index 1 is the default
        statusnamelist = []
        StatusNameDropDown_path = self.StatusName_DropDown_path % index
        while self.isElementExist(StatusNameDropDown_path):
            StatusName_DropDown_loc = (By.XPATH,StatusNameDropDown_path)
            statusnamelist.append(self.find_element(*StatusName_DropDown_loc).text)
            index = index + 1
            StatusNameDropDown_path = self.StatusName_DropDown_path % index
        return statusnamelist

    def get_PupupWindowInfo(self):
        popupwindowinfo = []
        popupwindowinfo.append(self.find_element(*self.PopupWindowTitle_loc).text)
        popupwindowinfo.append(self.find_element(*self.PopupWindowMessage_loc).text)
        popupwindowinfo.append(self.find_element(*self.PopupWindowDelete_loc).text)
        popupwindowinfo.append(self.find_element(*self.PopupWindowCancel_loc).text)
        return popupwindowinfo
    
    def click_PopupWindowCancel(self):
        self.find_element(*self.PopupWindowCancel_loc).click()
    
    def click_PopupWindowDelect(self):
        self.find_element(*self.PopupWindowDelete_loc).click()

    def get_SettingListCount(self):
        index = 1
        self.refresh_window()
        Get_AnyText = Get_AnyText_ForNormal()
        settinglist = Get_AnyText.Get_Text_ForLoop(index,self.CoachScheduleCount_path)
        return len(settinglist)
    
    def get_SettingListDeleteSuccess(self):
        return self.find_element(*self.SettingListDelete_loc).text

            