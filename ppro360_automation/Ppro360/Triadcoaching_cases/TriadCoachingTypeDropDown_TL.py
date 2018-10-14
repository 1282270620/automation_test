'''
Created on Jan 23, 2017

@author: symbio
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Coach_Triad_General import Coach_Triad_General
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
import time





class TriadCoachingTypeDropDown_TL(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="TriadCoachingTypeDropDown_TL"
        
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Get coachpopuptittle
        self.title=GetData.get_AddTriadCoachingFormTitle()
        #coaching or Triad coaching
        self.coachtype="triadcoaching"   


        #Get Triadcoaching sheetname
        self.triadcoachsheetname="TriadCoaching" 
        


    def tearDown(self):
        Gl.driver.quit()

    

    def test_TLcheckTriadCoachingTypeDropDown(self):
        CT=Coach_Triad_General()
        Tablet=TabletHomepage()
        GetTL=Get_AllRoleAccountForTest()
        GetConfig=Get_configration_data()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                Adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                ##GET THE CORRECT URL#####
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    triadcoach_all_list=GetConfig.get_TriadCoachingFormAllList(lobname)
                    triadcoach_disabled_list=GetConfig.get_TriadCoachingFormDisabledList(lobname)
                    #Get ExpectedTriadcoachingDropDownlist for AOL and DTVDS, and others need to add triadcoach of LC additional
                    ExpectedTriadcoachingDropDownlist=[]
                    for i in range(0,len(triadcoach_all_list)):
                        if triadcoach_all_list[i] not in triadcoach_disabled_list:
                            ExpectedTriadcoachingDropDownlist.append(triadcoach_all_list[i])
        
                    #Step0:Login tablet system and enter to My Team Info to select the first TL for testing
                    #TLinfo=GetTL.get_TLInfoFromMyteamInfo(self.tableturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    #TL_userid=GetTL.get_TLInfoFromMyteamInfo(self.tableturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    #TLinfo=GetTL.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, TL_userid)
                    TLinfo=GetTL.get_TLandAgentInfofromAdmin_Byrole(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, "L1")
                    TLhrid=TLinfo["Hrid"]
                    TLpassword=TLinfo["Password"]
                    time.sleep(Gl.waittime)
                    
                    #Login with TL to be testing
                    L=Login()
                    L.Login_tablet(tableturl,lobname,sitename,TLhrid,TLpassword)
                    #Step2:Enter triad coaching module.
                    Tablet.click_TL_Triadcoachingcirecle()
                    #Step3:Check type drop-down.
                    Enabledlist=[]
                    for i in range(0,len(triadcoach_all_list)):
                        if triadcoach_all_list[i] not in triadcoach_disabled_list:
                            Enabledlist.append(triadcoach_all_list[i])
                    DropDownlist=CT.Get_typelist()
                    print "DropDownlist:",DropDownlist
                    print "Enabledlist:",Enabledlist
                    assert DropDownlist==Enabledlist
                    #Step4:Logout
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                    continue



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
