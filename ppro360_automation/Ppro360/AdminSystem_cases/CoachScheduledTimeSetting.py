'''
Created on 2018-9-21

@author: Test.liu
'''

import unittest,random
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method.HandleMySQL import HandleMySQL
from AdminSystem_Pages.CoachScheduleSettingPage import CoachScheduleSettingPage
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage

class CoachScheduledTimeSetting(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        GetData=Get_configration_data()
        #Case ID
        self.caseID="CoachScheduledTimeSetting"
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        #The expected value of status options
        self.StatusList = ['ongoing','planned']
        self.PopupWindow = ['Delete Rule','Are you sure to delete?','Delete','Cancel']
        
    def tearDown(self):
        #Gl.driver.quit()
        pass
    def test_CoachScheduledTimeSetting(self):
        GetConfig=Get_configration_data()
        Log = Login()
        CSsetting = CoachScheduleSettingPage()
        TabletPage = TabletHomepage()
        CoachPage = Coachinghomepage()
        HMysql=HandleMySQL()
        
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag = GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                
                ##GET THE CORRECT URL#####
                tableturl=GetConfig.get_Test_Tablet(lobname)
                adminurl=GetConfig.get_Test_AdminUrl(lobname)
                hostindex=GetConfig.get_Test_Hostindex(lobname)
                
                ##Get Notification information
                notificationinfo=GetConfig.get_NotificationInfo(hostindex)
                
                #get each site which in this lob
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename = site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                    #Step 1:check default content.
                    #Login admin system and Click link 'Coach Schedule' -> 'Setting' to enter this module.
                    Log.Login_admin(adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    CSsetting.click_CoachScheduleSetting()
                    #Verify the title of Coach Schedule setting page 
                    assert CSsetting.get_CoachSchedulePageTitle() == 'Coach scheduled Time Setting'
                    
                    #List this site's Coach Schedule Tiem Settting
                    lobname_field,sitename_field = GetConfig.get_LobSitename_field(lobname, sitename)
                    notification_Sql = "select count(cst.id) from coach_scheduled_time cst where lob = '"+lobname_field+"' and site = '"+sitename_field+"' and scheduled_status = 0;"
                    SettingList_CountDB = HMysql.Get_DataFromDB_normal(notificationinfo['stage'], notificationinfo['username'], notificationinfo['password'], "ppro_notification", notification_Sql)
                    SettingList_Count = SettingList_CountDB[1][0][0]
                    ScheduleCount = CSsetting.get_SettingListCount()
                    assert SettingList_Count == ScheduleCount,"Display in coach schedule:%d doesn't equal database:%d"%(ScheduleCount,SettingList_Count)
                    
                    #Get Coach Name list from Coach Schedule
                    CSsetting.click_CoachNameDropDown()
                    CoachNameList_Admin = CSsetting.get_CoachNameDropDown()

                    #Get Status optino from Coach Schedule
                    CSsetting.click_StatusOption()
                    StatusNameList = CSsetting.get_StatusOption()
                    Log.logout_admin()
                    #Lpgin and Get Coach Name list from Coach module
                    Log.Login_tablet(tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    TabletPage.click_coachingcircle()
                    CoachPage.click_type()
                    TypeNameList_Tablet = CoachPage.get_TypeNameList()
                    Log.logout_tablet()
                    
                    #Form options are the same as coaching type drop-down in 'coaching' module
                    assert sorted(CoachNameList_Admin) == sorted(TypeNameList_Tablet),"CoachNameList_Admin:%s doesn't equql TypeNameList_Tablet:%s" %(sorted(CoachNameList_Admin),sorted(TypeNameList_Tablet))
                    
                    #Verify status optioins 
                    assert sorted(StatusNameList) == self.StatusList,"StatusNameList:%s doesn't equal expected:%s"%(sorted(StatusNameList),self.StatusList)
                    
                    #Login admin system and Click link 'Coach Schedule' -> 'Setting' to enter this module again.
                    Log.Login_admin(adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    CSsetting.click_CoachScheduleSetting()
                    
                    #Step 2:setting function              
                    length_CoachNameList = len(CoachNameList_Admin) + 1  #The index 1 is the default
                    coachname_1 = self.setting_CoachSchedule(2, "planned", 1)
                    self.assert_CoachScheduleList(coachname_1, "planned", '1 day')
                    coachname_2 = self.setting_CoachSchedule(2, "ongoing", 2)
                    self.assert_CoachScheduleList(coachname_2, "ongoing", '2 days')
                    coachname_3 = self.setting_CoachSchedule(length_CoachNameList, "planned", 2)
                    self.assert_CoachScheduleList(coachname_3, "planned", '2 days')
                    
                    #Step 3:Setting the same as other schedule
                    self.setting_CoachSchedule(length_CoachNameList, "planned", 3)
                    assert CSsetting.get_MessageDisplay().split("\n")[2] == "Setting already exists"
                    self.setting_CoachSchedule(length_CoachNameList, "planned", 3.5)
                    assert CSsetting.get_MessageError() == "Only allow integer number (1-100)."
                    
                    #Delete function
                    #Select any one list, click [Delete] button in setting table
                    ScheduleListCount = CSsetting.get_SettingListCount()
                    listindex = random.randint(1,ScheduleListCount)
                    CSsetting.click_SettingDeleteButton(listindex)
                    PopupWindowInfo = CSsetting.get_PupupWindowInfo()
                    assert PopupWindowInfo == self.PopupWindow,"The information about popup window:%s display errors.Correct is:%s"%(PopupWindowInfo,self.PopupWindow)
                    
                    #On this pop-up window - Click [Cancel] button
                    CSsetting.click_PopupWindowCancel()
                    assert CSsetting.get_SettingListCount() == ScheduleListCount
                    
                    #On this pop-up window - Click  [Delete] button
                    CSsetting.click_SettingDeleteButton(listindex)
                    CSsetting.click_PopupWindowDelect()
                    assert CSsetting.get_SettingListDeleteSuccess() == "delete successfully."
                    assert CSsetting.get_SettingListCount() == ScheduleListCount - 1
                    
                    Log.logout_admin()
                    GetConfig.print_EndTest_message(lobname, sitename)
                    
    def setting_CoachSchedule(self,CoachingName,Status,ScheduleTime):
        CSsetting = CoachScheduleSettingPage()
        coachname = CSsetting.select_CoachName(CoachingName)
        CSsetting.select_status(Status)
        CSsetting.input_ScheduleTime(ScheduleTime)
        try:
            CSsetting.click_AddCoachSchedule()
        except:
            print("Setting coach schedule error!!!")
        return coachname
    
    def assert_CoachScheduleList(self,CoachingName,Status,ScheduleTime):
        CSsetting = CoachScheduleSettingPage()
        valueofcolumn = CSsetting.get_SettingValue()
        assert [CoachingName,Status,ScheduleTime,'Delete'] == valueofcolumn,"%s doesn't equal valueofcolumn:%s"%([CoachingName,Status,ScheduleTime,'Delete'],valueofcolumn)



        
        