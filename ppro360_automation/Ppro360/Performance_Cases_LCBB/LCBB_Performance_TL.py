'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
#from public_method.Get_PerformanceData_Actual import Get_PerformanceData_Actual
from Performance_Cases_LCBB.Get_PerformanceData_Actual_LCBB import Get_PerformanceData_Actual_LCBB
from Performance_Cases_LCBB.Get_PerformanceData_Expected_LCBB import Get_PerformanceData_Expected_LCBB

from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest


class LCBB_Performance_TL(unittest.TestCase):


    def setUp(self):
        self.caseID="LCBB_Performance_TL"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #TL2's name
        ''' Name='Tl1 Test' '''
        self.TL_name='Tl1 Test'
        self.TL_userid='147573'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for LCBB
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        


    def tearDown(self):
        Gl.driver.quit() 


    def test_LCBB_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_LCBB()
        
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_LCBB()
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_LCBB_Goal_Expected(lineindex)
        
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
                    #L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    #THomepage.click_Myteaminfocircle()
                    #lineindex=Get_account.Get_lineindex(self.TL_userid)
                    #TL1_Info=Get_account.Get_MyTeamInfo(lineindex)
                    TL1_Info=Get_account.get_TLandAgentInfofromAdmin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.TL_userid)
                    TL1_name=TL1_Info['Name']
                    TL1_password=TL1_Info['Password']
                    #L.logout_tablet()
                    if TL1_name!=self.TL_name:
                        print "!!!!!!!!!!TL1 is not incorrect, please check it!!!!!!!!!"
                    else:
                        #Step0.1:All data has been ready manually
                        #Step0.3:Login with OM to do upload work
                        L.Login_tablet(self.tableturl, lobname, sitename, self.TL_userid, TL1_password)
                        Achiev_PerformanceCircle=THomepage.get_Achiev_performancecircle()
                        THomepage.click_performancecircle()
                        Achiev_TEAM_Monthly=GetPData_Actual.get_LCBB_TEAM_Data_()['Achiev'][0]
                        print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                        print Achiev_PerformanceCircle
                        print Achiev_TEAM_Monthly
                        assert Achiev_PerformanceCircle==Achiev_TEAM_Monthly
                        
                        for ywm in range(0,len(self.tablist)):
                            Ppage.click_timetab_performance(ywm+1)
                            
                            print "*********************Start********************",
                            print self.tablist[ywm],
                            print "is in testing:"
                            time.sleep(Gl.waittime)
                            #Step1:Verify Goal
                            print "=================1.Verify Each KPI of Goal=============="
                            Actual_GoalDic=GetPData_Actual.get_LCBB_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                            assert Expected_GoalDic["AHT"]==Actual_GoalDic["AHT"]
                            assert Expected_GoalDic["HoldTime"]==Actual_GoalDic["HoldTime"]
                            assert Expected_GoalDic["ACW"]==Actual_GoalDic["ACW"]
                            assert Expected_GoalDic["Transfers"]==Actual_GoalDic["Transfers"]
                            assert Expected_GoalDic["VOC"]==Actual_GoalDic["VOC"]
                            assert Expected_GoalDic["SOAR"]==Actual_GoalDic["SOAR"]
                            #assert Expected_GoalDic['Achiev']==Actual_GoalDic["Achiev"]
                            
                            '''Prepare Data for the following test '''
                            if self.tablist[ywm]=="LastTwoMonth":
                                Expected_KPIofSITEDic=GetPData_Expected.get_LCBB_Performance_Data_Expected(137)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_LCBB_Performance_Data_Expected(135)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(131, 134)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_LCBB_Performance_Data_Expected(131)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_LCBB_Performance_Data_Expected(134)#For Step6
                                
                            elif self.tablist[ywm]=="LastMonth":
                                Expected_KPIofSITEDic=GetPData_Expected.get_LCBB_Performance_Data_Expected(124)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_LCBB_Performance_Data_Expected(118)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(107, 117)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_LCBB_Performance_Data_Expected(114)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_LCBB_Performance_Data_Expected(117)#For Step6
                            elif self.tablist[ywm]=="Yesterday":
                                Expected_KPIofSITEDic=GetPData_Expected.get_LCBB_Performance_Data_Expected(25)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_LCBB_Performance_Data_Expected(16)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(5, 15)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_LCBB_Performance_Data_Expected(12)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_LCBB_Performance_Data_Expected(15)#For Step6
                            elif self.tablist[ywm]== "Week-to-Date":
                                Expected_KPIofSITEDic=GetPData_Expected.get_LCBB_Performance_Data_Expected(77)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_LCBB_Performance_Data_Expected(71)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(60, 70)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_LCBB_Performance_Data_Expected(67)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_LCBB_Performance_Data_Expected(70)#For Step6
                            elif self.tablist[ywm]=="Month-to-Date":
                                Expected_KPIofSITEDic=GetPData_Expected.get_LCBB_Performance_Data_Expected(99)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_LCBB_Performance_Data_Expected(93)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(82, 92)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_LCBB_Performance_Data_Expected(89)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_LCBB_Performance_Data_Expected(92)#For Step6
                            
                            #Step2:Verify KPI of SITES
                            print "=================2.Verify Each KPI of site, color, achievement=============="
                            '''Expected_KPIofSITEDic is from above.'''
                            print Expected_KPIofSITEDic
                            #Step2.2:Get the Actual KPI of site
                            '''Actual_KPIofSITEDic is from blow.''' 
                            Actual_KPIofSITEDic=GetPData_Actual.get_LCBB_SITE_Data_()
                            print Actual_KPIofSITEDic
                            #Step2.3:assert Expected==Actual
                            assert Expected_KPIofSITEDic["AHT"][0]==Actual_KPIofSITEDic["AHT"][0]#0 is KPI value
                            assert Expected_KPIofSITEDic["AHT"][1]==Actual_KPIofSITEDic["AHT"][1]#1 is KPI status
                            assert Expected_KPIofSITEDic["HoldTime"][0]==Actual_KPIofSITEDic["HoldTime"][0]#0 is KPI value
                            assert Expected_KPIofSITEDic["HoldTime"][1]==Actual_KPIofSITEDic["HoldTime"][1]#1 is KPI status
                            assert Expected_KPIofSITEDic["ACW"][0]==Actual_KPIofSITEDic["ACW"][0]#0 is KPI value
                            assert Expected_KPIofSITEDic["ACW"][1]==Actual_KPIofSITEDic["ACW"][1]#1 is KPI status
                            assert Expected_KPIofSITEDic["Transfers"][0]==Actual_KPIofSITEDic["Transfers"][0]#0 is KPI value
                            assert Expected_KPIofSITEDic["Transfers"][1]==Actual_KPIofSITEDic["Transfers"][1]#1 is KPI status
                            assert Expected_KPIofSITEDic["VOC"][0]==Actual_KPIofSITEDic["VOC"][0]#0 is KPI value
                            assert Expected_KPIofSITEDic["VOC"][1]==Actual_KPIofSITEDic["VOC"][1]#1 is KPI status
                            assert Expected_KPIofSITEDic["SOAR"][0]==Actual_KPIofSITEDic["SOAR"][0]#0 is KPI value
                            assert Expected_KPIofSITEDic["SOAR"][1]==Actual_KPIofSITEDic["SOAR"][1]#1 is KPI status
                            assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value
                            ''' Achiev has no KPI sort '''
                            
                            
                            #Step3:Verify achievement of Tl1
                            print "=================3.Verify TEAM (TL2's) KPI.=============="
                            #Step3.1:Get the Expected achievement of Tl1
                            '''Expected_KPIofTl2 is from above, and  Expected_Achi_Tl2 is from below'''
                            print Expected_KPIofTl1
                            #Step3.2:Get the Actual achievement of Tl2(TEAM)
                            Actual_KPIofTl1=GetPData_Actual.get_LCBB_TEAM_Data_()
                            print Actual_KPIofTl1
                            
                            #Step3.3:assert Expected==Actual
                            assert Expected_KPIofTl1["AHT"][0]==Actual_KPIofTl1["AHT"][0]#0 is KPI value
                            assert Expected_KPIofTl1["AHT"][1]==Actual_KPIofTl1["AHT"][1]#1 is KPI status
                            assert Expected_KPIofTl1["HoldTime"][0]==Actual_KPIofTl1["HoldTime"][0]#0 is KPI value
                            assert Expected_KPIofTl1["HoldTime"][1]==Actual_KPIofTl1["HoldTime"][1]#1 is KPI status
                            assert Expected_KPIofTl1["ACW"][0]==Actual_KPIofTl1["ACW"][0]#0 is KPI value
                            assert Expected_KPIofTl1["ACW"][1]==Actual_KPIofTl1["ACW"][1]#1 is KPI status
                            assert Expected_KPIofTl1["Transfers"][0]==Actual_KPIofTl1["Transfers"][0]#0 is KPI value
                            assert Expected_KPIofTl1["Transfers"][1]==Actual_KPIofTl1["Transfers"][1]#1 is KPI status
                            assert Expected_KPIofTl1["VOC"][0]==Actual_KPIofTl1["VOC"][0]#0 is KPI value
                            assert Expected_KPIofTl1["VOC"][1]==Actual_KPIofTl1["VOC"][1]#1 is KPI status
                            assert Expected_KPIofTl1["SOAR"][0]==Actual_KPIofTl1["SOAR"][0]#0 is KPI value
                            assert Expected_KPIofTl1["SOAR"][1]==Actual_KPIofTl1["SOAR"][1]#1 is KPI status
                            assert Expected_KPIofTl1["Achiev"][0]==Actual_KPIofTl1["Achiev"][0]#0 is KPI value

                            
                            #Step4:Verify achievement of all Tl1's Agents 
                            print "=================4.Verify only show all Agents of TL1=============="                       
                            #Step4.1:Get the Expected achievement of all Tl1's Agents
                            print "=================4.Expected all Agents of TL1==============" 
                            print Expected_AllAgentName_List
                           
                            #Step4.2:Get the Actual achievement of all Tl1's Agents
                            print "=================4.Actual all Agents of TL1=============="
                            
                            flag=True
                            Agentindex=1
                            Actual_AllAgentName_List=[]
                            Actual_AgentKPI={}
                            while flag==True:
                                Agent_Name=Ppage.get_anyKPIofAgent_TL(Agentindex, 1)[0]
                                Actual_AllAgentName_List.append(Agent_Name)
                                Agent_KPI=GetPData_Actual.get_LCBB_AgentKPI_TL_Actual(Agentindex)
                                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
                                Agentindex=Agentindex+1
                                flag=Ppage.Agent_line_exist_TL(Agentindex)
                            print Actual_AllAgentName_List
                            
                            #Step4.3:assert Expected==Actual
                            assert len(Expected_AllAgentName_List)==len(Actual_AllAgentName_List)
                            for i in range(0,len(Expected_AllAgentName_List)):
                                assert Expected_AllAgentName_List[i] in Actual_AllAgentName_List
                                
                            #Step5:Verify Agent8:check each KPI value, color.
                            print "=================5.Verify Agent8:check each KPI value, color==============" 
                            #Step5.1:Get the Expected KPI value and color for Agent8
                            print "=================5.1 Expected KPI value and color of Agent8=============="
                            print Expected_KPIofAgent8
                            #Step5.2:Get the Actual KPI and color for Agent8
                            print "=================5.2 Actual KPI value and color of Agent8=============="
                            Actual_KPIofAgent8=Actual_AgentKPI['Agent 8']
                            print Actual_KPIofAgent8
                            assert Expected_KPIofAgent8["AHT"][0]==Actual_KPIofAgent8["AHT"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["AHT"][1]==Actual_KPIofAgent8["AHT"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["HoldTime"][0]==Actual_KPIofAgent8["HoldTime"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["HoldTime"][1]==Actual_KPIofAgent8["HoldTime"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["ACW"][0]==Actual_KPIofAgent8["ACW"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["ACW"][1]==Actual_KPIofAgent8["ACW"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["Transfers"][0]==Actual_KPIofAgent8["Transfers"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["Transfers"][1]==Actual_KPIofAgent8["Transfers"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["VOC"][0]==Actual_KPIofAgent8["VOC"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["VOC"][1]==Actual_KPIofAgent8["VOC"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["SOAR"][0]==Actual_KPIofAgent8["SOAR"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["SOAR"][1]==Actual_KPIofAgent8["SOAR"][1]#1 is KPI status
    
    
                            
                            
                            #Step6:Verify Agent11:check each KPI value, color.
                            print "=================6.Verify Agent11:check each KPI value, color=============="
                            #Step6.1:Get the Expected KPI value and color for Agent8
                            print "=================6.1 Expected KPI value and color of Agent11=============="
                            print Expected_KPIofAgent11
                            #Step6.2:Get the Actual KPI and color for Agent8
                            print "=================6.2 Actual KPI value and color of Agent11=============="
                            Actual_KPIofAgent11=Actual_AgentKPI['Agent 11']
                            print Actual_KPIofAgent11
                            assert Expected_KPIofAgent11["AHT"][0]==Actual_KPIofAgent11["AHT"][0]#0 is KPI value
                            assert Expected_KPIofAgent11["AHT"][1]==Actual_KPIofAgent11["AHT"][1]#1 is KPI status
                            assert Expected_KPIofAgent11["HoldTime"][0]==Actual_KPIofAgent11["HoldTime"][0]#0 is KPI value
                            assert Expected_KPIofAgent11["HoldTime"][1]==Actual_KPIofAgent11["HoldTime"][1]#1 is KPI status
                            assert Expected_KPIofAgent11["ACW"][0]==Actual_KPIofAgent11["ACW"][0]#0 is KPI value
                            assert Expected_KPIofAgent11["ACW"][1]==Actual_KPIofAgent11["ACW"][1]#1 is KPI status
                            assert Expected_KPIofAgent11["Transfers"][0]==Actual_KPIofAgent11["Transfers"][0]#0 is KPI value
                            assert Expected_KPIofAgent11["Transfers"][1]==Actual_KPIofAgent11["Transfers"][1]#1 is KPI status
                            assert Expected_KPIofAgent11["VOC"][0]==Actual_KPIofAgent11["VOC"][0]#0 is KPI value
                            assert Expected_KPIofAgent11["VOC"][1]==Actual_KPIofAgent11["VOC"][1]#1 is KPI status
                            assert Expected_KPIofAgent11["SOAR"][0]==Actual_KPIofAgent11["SOAR"][0]#0 is KPI value
                            assert Expected_KPIofAgent11["SOAR"][1]==Actual_KPIofAgent11["SOAR"][1]#1 is KPI status

                        L.logout_tablet()    
                                

                               


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()