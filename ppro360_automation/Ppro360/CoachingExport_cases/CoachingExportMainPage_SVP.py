'''
Created on Feb 5, 2018

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
from Tablet_pages.CoachingExportPage import CoachingExportPage
class CoachingExportMainPage_SVP(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        #Case ID
        self.caseID="CoachingExportMainPage_SVP"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()
        #Get SVP account
        SVPaccount=GetData.get_SVPaccount()
        self.SVPuserid=SVPaccount["SVPuserid"]
        self.SVPpassword=SVPaccount["SVPpassword"]
        self.role="SVP"
        self.SVPname="SVP FOR SCRIPTS"
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
        self.sheetname="Sheet1"
        #Get current Date
        self.CurrentDate=GetData.get_ServerCurrentDate()
    
    def test_CoachingExportMainPage_SVP(self):
        CT=Coach_Triad_General()
        Tablet=TabletHomepage()
        GetConfig=Get_configration_data()
        GetLC=Get_AllRoleAccountForTest()
        CoachPublic=Coaching_PublicFunction()
        CoachHome=Coachinghomepage()
        Deletefile=Deleteexistfile()
        CoachExport=CoachingExportPage()
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
                    
                    print self.SVPuserid,self.SVPpassword
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.SVPuserid,self.SVPpassword)
                    time.sleep(Gl.waittime)      
                    Tablet.click_LC_coachingExportcircle()
                    
                    #if lobname in ["PAYPAL","CENTURYLINK"]:
                    coach_list=GetConfig.get_CoachingExportFormList(lobname)
                    
                        
                    CT.Check_Header(self.SVPname, self.role, lobname, sitename)
                    CT.Check_CoachingExportItemName()
                    if coach_list!=[u'']:
                        Type=CoachExport.get_Type_download(1)
                    else:
                        Type="All"
                    CoachExport.click_TypeBox()
                    #Type=CoachExport.get_Type_download(1)
                    CoachExport.click_TypeBox()
                    CoachName="All"
                    EmployeeName="All"
                    Status="All"
                    
                    Created_StartDate=""
                    Created_EndDate=""
                    Completed_StartDate=""
                    Completed_EndDate=""
                    CT.Check_CoachingExportFilterValue(CoachName, EmployeeName, Status, Type, Created_StartDate, Created_EndDate, Completed_StartDate, Completed_EndDate)
                    if Type !='All':
                        FormID=str(GetConfig.get_CoachID(Type))
                        TotalCoach_page_Dic=CoachPublic.get_Total_PageandCoachnumber()
                        TotalCoachNumber_page=TotalCoach_page_Dic['Total_coachnumber_tablet']
                        sql_coach="select * from coach  where type='"+FormID+"' order by id desc"
                        
                        CT.Check_TotalCoachNumber_withDB(TotalCoachNumber_page,self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    #Delete all coaching file before click export button
                    Deletefile.delete_coachfile(self.downloadpath)
                    if coach_list!=[u'']:
                        CoachExport.click_Export()
                        CT.Check_TotalCoachNumber_withExcel(TotalCoachNumber_page,self.filename_prefix, self.sheetname)
                    CoachExport.click_CoachNameBox()
                    TotalCoachName_page=CoachExport.get_all_CoachName()
                    sql_OMLC="select a.firstname,a.lastname,ur.user_id,ur.role_id,r.id,r.description,r.name  \
                    from account a join user_role ur on a.hr_id=ur.user_id  \
                    join role r  on ur.role_id=r.id where r.name='OM' or r.name='LC' \
                    group by a.firstname,a.lastname,ur.user_id,ur.role_id,r.id,r.description,r.name;"
                    sql_TL="select  tl_hr_id,tl_first_name,tl_last_name,rt_teamID,agentHRID, agentFirstName,agentLastName  \
                    from  ( SELECT rt.hr_id tl_hr_id,rtl.firstname tl_first_name,rtl.lastname tl_last_name,rt.team_id as rt_teamID,r.hr_id \
                    as agentHRID,rag.firstname as agentFirstName,rag.lastname as agentLastName FROM roster_teamleaders rt \
                    JOIN roster rtl ON rt.history_id = rtl.history_id AND rt.hr_id = rtl.hr_id \
                    LEFT JOIN roster r ON rt.history_id=r.history_id AND rt.team_id=r.team_id \
                    JOIN roster rag ON r.history_id = rag.history_id AND r.hr_id = rag.hr_id \
                    WHERE rt.history_id=(\
                    SELECT id \
                    FROM upload_history uh \
                    WHERE TYPE='2' AND uh.active_time=(\
                    SELECT MAX(active_time) \
                    FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<='"+self.CurrentDate+"')) and rt.hr_id=r.hr_id) s join \
                    user_role ur on tl_hr_id=ur.user_id where ur.role_id  in (2) \
                    group by tl_hr_id,tl_first_name,tl_last_name,rt_teamID,agentHRID, agentFirstName,agentLastName;"
                    
                    CT.Check_AllCoachName_withDB(TotalCoachName_page,self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_OMLC, sql_TL)
                    
                    #CoachExport.click_CoachNameBox()
                    CoachExport.click_EmployeeNameBox()
                    #CoachHome.click_EmployeeNamebox()
                    TotalEmployeeName_page=CoachExport.get_all_EmployeeName()
                    sql_Employee="select r.* from roster r join upload_history up on r.history_id=up.id where up.active_time=(\
                    SELECT MAX(active_time) \
                    FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<='"+self.CurrentDate+"');"
                    
                    CT.Check_AllEmployeeName_withDB(self.role,self.coachtype,TotalEmployeeName_page, self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_Employee)
                    CoachExport.click_EmployeeNameBox()
                    
                    CoachExport.click_StatusBox()
                    #CoachHome.click_statusbox()
                    TotalStatus_page=CoachExport.get_all_StatusValue()
                    CT.Check_AllStatusValue_withStandardValue(TotalStatus_page)
                    CoachListHeader_List_page=CoachExport.get_all_CoachListHeader()
                    CT.Check_CoachExportListHeader_withStandardValue(CoachListHeader_List_page)
                    L.logout_tablet()
                    
    def tearDown(self):
        Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 
                    
                    