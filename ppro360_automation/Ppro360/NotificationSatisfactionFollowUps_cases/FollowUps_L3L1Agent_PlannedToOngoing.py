'''
Created on 2018-9-26

@author: Test.liu
'''
import unittest,time
from public_method import Gl
from public_method.Login import Login
from public_method.HandleMySQL import HandleMySQL
from public_method.Get_configration_data import Get_configration_data
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
from Tablet_pages.Popupaddcoachpage import Popupaddcoachpage
from Tablet_pages.Coachinghomepage import Coachinghomepage

class FollowUps_L3L1Agent_PlannedToOngoing(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        #caseID
        self.caseID = "FollowUps_L3L1Agent_PlannedToOngoing"
        GetConfData = Get_configration_data()
        
        #Get all lobs from CSV
        self.testLOBSITE_list = GetConfData.get_LOBSITEtoTest(self.caseID)
        
        #Get OM account
        OMaccount = GetConfData.get_OMaccount()
        self.OMuserid = OMaccount["OMuserid"]
        self.OMpwd = OMaccount["OMpassword"]
        self.L3userid='66776677'
        self.role='L1'
        
        #Database info
        #self.host=GetConfData.get_StageDatabaseHost()
        self.dbuser=GetConfData.get_StageDatabaseUser()
        self.dbpassword=GetConfData.get_StageDatabasePassword()
        
        #input content
        self.Add_FollowUpsInfoL3 = "Using automation script to L3 add follow up info"
        self.Edit_NewContentL3 = "Using automation script to L3 add follow up info, edit info"
        self.Add_FollowUpsInfoTL = "Using automation script to L1 add follow up info"
        self.Edit_NewContentTL = 'Using automation script to L1 add follow up info, edit info'
        self.Add_FollowUpsInfoAgent = 'Using automation script to Agent  add follow up info'
        self.Edit_NewContentAgent = 'Using automation script to Agent add follow up info, edit info'
        
    def tearDown(self):
        #Gl.driver.quit()
        pass
    
    def test_FollowUps_L3L1Agent_PlannedToOngoing(self):
        GetConfig=Get_configration_data()
        Log = Login()
        HMysql=HandleMySQL()
        THPage = TabletHomepage()
        PPage = PerformancePage()
        PACPage = Popupaddcoachpage()
        CHPage = Coachinghomepage()
        Get_Roleinfo = Get_AllRoleAccountForTest()
           
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
                
                #get each site which in this lob
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename = site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                    #step1:L3 add/edit follow-ups_ planned
                    #get L3 info and login tablet
                    L3info = Get_Roleinfo.get_LCInfo(adminurl, lobname, sitename, self.OMuserid, self.OMpwd, self.L3userid)
                    Log.Login_tablet(tableturl, lobname, sitename, L3info['Hrid'], L3info["Password"])
                    
                    #Add a coaching form. 
                    THPage.click_performancecircle()
                    
                    TLname,Agentname=PPage.select_AgentkpiNew()
                    print(TLname,Agentname)
                    PPage.click_addcoachbutton()
                    PACPage.select_coach(1)
                    PACPage.add_coach()
                    
                    #Enter this form detail page. 
                    PPage.click_backbutton()
                    THPage.click_coachingcircle()
                    CHPage.click_eachcoach(1)
                    
                    #Click link 'Follow-Ups' from bottom page.
                    CHPage.click_FollowUps()
                    time.sleep(1)
                    
                    defaulttitle,defaultstatus = CHPage.default_FollowUps()
                    assert defaulttitle == "No follow ups."
                    assert defaultstatus == 'true'
                    
                    
                    #Input content in ths newly added text box. e.g 'Using automation script to L3 add follow up info' and Click add button.
                    CHPage.Add_FollowUps(self.Add_FollowUpsInfoL3)
                    time.sleep(1)
                    AddedInfoList = CHPage.get_AddedFollowUpsInfo()
                    
                    #Get added Follow_Ups Information from database 
                    FollowUpsInfo_Sql = "select concat(cfu.avatar_name,' added on ',cfu.create_time,' -0400'),ta.Agentname,ta.firstname,ta.hr_id,ta.tl_id,co.sn from coaching_follow_ups cfu \
                    left join coach co on cfu.coach_id=co.id left join (select ro.hr_id,concat(ro.firstname,' ',ro.lastname) Agentname,rs.firstname,rs.hr_id tl_id from roster ro left join roster_teamleaders rt on rt.team_id=ro.team_id \
                    join roster rs on rt.hr_id=rs.hr_id where ro.history_id=(SELECT id FROM upload_history uh WHERE TYPE='2' AND uh.active_time=(SELECT MAX(active_time) FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<=now()))) as ta on ta.hr_id=co.hr_id order by cfu.create_time desc limit 1;"
                    
                    AddedFollowUpsInfo = HMysql.Get_datafromDB(hostindex, lobname, sitename, self.dbuser,self.dbpassword, FollowUpsInfo_Sql)[1][0]
                    assert AddedInfoList == [list(L3info['Name'])[0],AddedFollowUpsInfo[0],self.Add_FollowUpsInfoL3],"AddedInfoList:%s doesn't equal %s"%(AddedInfoList,[list(L3info['Name'])[0],AddedFollowUpsInfo[0],self.Add_FollowUpsInfoL3])
                    
                    #Click 'save and continue later' button and Again enter this form detail page.
                    CHPage.click_SaveAndContinueLater()
                    time.sleep(2)
                    CHPage.click_eachcoach(1)
                    CHPage.click_FollowUps()
                    EnterAddedInfoList_Again = CHPage.get_AddedFollowUpsInfo()
                    assert EnterAddedInfoList_Again == [list(L3info['Name'])[0],AddedFollowUpsInfo[0],self.Add_FollowUpsInfoL3],"EnterAddedInfoList_Again:%s doesn't equal %s"%(EnterAddedInfoList_Again,[list(L3info['Name'])[0],AddedFollowUpsInfo[0],self.Add_FollowUpsInfoL3])
                    
                    #Mouse hover on my inpuuting info-> click edit icon.Edit content to another new one.  e.g 'Using automation script to L3 add follow up info, edit info'
                    CHPage.click_EditIcon(1)
                    CHPage.Edit_SaveContent(self.Edit_NewContentL3)
                    EditedFollowUpsInfo_Sql = "select concat(cfu.avatar_name,' added on ',cfu.create_time,' -0400'),ta.Agentname,ta.firstname,ta.hr_id,ta.tl_id,co.sn from coaching_follow_ups cfu \
                    left join coach co on cfu.coach_id=co.id left join (select ro.hr_id,concat(ro.firstname,' ',ro.lastname) Agentname,rs.firstname,rs.hr_id tl_id from roster ro left join roster_teamleaders rt on rt.team_id=ro.team_id \
                    join roster rs on rt.hr_id=rs.hr_id where ro.history_id=(SELECT id FROM upload_history uh WHERE TYPE='2' AND uh.active_time=(SELECT MAX(active_time) FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<=now()))) as ta on ta.hr_id=co.hr_id order by cfu.create_time desc limit 1;"
                    EditFollowUpsInfo = HMysql.Get_datafromDB(hostindex, lobname, sitename, self.dbuser,self.dbpassword, EditedFollowUpsInfo_Sql)[1][0]
                    EditedInfoList = CHPage.get_AddedFollowUpsInfo()
                    assert EditedInfoList == [list(L3info['Name'])[0],EditFollowUpsInfo[0],self.Edit_NewContentL3],"EditedInfoList:%s doesn't equal %s"%(EditedInfoList,[list(L3info['Name'])[0],EditFollowUpsInfo[0],self.Edit_NewContentL3])
                    Log.logout_tablet()
                    
                    #step2:L1 Add /edit follow up_ongoing
                    #get this form relevant L1 info and login tablet.
                    TLinfo = Get_Roleinfo.get_TLandAgentInfofromAdmin(adminurl, lobname, sitename, self.OMuserid, self.OMpwd, EditFollowUpsInfo[4])
                    Log.Login_tablet(tableturl, lobname, sitename, TLinfo['Hrid'], TLinfo["Password"])
                    
                    #Enter this form detail page. Click Link 'Follow ups '.
                    THPage.click_coachingcircle()
                    self.filter_CoachJustAdded(EditFollowUpsInfo[5], 'All','All')
                    CHPage.click_eachcoach(1)
                    CHPage.click_FollowUps()
                    #edit follow up which added
                    assert CHPage.click_EditIcon(1) == False #False means: L1 Can not edit this follow-ups which added by L3
                    
                    #add/edit new follow up
                    CHPage.Add_FollowUps(self.Add_FollowUpsInfoTL)
                    time.sleep(1)
                    CHPage.click_EditIcon(2)
                    CHPage.Edit_SaveContent(self.Edit_NewContentTL)
                    CHPage.refresh_CurrentWindow()
                    Log.logout_tablet()
                    
                    #step3:Agent Add /edit follow up_ongoing
                    #get this form relevant Agent info and login tablet
                    Agentinfo = Get_Roleinfo.get_TLandAgentInfofromAdmin(adminurl, lobname, sitename, self.OMuserid, self.OMpwd, EditFollowUpsInfo[3])
                    Log.Login_tablet(tableturl, lobname, sitename, Agentinfo['Hrid'], Agentinfo["Password"])
                    
                    #Enter this form detail page. Click Link 'Follow ups '.
                    THPage.click_coachingcircle()
                    self.filter_CoachJustAdded(EditFollowUpsInfo[5], 'All','All')
                    CHPage.click_eachcoach(1)
                    CHPage.click_FollowUps()
                    #edit follow up which added by L3 and L1
                    assert CHPage.click_EditIcon(1) == False #False means: Agent Can not edit this follow-ups which added by L3
                    assert CHPage.click_EditIcon(2) == False #False means: Agent Can not edit this follow-ups which added by L1
                    
                    #Add /edit follow up
                    CHPage.Add_FollowUps(self.Add_FollowUpsInfoAgent)
                    time.sleep(1)
                    CHPage.click_EditIcon(3)
                    CHPage.Edit_SaveContent(self.Edit_NewContentAgent)
                    
                    CHPage.refresh_CurrentWindow()
                    Log.logout_tablet()
                    GetConfig.print_EndTest_message(lobname, sitename)
                    
    def filter_CoachJustAdded(self,SNnumber,coachname,status):
        CHPage = Coachinghomepage()
        CHPage.input_SN(SNnumber)
        CHPage.select_coachname(coachname)
        CHPage.select_status(status)
        CHPage.click_filterbutton()
        