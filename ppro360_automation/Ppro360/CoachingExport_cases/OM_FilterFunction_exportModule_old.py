'''
Created on Apr 25, 2017

@author: symbio
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.CoachingExportPage import CoachingExportPage
import MySQLdb
from public_method import Gl
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.Deleteexistfile import Deleteexistfile
from public_method.Get_file import Get_file
from public_method.Get_CoachContent import Get_CoachContent


class OM_FilterFunction_exportModule(unittest.TestCase):


    def setUp(self):
        self.caseID="OM_FilterFunction_exportModule"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.Adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.LCuserid=GetData.get_LCuserid()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Whose database name is special
        self.lob_databasespecial=GetData.get_SpecialLobforDatabase()
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
       
        #CoachExport file prefix
        self.filename_prefix="coaching_export"
        
        self.sheetname="Sheet1"
        
        


    def tearDown(self):
        Gl.driver.quit()


    def test_OM_FilterFunction_exportModule(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        GetAccount=Get_AllRoleAccountForTest()
        #CoachExportPage=CoachingExportPage()
        Deletefile=Deleteexistfile()
        GetCoachContent=Get_CoachContent()
        
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
                    if lobname in self.lob_databasespecial:
                        print 'get database name from configration file.'
                    else:
                        database_name=lobname.lower()+'_'+sitename.lower()
                    
        
                    #Step0.1:Login to get TL, Agent,OM
                    '''Prepare all role data '''
                    OM1_Hrid=self.OMuserid
                    OM1_Info=GetAccount.get_LCInfo(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, OM1_Hrid)
                    OM1_Name=OM1_Info["Name"]
                    
                    LC1_Info=GetAccount.get_LCInfo(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword,self.LCuserid)
                    LC1_Name=LC1_Info["Name"]
                        
                    TL1_Info=GetAccount.get_TLInfoFromMyteamInfo(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    TL1_Name=TL1_Info["Name"]
                    TL1_Hird=TL1_Info["Hrid"]
                    TL1_Pwd=TL1_Info["Password"]
                    
                    Agent1_Info=GetAccount.get_AgentInfoFrom_TLMyteamInfo(self.tableturl, lobname, sitename, TL1_Hird, TL1_Pwd)
                    Agent1_Name=Agent1_Info["Name"]
                    Agent1_Hrid=Agent1_Info["Hrid"]
                    
                    ''' Prepare all role data'''
                    
                    #Step0.1:Connect to Mysql
                    conn=MySQLdb.connect(self.host,self.dbuser,self.dbpassword,database_name)
                    cursor=conn.cursor()
                    '''Start to test........ '''
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    THomepage.click_OM_coachingExportcircle()
                    
                    #Step1:Case for Coaching Name="All"  Employee Name="All"  Type=select one form    Other option 'All'
                    '''1.Coaching Name="All"  Employee Name="All"  Type=select one form    Other option="All" '''
                    
                    coachname='All'
                    employeename='All'
                    Typename='Skill Transfer'
                    Statusname='All'
                    sql_all="select * from coach where type=7 order by id desc;"
                    
                    #Step1.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step1.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_1=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step1.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_1=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    #Step1.3:get total_coachnumber from database
                    #Connect to database
                    conn=MySQLdb.connect(self.host,self.dbuser,self.dbpassword,database_name)
                    cursor=conn.cursor()
                    #Execute sql
                    Total_coachnumber_database_1=cursor.execute(sql_all)
                    print Total_coachnumber_database_1
                    print Total_coachnumber_excel_1
                    assert Total_coachnumber_tablet_1==Total_coachnumber_database_1
                    assert Total_coachnumber_excel_1==Total_coachnumber_database_1
                    
                    #Step2:Case for Coaching Name="All"  Employee Name=TL1   Type=select one form    Other option 'All'
                    '''2.Coaching Name="All"  Employee Name=TL1  Type=select one form    Other option 'All' '''
                    
                    coachname='All'
                    employeename=TL1_Name
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step2.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step2.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_2=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step2.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_2=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Employeename_excel_2_Dic=GetCoachContent.Get_EmployeeName(self.filename_prefix, self.sheetname)
                    AttributeofAllCoach_tablet_2_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_2)
                    #Step2.3:#Get data from database
                    TL1_hird=TL1_Hird
                    type_id='7'
                    
                    sql_EN_TL1="select * from coach  c join roster r on c.history_id=r.history_id where c.hr_id="+TL1_hird+" and c.type="+type_id+" and r.hr_id="+TL1_hird+" order by id desc;"
                    Total_coachnumber_database_2=cursor.execute(sql_EN_TL1)
                    Employeename_database_2_Dic={}
                    for row in cursor:#SN=row[10],Employeename=row[20]+row[21]
                        Employeename_database_2_Dic[row[10]]=row[20]+" "+row[21]
                    
                    #Step2.4:#assert all    
                    assert Total_coachnumber_tablet_2==Total_coachnumber_database_2
                    assert Total_coachnumber_excel_2==Total_coachnumber_database_2
                    for key in Employeename_database_2_Dic:
                        assert Employeename_database_2_Dic[key]==Employeename_excel_2_Dic[key]
                    for key in AttributeofAllCoach_tablet_2_Dic:
                        assert AttributeofAllCoach_tablet_2_Dic[key][2]==Employeename_database_2_Dic[AttributeofAllCoach_tablet_2_Dic[key][0]]
                    
                    #Step3:Case for Coaching Name="All"  Employee Name=Agent1   Type=select one form    Other option 'All'
                    '''3.Coaching Name="All"  Employee Name=Agent1  Type=select one form    Other option 'All' '''
                    
                    coachname='All'
                    employeename=Agent1_Name
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step3.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step3.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_3=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step3.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_3=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Employeename_excel_3_Dic=GetCoachContent.Get_EmployeeName(self.filename_prefix, self.sheetname)
                    AttributeofAllCoach_tablet_3_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_3)
                    print Total_coachnumber_tablet_3
                    #Step3.3:#Get data from database
                    Agent1_hird=Agent1_Hrid
                    type_id='7'
                    sql_EN_Agent1="select * from coach  c join roster r on c.history_id=r.history_id where c.hr_id="+Agent1_hird+" and c.type="+type_id+" and r.hr_id="+Agent1_hird+" order by id desc;"
                    #sql_EN_Agent1="select * from coach  where hr_id="+Agent1_hird+" and type="+type_id+" order by id desc;"
                    Total_coachnumber_database_3=cursor.execute(sql_EN_Agent1)
                    Employeename_database_3_Dic={}
                    for row in cursor:#SN=row[10],Employeename=row[20]+row[21]
                        Employeename_database_3_Dic[row[10]]=row[20]+" "+row[21]
                    print Total_coachnumber_database_3
                    #Step3.4:#assert all 
                    assert Total_coachnumber_tablet_3==Total_coachnumber_database_3
                    assert Total_coachnumber_excel_3==Total_coachnumber_database_3
                    for key in Employeename_database_3_Dic:
                        assert Employeename_database_3_Dic[key]==Employeename_excel_3_Dic[key]
                    for key in AttributeofAllCoach_tablet_3_Dic:
                        assert AttributeofAllCoach_tablet_3_Dic[key][2]==Employeename_database_3_Dic[AttributeofAllCoach_tablet_3_Dic[key][0]]
                        
                   
                    #Step4:Case for Coaching Name=OM1  Employee Name="All"   Type=select one form    Other option 'All'
                    '''4.Coaching Name=OM1  Employee Name="All"  Type=select one form    Other option 'All' '''
                    
                    coachname=OM1_Name
                    employeename='All'
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step4.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step4.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_4=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step4.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_4=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Coachname_excel_4_Dic=GetCoachContent.Get_CoachingName(self.filename_prefix, self.sheetname)
                    print Total_coachnumber_tablet_4
                    #Step4.3:#Get data from database
                    OM1_hird=OM1_Hrid
                    type_id='7'
                    sql_CN_OM1="select * from coach  where assign_to_id="+OM1_hird+" and type="+type_id+" order by id desc;"
                    Total_coachnumber_database_4=cursor.execute(sql_CN_OM1)
                    AttributeofAllCoach_tablet_4_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_4)
                    print Total_coachnumber_database_4
                    print "Total_coachnumber_excel_4=",
                    print Total_coachnumber_excel_4
                    #Step4.4:#assert all 
                    assert Total_coachnumber_tablet_4==Total_coachnumber_database_4
                    assert Total_coachnumber_excel_4==Total_coachnumber_database_4
                    for key in Coachname_excel_4_Dic:
                        assert Coachname_excel_4_Dic[key]==coachname
                    for key in AttributeofAllCoach_tablet_4_Dic:
                        assert AttributeofAllCoach_tablet_4_Dic[key][1]==coachname
                          
                    #Step5:Case for Coaching Name=TL1  Employee Name="All"   Type=select one form    Other option 'All'
                    '''5.Coaching Name=TL1  Employee Name="All"  Type=select one form    Other option='All' '''
                    
                    coachname=TL1_Name
                    employeename='All'
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step5.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step5.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_5=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step5.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_5=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Coachname_excel_5_Dic=GetCoachContent.Get_CoachingName(self.filename_prefix, self.sheetname)
                    AttributeofAllCoach_tablet_5_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_5)
                    print Total_coachnumber_tablet_5
                    #Step5.3:#Get data from database
                    TL1_hird=TL1_Hird
                    type_id='7'
                    sql_CN_TL1="select * from coach  c join roster r on c.history_id=r.history_id where c.assign_to_id="+TL1_hird+" and c.type="+type_id+" and r.hr_id="+TL1_hird+" order by id desc;"
                    #sql_CN_TL1="select * from coach  where assign_to_id="+TL1_hird+" and type="+type_id+" order by id desc;"
                    Total_coachnumber_database_5=cursor.execute(sql_CN_TL1)
                    Coachname_database_5_Dic={}
                    for row in cursor:#SN=row[10],Employeename=row[20]+row[21]
                        Coachname_database_5_Dic[row[10]]=row[20]+" "+row[21]
                    print Total_coachnumber_database_5
                    #Step5.4:#assert all 
                    assert Total_coachnumber_tablet_5==Total_coachnumber_database_5
                    assert Total_coachnumber_excel_5==Total_coachnumber_database_5
                    for key in Coachname_database_5_Dic:
                        print Coachname_database_5_Dic[key]
                        print Coachname_excel_5_Dic[key]
                        assert Coachname_database_5_Dic[key]==Coachname_excel_5_Dic[key]
                    for key in AttributeofAllCoach_tablet_5_Dic:
                        assert AttributeofAllCoach_tablet_5_Dic[key][1]==Coachname_database_5_Dic[AttributeofAllCoach_tablet_5_Dic[key][0]]
                    
                    #Step6:Case for Coaching Name=LC1  Employee Name=TL1   Type=select one form    Other option 'All'
                    '''6.Coaching Name=LC1 Employee Name=TL1  Type=select one form    Other option 'All' '''
                    
                    coachname=LC1_Name
                    employeename=TL1_Name
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step6.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step6.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_6=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step6.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_6=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Employeename_excel_6_Dic=GetCoachContent.Get_EmployeeName(self.filename_prefix, self.sheetname)
                    Coachname_excel_6_Dic=GetCoachContent.Get_CoachingName(self.filename_prefix, self.sheetname)
                    AttributeofAllCoach_tablet_6_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_6)
                    print Total_coachnumber_tablet_6
                    #Step6.3:#Get data from database
                    TL1_hird=TL1_Hird
                    LC1_hird=self.LCuserid
                    type_id='7'
                    sql_CNLC1_ENTL1="select * from coach  c join roster r on c.history_id=r.history_id where c.hr_id="+TL1_hird+" and c.assign_to_id="+LC1_hird+" and c.type="+type_id+" and r.hr_id="+TL1_hird+" order by id desc;"
                    #sql_CNLC1_ENTL1="select * from coach  where  hr_id="+TL1_hird+" and assign_to_id="+LC1_hird+" and type="+type_id+" order by id desc"
                    Total_coachnumber_database_6=cursor.execute(sql_CNLC1_ENTL1)
                    Employeename_database_6_Dic={}
                    for row in cursor:#SN=row[10],Employeename=row[20]+row[21]
                        Employeename_database_6_Dic[row[10]]=row[20]+" "+row[21]
                    print Total_coachnumber_database_6
                    #Step6.4:#assert all 
                    assert Total_coachnumber_tablet_6==Total_coachnumber_database_6
                    assert Total_coachnumber_excel_6==Total_coachnumber_database_6
                    for key in Employeename_database_6_Dic:
                        assert Employeename_database_6_Dic[key]==Employeename_excel_6_Dic[key]
                    for key in Coachname_excel_6_Dic:
                        assert Coachname_excel_6_Dic[key]==coachname
                    for key in AttributeofAllCoach_tablet_6_Dic:
                        assert AttributeofAllCoach_tablet_6_Dic[key][1]==coachname
                        assert AttributeofAllCoach_tablet_6_Dic[key][2]==Employeename_database_6_Dic[AttributeofAllCoach_tablet_6_Dic[key][0]]
                    
                    #Step7:Case for Coaching Name=OM1  Employee Name=TL1   Type=select one form    Other option 'All'
                    '''7.Coaching Name=OM1 Employee Name=TL1  Type=select one form    Other option 'All' '''
                    
                    coachname=OM1_Name
                    employeename=TL1_Name
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step7.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step7.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_7=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step7.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_7=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Employeename_excel_7_Dic=GetCoachContent.Get_EmployeeName(self.filename_prefix, self.sheetname)
                    Coachname_excel_7_Dic=GetCoachContent.Get_CoachingName(self.filename_prefix, self.sheetname)
                    AttributeofAllCoach_tablet_7_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_7)
                    print Total_coachnumber_tablet_7
                    #Step7.3:#Get data from database
                    TL1_hird=TL1_Hird
                    OM1_hird=self.OMuserid
                    type_id='7'
                    sql_CNOM1_ENTL1="select * from coach  c join roster r on c.history_id=r.history_id where c.hr_id="+TL1_hird+" and c.assign_to_id="+OM1_hird+" and c.type="+type_id+" and r.hr_id="+TL1_hird+" order by id desc;"
                    #sql_CNOM1_ENTL1="select * from coach  where  hr_id="+TL1_hird+" and assign_to_id="+OM1_hird+" and type="+type_id+" order by id desc"
                    Total_coachnumber_database_7=cursor.execute(sql_CNOM1_ENTL1)
                    Employeename_database_7_Dic={}
                    for row in cursor:#SN=row[10],Employeename=row[20]+row[21]
                        Employeename_database_7_Dic[row[10]]=row[20]+" "+row[21]
                    print Total_coachnumber_database_7
                    print "AttributeofAllCoach_tablet_7_Dic=",
                    print AttributeofAllCoach_tablet_7_Dic
                    print "Employeename_database_7_Dic=",
                    print Employeename_database_7_Dic
                    #Step7.4:#assert all 
                    assert Total_coachnumber_tablet_7==Total_coachnumber_database_7
                    assert Total_coachnumber_excel_7==Total_coachnumber_database_7
                    for key in Employeename_database_7_Dic:
                        assert Employeename_database_7_Dic[key]==Employeename_excel_7_Dic[key]
                    for key in Coachname_excel_7_Dic:
                        assert Coachname_excel_7_Dic[key]==coachname
                        
                    for key in AttributeofAllCoach_tablet_7_Dic:
                        assert AttributeofAllCoach_tablet_7_Dic[key][1]==coachname
                        assert AttributeofAllCoach_tablet_7_Dic[key][2]==Employeename_database_7_Dic[AttributeofAllCoach_tablet_7_Dic[key][0]]
                    
                    #Step8:Case for Coaching Name=OM2  Employee Name=Agent1   Type=select one form    Other option 'All'
                    '''8.Coaching Name=OM1_Name Employee Name=Agent1 Type=select one form    Other option 'All' '''
                    
                    coachname=OM1_Name
                    employeename=Agent1_Name
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step8.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step8.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_8=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step8.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_8=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Employeename_excel_8_Dic=GetCoachContent.Get_EmployeeName(self.filename_prefix, self.sheetname)
                    Coachname_excel_8_Dic=GetCoachContent.Get_CoachingName(self.filename_prefix, self.sheetname)
                    AttributeofAllCoach_tablet_8_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_8)
                    print Total_coachnumber_tablet_8
                    print AttributeofAllCoach_tablet_8_Dic
                    #Step8.3:#Get data from database
                    Agent1_hird=Agent1_Hrid
                    OM1_hird=self.OMuserid
                    type_id='7'
                    sql_CNOM1_ENA1="select * from coach  c join roster r on c.history_id=r.history_id where c.hr_id="+Agent1_hird+" and c.assign_to_id="+OM1_hird+" and c.type="+type_id+" and r.hr_id="+Agent1_hird+" order by id desc;"
                    #sql_CNOM1_ENA1="select * from coach  where  hr_id="+Agent1_hird+" and assign_to_id="+OM2_hird+" and type="+type_id+" order by id desc"
                    Total_coachnumber_database_8=cursor.execute(sql_CNOM1_ENA1)
                    Employeename_database_8_Dic={}
                    for row in cursor:#SN=row[10],Employeename=row[20]+row[21]
                        Employeename_database_8_Dic[row[10]]=row[20]+" "+row[21]
                    print Total_coachnumber_database_8
                    #Step8.4:#assert all 
                    assert Total_coachnumber_tablet_8==Total_coachnumber_database_8
                    assert Total_coachnumber_excel_8==Total_coachnumber_database_8
                    for key in Employeename_database_8_Dic:
                        assert Employeename_database_8_Dic[key]==Employeename_excel_8_Dic[key]
                    for key in Coachname_excel_8_Dic:
                        assert Coachname_excel_8_Dic[key]==coachname
                    
                    
                    for key in AttributeofAllCoach_tablet_8_Dic:
                        assert AttributeofAllCoach_tablet_8_Dic[key][1]==coachname
                        assert AttributeofAllCoach_tablet_8_Dic[key][2]==Employeename_database_8_Dic[AttributeofAllCoach_tablet_8_Dic[key][0]]
                   
                    #Step9:Case for Coaching Name=TL1  Employee Name=Agent1   Type=select one form    Other option 'All'
                    '''9.Coaching Name=TL1 Employee Name=Agent1 Type=select one form    Other option 'All' '''
                    
                    coachname=TL1_Name
                    employeename=Agent1_Name
                    Typename='Skill Transfer'
                    Statusname='All'
                    #Step9.0:Delete coaching_export file
                    Deletefile.delete_coachfile(self.downloadpath)
                    #Step9.1:Get total_coachnumber from tablet
                    Total_coachnumber_tablet_9=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step9.2:Get total_coachnumber from excel
                    Total_coachnumber_excel_9=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                    Employeename_excel_9_Dic=GetCoachContent.Get_EmployeeName(self.filename_prefix, self.sheetname)
                    Coachname_excel_9_Dic=GetCoachContent.Get_CoachingName(self.filename_prefix, self.sheetname)
                    print Total_coachnumber_tablet_9
                    #Step9.3:#Get data from database
                    Agent1_hird=Agent1_Hrid
                    TL1_hird=TL1_Hird
                    type_id='7'
                    
                    sql_CNTL1_ENA1="select c.sn,a.firstname createrFirstN,a.lastname createrLastN,r.firstname EmployeeFirstN,r.lastname EmployeeLastN,c.`type`,c.`status`,c.created_time,c.completed_time,c.acknowledge_time from coach c join account a on c.assign_to_id=a.hr_id join roster r on c.history_id=r.history_id and c.hr_id=r.hr_id where c.hr_id="+Agent1_hird+" and c.assign_to_id="+TL1_hird+"  and type="+type_id+";"
                    #sql_CNTL1_ENA1_EmployeeName="select * from coach  c join roster r on c.history_id=r.history_id where c.hr_id="+Agent1_hird+" and c.assign_to_id="+TL1_hird+" and c.type="+type_id+" and r.hr_id="+Agent1_hird+" order by id desc;"
                    #sql_CNTL1_ENA1_CoachingName="select * from coach  c join roster r on c.history_id=r.history_id where c.hr_id="+Agent1_hird+" and c.assign_to_id="+TL1_hird+" and c.type="+type_id+" and r.hr_id="+TL1_hird+" order by id desc;"
                    Total_coachnumber_database_9=cursor.execute(sql_CNTL1_ENA1)
                    Employeename_database_9_Dic={}
                    Coachname_database_9_Dic={}
                    AttributeofAllCoach_tablet_9_Dic=self.Get_AnyattributeofAllCoach_tablet(Total_coachnumber_tablet_9)
                    
                    for row in cursor:#SN=row[10],Employeename=row[20]+row[21]
                        Employeename_database_9_Dic[row[0]]=row[3]+" "+row[4]
                        Coachname_database_9_Dic[row[0]]=row[1]+" "+row[2]
                    
                                 
                    print Total_coachnumber_database_9
                    #Step8.4:#assert all 
                    assert Total_coachnumber_tablet_9==Total_coachnumber_database_9
                    assert Total_coachnumber_excel_9==Total_coachnumber_database_9
                    for key in Employeename_database_9_Dic:
                        assert Employeename_database_9_Dic[key]==Employeename_excel_9_Dic[key]
                    for key in Coachname_database_9_Dic:
                        assert Coachname_database_9_Dic[key]==Coachname_excel_9_Dic[key]
                        
                    for key in AttributeofAllCoach_tablet_9_Dic:
                        assert AttributeofAllCoach_tablet_9_Dic[key][1]==Coachname_database_9_Dic[AttributeofAllCoach_tablet_9_Dic[key][0]]
                        assert AttributeofAllCoach_tablet_9_Dic[key][2]==Employeename_database_9_Dic[AttributeofAllCoach_tablet_9_Dic[key][0]]
                    
                     
                    
                       
                        
                    
    def Filter_combination(self,coachname, employeename, Typename, Statusname): 
        Cexport=CoachingExportPage()
        Cexport.select_CombinationConditions(coachname, employeename, Typename, Statusname)
        Cexport.click_Filter()
        Cexport.click_Export()
        #Step1.1:Get total_coachnumber from tablet
        Total_coachnumber_tablet=Cexport.get_Total_coachnumber()
        return Total_coachnumber_tablet
    
    def Get_AnyattributeofAllCoach_tablet(self,Total_coachnumber_tablet):#attrindex=1:SN,attrindex=2:CoachName,attrindex=3:EmployeeName
        Cexport=CoachingExportPage()
        Attribute_All_Coach_tablet_Dic={}
        if Total_coachnumber_tablet==0:
            Attribute_All_Coach_tablet_Dic={}
        elif Total_coachnumber_tablet<=20:
            pagenumber=1
            pageindex=0
            coachindex=Total_coachnumber_tablet
            Attribute_All_Coach_tablet_Dic=self.Get_AnyattributeofEachCoach_tablet(pageindex,coachindex)
        elif Total_coachnumber_tablet>20:
            if Total_coachnumber_tablet % 20==0:
                pagenumber=Total_coachnumber_tablet/20
                for pageindex in range(1,pagenumber+1):
                    Cexport.click_Pagenumber(pageindex+2)
                    dic_page=self.Get_AnyattributeofEachCoach_tablet(pageindex,20)
                    Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_page.items())
            else:
                pagenumber_int=Total_coachnumber_tablet/20
                pagenumber_total=pagenumber_int+1
                coachnumber_lastpage=Total_coachnumber_tablet%20
                for pageindex in range(1,pagenumber_int+1):
                    Cexport.click_Pagenumber(pageindex+2)
                    dic_page=self.Get_AnyattributeofEachCoach_tablet(pageindex,20)
                    Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_page.items())
                Cexport.click_Pagenumber(pagenumber_total+2)
                dic_lastpage=self.Get_AnyattributeofEachCoach_tablet(pagenumber_total,coachnumber_lastpage)
                Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_lastpage.items())
        
        return Attribute_All_Coach_tablet_Dic
                
            
    def Get_AnyattributeofEachCoach_tablet(self,pageindex,coachnumber):
        Cexport=CoachingExportPage()
        Coach_tablet_Dic={}
        print "coachnumber=",
        print coachnumber
        for coachindex in range(1,coachnumber+1):
            print coachindex
            SNofCoach_tablet=Cexport.get_anyCoach_attribute(coachindex, 1)
            CoachNameofCoach_tablet=Cexport.get_anyCoach_attribute(coachindex, 2)
            EmployeeNameofCoach_tablet=Cexport.get_anyCoach_attribute(coachindex, 3)
            Info_EachCoach_List=[SNofCoach_tablet,CoachNameofCoach_tablet,EmployeeNameofCoach_tablet]
            key=pageindex*20+(coachindex-1)
            Coach_tablet_Dic[key]=Info_EachCoach_List
        return Coach_tablet_Dic

    
    
 
             
                    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()