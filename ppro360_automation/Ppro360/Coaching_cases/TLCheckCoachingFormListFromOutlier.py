'''
Created on July 28, 2017

@author: symbio
'''
import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
from Tablet_pages.PerformancPage import PerformancePage
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Popupaddcoachpage import Popupaddcoachpage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.OutlierPage import OutlierPage
from Tablet_pages.HeaderPage import HeaderPage


class TLCheckCoachingFormListFromOutlier(unittest.TestCase):
    def setUp(self):
        #Case ID
        self.caseID="TLCheckCoachingFormListFromOutlier"
        
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Get coachpopuptittle
        self.title=GetData.get_AddCoachingFormTitle()
        #coaching or Triad coaching
        self.coachtype="coaching"   
    
    def test_OMCheckCoachingFormList(self):
        CT=Coach_Triad_General()
        Ppage=PerformancePage()
        Tablet=TabletHomepage()
        Popup=Popupaddcoachpage()
        GetConfig=Get_configration_data()
        GetTL=Get_AllRoleAccountForTest()
        Outlier=OutlierPage()
        Header=HeaderPage()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                ##GET THE CORRECT URL#####
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    coach_list=GetConfig.get_CoachingFormList(lobname)
                    #Step1:Login tablet
                    
                    #TLInfo=GetTL.get_TLInfoandAgentHridFromPerformance(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    TLInfo=GetTL.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, "L1")
                    print TLInfo
                    TLHrid=TLInfo["Hrid"]
                    TLPassword=TLInfo["Password"]
                    #Step1:Login with TL to be testing
                    #time.sleep(10*Gl.waittime)
                    L=Login()
                    L.Login_tablet(tableturl,lobname,sitename,TLHrid,TLPassword)
                    time.sleep(Gl.waittime)
                    #Step2:Enter performance
                    Tablet.click_TL_outliercircle()
                    #Step3:Check Coaching for POP-UP window
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        tablist=Gl.Multi_timetab
                        for ywm in range(0,len(tablist)):
                            if tablist[ywm]=="LastTwoMonth":
                                Outlier.click_timetab_Outlier(1)
                            elif tablist[ywm]=="LastMonth":
                                Outlier.click_timetab_Outlier(2)
                            elif tablist[ywm]=="Yesterday":
                                Outlier.click_timetab_Outlier(3)
                            elif tablist[ywm]== "Week-to-Date":
                                Outlier.click_timetab_Outlier(4)
                            elif tablist[ywm]=="Month-to-Date":
                                Outlier.click_timetab_Outlier(5)
                            print "Start=====",
                            print tablist[ywm],
                            print "is in testing:"
                            time.sleep(Gl.waittime)
                            Outlier.click_anyKPIofTop20(1, 2)#select the first Agent's kpi of top20
                            Outlier.click_addCoachButton()#Click add coaching button
                            AddWindowTitle=CT.Get_AddWindow_title(self.coachtype)
                            assert AddWindowTitle==self.title
                            AllCoachInfo=CT.Get_CoachOrTriad_FromPopUpWindow()
                            AllPOPUP_coach_list=AllCoachInfo["All_list"]
                            print AllPOPUP_coach_list
                            print coach_list
                            assert AllPOPUP_coach_list==coach_list#Check all coaching is correct
                            assert len(AllPOPUP_coach_list)==len(coach_list)#Very the number is correct   
                            Popup.close_popup()                            
                            Outlier.click_anyKPIofTop20(1, 2)#Cancel selecting kpi for Agent to do next test
                            continue
                    elif lobname in Gl.performancefor_3TimeTab_lob:
                        tablist=Gl.Less_timetab
                        for ywm in range(0,len(tablist)):
                            if tablist[ywm]=="LastTwoMonth":
                                Outlier.click_timetab_Outlier(1)
                            elif tablist[ywm]=="LastMonth":
                                Outlier.click_timetab_Outlier(2)
                            elif tablist[ywm]=="Month-to-Date":
                                Outlier.click_timetab_Outlier(3)
                            print "Start=====",
                            print tablist[ywm],
                            print "is in testing:"
                            Outlier.click_anyKPIofTop20(1, 2)#select the first Agent's kpi of top20
                            Outlier.click_addCoachButton()#Click add coaching button
                            AddWindowTitle=CT.Get_AddWindow_title(self.coachtype)
                            assert AddWindowTitle==self.title
                            AllCoachInfo=CT.Get_CoachOrTriad_FromPopUpWindow()
                            AllPOPUP_coach_list=AllCoachInfo["All_list"]
                            assert AllPOPUP_coach_list==coach_list#Check all coaching is correct
                            assert len(AllPOPUP_coach_list)==len(coach_list)#Very the number is correct   
                            Popup.close_popup()                            
                            Outlier.click_anyKPIofTop20(1, 2)#Cancel selecting kpi for Agent to do next test         
                            #Ppage.select_Agentkpi()#Cancel selecting kpi for Agent to do next test
                    else:
                        tablist=Gl.Old_timetab
                        for ywm in range(0,len(tablist)):
                            if tablist[ywm]=="Yesterday":
                                Outlier.click_timetab_Outlier(1)
                            elif tablist[ywm]=="Week-to-Date":
                                Outlier.click_timetab_Outlier(2)
                            elif tablist[ywm]=="Month-to-Date":
                                Outlier.click_timetab_Outlier(3)
                            print "Start=====",
                            print tablist[ywm],
                            print "is in testing:"
                            Outlier.click_anyKPIofTop20(1, 2)#select the first Agent's kpi of top20
                            Outlier.click_addCoachButton()#Click add coaching button
                            AddWindowTitle=CT.Get_AddWindow_title(self.coachtype)
                            assert AddWindowTitle==self.title
                            AllCoachInfo=CT.Get_CoachOrTriad_FromPopUpWindow()
                            AllPOPUP_coach_list=AllCoachInfo["All_list"]
                            assert AllPOPUP_coach_list==coach_list#Check all coaching is correct
                            assert len(AllPOPUP_coach_list)==len(coach_list)#Very the number is correct   
                            Popup.close_popup()                            
                            Outlier.click_anyKPIofTop20(1, 2)#Cancel selecting kpi for Agent to do next test         
                            #Ppage.select_Agentkpi()#Cancel selecting kpi for Agent to do next test
                    
                    #Step4:Back to home page
                    Header.click_backbutton()
                    #Step5:Enter to Triad coaching page
                    Tablet.click_TL_coachingcircle()
                    time.sleep(Gl.waittime)
                    #Step6:Check type drop down list
                    #Get ExpectedTriadcoachingDropDownlist for AOL and DTVDS, and others need to add triadcoach of LC additional
                    DropDownlist=CT.Get_typelist()
                    assert DropDownlist==coach_list
                    #Step4:Logout
                    #L=Login(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                    continue
            



    def tearDown(self):
        #Gl.driver.quit()
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()