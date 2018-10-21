import unittest,time,os,ConfigParser
import MySQLdb
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.MyTeamInfoPage import MyTeamInfoPage
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.HandleMySQL import HandleMySQL

class MyTeamInfo_TLRedeemPoints(unittest.TestCase):
    def setUp(self):
        #caseID
        self.caseID = "MyTeamInfo_TLRedeemPoints"
        GetConfData = Get_configration_data()
        
        #Get OM account
        OMaccount = GetConfData.get_OMaccount()
        self.OMuserid = OMaccount["OMuserid"]
        self.OMpwd = OMaccount["OMpassword"]
        self.role ="L1"

        #Get all lobs from CSV
        self.testLOBSITE_list = GetConfData.get_LOBSITEtoTest(self.caseID)

        #Database info
        self.host=GetConfData.get_StageDatabaseHost()
        self.dbuser=GetConfData.get_StageDatabaseUser()
        self.dbpassword=GetConfData.get_StageDatabasePassword()

        #set redeem value and redeem role
        self.redeem_value = 1
        self.redeemrole = "Agent11"
        
    def tearDown(self):
        Gl.driver.quit()
       
    def test_MyTeamInfo_TLRedeemPoints(self):
        Log = Login()
        Tablet = TabletHomepage()
        GetConfData = Get_configration_data()
        Myteaminfo = MyTeamInfoPage()
        Get_TLinfo = Get_AllRoleAccountForTest()       
        
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

                #get each site which in this lob
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename = site_list[n]
                    GetConfData.print_StartTest_message(lobname, sitename)

                    #get T1 info from admin
                    TLinfo = Get_TLinfo.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpwd, self.role)
                    TLHrid = TLinfo['Hrid']
                    TLpwd = TLinfo["Password"]
                    
                    #########  Points and Redeem line 14-16 #########
                    #Login tablet with TL1 and navigate to My Team Info module
                    Log.Login_tablet(tableturl, lobname, sitename, TLHrid, TLpwd)
                    time.sleep(Gl.waittime)
                    Tablet.click_TL_Myteaminfocircle()
                    
                    #All agent info under this TL are listed on the page of MyTeamInfo
                    actual,agent_loc = Myteaminfo.get_MyTeamTableInfo(self.redeemrole)
                    actual = sorted(actual)
                    expected = self.get_infoconfigrationaboutpointdatabase(hostindex, TLHrid, lobname, sitename)
                    assert actual == expected,"acutal:%s doesn't equal expected:%s"%(actual,expected)
                    print("---All agent under this TL are listed as same as the relevant database--assert successfully")
                    
                    #########  Points and Redeem line 17-18 #########
                    expected_Redeempointinfo = ["Redeem the Points","Please input how many points you want redeem","Please input the prize you award agent","True","True"]
                   
                    #click the redeem point button when Agent's points is not 0
                    Myteaminfo.click_RedeemPoints(agent_loc)
                    
                    #verify UI of 'Redeem the points' pop-up window
                    actual_Redeempointinfo = Myteaminfo.get_infoofpop_upwindow()
                    assert expected_Redeempointinfo == actual_Redeempointinfo
                    print("---Verify that UI of 'Redeem the points' pop-up window is correct--assert successfully")
                    
                    #input 1 in first testbox and input 'Text 1' in second text box
                    Myteaminfo.input_redeempointin_textbox(self.redeem_value, "Text 1")
                    
                    #click Redeem button
                    Myteaminfo.click_redeembutton()
                    RedeemPointStatus = Myteaminfo.get_redeemstatus()
                    assert RedeemPointStatus == "redeem points seccussfully"
                    print("---display redeem points successfully--assert successfully")
                    time.sleep(Gl.waittime)
                    
                    #the points will Reduce the corresponding points and Points of other agents keep the same as before
                    actual_afterredeempoint,agentuseless_loc = Myteaminfo.get_MyTeamTableInfo(self.redeemrole)
                    actual_afterredeempoint = sorted(actual_afterredeempoint)
                    for index in range(0,len(actual)):
                        expected_agent = actual[index]
                        actual_agent = actual_afterredeempoint[index]
                        if expected_agent[0] == self.redeemrole:
                            expected_agent[3] = str(int(expected_agent[3]) - self.redeem_value)
                        assert expected_agent == actual_agent
                    print("---the points will Reduce the corresponding points and Points of other agents keep the same as before--assert successfully")
                    
                    #check in database
                    expected_afterredemmpointindb = self.get_infoconfigrationaboutpointdatabase(hostindex, TLHrid, lobname, sitename)
                    assert actual_afterredeempoint == expected_afterredemmpointindb
                    
                    Log.logout_tablet()
                    GetConfData.print_EndTest_message(lobname, sitename)
                    
    #the method used to get sqls from the file which is MyTeamInfoORMyinfo.ini
    def get_SqlsFromConfigration(self,section,sql_key):
        ConfPars = ConfigParser.ConfigParser()
        ConfPars.read(os.path.join(os.path.dirname(os.getcwd()),"Configration","MyTeamInfoORMyinfo.ini"))      
        sql_Config = ConfPars.get(section,sql_key)
        return sql_Config
    
    #get points from database
    def Get_pointdatafromDB(self,host,database_name,dbuser,dbpassword,sql):
        Data_list=[] 
        conn=MySQLdb.connect(host,dbuser,dbpassword,database_name)
        cursor=conn.cursor()
        conn.autocommit(True)
        number=cursor.execute(sql)#Get all info of Coaching except coach_name
        data=cursor.fetchall()
        Data_list.append(number)
        Data_list.append(data)
        cursor.close()
        conn.close()
        return Data_list
    
    #get corresponding info from configration about database to get point
    def get_infoconfigrationaboutpointdatabase(self,hostindex,TLHrid,lobname,sitename):
        GetData=Get_configration_data()
        HMysql=HandleMySQL()
        expected = []
        #get all agent info under this TL from in database
        sql_activedate = self.get_SqlsFromConfigration("MyTeamInfo_TLRedeemPoints_sqls","Sql_AllAgentInfoActivedate").replace("login_hr_id",TLHrid)
        DataActivedate = HMysql.Get_datafromDB(hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_activedate)[1]
        #modify the string format
        LobSiteDBName=GetData.get_LobSiteDBName(lobname, sitename)
        lobname_database=LobSiteDBName.get("lobname_database")
        sitename_database=LobSiteDBName.get("sitename_database")
        lobnamedb=lobname_database.lower().replace(" ","")
        sitenamedb=sitename_database.lower().replace("-","").replace(" ","")
        sql_point = self.get_SqlsFromConfigration("MyTeamInfo_TLRedeemPoints_sqls","Sql_GetPointfromDataBase") % (lobnamedb,sitenamedb)

        #get the URL about VXI or AWS
        if hostindex == 92:
            URL = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "URL_VXI")
        elif hostindex == 93:
            URL = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "URL_AWS")
        DBname = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "DBname")
        DBuser = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "DBuser")
        DBpassword = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "DBpassword")                 
        DataPoint = self.Get_pointdatafromDB(URL, DBname, DBuser, DBpassword, sql_point)[1] 
        DataActivedate = list(DataActivedate)
        DataPoint = list(DataPoint)
        for dataactive in DataActivedate:
            dataactive = list(dataactive)
            dataactive[2] = str(dataactive[2]).replace("-","/")
            dataactive.append("0")
            for point in DataPoint:
                point = list(point)
                if dataactive[1] == point[0]:
                    dataactive[3] = str(point[1])
            expected.append(dataactive)
        expected = sorted(expected)
        return expected
    
                    
                    
                    
                    
                    
                    
                    