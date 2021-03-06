'''
Created on 2018.8.13

@author: Sissi.liu
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from Performance_Cases_ISM.Get_PerformanceData_Expected_ISM import Get_PerformanceData_Expected_ISM
from Performance_Cases_ISM.Get_PerformanceData_Actual_ISM import Get_PerformanceData_Actual_ISM
from Performance_Cases_ISM.Check_All_ISM import Check_All_ISM


class ISM_Performance_OM(unittest.TestCase):
    
    def setUp(self):
        self.caseID="ISM_Performance_OM"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for dbs
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        self.kpikey=['NumberOfSurveys','OverallScore','eg7d_Calls','eg7d_Transfers','eg7d_OneAndDone7Day','eg7d_Rpt7Day','eg7d_7DREPEATS','AHT',
                     'Transfers','Hold','Adjustments','Wireless','Broadband','Achiev']
        
    def tearDown(self):
        Gl.driver.quit() 
    
    def test_ISM_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        Check_all=Check_All_ISM()
        GetPData_Actual=Get_PerformanceData_Actual_ISM()
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_ISM()
        lineindex=2 #The goal is in the row 3 of excel file,so line index is 2
        Expected_GoalDic=GetPData_Expected.get_ISM_Goal_Expected(lineindex)
        
        
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
                    
                    #login tablet
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    #Click performance circle
                    THomepage.click_performancecircle()
                    
                    for ywm in range(0,len(self.tablist)):
                        if self.tablist[ywm]=="Yesterday": 
                            Ppage.click_timetab_performance(3)
                        elif self.tablist[ywm]== "Week-to-Date":
                            Ppage.click_timetab_performance(4)
                        elif self.tablist[ywm]== "Month-to-Date":
                            Ppage.click_timetab_performance(5)
                        elif self.tablist[ywm]== "LastMonth":
                            Ppage.click_timetab_performance(2)
                        elif self.tablist[ywm]== "LastTwoMonth":
                            Ppage.click_timetab_performance(1)
                                                        
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        #Step1:Verify Goal
                        print "=================1.Verify Each KPI of Goal=============="
                        Actual_GoalDic=GetPData_Actual.get_ISM_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                                          
                        Check_all.Check_Goal(Expected_GoalDic, Actual_GoalDic)
                        
                        '''Prepare Data for the following test '''
                        if self.tablist[ywm]=="Yesterday":
                            #Expected_KPIofSITEDic=GetPData_Expected.get_ISM_Performance_Data_Expected(28) #For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_ISM_Performance_Data_Expected(16) #For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(5, 15) #For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_ISM_Performance_Data_Expected(12) #For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_ISM_Performance_Data_Expected(15) #For Step6                            
                        elif self.tablist[ywm]== "Week-to-Date":
                            #Expected_KPIofSITEDic=GetPData_Expected.get_ISM_Performance_Data_Expected(74)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_ISM_Performance_Data_Expected(66)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(55, 65)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_ISM_Performance_Data_Expected(62)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_ISM_Performance_Data_Expected(65)#For Step6
                        elif self.tablist[ywm]=="Month-to-Date":
                            #Expected_KPIofSITEDic=GetPData_Expected.get_ISM_Performance_Data_Expected(99)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_ISM_Performance_Data_Expected(91)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(80, 90)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_ISM_Performance_Data_Expected(87)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_ISM_Performance_Data_Expected(90)#For Step6                            
                        elif self.tablist[ywm]=="LastMonth": #last month
                            #Expected_KPIofSITEDic=GetPData_Expected.get_ISM_Performance_Data_Expected(123)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_ISM_Performance_Data_Expected(115)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(104, 114)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_ISM_Performance_Data_Expected(111)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_ISM_Performance_Data_Expected(114)#For Step6                            
                        elif self.tablist[ywm]=="LastTwoMonth": #last two months
                            #Expected_KPIofSITEDic=GetPData_Expected.get_ISM_Performance_Data_Expected(135)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_ISM_Performance_Data_Expected(132)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(129, 131)#For Step4
                            #Expected_KPIofAgent8=GetPData_Expected.get_ISM_Performance_Data_Expected(132)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_ISM_Performance_Data_Expected(131)#For Step6
                            
                            
                        #step2:Verify Each KPI of site (ISM without Site KPI break)
                        
                        #Step3:Verify achievement of Tl1
                        Tl1_line=Check_all.Check_TL1Achive(Expected_KPIofTl1)                        
                        
                        #Step4:Verify achievement of all Tl1's Agents              
                        print Expected_AgentAchiev
                        Actual_AgentKPI=Check_all.Check_AllAgentofTL1(Tl1_line,self.tablist[ywm],Expected_AgentAchiev)
                             
                        #Step5:Verify Agent8
                        Check_all.Check_Agent8(self.tablist[ywm], Expected_KPIofAgent8, Actual_AgentKPI)
                        
                        #Step6:Verify Agent11
                        Check_all.Check_Agent11(Expected_KPIofAgent11, Actual_AgentKPI)
                    L.logout_tablet()   
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()