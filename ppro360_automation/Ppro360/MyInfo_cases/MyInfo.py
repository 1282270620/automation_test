import unittest,ConfigParser,os,time
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.MyInfoPage import MyInfoPage
import MySQLdb
from public_method import Gl
from public_method.Login import Login
from public_method.Get_configration_data import Get_configration_data
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.HandleMySQL import HandleMySQL

class MyInfo(unittest.TestCase):
    def setUp(self):
        #caseID
        self.caseID = "MyInfo"
        GetConfData = Get_configration_data()
        
        #Get OM account
        OMaccount = GetConfData.get_OMaccount()
        self.OMuserid = OMaccount["OMuserid"]
        self.OMpwd = OMaccount["OMpassword"]
        self.role ="Agent"
    
        #Database info
        self.host=GetConfData.get_StageDatabaseHost()
        self.dbuser=GetConfData.get_StageDatabaseUser()
        self.dbpassword=GetConfData.get_StageDatabasePassword()

        #Get all lobs from CSV
        self.testLOBSITE_list = GetConfData.get_LOBSITEtoTest(self.caseID)
        
        #Define the color with RGB
        self.gray = 'rgba(128, 128, 128, 1)'
        self.blue = 'rgba(255, 255, 255, 1)'
        self.position = 'center'
        self.tablecolunms=['Type','Description','Period Total','Total Points','Date']
    
    def test_MyInfo(self):
        Log = Login()
        Tablet = TabletHomepage()
        GetConfData = Get_configration_data()
        Get_allroleinfo = Get_AllRoleAccountForTest()
        MyInfo = MyInfoPage()
        HMysql=HandleMySQL()
        
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
    
                #######Get lob database name########
                #get each site which in this lob
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename = site_list[n]
                    GetConfData.print_StartTest_message(lobname, sitename)          
                    
                    #get Agent info from admin
                    Agentinfo = Get_allroleinfo.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpwd, self.role)
                    AgentHrid = Agentinfo["Hrid"]
                    Agentpwd = Agentinfo["Password"]
                    
                    #Login tablet with Agent, and into My Info modules
                    Log.Login_tablet(tableturl, lobname, sitename, AgentHrid, Agentpwd)
                    Tablet.click_Myinfo()
                    
                    #Click on the 'Points History' button in 'My Info' page
                    MyInfo.click_PointsHistory()
                    
                    ##### verify the UI #####
                    #Points History' button is blue, and 'Personal info' button is gray
                    PersonalInfoColor = MyInfo.get_ColorofPersonalInfo()
                    PointsHistoryColor = MyInfo.get_ColorofPointsHistory()
                    assert self.gray == PersonalInfoColor
                    assert self.blue == PointsHistoryColor
                    print("Points History' button is blue, and 'Personal info' button is gray---display correct!!!")
                    #Show the title 'My Info' at the middle top of the screen
                    MyInfoPosition = MyInfo.get_TitleMyInfoPosition()
                    assert self.position == MyInfoPosition
                    print("Show the title 'My Info' at the middle top of the screen---display correct!!!")
                    #Show the points history table at the right side of main frame
                    
                    #Table colunms:'Type','Description','Period Total','Total Points','Date'
                    actual_tablecolunms = MyInfo.get_TabletColunms()
                    assert self.tablecolunms == actual_tablecolunms
                    print("Table colunms:'Type','Description','Period Total','Total Points','Date'---display correct!!!")
                    
                    ##### check default records shown on page #####
                    #get the default records from database
                    expected_pointshistory = self.get_infoconfigrationaboutpointdatabase(hostindex, AgentHrid,lobname, sitename)
                    #get the agent points histroy data from tablet
                    actual_pointhistory = MyInfo.get_PointHistoryTablet()
                    assert expected_pointshistory == actual_pointhistory,"expected:%s doesn't equal actual:%s"%(expected_pointshistory,actual_pointhistory)
                    print('The agent points history data match with the database ---verified correct!!!')
                    
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
    def get_infoconfigrationaboutpointdatabase(self,hostindex,Hrid,lobname,sitename):
        HMysql=HandleMySQL()
        expected = []
        #modify the string format
        LobSiteDBName=Get_configration_data().get_LobSiteDBName(lobname,sitename)
        lobnamedb=LobSiteDBName["lobname_database"]
        sitenamedb=LobSiteDBName["sitename_database"]
        
        sql_pointshistory = self.get_SqlsFromConfigration("MyInfo_AgentPointsHistoryData_sql","Sql_MyInfoPointsHistory") % (lobnamedb,sitenamedb,Hrid)
        #get the URL about VXI or AWS
        if hostindex == 92:
            URL = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "URL_VXI")
        elif hostindex == 93:
            URL = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "URL_AWS")
        DBname = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "DBname")
        DBuser = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "DBuser")
        DBpassword = self.get_SqlsFromConfigration("GetPointinfo_fromdatabase", "DBpassword")                    
        DataPointsHistory = self.Get_pointdatafromDB(URL, DBname, DBuser, DBpassword, sql_pointshistory)[1] 
        expected = self.process_DatabaseData(DataPointsHistory)
        expected=sorted(expected)
        return expected
    
    #Process data from database 
    def process_DatabaseData(self,DataList):
        DataList_process = []
        for datalist in DataList:
            datalist_process = []
            if int(datalist[4]) == 1: #index=4:type field
                datalist_process.append('REDEEM')
                datalist_process.append(datalist[5]) #index=5:description field
            elif int(datalist[4]) == 0:
                datalist_process.append('REWARD')
                datalist_process.append('')
            datalist_process.append(str(datalist[6])) #index=6:point field
            datalist_process.append(str(datalist[7])) #index=7:total field
            str_time = datalist[10].strftime("%Y/%m/%d") #index=10:created_time
            datalist_process.append(str_time)
            DataList_process.append(datalist_process)
        return DataList_process
               
    def tearDown(self):
        Gl.driver.quit()
        pass  

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 