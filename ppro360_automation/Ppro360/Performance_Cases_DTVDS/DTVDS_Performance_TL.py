'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
#from public_method.Get_PerformanceData_Actual import Get_PerformanceData_Actual
from Performance_Cases_DTVDS.Get_PerformanceData_Actual_DTVDS import Get_PerformanceData_Actual_DTVDS
from Performance_Cases_DTVDS.Get_PerformanceData_Expected_DTVDS import Get_PerformanceData_Expected_DTVDS

from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest


class DTVDS_Performance_TL(unittest.TestCase):


    def setUp(self):
        self.caseID="DTVDS_Performance_TL"
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
        self.TL_userid='300012'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for DTVDS
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        


    def tearDown(self):
        Gl.driver.quit() 


    def test_DTVDS_Performance_TL(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_DTVDS()
        
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_DTVDS()
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
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
                        Achiev_TEAM_Monthly=GetPData_Actual.get_DTVDS_TEAM_Data_()['Achiev'][0]
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
                            if self.tablist[ywm]=="LastTwoMonth":
                                Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(118)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(117)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(114, 116)#For Step4
                                #Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(132)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(116)#For Step6
                                
                            elif self.tablist[ywm]=="LastMonth":
                                Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(107)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(105)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(94, 104)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(101)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(104)#For Step6
                            
                            elif self.tablist[ywm]=="Yesterday":
                                Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(25) #For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(17) #For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(5, 15) #For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(12) #For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(15) #For Step6
                            
                            elif self.tablist[ywm]== "Week-to-Date":
                                Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(68)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(66)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(55, 65)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(62)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(65)#For Step6
                            
                            elif self.tablist[ywm]=="Month-to-Date":
                                Expected_KPIofSITEDic=GetPData_Expected.get_DTVDS_Performance_Data_Expected(88)#For Step2
                                Expected_KPIofTl1=GetPData_Expected.get_DTVDS_Performance_Data_Expected(86)#For Step3
                                Expected_AllAgentName_List=GetPData_Expected.Get_AllAgentName_Expected(75, 85)#For Step4
                                Expected_KPIofAgent8=GetPData_Expected.get_DTVDS_Performance_Data_Expected(82)#For Step5
                                Expected_KPIofAgent11=GetPData_Expected.get_DTVDS_Performance_Data_Expected(85)#For Step6
                            
                            #Step2:Verify KPI of SITES
                            print "=================2.Verify Each KPI of site, color, achievement=============="
                            '''Expected_KPIofSITEDic is from above.'''
                            print Expected_KPIofSITEDic
                            #Step2.2:Get the Actual KPI of site
                            '''Actual_KPIofSITEDic is from blow.''' 
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
                            ''' Achiev has no KPI sort '''
                            
                            
                            #Step3:Verify achievement of Tl1
                            print "=================3.Verify TEAM (TL2's) KPI.=============="
                            #Step3.1:Get the Expected achievement of Tl1
                            '''Expected_KPIofTl2 is from above, and  Expected_Achi_Tl2 is from below'''
                            print Expected_KPIofTl1
                            #Step3.2:Get the Actual achievement of Tl2(TEAM)
                            Actual_KPIofTl1=GetPData_Actual.get_DTVDS_TEAM_Data_()
                            print Actual_KPIofTl1
                            
                            #Step3.3:assert Expected==Actual
                            assert Expected_KPIofTl1['AHT'][0]==Actual_KPIofTl1['AHT'][0] #0 is KPI value
                            assert Expected_KPIofTl1['AHT'][1]==Actual_KPIofTl1['AHT'][1] #1 is KPI status
                            assert Expected_KPIofTl1["VideoActivations"][0]==Actual_KPIofTl1["VideoActivations"][0] #0 is KPI value
                            assert Expected_KPIofTl1["VideoActivations"][1]==Actual_KPIofTl1["VideoActivations"][1] #1 is KPI status
                            assert Expected_KPIofTl1["IPPBAttachRate"][0]==Actual_KPIofTl1["IPPBAttachRate"][0] #0 is KPI value
                            assert Expected_KPIofTl1["IPPBAttachRate"][1]==Actual_KPIofTl1["IPPBAttachRate"][1] #1 is KPI status
                            assert Expected_KPIofTl1["MobilitySales"][0]==Actual_KPIofTl1["MobilitySales"][0] #0 is KPI value
                            assert Expected_KPIofTl1["MobilitySales"][1]==Actual_KPIofTl1["MobilitySales"][1] #1 is KPI status
                            assert Expected_KPIofTl1["CC"][0]==Actual_KPIofTl1["CC"][0] #0 is KPI value
                            assert Expected_KPIofTl1["CC"][1]==Actual_KPIofTl1["CC"][1] #1 is KPI status
                            assert Expected_KPIofTl1["CloseRate"][0]==Actual_KPIofTl1["CloseRate"][0] #0 is KPI value
                            assert Expected_KPIofTl1["CloseRate"][1]==Actual_KPIofTl1["CloseRate"][1] #1 is KPI status
                            assert Expected_KPIofTl1["IPPBGrossSales"][0]==Actual_KPIofTl1["IPPBGrossSales"][0] #0 is KPI value
                            assert Expected_KPIofTl1["IPPBGrossSales"][1]==Actual_KPIofTl1["IPPBGrossSales"][1] #1 is KPI status
                            assert Expected_KPIofTl1["OverallCallExp"][0]==Actual_KPIofTl1["OverallCallExp"][0] #0 is KPI value
                            assert Expected_KPIofTl1["OverallCallExp"][1]==Actual_KPIofTl1["OverallCallExp"][1] #1 is KPI status
                            assert Expected_KPIofTl1["NFCR"][0]==Actual_KPIofTl1["NFCR"][0] #0 is KPI value
                            assert Expected_KPIofTl1["NFCR"][1]==Actual_KPIofTl1["NFCR"][1] #1 is KPI status
                            assert Expected_KPIofTl1["Achiev"][0]==Actual_KPIofTl1["Achiev"][0] #0 is KPI value

                            
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
                                Agent_KPI=GetPData_Actual.get_DTVDS_AgentKPI_TL_Actual(Agentindex)
                                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
                                Agentindex=Agentindex+1
                                flag=Ppage.Agent_line_exist_TL(Agentindex)
                            print Actual_AllAgentName_List
                            
                            #Step4.3:assert Expected==Actual
                            assert len(Expected_AllAgentName_List)==len(Actual_AllAgentName_List)
                            for i in range(0,len(Expected_AllAgentName_List)):
                                assert Expected_AllAgentName_List[i] in Actual_AllAgentName_List
                            if self.tablist[ywm]!="LastTwoMonth":    
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