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
class CoachingExportMainPage_TL(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        #Case ID
        self.caseID="CoachingExportMainPage_TL"
        
        GetData=Get_configration_data()
        
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
        #self.hostindex=92
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()    
        
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #CoachExport file prefix
        self.filename_prefix="coach"
        self.sheetname="Sheet1"
        #Get current Date
        self.CurrentDate=GetData.get_ServerCurrentDate()
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()
    
    def test_CoachingExportMainPage_TL(self):
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
                ##GET THE CORRECT URL#####
                Adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                hostindex=GetConfig.get_Test_Hostindex(lobname)
                ##GET THE CORRECT URL#####
                #######Get lob database name########
                if lobname in self.AllSpecialLobs_list:
                    lobname_database=GetConfig.get_DatabaseName_ByLobName(lobname)
                else:
                    lobname_database=lobname
                #######Get lob database name########
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #######Get Site database name########
                    lob_site=lobname+':'+sitename
                    if lob_site in self.AllSpecialSites_list:
                        sitename_database=GetConfig.get_DatabaseName_BySiteName(lob_site)
                    else:
                        sitename_database=sitename
                    #######Get Site database name########
                    #Step1:Login tablet
                    
                    #TLuserid=GetLC.get_TLInfoFromMyteamInfo(tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    #TLInfo=GetLC.get_TLandAgentInfofromAdmin(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, TLuserid)
                    TLInfo=GetLC.get_TLandAgentInfofromAdmin_Byrole(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, "L1")
                    TLuserid=TLInfo["Hrid"]
                    TLpassword=TLInfo["Password"]
                    TLname=TLInfo["Name"]
                    L=Login()
                    L.Login_tablet(tableturl,lobname,sitename,TLuserid,TLpassword)
                    time.sleep(Gl.waittime)      
                    Tablet.click_TL_coachingExportcircle()
                    
                    #if lobname in ["PAYPAL","CENTURYLINK"]:
                    coach_list=GetConfig.get_CoachingExportFormList(lobname)
                    '''
                    if coach_list==[]:
                        CT.Check_WarningMessage_CoachingExport()'''
                        
                    CT.Check_Header(TLname, self.role, lobname, sitename)
                    CT.Check_CoachingExportItemName()
                    CoachExport.click_TypeBox()
                    print "coach_list:",coach_list
                    if coach_list!=[u'']:
                        Type=CoachExport.get_Type_download(1)
                    else:
                        Type="All"
                    
                    #Type=CoachExport.get_Type_download(1)
                    CoachExport.click_TypeBox()
                    CoachName=TLname
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
                        sql_coach="select * from coach  where  assign_to_id='"+TLuserid+"' and type='"+FormID+"' order by id desc;"
                        
                        CT.Check_TotalCoachNumber_withDB(TotalCoachNumber_page,hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_coach)
                    #Delete all coaching file before click export button
                    Deletefile.delete_coachfile(self.downloadpath)
                    if coach_list!=[u'']:
                        CoachExport.click_Export()
                        CT.Check_TotalCoachNumber_withExcel(TotalCoachNumber_page,self.filename_prefix, self.sheetname)
                    CoachExport.click_CoachNameBox()
                    TotalCoachName_page=CoachExport.get_all_CoachName()
                    sql_OMLC="select a.firstname,a.lastname,ur.user_id,ur.role_id,r.id,r.description,r.name  \
                    from account a join user_role ur on a.hr_id=ur.user_id  \
                    join role r  on ur.role_id=r.id where r.name='L3' or r.name='LC' \
                    group by a.firstname,a.lastname,ur.user_id,ur.role_id,r.id,r.description,r.name;"
                    sql_TL=""
                    assert TotalCoachName_page[-1]==TLname
                    CT.Check_AllCoachName_withDB(TotalCoachName_page[:-1],hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_OMLC, sql_TL)
                    
                    #CoachExport.click_CoachNameBox()
                    CoachExport.click_EmployeeNameBox()
                    #CoachHome.click_EmployeeNamebox()
                    TotalEmployeeName_page=CoachExport.get_all_EmployeeName()
                    sql_Employee="select * from (SELECT rt.hr_id tl_hr_id,rtl.firstname tl_first_name,rtl.lastname \
                    tl_last_name,rt.team_id as rt_teamID,r.hr_id as agentHRID,rag.firstname as agentFirstName,rag.lastname \
                    as agentLastName FROM roster_teamleaders rt \
                    JOIN roster rtl ON rt.history_id = rtl.history_id AND rt.hr_id = rtl.hr_id \
                    LEFT JOIN roster r ON rt.history_id=r.history_id AND rt.team_id=r.team_id \
                    JOIN roster rag ON r.history_id = rag.history_id AND r.hr_id = rag.hr_id \
                    WHERE rt.history_id=(\
                    SELECT id FROM upload_history uh \
                    WHERE TYPE='2' AND uh.active_time=(\
                    SELECT MAX(active_time) FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<='"+self.CurrentDate+"')) \
                    group  by  tl_hr_id, tl_first_name,  tl_last_name, rt_teamID,agentHRID, agentFirstName, agentLastName) s  \
                    where tl_hr_id<>agentHRID and tl_hr_id="+TLuserid+";"
                    
                    CT.Check_AllEmployeeName_withDB(self.role,self.coachtype,TotalEmployeeName_page, hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_Employee)
                    CoachExport.click_EmployeeNameBox()
                    
                    CoachExport.click_StatusBox()
                    #CoachHome.click_statusbox()
                    TotalStatus_page=CoachExport.get_all_StatusValue()
                    CT.Check_AllStatusValue_withStandardValue(TotalStatus_page)
                    CoachListHeader_List_page=CoachExport.get_all_CoachListHeader()
                    CT.Check_CoachExportListHeader_withStandardValue(CoachListHeader_List_page)
                    L.logout_tablet()
                    
    def tearDown(self):
        pass
        #Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 
                    
                    