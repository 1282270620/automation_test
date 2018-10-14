'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
#from public_method.Get_PerformanceData_Actual import Get_PerformanceData_Actual
from Performance_Cases_UBIZICM.Get_PerformanceData_Actual_UBIZICM import Get_PerformanceData_Actual_UBIZICM
from Performance_Cases_UBIZICM.Get_PerformanceData_Expected_UBIZICM import Get_PerformanceData_Expected_UBIZICM
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest


class UBIZICM_Performance_Agent(unittest.TestCase):


    def setUp(self):
        self.caseID="UBIZICM_Performance_Agent"
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
        self.TL_userid='17555'
        #Agent14's name
        ''' Name='Agent 14' '''
        self.Agent_name='Agent 14'
        self.Agent_userid='240017'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for UBIZICM
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]
        


    def tearDown(self):
        Gl.driver.quit() 


    def test_UBIZICM_Performance_Agent(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_UBIZICM()
        
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_UBIZICM()
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_UBIZICM_Goal_Expected(lineindex)
        
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
                            Achiev_TEAM_Monthly=GetPData_Actual.get_UBIZICM_TEAM_Data_()['Achiev'][0]
                            print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                            assert Achiev_PerformanceCircle==Achiev_TEAM_Monthly
                            
                            for ywm in range(0,len(self.tablist)):
                                Ppage.click_timetab_performance(ywm+1)
                                
                                print "*********************Start********************",
                                print self.tablist[ywm],
                                print "is in testing:"
                                time.sleep(Gl.waittime)
                                #Step1:Verify Goal
                                print "=================1.Verify Each KPI of Goal=============="
                                Actual_GoalDic=GetPData_Actual.get_UBIZICM_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                                assert Expected_GoalDic["AvgHoldTime"]==Actual_GoalDic["AvgHoldTime"]
                                assert Expected_GoalDic["IBAHT"]==Actual_GoalDic["IBAHT"]
                                assert Expected_GoalDic["CaseTocall"]==Actual_GoalDic["CaseTocall"]
                                assert Expected_GoalDic["Misdirects"]==Actual_GoalDic["Misdirects"]
                                assert Expected_GoalDic["Ghosts"]==Actual_GoalDic["Ghosts"]
                                assert Expected_GoalDic["SwitchTransfer"]==Actual_GoalDic["SwitchTransfer"]
                                assert Expected_GoalDic["DailyRepeatRate"]==Actual_GoalDic["DailyRepeatRate"]
                                assert Expected_GoalDic["DispatchRateByCTV"]==Actual_GoalDic["DispatchRateByCTV"]
                                assert Expected_GoalDic["WFEComplianceRate"]==Actual_GoalDic["WFEComplianceRate"]
                                assert Expected_GoalDic["R3AllIn"]==Actual_GoalDic["R3AllIn"]
                                assert Expected_GoalDic["R30AllIn"]==Actual_GoalDic["R30AllIn"]
                                assert Expected_GoalDic["R7AllIn"]==Actual_GoalDic["R7AllIn"]

                                #assert Expected_GoalDic['Achiev']==Actual_GoalDic["Achiev"]
                                
                                '''Prepare Data for the following test '''
                                if self.tablist[ywm]=="LastTwoMonth":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(137)#For Step2
                                elif self.tablist[ywm]=="LastMonth":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(126)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(125)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(124)#For Step4
                                elif self.tablist[ywm]=="Yesterday":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(25)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(24)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(23)#For Step4
                                      
                                elif self.tablist[ywm]== "Week-to-Date":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(81)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(80)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(79)#For Step4
                                elif self.tablist[ywm]=="Month-to-Date":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(103)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(102)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(101)#For Step4
                                
                                #Step2:Verify KPI of SITES
                                print "=================2.Verify Each KPI of site, color, achievement=============="
                                '''Expected_KPIofSITEDic is from above.'''
                                print Expected_KPIofSITEDic
                                #Step2.2:Get the Actual KPI of site
                                '''Actual_KPIofSITEDic is from blow.''' 
                                Actual_KPIofSITEDic=GetPData_Actual.get_UBIZICM_SITE_Data_()
                                print Actual_KPIofSITEDic
                                #Step2.3:assert Expected==Actual
                                assert Expected_KPIofSITEDic["AvgHoldTime"][0]==Actual_KPIofSITEDic["AvgHoldTime"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["AvgHoldTime"][1]==Actual_KPIofSITEDic["AvgHoldTime"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["IBAHT"][0]==Actual_KPIofSITEDic["IBAHT"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["IBAHT"][1]==Actual_KPIofSITEDic["IBAHT"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["CaseTocall"][0]==Actual_KPIofSITEDic["CaseTocall"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["CaseTocall"][1]==Actual_KPIofSITEDic["CaseTocall"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Misdirects"][0]==Actual_KPIofSITEDic["Misdirects"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["Misdirects"][1]==Actual_KPIofSITEDic["Misdirects"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Ghosts"][0]==Actual_KPIofSITEDic["Ghosts"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["Ghosts"][1]==Actual_KPIofSITEDic["Ghosts"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["SwitchTransfer"][0]==Actual_KPIofSITEDic["SwitchTransfer"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["SwitchTransfer"][1]==Actual_KPIofSITEDic["SwitchTransfer"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["DailyRepeatRate"][0]==Actual_KPIofSITEDic["DailyRepeatRate"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["DailyRepeatRate"][1]==Actual_KPIofSITEDic["DailyRepeatRate"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["DispatchRateByCTV"][0]==Actual_KPIofSITEDic["DispatchRateByCTV"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["DispatchRateByCTV"][1]==Actual_KPIofSITEDic["DispatchRateByCTV"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["WFEComplianceRate"][0]==Actual_KPIofSITEDic["WFEComplianceRate"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["WFEComplianceRate"][1]==Actual_KPIofSITEDic["WFEComplianceRate"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["R3AllIn"][0]==Actual_KPIofSITEDic["R3AllIn"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["R3AllIn"][1]==Actual_KPIofSITEDic["R3AllIn"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["R30AllIn"][0]==Actual_KPIofSITEDic["R30AllIn"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["R30AllIn"][1]==Actual_KPIofSITEDic["R30AllIn"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["R7AllIn"][0]==Actual_KPIofSITEDic["R7AllIn"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["R7AllIn"][1]==Actual_KPIofSITEDic["R7AllIn"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value
                                ''' Achiev has no KPI sort '''
                                
                                if self.tablist[ywm]!="LastTwoMonth":
                                    #Step3:Verify achievement of Tl2
                                    print "=================3.Verify TEAM (TL2's) KPI.=============="
                                    #Step3.1:Get the Expected achievement of Tl1
                                    '''Expected_KPIofTl2 is from above, and  Expected_Achi_Tl2 is from below'''
                                    print Expected_KPIofTl2
                                    #Step3.2:Get the Actual achievement of Tl2(TEAM)
                                    Actual_KPIofTl2=GetPData_Actual.get_UBIZICM_TEAM_Data_()
                                    print Actual_KPIofTl2
                                    
                                    #Step3.3:assert Expected==Actual
                                    assert Expected_KPIofTl2["AvgHoldTime"][0]==Actual_KPIofTl2["AvgHoldTime"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["AvgHoldTime"][1]==Actual_KPIofTl2["AvgHoldTime"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["IBAHT"][0]==Actual_KPIofTl2["IBAHT"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["IBAHT"][1]==Actual_KPIofTl2["IBAHT"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["CaseTocall"][0]==Actual_KPIofTl2["CaseTocall"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["CaseTocall"][1]==Actual_KPIofTl2["CaseTocall"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Misdirects"][0]==Actual_KPIofTl2["Misdirects"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["Misdirects"][1]==Actual_KPIofTl2["Misdirects"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Ghosts"][0]==Actual_KPIofTl2["Ghosts"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["Ghosts"][1]==Actual_KPIofTl2["Ghosts"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["SwitchTransfer"][0]==Actual_KPIofTl2["SwitchTransfer"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["SwitchTransfer"][1]==Actual_KPIofTl2["SwitchTransfer"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["DailyRepeatRate"][0]==Actual_KPIofTl2["DailyRepeatRate"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["DailyRepeatRate"][1]==Actual_KPIofTl2["DailyRepeatRate"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["DispatchRateByCTV"][0]==Actual_KPIofTl2["DispatchRateByCTV"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["DispatchRateByCTV"][1]==Actual_KPIofTl2["DispatchRateByCTV"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["WFEComplianceRate"][0]==Actual_KPIofTl2["WFEComplianceRate"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["WFEComplianceRate"][1]==Actual_KPIofTl2["WFEComplianceRate"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["R3AllIn"][0]==Actual_KPIofTl2["R3AllIn"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["R3AllIn"][1]==Actual_KPIofTl2["R3AllIn"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["R30AllIn"][0]==Actual_KPIofTl2["R30AllIn"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["R30AllIn"][1]==Actual_KPIofTl2["R30AllIn"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["R7AllIn"][0]==Actual_KPIofTl2["R7AllIn"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["R7AllIn"][1]==Actual_KPIofTl2["R7AllIn"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Achiev"][0]==Actual_KPIofTl2["Achiev"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["Achiev"][1]==Actual_KPIofTl2["Achiev"][1]#1 is KPI status
    
                                    
                                    #Step4:Verify achievement of all Tl1's Agents 
                                    print "=================4.Verify Agent14's all KPIs=============="                       
                                    #Step4.1:Get the Expected achievement of all Tl1's Agents
                                    print "=================4.Expected Agent14's all KPIs==============" 
                                    print Expected_KPIofAgent14
                                   
                                    #Step4.2:Get the Actual achievement of all Tl1's Agents
                                    print "=================4.Actual Agent14's all KPIs=============="
                                    Actual_KPIofAgent14=GetPData_Actual.get_UBIZICM_AgentKPI_Agent_Actual()
                                    print Actual_KPIofAgent14
                                    
                                    #Step4.3:assert Expected==Actual
                                    assert Expected_KPIofAgent14["AvgHoldTime"][0]==Actual_KPIofAgent14["AvgHoldTime"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["AvgHoldTime"][1]==Actual_KPIofAgent14["AvgHoldTime"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["IBAHT"][0]==Actual_KPIofAgent14["IBAHT"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["IBAHT"][1]==Actual_KPIofAgent14["IBAHT"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["CaseTocall"][0]==Actual_KPIofAgent14["CaseTocall"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["CaseTocall"][1]==Actual_KPIofAgent14["CaseTocall"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Misdirects"][0]==Actual_KPIofAgent14["Misdirects"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["Misdirects"][1]==Actual_KPIofAgent14["Misdirects"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Ghosts"][0]==Actual_KPIofAgent14["Ghosts"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["Ghosts"][1]==Actual_KPIofAgent14["Ghosts"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["SwitchTransfer"][0]==Actual_KPIofAgent14["SwitchTransfer"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["SwitchTransfer"][1]==Actual_KPIofAgent14["SwitchTransfer"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["DailyRepeatRate"][0]==Actual_KPIofAgent14["DailyRepeatRate"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["DailyRepeatRate"][1]==Actual_KPIofAgent14["DailyRepeatRate"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["DispatchRateByCTV"][0]==Actual_KPIofAgent14["DispatchRateByCTV"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["DispatchRateByCTV"][1]==Actual_KPIofAgent14["DispatchRateByCTV"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["WFEComplianceRate"][0]==Actual_KPIofAgent14["WFEComplianceRate"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["WFEComplianceRate"][1]==Actual_KPIofAgent14["WFEComplianceRate"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["R3AllIn"][0]==Actual_KPIofAgent14["R3AllIn"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["R3AllIn"][1]==Actual_KPIofAgent14["R3AllIn"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["R30AllIn"][0]==Actual_KPIofAgent14["R30AllIn"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["R30AllIn"][1]==Actual_KPIofAgent14["R30AllIn"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["R7AllIn"][0]==Actual_KPIofAgent14["R7AllIn"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["R7AllIn"][1]==Actual_KPIofAgent14["R7AllIn"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["Achiev"][0]==Actual_KPIofAgent14["Achiev"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["Achiev"][1]==Actual_KPIofAgent14["Achiev"][1]#1 is KPI status

                               


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()