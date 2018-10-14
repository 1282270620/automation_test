'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
#from public_method.Get_PerformanceData_Actual import Get_PerformanceData_Actual
from Performance_Cases_VXIIP.Get_PerformanceData_Actual_VXIIP import Get_PerformanceData_Actual_VXIIP
from Performance_Cases_VXIIP.Get_PerformanceData_Expected_VXIIP import Get_PerformanceData_Expected_VXIIP
from Performance_Cases_VXIIP.Check_All_VXIIP import Check_All_VXIIP

from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time


class VXIIP_Performance_OM(unittest.TestCase):


    def setUp(self):
        self.caseID="VXIIP_Performance_OM"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        print self.testLOBSITE_list
        
        #Yesterday,WTD,MTD for VXIIP
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        


    def tearDown(self):
        Gl.driver.quit() 


    def test_VXIIP_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_VXIIP()
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_VXIIP()
        Check_all=Check_All_VXIIP()
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_VXIIP_Goal_Expected(lineindex)
        
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
                    Achiev_SITE_Monthly=GetPData_Actual.get_VXIIP_SITE_Data_()['Achiev'][0]
                    print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                    assert Achiev_PerformanceCircle==Achiev_SITE_Monthly
                    lob_site=lobname+"_"+sitename
                    Time=GetConfig.get_Lobtime_From_LobTimeConfig(lob_site)
                    Timetablist=Time.split(",")
                    print Timetablist
                    print len(Timetablist)
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        for i in range(0,len(Timetablist)):
                            if Timetablist[i]=="LastTwoMonth":
                                ywm=1
                            elif Timetablist[i]=="LastMonth":
                                ywm=2
                            elif Timetablist[i]=="Yesterday":
                                ywm=3
                            elif Timetablist[i]=="Week-to-Date":
                                ywm=4
                            elif Timetablist[i]=="Month-to-Date":
                                ywm=5
                            #print "i:",i
                            #print "ywm:",ywm 
                            Ppage.click_timetab_performance(ywm)
                    
                            print "*********************Start********************",
                            print Timetablist[i],
                            print "is in testing:"
                            time.sleep(Gl.waittime)
                            #Step1:Verify Goal
                            print "=================1.Verify Each KPI of Goal=============="
                            Actual_GoalDic=GetPData_Actual.get_VXIIP_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                            print Expected_GoalDic
                            print Actual_GoalDic
                            Check_all.Check_Goal(Expected_GoalDic, Actual_GoalDic)
                            TimeTab=Timetablist[i]
                            
                            AllExpectedValue_Dic=GetPData_Expected.Get_AllDic_Expected(TimeTab)
                            Expected_KPIofSITEDic=AllExpectedValue_Dic["Expected_KPIofSITEDic"]
                            Expected_KPIofTl1=AllExpectedValue_Dic["Expected_KPIofTl1"]
                            Expected_AgentAchiev=AllExpectedValue_Dic["Expected_AgentAchiev"]
                            Expected_KPIofAgent8=AllExpectedValue_Dic["Expected_KPIofAgent8"]
                            Expected_KPIofAgent11=AllExpectedValue_Dic["Expected_KPIofAgent11"]
                            
                            Actual_KPIofSITEDic=GetPData_Actual.get_VXIIP_SITE_Data_()
                            #Step2:Verify SITE
                            Check_all.Check_Site(Expected_KPIofSITEDic, Actual_KPIofSITEDic)
                            
                            #Step3:Verify Tl1
                            Tl1_line=Check_all.Check_TL1Achive(Expected_KPIofTl1)
                            
                            
                            #Step4:Verify achievement of all Tl1's Agents              
                            print Expected_AgentAchiev
                            Actual_AgentKPI=Check_all.Check_AllAgentofTL1(Tl1_line,TimeTab,Expected_AgentAchiev)
                            
                            #Step5:Verify Agent8
                            Check_all.Check_Agent8(TimeTab, Expected_KPIofAgent8, Actual_AgentKPI)
                            #Step6:Verify Agent11
                            Check_all.Check_Agent11(Expected_KPIofAgent11, Actual_AgentKPI)

                            
                    elif lobname in Gl.performancefor_3TimeTab_lob:
                        for i in range(0,len(Timetablist)):
                            if Timetablist[i]=="LastTwoMonth":
                                ywm=1
                            elif Timetablist[i]=="LastMonth":
                                ywm=2
                            elif Timetablist[i]=="Month-to-Date":
                                ywm=3
                    elif lobname in Gl.performancefor_OldTimeTab_lob:
                        for i in range(0,len(Timetablist)):
                            if Timetablist[i]=="Yesterday":
                                ywm=1
                            elif Timetablist[i]=="Week-to-Date":
                                ywm=2
                            elif Timetablist[i]=="Month-to-Date":
                                ywm=3
                    
                    

                    
                    
                    

                    L.logout_tablet()    
     

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()