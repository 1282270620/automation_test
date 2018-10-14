'''
Created on Jan 3, 2017

@author: symbio
'''
import unittest
from public_method.Login import Login
from Tablet_pages.PerformancPage import PerformancePage
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
import time
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Popupaddcoachpage import Popupaddcoachpage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest


#This case is for "ICM","UBIZ","BLUE","SPANISH"
class LCCheckTriadCoachingFormList(unittest.TestCase):
    def setUp(self):
        #Case ID
        self.caseID="LCCheckTriadCoachingFormList"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.LCuserid=GetData.get_LCuserid()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Get coachpopuptittle
        self.title=GetData.get_AddTriadCoachingFormTitle()
        #coaching or Triad coaching
        self.coachtype="triadcoaching"          
    
    
    def test_LCchecktriadcoachlist(self):
        CT=Coach_Triad_General()
        Ppage=PerformancePage()
        Tablet=TabletHomepage()
        Popup=Popupaddcoachpage()
        #GetTestData=Get_configration_data()
        GetLC=Get_AllRoleAccountForTest()
        GetConfig=Get_configration_data()
        #Test several LOBs
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
                    triadcoach_all_list=GetConfig.get_TriadCoachingFormAllList(lobname)
                    triadcoach_disabled_list=GetConfig.get_TriadCoachingFormDisabledList(lobname)
                    #Step0:Login admin system to get LC's Password
                    LCInfo=GetLC.get_LCInfo(self.adminurl,lobname, sitename, self.OMuserid, self.OMpassword, self.LCuserid)
                    LCpassword=LCInfo["Password"]
                    
                    #Step1:Longin tablet
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.LCuserid,LCpassword)
                    #Step2:Enter performance
                    time.sleep(Gl.waittime)
                    Tablet.click_performancecircle()
                    #Step3:Check Traidcoching for pop-up window
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        tablist=Gl.Multi_timetab
                        for ywm in range(0,len(tablist)):
                            if tablist[ywm]=="LastTwoMonth":
                                Ppage.click_timetab_performance(1)
                            elif tablist[ywm]=="LastMonth":
                                Ppage.click_timetab_performance(2)
                            elif tablist[ywm]=="Yesterday":
                                Ppage.click_timetab_performance(3)
                            elif tablist[ywm]== "Week-to-Date":
                                Ppage.click_timetab_performance(4)
                            elif tablist[ywm]=="Month-to-Date":
                                Ppage.click_timetab_performance(5)
                            print "Start=====",
                            print tablist[ywm],
                            print "is in testing:"
                            time.sleep(Gl.waittime)
                            Ppage.select_TLkpi()#select the first TL
                            Ppage.click_addTriadcoachbutton()#Click add coaching button 
                            AddWindowTitle=CT.Get_AddWindow_title(self.coachtype)
                            assert AddWindowTitle==self.title
                            AllCoachInfo=CT.Get_CoachOrTriad_FromPopUpWindow()
                            Alllist=AllCoachInfo["All_list"]
                            Enabledlist=AllCoachInfo["Enabled_list"]
                            Disabledlist=AllCoachInfo["Disabled_list"]
                            print Alllist
                            print triadcoach_all_list
                            assert Alllist==triadcoach_all_list#Check all coaching is correct
                            assert len(Alllist)==len(triadcoach_all_list)#Very the number is correct 
                            if triadcoach_disabled_list!=[u'']:
                                assert Disabledlist==triadcoach_disabled_list
                                assert len(Enabledlist)==len(Alllist)-len(triadcoach_disabled_list)
                            else:
                                assert Disabledlist==[]
                                assert len(Enabledlist)==len(Alllist)
                            Popup.close_popup()                            
                            Ppage.unselect_TLkpi()#Cancel selecting kpi for Agent to do next test
                            continue
                    elif lobname in Gl.performancefor_3TimeTab_lob:
                        tablist=Gl.Less_timetab
                        for ywm in range(0,len(tablist)):
                            if tablist[ywm]=="LastTwoMonth":
                                Ppage.click_timetab_performance(1)
                            elif tablist[ywm]=="LastMonth":
                                Ppage.click_timetab_performance(2)
                            elif tablist[ywm]=="Month-to-Date":
                                Ppage.click_timetab_performance(3)
                                print "Start=====",
                            print tablist[ywm],
                            print "is in testing:"
                            Ppage.select_TLkpi()#select the first TL
                            Ppage.click_addTriadcoachbutton()#Click add coaching button 
                            AddWindowTitle=CT.Get_AddWindow_title(self.coachtype)
                            assert AddWindowTitle==self.title
                            AllCoachInfo=CT.Get_CoachOrTriad_FromPopUpWindow()
                            Alllist=AllCoachInfo["All_list"]
                            Enabledlist=AllCoachInfo["Enabled_list"]
                            Disabledlist=AllCoachInfo["Disabled_list"]
                            print Alllist
                            print triadcoach_all_list
                            assert Alllist==triadcoach_all_list#Check all coaching is correct
                            assert len(Alllist)==len(triadcoach_all_list)#Very the number is correct 
                            print Disabledlist
                            print triadcoach_disabled_list
                            if triadcoach_disabled_list!=[u'']:
                                    assert Disabledlist==triadcoach_disabled_list
                                    assert len(Enabledlist)==len(Alllist)-len(triadcoach_disabled_list)
                            else:
                                    assert Disabledlist==[]
                                    assert len(Enabledlist)==len(Alllist)
                            #assert Disabledlist==triadcoach_disabled_list
                            #assert len(Enabledlist)==len(Alllist)-len(triadcoach_disabled_list)
                            Popup.close_popup()                            
                            Ppage.unselect_TLkpi()#Cancel selecting kpi for Agent to do next test
                    #Step4:Back to home page
                    Ppage.click_backbutton()
                    #Step5:Enter to Triad coaching page
                    Tablet.click_Triadcoachingcirecle()
                    time.sleep(Gl.waittime)
                    #Step6:Check type drop down list
                    #Get ExpectedTriadcoachingDropDownlist for AOL and DTVDS, and others need to add triadcoach of LC additional
                    DropDownlist=CT.Get_typelist()
                    print DropDownlist
                    print Enabledlist
                    assert DropDownlist==Enabledlist
                    #Step7:Logout
                    #L=Login(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                    continue
            continue            
                
                   


    def tearDown(self):
        Gl.driver.quit()
    
    ###################The blew scripts are steps for case.########################
 
        
    
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
