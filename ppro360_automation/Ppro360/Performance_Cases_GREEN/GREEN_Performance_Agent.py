'''
Created on 2017.10.13

@author: yalan.yin
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Performance_Cases_GREEN.Get_PerformanceData_Expected_GREEN import Get_PerformanceData_Expected_GREEN
from Performance_Cases_GREEN.Get_PerformanceData_Actual_GREEN import Get_PerformanceData_Actual_GREEN

class GREEN_Performance_Agent(unittest.TestCase):


    def setUp(self):
        self.caseID="GREEN_Performance_Agent"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #TL2's name
        ''' Name='Tl2 Test' '''
        self.TL_name='Tl2 Test'
        self.TL_userid='147879'
        #Agent14's name
        ''' Name='Agent 11' '''
        self.Agent_name='Agent 14'
        self.Agent_userid='148194'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for GREEN
        self.tablist=Gl.Less_timetab #["Month-to-Day","LastMonth", "LastTwoMonth"]
        


    def tearDown(self):
        #Gl.driver.quit() 
        pass


    def test_GREEN_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_GREEN()
        
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_GREEN()
        lineindex=2#The goal is in the row 3 of excel file,so lineindex is 2
        Expected_GoalDic=GetPData_Expected.get_GREEN_Goal_Expected(lineindex)
        
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
                    
                    #Get TL2's account
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    THomepage.click_Myteaminfocircle()
                    lineindex=Get_account.Get_lineindex(self.TL_userid)
                    TL2_Info=Get_account.Get_MyTeamInfo(lineindex)
                    TL2_name=TL2_Info['Name']
                    TL2_password=TL2_Info['Password']
                    L.logout_tablet()
                    if TL2_name!=self.TL_name:
                        print "!!!!!!!!!!TL2 is not incorrect, please check it!!!!!!!!!"
                    else:
                        #Agent14's user id and password
                        L.Login_tablet(self.tableturl, lobname, sitename, self.TL_userid, TL2_password)
                        THomepage.click_TL_Myteaminfocircle()
                        lineindex=Get_account.Get_lineindex(self.Agent_userid)
                        Agent14_Info=Get_account.Get_MyTeamInfo(lineindex)
                        Agent14_name=Agent14_Info['Name']
                        Agent14_password=Agent14_Info['Password']
                        L.logout_tablet()
                        if Agent14_name!=self.Agent_name:
                            print "!!!!!!!!!!Agent14 is not incorrect, please check it!!!!!!!!!"
                        else:
        
                            #Step0.1:All data has been ready manually
                            #Step0.3:Login with OM to do upload work
                            L.Login_tablet(self.tableturl, lobname, sitename, self.Agent_userid, Agent14_password)
                            Achiev_PerformanceCircle=THomepage.get_Achiev_performancecircle()
                            THomepage.click_performancecircle()
                            Achiev_TEAM_Monthly=GetPData_Actual.get_GREEN_TEAM_Data_()['Achiev'][0]
                            print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                            assert Achiev_PerformanceCircle==Achiev_TEAM_Monthly
                            
                            for ywm in range(2,len(self.tablist)):
                                Ppage.click_timetab_performance(ywm+1)
                                '''
                                if self.tablist[ywm]=="yesterday":
                                    Ppage.click_ytd()
                                elif self.tablist[ywm]== "Week-to-Day":
                                    Ppage.click_wtd()
                                elif self.tablist[ywm]=="Month-to-Day":
                                    Ppage.click_mtd()'''
                                
                                print "*********************Start********************",
                                print self.tablist[ywm],
                                print "is in testing:"
                                time.sleep(Gl.waittime)
                                #Step1:Verify Goal
                                print "=================1.Verify Each KPI of Goal=============="
                                Actual_GoalDic=GetPData_Actual.get_GREEN_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                                assert Expected_GoalDic["AHT"]==Actual_GoalDic["AHT"]
                                assert Expected_GoalDic["Revenue"]==Actual_GoalDic["Revenue"]
                                assert Expected_GoalDic["Video"]==Actual_GoalDic["Video"]
                                assert Expected_GoalDic["Broadband"]==Actual_GoalDic["Broadband"]
                                assert Expected_GoalDic["VOC"]==Actual_GoalDic["VOC"]
                                assert Expected_GoalDic["VOIP"]==Actual_GoalDic["VOIP"]
                                assert Expected_GoalDic["BARAttainment"]==Actual_GoalDic["BARAttainment"]
                                assert Expected_GoalDic["Wireless"]==Actual_GoalDic["Wireless"]
                                #assert Expected_GoalDic['Achiev']==Actual_GoalDic["Achiev"]
                                
                                '''Prepare Data for the following test '''
                                if self.tablist[ywm]=="Month-to-Date": #data3
                                    Expected_KPIofSITEDic=GetPData_Expected.get_GREEN_Performance_Data_Expected(47)#For Step2
                                    #Expected_KPIofTl2=GetPData_Expected.get_GREEN_Performance_Data_Expected(98)#For Step3
                                    #Expected_KPIofAgent14=GetPData_Expected.get_GREEN_Performance_Data_Expected(97)#For Step4
                                elif self.tablist[ywm]=="LastMonth": #data1
                                    Expected_KPIofSITEDic=GetPData_Expected.get_GREEN_Performance_Data_Expected(23)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_GREEN_Performance_Data_Expected(22)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_GREEN_Performance_Data_Expected(21)#For Step4
                                elif self.tablist[ywm]=="LastTwoMonth": #data2
                                    Expected_KPIofSITEDic=GetPData_Expected.get_GREEN_Performance_Data_Expected(35)#For Step2
                                    #Expected_KPIofTl2=GetPData_Expected.get_GREEN_Performance_Data_Expected(0)#For Step3
                                    #Expected_KPIofAgent14=GetPData_Expected.get_GREEN_Performance_Data_Expected(0)#For Step4
                                
                                #Step2:Verify KPI of SITES
                                print "=================2.Verify Each KPI of site, color, achievement=============="
                                '''Expected_KPIofSITEDic is from above.'''
                                #Step2.2:Get the Actual KPI of site
                                '''Actual_KPIofSITEDic is from blow.''' 
                                Actual_KPIofSITEDic=GetPData_Actual.get_GREEN_SITE_Data_()
                                print 'Actual_KPIofSITEDic:',Actual_KPIofSITEDic
                                print 'Expected_KPIofSITEDic:',Expected_KPIofSITEDic
                                #Step2.3:assert Expected==Actual
                                assert Expected_KPIofSITEDic["AHT"][0]==Actual_KPIofSITEDic["AHT"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["AHT"][1]==Actual_KPIofSITEDic["AHT"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Revenue"][0]==Actual_KPIofSITEDic["Revenue"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["Revenue"][1]==Actual_KPIofSITEDic["Revenue"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Video"][0]==Actual_KPIofSITEDic["Video"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["Video"][1]==Actual_KPIofSITEDic["Video"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Wireless"][0]==Actual_KPIofSITEDic["Wireless"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["Wireless"][1]==Actual_KPIofSITEDic["Wireless"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["VOC"][0]==Actual_KPIofSITEDic["VOC"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["VOC"][1]==Actual_KPIofSITEDic["VOC"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["VOIP"][0]==Actual_KPIofSITEDic["VOIP"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["VOIP"][1]==Actual_KPIofSITEDic["VOIP"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["BARAttainment"][0]==Actual_KPIofSITEDic["BARAttainment"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["BARAttainment"][1]==Actual_KPIofSITEDic["BARAttainment"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Broadband"][0]==Actual_KPIofSITEDic["Broadband"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["Broadband"][1]==Actual_KPIofSITEDic["Broadband"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value
                                ''' Achiev has no KPI sort '''
                                
                                if self.tablist[ywm]=='LastMonth':
                                    #Step3:Verify achievement of Tl1
                                    print "=================3.Verify TEAM (TL2's) KPI.=============="
                                    #Step3.1:Get the Expected achievement of Tl1
                                    '''Expected_KPIofTl2 is from above, and  Expected_Achi_Tl2 is from below'''
                                    print 'Expected_KPIofTl2:',Expected_KPIofTl2
                                    #Step3.2:Get the Actual achievement of Tl2(TEAM)
                                    Actual_KPIofTl2=GetPData_Actual.get_GREEN_TEAM_Data_()
                                    print 'Actual_KPIofTl2:',Actual_KPIofTl2
                                
                                #Step3.3:assert Expected==Actual
                                
                                    print Expected_KPIofTl2['AHT']
                                    print Actual_KPIofTl2['AHT']
                                    assert Expected_KPIofTl2["AHT"][0]==Actual_KPIofTl2["AHT"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["AHT"][1]==Actual_KPIofTl2["AHT"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Revenue"][0]==Actual_KPIofTl2["Revenue"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["Revenue"][1]==Actual_KPIofTl2["Revenue"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Wireless"][0]==Actual_KPIofTl2["Wireless"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["Wireless"][1]==Actual_KPIofTl2["Wireless"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["VOIP"][0]==Actual_KPIofTl2["VOIP"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["VOIP"][1]==Actual_KPIofTl2["VOIP"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["VOC"][0]==Actual_KPIofTl2["VOC"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["VOC"][1]==Actual_KPIofTl2["VOC"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Broadband"][0]==Actual_KPIofTl2["Broadband"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["Broadband"][1]==Actual_KPIofTl2["Broadband"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["BARAttainment"][0]==Actual_KPIofTl2["BARAttainment"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["BARAttainment"][1]==Actual_KPIofTl2["BARAttainment"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Video"][0]==Actual_KPIofTl2["Video"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["Video"][1]==Actual_KPIofTl2["Video"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Achiev"][0]==Actual_KPIofTl2["Achiev"][0]#0 is KPI value

                                    
                                    #Step4:Verify achievement of all Tl2's Agents 
                                    print "=================4.Verify Agent14's all KPIs=============="                       
                                    #Step4.1:Get the Expected achievement of all Tl1's Agents
                                    print "=================4.Expected Agent14's all KPIs==============" 
                                    print Expected_KPIofAgent14
                                   
                                    #Step4.2:Get the Actual achievement of all Tl2's Agents
                                    print "=================4.Actual Agent14's all KPIs=============="
                                    Actual_KPIofAgent14=GetPData_Actual.get_GREEN_AgentKPI_Agent_Actual()
                                    print Actual_KPIofAgent14
                                    
                                    #Step4.3:assert Expected==Actual
                                
                                    assert Expected_KPIofAgent14["AHT"][0]==Actual_KPIofAgent14["AHT"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["AHT"][1]==Actual_KPIofAgent14["AHT"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Revenue"][0]==Actual_KPIofAgent14["Revenue"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["Revenue"][1]==Actual_KPIofAgent14["Revenue"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Broadband"][0]==Actual_KPIofAgent14["Broadband"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["Broadband"][1]==Actual_KPIofAgent14["Broadband"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Wireless"][0]==Actual_KPIofAgent14["Wireless"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["Wireless"][1]==Actual_KPIofAgent14["Wireless"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["VOC"][0]==Actual_KPIofAgent14["VOC"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["VOC"][1]==Actual_KPIofAgent14["VOC"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["VOIP"][0]==Actual_KPIofAgent14["VOIP"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["VOIP"][1]==Actual_KPIofAgent14["VOIP"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["BARAttainment"][0]==Actual_KPIofAgent14["BARAttainment"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["BARAttainment"][1]==Actual_KPIofAgent14["BARAttainment"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Video"][0]==Actual_KPIofAgent14["Video"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["Video"][1]==Actual_KPIofAgent14["Video"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Achiev"][0]==Actual_KPIofAgent14["Achiev"][0]#0 is KPI value


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()