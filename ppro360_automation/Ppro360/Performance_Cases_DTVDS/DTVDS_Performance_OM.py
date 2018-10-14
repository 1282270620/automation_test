'''
Created on 2017.9.21

@author: yalan.yin
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from Performance_Cases_DTVDS.Get_PerformanceData_Actual_DTVDS import Get_PerformanceData_Actual_DTVDS
from Performance_Cases_DTVDS.Get_PerformanceData_Expected_DTVDS import Get_PerformanceData_Expected_DTVDS

class DTVDS_Performance_OM(unittest.TestCase):


    def setUp(self):
        self.caseID="DTVDS_Performance_OM"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for DTVDS
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        


    def tearDown(self):
        Gl.driver.quit() 


    def test_DTVDS_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_DTVDS()
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_DTVDS()
        lineindex=2 #The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_DTVDS_Goal_Expected(lineindex)
        
        
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
                    
                    #Step0.1:All data has been ready manually
                    #Step0.3:Login with OM to do upload work
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    Achiev_PerformanceCircle=THomepage.get_Achiev_performancecircle()
                    THomepage.click_performancecircle()
                    Achiev_SITE_Monthly=GetPData_Actual.get_DTVDS_SITE_Data_()['Achiev'][0]
                    print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                    assert Achiev_PerformanceCircle==Achiev_SITE_Monthly
                    
                    for ywm in range(0,len(self.tablist)):
                        Ppage.click_timetab_performance(ywm+1)
                        
                
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        #Step1:Verify Goal
                        print "=================1.Verify Each KPI of Goal=============="
                        Actual_GoalDic=GetPData_Actual.get_DTVDS_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                        
                        assert Expected_GoalDic['AHT']==Actual_GoalDic['AHT']
                        assert Expected_GoalDic["CloseRate"]==Actual_GoalDic["CloseRate"]
                        assert Expected_GoalDic["VideoActivations"]==Actual_GoalDic["VideoActivations"]
                        assert Expected_GoalDic["IPPBAttachRate"]==Actual_GoalDic["IPPBAttachRate"]
                        assert Expected_GoalDic["IPPBGrossSales"]==Actual_GoalDic["IPPBGrossSales"]
                        assert Expected_GoalDic["MobilitySales"]==Actual_GoalDic["MobilitySales"]
                        assert Expected_GoalDic["OverallCallExp"]==Actual_GoalDic["OverallCallExp"]
                        assert Expected_GoalDic["CC"]==Actual_GoalDic["CC"]
                        assert Expected_GoalDic["NFCR"]==Actual_GoalDic["NFCR"]
                        #assert Expected_GoalDic['Achiev']==Actual_GoalDic["Achiev"]
                        
                        '''Prepare Data for the following test '''
                        if self.tablist[ywm]=="Yesterday":
                            Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(25) #For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(17) #For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(5, 15) #For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(12) #For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(15) #For Step6
                            
                        elif self.tablist[ywm]== "Week-to-Date":
                            Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(68)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(66)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(55, 65)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(62)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(65)#For Step6
                        elif self.tablist[ywm]=="Month-to-Date":
                            Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(88)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(86)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(75, 85)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(82)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(85)#For Step6
                            
                        elif self.tablist[ywm]=="LastMonth": #last month
                            Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(107)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(105)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(94, 104)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(101)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(104)#For Step6
                            
                        elif self.tablist[ywm]=="LastTwoMonth": #last two months
                            Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(118)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(117)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(114, 116)#For Step4
                            #Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(132)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(116)#For Step6
                        
                        #Step2:Verify KPI of SITES
                        print "=================2.Verify Each KPI of site, color, achievement=============="
                        '''Expected_KPIofSITEDic is from above.'''
                        print Expected_KPIofSITEDic
                        #Step2.2:Get the Actual KPI of site
                        '''Expected_KPIofSITEDic is from blow.''' 
                        Actual_KPIofSITEDic=GetPData_Actual.get_DTVDS_SITE_Data_()
                        print Actual_KPIofSITEDic
                        #Step2.3:assert Expected==Actual
                        
                        assert Expected_KPIofSITEDic['AHT'][0]==Actual_KPIofSITEDic['AHT'][0] #0 is KPI value
                        assert Expected_KPIofSITEDic['AHT'][1]==Actual_KPIofSITEDic['AHT'][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["VideoActivations"][0]==Actual_KPIofSITEDic["VideoActivations"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["VideoActivations"][1]==Actual_KPIofSITEDic["VideoActivations"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["IPPBAttachRate"][0]==Actual_KPIofSITEDic["IPPBAttachRate"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["IPPBAttachRate"][1]==Actual_KPIofSITEDic["IPPBAttachRate"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["MobilitySales"][0]==Actual_KPIofSITEDic["MobilitySales"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["MobilitySales"][1]==Actual_KPIofSITEDic["MobilitySales"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["CC"][0]==Actual_KPIofSITEDic["CC"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["CC"][1]==Actual_KPIofSITEDic["CC"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["CloseRate"][0]==Actual_KPIofSITEDic["CloseRate"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["CloseRate"][1]==Actual_KPIofSITEDic["CloseRate"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["IPPBGrossSales"][0]==Actual_KPIofSITEDic["IPPBGrossSales"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["IPPBGrossSales"][1]==Actual_KPIofSITEDic["IPPBGrossSales"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["OverallCallExp"][0]==Actual_KPIofSITEDic["OverallCallExp"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["OverallCallExp"][1]==Actual_KPIofSITEDic["OverallCallExp"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["NFCR"][0]==Actual_KPIofSITEDic["NFCR"][0] #0 is KPI value
                        assert Expected_KPIofSITEDic["NFCR"][1]==Actual_KPIofSITEDic["NFCR"][1] #1 is KPI status
                        assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0] #0 is KPI value
                        #assert Expected_KPIofSITEDic["Achiev"][1]==Actual_KPIofSITEDic["Achiev"][1] #1 is KPI status
                        
                        
                        
                        #Step3:Verify achievement of Tl1
                        print "=================3.Verify TL1's achievement.=============="
                        #Step3.1:Get the Expected achievement of Tl1
                        '''Expected_KPIofTl1 is from above, and  Expected_Achi_Tl1 is from below'''
                        Expected_Achi_Tl1=Expected_KPIofTl1["Achiev"][0]
                        #Step3.2:Get the Actual achievement of Tl1
                        flag=True
                        lineindex=1
                        while flag==True:
                            TL_name=Ppage.get_anyKPIofTL(lineindex, 1)[0]
                            if TL_name=='Tl1 Test':
                                Actual_Achiev_TL1=GetPData_Actual.get_DTVDS_TL_KPI_Actual(lineindex)["Achiev"][0]
                                Tl1_line=lineindex#For Step4
                                break
                            lineindex=lineindex+1
                            flag=Ppage.TL_line_exist(lineindex)
                       
                        '''Actual_Achiev_TL1'''
                        #Step3.3:assert Expected==Actual
                        assert Expected_Achi_Tl1==Actual_Achiev_TL1
                        
                        #Step4:Verify achievement of all Tl1's Agents 
                        print "=================4.Verify TL1's all agents achivement=============="                       
                        #Step4.1:Get the Expected achievement of all Tl1's Agents
                        print "=================4.Expected_All Agents' Achiev of Tl1==============" 
                        print Expected_AgentAchiev
                        #Step4.2:Get the Actual achievement of all Tl1's Agents
                        
                        TLindex=Tl1_line#From Step3
                        Ppage.unfold_anyTL(TLindex)#Click this TL1, then all his agents will be shown
                        flag=True
                        Agentindex=1
                        Actual_AgentAchiev={}
                        Actual_AgentKPI={}
                        while flag==True:
                            Agent_Name=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 1)[0]
                            Agent_Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 12)[0]
                            Actual_AgentAchiev[Agent_Name]=Agent_Achiev
                            if Agent_Name=='Agent 8' or Agent_Name=='Agent 11':
                                Agent_KPI=GetPData_Actual.get_DTVDS_Agent_KPI_Actual(TLindex, Agentindex)
                                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
                            Agentindex=Agentindex+1
                            flag=Ppage.Agent_line_exist_OM(TLindex, Agentindex)
                            
                        print "=================4.Actual_All Agents' Achiev of Tl1=============="
                        print Agentindex
                        print Actual_AgentAchiev
                        #Step4.3:assert Expected==Actual
                        print 'Expected_AgentAchiev:',Expected_AgentAchiev
                        print 'Actual_AgentAchiev:',Actual_AgentAchiev
                        if self.tablist[ywm]!='LastTwoMonth': 
                            assert Expected_AgentAchiev["Agent 1"][0]==Actual_AgentAchiev["Agent 1"][0]
                            assert Expected_AgentAchiev["Agent 2"][0]==Actual_AgentAchiev["Agent 2"][0]
                            assert Expected_AgentAchiev["Agent 3"][0]==Actual_AgentAchiev["Agent 3"][0]
                            assert Expected_AgentAchiev["Agent 4"][0]==Actual_AgentAchiev["Agent 4"][0]
                            assert Expected_AgentAchiev["Agent 5"][0]==Actual_AgentAchiev["Agent 5"][0]
                            assert Expected_AgentAchiev["Agent 6"][0]==Actual_AgentAchiev["Agent 6"][0]
                            assert Expected_AgentAchiev["Agent 7"][0]==Actual_AgentAchiev["Agent 7"][0]
                            assert Expected_AgentAchiev["Agent 8"][0]==Actual_AgentAchiev["Agent 8"][0]
                        
                        assert Expected_AgentAchiev["Agent 9"][0]==Actual_AgentAchiev["Agent 9"][0]
                        assert Expected_AgentAchiev["Agent 10"][0]==Actual_AgentAchiev["Agent 10"][0]
                        assert Expected_AgentAchiev["Agent 11"][0]==Actual_AgentAchiev["Agent 11"][0]
                        
                        if  self.tablist[ywm]!='LastTwoMonth':     
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
                            assert Expected_KPIofAgent8["VideoActivations"][0]==Actual_KPIofAgent8["VideoActivations"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["VideoActivations"][1]==Actual_KPIofAgent8["VideoActivations"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["IPPBAttachRate"][0]==Actual_KPIofAgent8["IPPBAttachRate"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["IPPBAttachRate"][1]==Actual_KPIofAgent8["IPPBAttachRate"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["IPPBGrossSales"][0]==Actual_KPIofAgent8["IPPBGrossSales"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["IPPBGrossSales"][1]==Actual_KPIofAgent8["IPPBGrossSales"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["MobilitySales"][0]==Actual_KPIofAgent8["MobilitySales"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["MobilitySales"][1]==Actual_KPIofAgent8["MobilitySales"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["CloseRate"][0]==Actual_KPIofAgent8["CloseRate"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["CloseRate"][1]==Actual_KPIofAgent8["CloseRate"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["OverallCallExp"][0]==Actual_KPIofAgent8["OverallCallExp"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["OverallCallExp"][1]==Actual_KPIofAgent8["OverallCallExp"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["CC"][0]==Actual_KPIofAgent8["CC"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["CC"][1]==Actual_KPIofAgent8["CC"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["NFCR"][0]==Actual_KPIofAgent8["NFCR"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["NFCR"][1]==Actual_KPIofAgent8["NFCR"][1]#1 is KPI status


                        
                        
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
                        assert Expected_KPIofAgent11["VideoActivations"][0]==Actual_KPIofAgent11["VideoActivations"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["VideoActivations"][1]==Actual_KPIofAgent11["VideoActivations"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["IPPBAttachRate"][0]==Actual_KPIofAgent11["IPPBAttachRate"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["IPPBAttachRate"][1]==Actual_KPIofAgent11["IPPBAttachRate"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["IPPBGrossSales"][0]==Actual_KPIofAgent11["IPPBGrossSales"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["IPPBGrossSales"][1]==Actual_KPIofAgent11["IPPBGrossSales"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["MobilitySales"][0]==Actual_KPIofAgent11["MobilitySales"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["MobilitySales"][1]==Actual_KPIofAgent11["MobilitySales"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["CloseRate"][0]==Actual_KPIofAgent11["CloseRate"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["CloseRate"][1]==Actual_KPIofAgent11["CloseRate"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["OverallCallExp"][0]==Actual_KPIofAgent11["OverallCallExp"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["OverallCallExp"][1]==Actual_KPIofAgent11["OverallCallExp"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["CC"][0]==Actual_KPIofAgent11["CC"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["CC"][1]==Actual_KPIofAgent11["CC"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["NFCR"][0]==Actual_KPIofAgent11["NFCR"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["NFCR"][1]==Actual_KPIofAgent11["NFCR"][1]#1 is KPI status

                    L.logout_tablet()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()