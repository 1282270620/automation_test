import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.Deleteexistfile import Deleteexistfile
from public_method.Coaching_PublicFunction import Coaching_PublicFunction

class TriadCoachingMainPage_L2(unittest.TestCase):
    def setUp(self):
        #Case ID
        self.caseID="TriadCoachingMainPage_L2"
        GetData=Get_configration_data()

        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.role="L2"
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Get coachpopuptittle
        self.title=GetData.get_AddCoachingFormTitle()
        #coaching or Triad coaching
        self.coachtype="Triadcoaching"   
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #CoachExport file prefix
        self.filename_prefix="coach"
        self.sheetname="Coach"
        #Get current Date
        self.CurrentDate=GetData.get_ServerCurrentDate()
        
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()
    
    def test_TriadCoachingMainPage_L2(self):
        CT=Coach_Triad_General()
        Tablet=TabletHomepage()
        GetConfig=Get_configration_data()
        GetLC=Get_AllRoleAccountForTest()
        CoachPublic=Coaching_PublicFunction()
        CoachHome=Coachinghomepage()
        Deletefile=Deleteexistfile()
        TriadCoach=Coach_Triad_General()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                hostindex=GetConfig.get_Test_Hostindex(lobname)
                
                #######Get lob database name when lob in specialLobs_list########
                if lobname in self.AllSpecialLobs_list:
                    lobname_database=GetConfig.get_DatabaseName_ByLobName(lobname)
                else:
                    lobname_database=lobname
                
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                    #get site's database name
                    lob_site=lobname+':'+sitename
                    if lob_site in self.AllSpecialSites_list:
                        sitename_database=GetConfig.get_DatabaseName_BySiteName(lob_site)
                    else:
                        sitename_database=sitename
                        
                    #----------Step1:Login tablet with L2 and click triad coaching icon
                    L2Info = GetLC.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.role)
                    L2password=L2Info["Password"]
                    L2name=L2Info["Name"]
                    L2Hrid=L2Info["Hrid"]
                    L=Login()
                    L.Login_tablet(tableturl,lobname,sitename,L2Hrid,L2password)   
                    Tablet.click_L2_Triadcoachingcirecle()
                    
                    #check search main page title and login infomation on the right of this page
                    CT.Check_Header(L2name, self.role, lobname, sitename)
                    CT.Check_CoachingItemName(lobname)
                    
                    #check the field in the filter section 
                    #check default triad coaching list
                    CoachName=L2name
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
                    sql_coach="select * from coach c where c.assign_to_id='"+L2Hrid+"' and c.classification=1 and (status in (0, 3)) order by c.id desc;"
                    CT.Check_TotalCoachNumber_withDB(TotalCoachNumber_page,hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    
                    #Delete all coaching file before click export button
                    Deletefile.delete_coachfile(self.downloadpath)
                    CoachHome.click_exportbutton()
                    CT.Check_TotalCoachNumber_withExcel(TotalCoachNumber_page,self.filename_prefix, self.sheetname)
                    
                    #Check CoachName drop-down list
                    CoachHome.click_coachnamebox()
                    TotalCoachName_page=CoachHome.get_all_CoachNameforAgent()
                    print(TotalCoachName_page)
                    assert TotalCoachName_page==['All',L2name]
                    
                    #Check EmployeeName drop-down list
                    coachtype = "Coaching"
                    sql_teamunderL2 = "select t.firstname tl_firstname, t.lastname tl_lastname from  manager l2 join manager t on l2.id=t.parent_id where  l2.history_id=( \
                    SELECT id FROM upload_history uh WHERE TYPE='2' AND uh.active_time=(SELECT MAX(active_time) FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<=now())) and l2.hr_id="+L2Hrid+";"
                    CoachHome.click_EmployeeNamebox()
                    TotalEmployeeName_page=CoachHome.get_all_EmployeeNameforAgent()
                    TriadCoach.Check_AllEmployeeName_withDB(self.role, coachtype, TotalEmployeeName_page, hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_teamunderL2)

                    #Check Status drop-down
                    CoachHome.click_EmployeeNamebox()
                    CoachHome.click_statusbox()
                    TotalStatus_page=CoachHome.get_all_StatusValue()
                    CT.Check_AllStatusValue_withStandardValue(TotalStatus_page)
                    
                    #show black by default
                    CoachHome.verify_CoachDatebydefault()
                    
                    #Check search list header
                    CoachListHeader_List_page=CoachHome.get_all_CoachListHeader()
                    CT.Check_CoachListHeader_withStandardValue(CoachListHeader_List_page)
                    
                    L.logout_tablet()
                    GetConfig.print_EndTest_message(lobname, sitename)
                    
    def tearDown(self):
        Gl.driver.quit()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 
                    
                    