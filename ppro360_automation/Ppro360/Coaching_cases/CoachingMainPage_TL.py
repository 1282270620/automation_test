'''
Created on Jan 23, 2018

@author: symbio
'''
import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.Deleteexistfile import Deleteexistfile
from public_method.Coaching_PublicFunction import Coaching_PublicFunction

from Tablet_pages.Coachinghomepage import Coachinghomepage


class CoachingMainPage_TL(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="CoachingMainPage_TL"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.role="L1"
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Get coachpopuptittle
        self.title=GetData.get_AddCoachingFormTitle()
        #coaching or Triad coaching
        self.coachtype="Coaching"   
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.hostindex=92
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #CoachExport file prefix
        self.filename_prefix="coach"
        self.sheetname="Coach"
        #Get current Date
        self.CurrentDate=GetData.get_ServerCurrentDate()



    def test_CoachingMainPage_TL(self):
        CT=Coach_Triad_General()
        Tablet=TabletHomepage()
        GetConfig=Get_configration_data()
        GetLC=Get_AllRoleAccountForTest()
        CoachPublic=Coaching_PublicFunction()
        CoachHome=Coachinghomepage()
        Deletefile=Deleteexistfile()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #Step1:Login tablet
                    
                    
                    TLuserid=GetLC.get_TLInfoFromMyteamInfo(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    TLInfo=GetLC.get_TLandAgentInfofromAdmin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword, TLuserid)
                    TLpassword=TLInfo["Password"]
                    TLname=TLInfo["Name"]
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,TLuserid,TLpassword)
                    time.sleep(Gl.waittime)      
                    Tablet.click_TL_coachingcircle()
                    
                    CT.Check_Header(TLname, self.role, lobname, sitename)
                    CT.Check_CoachingItemName(lobname)
                    CoachName=TLname
                    EmployeeName="All"
                    Status="Incompleted"
                    Type="All"
                    Created_StartDate=""
                    Created_EndDate=""
                    Completed_StartDate=""
                    Completed_EndDate=""
                    Acknowledge_StartDate=""
                    Acknowledge_EndDate=""
                    CT.Check_CoachFilterValue(CoachName, EmployeeName, Status, Type, Created_StartDate, Created_EndDate, Completed_StartDate, Completed_EndDate, Acknowledge_StartDate, Acknowledge_EndDate)
                    TotalCoach_page_Dic=CoachPublic.get_Total_PageandCoachnumber()
                    TotalCoachNumber_page=TotalCoach_page_Dic['Total_coachnumber_tablet']
                    sql_coach="select * from coach  where  assign_to_id="+TLuserid+" and status in (0,3) order by id desc"
                    CT.Check_TotalCoachNumber_withDB(TotalCoachNumber_page,self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    #Delete all coaching file before click export button
                    Deletefile.delete_coachfile(self.downloadpath)
                    CoachHome.click_exportbutton()
                    CT.Check_TotalCoachNumber_withExcel(TotalCoachNumber_page,self.filename_prefix, self.sheetname)
                    CoachHome.click_coachnamebox()
                    TotalCoachName_page=CoachHome.get_all_CoachName()
                    print TotalCoachName_page
                    assert TotalCoachName_page==[TLname]
                    
                    CoachHome.click_EmployeeNamebox()
                    TotalEmployeeName_page=CoachHome.get_all_EmployeeName()
                    sql_Employee="select * from (SELECT rt.hr_id tl_hr_id,rtl.firstname tl_first_name,rtl.lastname tl_last_name,rt.team_id \
                    as rt_teamID,r.hr_id as agentHRID,rag.firstname as agentFirstName,rag.lastname as agentLastName \
                    FROM roster_teamleaders rt \
                    JOIN roster rtl ON rt.history_id = rtl.history_id AND rt.hr_id = rtl.hr_id \
                    LEFT JOIN roster r ON rt.history_id=r.history_id AND rt.team_id=r.team_id \
                    JOIN roster rag ON r.history_id = rag.history_id AND r.hr_id = rag.hr_id \
                    WHERE rt.history_id=(\
                    SELECT id FROM upload_history uh \
                    WHERE TYPE='2' AND uh.active_time=(\
                    SELECT MAX(active_time) \
                    FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<='"+self.CurrentDate+"')) \
                    group  by  tl_hr_id, tl_first_name,  tl_last_name, rt_teamID,agentHRID, agentFirstName, agentLastName) \
                    s  where tl_hr_id<>agentHRID and tl_hr_id="+TLuserid+";"
                    
                    
                    CT.Check_AllEmployeeName_withDB(self.role,self.coachtype,TotalEmployeeName_page, self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_Employee)
                    CoachHome.click_EmployeeNamebox()
                    
                    CoachHome.click_statusbox()
                    TotalStatus_page=CoachHome.get_all_StatusValue()
                    CT.Check_AllStatusValue_withStandardValue(TotalStatus_page)
                    CoachListHeader_List_page=CoachHome.get_all_CoachListHeader()
                    CT.Check_CoachListHeader_withStandardValue(CoachListHeader_List_page)
                    
                    
    def tearDown(self):
        Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()