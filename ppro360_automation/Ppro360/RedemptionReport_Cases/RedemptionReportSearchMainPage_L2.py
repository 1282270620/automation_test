'''
Created on 2018.8.3

@author: haodong.liu
'''

import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.RedemptionReport_Page import RedemptionReport_Page
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.DatePicker_Method import DatePicker_Method
from Tablet_pages.TabletHomepage import TabletHomepage

class RedemptionReportSearchMainPage_L2(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="RedemptionReportSearchMainPage_L2"
        
        GetData=Get_configration_data()
#         #Get URL 
#         self.tableturl=GetData.get_TabletUrl()
#         self.Adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.role = "L2"
#         L2account=GetData.get_L2account()
#         L2userid=L2account["L2userid"]
#         L2password=L2account["L2password"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
       
        self.CurrentDate=GetData.get_ServerCurrentDate()
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #Reward Database info
        self.RewardUserName=GetData.get_RewardDatabaseUser()
        self.RewardPassword=GetData.get_RewardDatabasePassword()
        
    def test_RedemptionReportSearchMainPage_L2(self):
        GetConfig=Get_configration_data()
        DatePicker=DatePicker_Method()
        RedemptionReportPage=RedemptionReport_Page()
        THPage = TabletHomepage()
        Get_TLinfo = Get_AllRoleAccountForTest()
        
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                
                tableturl=GetConfig.get_Test_Tablet(lobname)
                adminurl=GetConfig.get_Test_AdminUrl(lobname)
                hostindex=GetConfig.get_Test_Hostindex(lobname)
                print hostindex
                Rewardhostindex=GetConfig.get_Test_RewardHostindex(lobname)
                print Rewardhostindex

                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                    #get TL info and login tablet
                    L2info = Get_TLinfo.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.role)
                    L2userid = L2info['Hrid']
                    L2password = L2info["Password"]
                    
                    DB_LOBSitename = GetConfig.get_LobSiteDBName(lobname,sitename)
                    db_lobname = DB_LOBSitename["lobname_database"]
                    db_sitename = DB_LOBSitename["sitename_database"]
                        
                    #Login tablet,and Get HRID using for testing
                    L=Login()
                    L.Login_tablet(tableturl,lobname,sitename,L2userid,L2password)
                    #RedemptionReportPage.Click_RedemptionModules()
                    THPage.click_RedemptionReportcircle()
                    print RedemptionReportPage.GetDataNumber()
                    assert RedemptionReportPage.GetDataNumber()==0
                    
                    #Check defalutValues
                    DefalutTitleInfo=['TL Name','TL ID','Employee Name','HR ID','Redeem Date','Description','Redeem Points']
                    assert RedemptionReportPage.get_TLNameDefaultValue()=='All'
                    RedemptionReportPage.Click_TLNameDropDown()
                    ALLTLNameWithPage=RedemptionReportPage.get_all_TLName()
                    #print ALLTLName
                    RedemptionReportPage.Click_TLNameDropDown()
                    assert RedemptionReportPage.get_DatefaultValue(1)==''
                    assert RedemptionReportPage.get_DatefaultValue(2)==''
                    assert RedemptionReportPage.get_FilterButtonDatafaultStutus()=='true'
                    assert RedemptionReportPage.get_ExportButtonDatafaultStutus()=='true'
                    for t in range(0,len(DefalutTitleInfo)):
                        assert RedemptionReportPage.get_TiltleInfo(t+1)==DefalutTitleInfo[t]
                    
                    
                    #GET TL name from ppro database
                    RedemptionReportPage.Click_TLNameDropDown()
                    sql_TL='select ml1.hr_id tl_hr_id, ml1.firstname tl_first_name,ml1.lastname tl_last_name, \
                    r.team_id as rt_teamID,r.hr_id as agentHRID,r.firstname as agentFirstName,r.lastname as agentLastName \
                    from manager ml2 join manager ml1 on ml1.history_id=ml2.history_id and ml1.parent_id=ml2.id \
                    left join roster r on r.history_id=ml1.history_id and ml1.hr_id=r.hr_id where ml2.hr_id='+L2userid+' and  \
                    ml2.history_id=(SELECT id FROM upload_history uh WHERE TYPE="2" AND uh.active_time=( \
                    SELECT MAX(active_time)FROM upload_history WHERE TYPE="2" AND DATE(data_date)<=NOW()))'

                    
                    ALLTLNameWithDB=RedemptionReportPage.Get_AllTLName_withDB(hostindex, db_lobname, db_sitename, self.dbuser, self.dbpassword, sql_TL)
                    print ALLTLNameWithDB
                    print ALLTLNameWithPage
                    assert ALLTLNameWithDB==ALLTLNameWithPage
                    #ALLTLhridWithDB=RedemptionReportPage.Get_AllTLHRID_withDB(hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_TL)
                    
                    #Select TL and DateTime Filter
                    SlectTLHRID=RedemptionReportPage.Get_selectTLhrid(2)
                    SelectTLName=RedemptionReportPage.Get_selectTLName(2)
                    RedemptionReportPage.Select_TL(2)
                    RedemptionReportPage.Click_DateButton(1)
                    
                    #Filter one a month date
                    Monthindex=1
                    OneMonthAgo_Date=GetConfig.get_TheDateOfLastAnyMonth(Monthindex, "Local")
                    for i in range(0,Monthindex):
                        time.sleep(5)
                        RedemptionReportPage.Click_Arrow_path(1,1)
                    Month_need1=OneMonthAgo_Date[5:7]
                    Date_need1=OneMonthAgo_Date[8:10]
                    Current_location_list1=DatePicker.get_DateLocation("Redeem Date", 1, Date_need1, Month_need1)
                    RedemptionReportPage.Slect_Date(1, Current_location_list1[0], Current_location_list1[1])
                    
                    RedemptionReportPage.Click_DateButton(2)
                    Current_Date=GetConfig.get_LocalCurrentTime()                        
                    #Check Created Date picker and Filter
                    Month_need=Current_Date[5:7]
                    Date_need=Current_Date[8:10]
                    Current_location_list2=DatePicker.get_DateLocation("Redeem Date", 2, Date_need, Month_need)
                    RedemptionReportPage.Slect_Date(2, Current_location_list2[0], Current_location_list2[1])
                    RedemptionReportPage.Click_FilterButton()
                    if RedemptionReportPage.GetDataNumber()!=0:
                    
                        time.sleep(1)
                        RedemptionReportPage.Click_ExportButton()
                        
                        #Get all agents under the TL From ppro database
                        AllAgentHRID=[]
                        sql_Agent='SELECT rt.team_id as rt_teamID,r.hr_id as agentHRID,rag.firstname as agentFirstName,rag.lastname as agentLastName \
                        FROM roster_teamleaders rt \
                        JOIN roster rtl ON rt.history_id = rtl.history_id AND rt.hr_id = rtl.hr_id \
                        LEFT JOIN roster r ON rt.history_id=r.history_id AND rt.team_id=r.team_id \
                        JOIN roster rag ON r.history_id = rag.history_id AND r.hr_id = rag.hr_id \
                        WHERE rt.hr_id=\''+SlectTLHRID+'\' and rt.history_id=( \
                        SELECT id \
                        FROM upload_history uh \
                        WHERE TYPE='+'2'+' AND uh.active_time=( \
                        SELECT MAX(active_time) \
                        FROM upload_history \
                        WHERE TYPE='+'2'+' AND DATE(data_date)<=NOW())) and rt.hr_id<>r.hr_id;'
                        AgentHridWithdb=RedemptionReportPage.Get_AllAgentHrid_withDB(hostindex, db_lobname, db_sitename, self.dbuser, self.dbpassword, sql_Agent)
                        AllAgentHRID.append(AgentHridWithdb)
                        
                        #Get all Reward Info for all agent
                        ALLRewardInfoWithDB=[]
                        for m in range(0,len(AgentHridWithdb)):
                            Redeem_sql='select lob, site, hr_id, created_time, description, point from point_transaction \
                            where lob=\''+db_lobname+'\' and site=\''+db_sitename+'\' and type=1 \
                            and hr_id in (\''+AgentHridWithdb[m]+'\')  \
                            and (left(created_time,10) between \''+OneMonthAgo_Date+'\' and NOW());'
                            Info=RedemptionReportPage.Get_RedeemInfoWithDB(Rewardhostindex, db_lobname, db_sitename,self.RewardUserName, self.RewardPassword, Redeem_sql)
                            ALLRewardInfoWithDB.append(Info)  
                        
                        #Page data Compare with database data 
                        EndCompareList1=[]
                        for n in range(0,len(ALLRewardInfoWithDB)):
                            if len(ALLRewardInfoWithDB[n])>0:
                                EndCompareList1.append(ALLRewardInfoWithDB[n])
                            else:
                                continue
                        print 'EndCompareList1-------------------------------------------'
                        print EndCompareList1
                        EndCompareList2=[]
                        if  len(EndCompareList1)==1:
                            for v1 in range(0,len(EndCompareList1[0])):
                                EndCompareList2.append(EndCompareList1[0][v1])
                        else:
                            for v2 in range(0,len(EndCompareList1)):
                                if len(EndCompareList1[v2])==1:
                                    EndCompareList2.append(EndCompareList1[v2][0])
                                else:
                                    for v22 in range(0,len(EndCompareList1[v2])):
                                        EndCompareList2.append(EndCompareList1[v2][v22])
                        print 'EndCompareList2---------------------------------'
                        print EndCompareList2
                          
                        CompareData=[]
                        for j in range(0,len(EndCompareList2)):
                            Datalist=[]
                            Datalist.append(EndCompareList2[j][2])
                            Datalist.append(EndCompareList2[j][3].strftime("%Y-%m-%d"))
                            Datalist.append(EndCompareList2[j][4])
                            Datalist.append(EndCompareList2[j][5])
                            CompareData.append(Datalist)
                        print CompareData
                          
                        DataNumberWithPage=RedemptionReportPage.GetDataNumber()
                        for i in range(1,DataNumberWithPage+1):
                            assert RedemptionReportPage.get_FilterInfo(i,1)==SelectTLName
                            assert RedemptionReportPage.get_FilterInfo(i,2)==SlectTLHRID
                            assert RedemptionReportPage.get_FilterInfo(i, 4)==CompareData[i-1][0]
                            assert RedemptionReportPage.get_FilterInfo(i, 5)==CompareData[i-1][1]
                            assert RedemptionReportPage.get_FilterInfo(i,6)==CompareData[i-1][2]
                            assert str(RedemptionReportPage.get_FilterInfo(i,7))==str(CompareData[i-1][3])
                    else:
                        assert RedemptionReportPage.get_ExportButtonDatafaultStutus()=='true'
                        
                    GetConfig.print_EndTest_message(lobname, sitename)


    def tearDown(self):
        Gl.driver.quit()                
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()   

