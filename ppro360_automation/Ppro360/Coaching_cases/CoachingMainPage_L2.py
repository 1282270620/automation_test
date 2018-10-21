import unittest
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.HandleMySQL import HandleMySQL
from public_method.Coach_Triad_General import Coach_Triad_General
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from public_method.Deleteexistfile import Deleteexistfile

class CoachingMainPage_L2(unittest.TestCase):
    def setUp(self):
        self.caseID="CoachingMainPage_L2"
        #Get OM account
        GetData = Get_configration_data()
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        #Database info
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #Get all lobs from CSV
        self.testLOBSITE_list = GetData.get_LOBSITEtoTest(self.caseID)
        
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()
        
        #get login role
        self.role = "L2"
        #CoachExport file prefix
        self.filename_prefix="coach"
        self.sheetname="Coach"
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        
    def tearDown(self):
        #Gl.driver.quit()
        pass
    def test_CoachingMainPage_L2(self):
        Tablet = TabletHomepage()
        GetConfData = Get_configration_data()
        Log = Login()
        Get_TLinfo = Get_AllRoleAccountForTest()
        CT=Coach_Triad_General()
        CoachPublic=Coaching_PublicFunction()
        HMysql=HandleMySQL()
        CoachHome=Coachinghomepage()
        Deletefile=Deleteexistfile()

        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag = GetConfData.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]

                ##GET THE CORRECT URL#####
                adminurl=GetConfData.get_Test_AdminUrl(lobname)
                tableturl=GetConfData.get_Test_Tablet(lobname)
                hostindex=GetConfData.get_Test_Hostindex(lobname)
                
                #######Get lob database name when lob in specialLobs_list########
                if lobname in self.AllSpecialLobs_list:
                    lobname_database=GetConfData.get_DatabaseName_ByLobName(lobname)
                else:
                    lobname_database=lobname
                
                #######Get lob database name########
                #get each site which in this lob
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename = site_list[n]
                    GetConfData.print_StartTest_message(lobname, sitename)
                    #get site's database name
                    lob_site=lobname+':'+sitename
                    if lob_site in self.AllSpecialSites_list:
                        sitename_database=GetConfData.get_DatabaseName_BySiteName(lob_site)
                    else:
                        sitename_database=sitename
                        
                    #get TL info and login tablet
                    L2info = Get_TLinfo.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.role)
                    L2Hrid = L2info['Hrid']
                    L2pwd = L2info["Password"]
                    L2name = L2info['Name']
                    print(L2info)
                    #----------------------------Login tablet with TL1/TL2 account,Click 'Coaching' icon to check search main page------------------------------
                    #log on to the tablet in the role of L2 and enter coaching search page with title 'Coaching'
                    Log.Login_tablet(tableturl, lobname, sitename, L2Hrid, L2pwd)
                    Tablet.click_coachingcircle()
                    #On the top right of this page, verify login information
                    CT.Check_Header(L2name, self.role, lobname, sitename)
                    CT.Check_CoachingItemName(lobname)
                    
                    #--------------------------Check default Coaching list-----------------------------------
                    #On filter section, show following 10 fields
                    #Display a default Coaching list of all incompleted coaching records conducted by logged-in user
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
                    
                    
                    #get Display all records of creater logged-in user from Coaching Page
                    TotalCoach_page_Dic=CoachPublic.get_Total_PageandCoachnumber()
                    TotalCoachNumber_page=TotalCoach_page_Dic['Total_coachnumber_tablet']
                    print(TotalCoachNumber_page)
                    
                    #get Display all records of creater logged-in user from database
                    sql_coach="select co.sn,concat(ro.firstname,' ',ro.lastname) coachname,co.employname,co.hr_id,co.status,substring_index(co.created_time,' ',1) \
                    from (select c.*,concat(r.firstname,' ',r.lastname) employname from coach c left join roster r on c.hr_id = r.hr_id \
                    where c.assign_to_id='"+L2info['Hrid']+"' and c.classification=0 and status in (0,3) order by c.id desc) co \
                    left join roster ro on co.assign_to_id = ro.hr_id;"
                    
                    CT.Check_TotalCoachNumber_withDB(TotalCoachNumber_page,hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)

                    #-----------------------------------------Directly click Export button.(no matter if have data or not)------------------------------------
                    #click export Coaching records which are the same as that's shown on page
                    Deletefile.delete_coachfile(self.downloadpath)
                    CoachHome.click_exportbutton()
                    CT.Check_TotalCoachNumber_withExcel(TotalCoachNumber_page,self.filename_prefix, self.sheetname)

                    
                    sql_teamunderL2="select ma.firstname,ma.lastname,TL1.rt_teamID,TL1.agentHRID from \
                    (select ml1.hr_id tl_hr_id, ml1.firstname tl_first_name,ml1.lastname tl_last_name, \
                    r.team_id as rt_teamID,r.hr_id as agentHRID,r.firstname as agentFirstName,r.lastname as agentLastName \
                    from manager ml2 join manager ml1 on ml1.history_id=ml2.history_id and ml1.parent_id=ml2.id \
                    left join roster r on r.history_id=ml1.history_id and ml1.hr_id=r.hr_id where ml2.hr_id='"+L2Hrid+"' and  \
                    ml2.history_id=(SELECT id FROM upload_history uh WHERE TYPE='2' AND uh.active_time=(  \
                    SELECT MAX(active_time)FROM upload_history WHERE TYPE='2' AND DATE(data_date)<=NOW()))) TL1 \
                    right join manager ma on TL1.tl_hr_id = ma.hr_id where TL1.tl_hr_id is not NULL or hr_id = '"+L2Hrid+"';"
                   
                    sql_Employee="select agentFirstName,agentLastName from (SELECT l.hr_id L2_hrid,l.firstname L2_firstname,l.lastname L2_lastname, rt.hr_id tl_hr_id,rtl.firstname tl_first_name,rtl.lastname tl_last_name,rt.team_id as rt_teamID,r.hr_id as agentHRID,r.firstname as agentFirstName,r.lastname as agentLastName \
                    from manager l join manager t on l.id=t.parent_id left join roster_teamleaders rt on t.history_id=rt.history_id and t.hr_id=rt.hr_id \
                    left JOIN roster rtl ON rt.history_id = rtl.history_id AND rt.hr_id = rtl.hr_id  \
                    LEFT JOIN roster r ON rt.history_id=r.history_id AND rt.team_id=r.team_id  \
                    WHERE rt.history_id=(  \
                    SELECT id  \
                    FROM upload_history uh  \
                    WHERE TYPE='2' AND uh.active_time=(  \
                    SELECT MAX(active_time)  \
                    FROM upload_history   \
                    WHERE TYPE='2' AND DATE(data_date)<=now())) group  by L2_hrid,L2_firstname,L2_lastname,tl_hr_id,tl_first_name,tl_last_name,rt_teamID,agentHRID,agentFirstName,agentLastName) s  where tl_hr_id<>  agentHRID and  l2_hrid="+L2info['Hrid']+";"
                    
                    sql_TL = ''
                    
                    #-------------------------------Check CoachName drop-down list-----------------------------------
                    CoachHome.click_coachnamebox()
                    TotalCoachName_page=CoachHome.get_all_CoachName()
                    CT.Check_AllCoachName_withDB(TotalCoachName_page,hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_teamunderL2, sql_TL)
                    
                    #-------------------------------Check EmployeeName drop-down list-----------------------------------
                    coachtype = "Coaching"
                    CoachHome.click_EmployeeNamebox()
                    TotalEmployeeName_page=CoachHome.get_all_EmployeeName()
                    CT.Check_AllEmployeeName_withDB(self.role, coachtype, TotalEmployeeName_page, hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_Employee)
                    
                    #-------------------------------Check Status drop-down--------------------------------------------------
                    CoachHome.click_EmployeeNamebox()
                    CoachHome.click_statusbox()
                    TotalStatus_page=CoachHome.get_all_StatusValue()
                    CT.Check_AllStatusValue_withStandardValue(TotalStatus_page)
                    
                    #-------------------------------Field 'Created Date','Completed Date','Acknowledge Date'-----------------------------------
                    #show black by default
                    CoachHome.verify_CoachDatebydefault()
                    
                    #-------------------------------Check search list header------------------------------------------------
                    CoachListHeader_List_page=CoachHome.get_all_CoachListHeader()
                    CT.Check_CoachListHeader_withStandardValue(CoachListHeader_List_page)
                    
                    Log.logout_tablet()
                    GetConfData.print_EndTest_message(lobname, sitename)
                    