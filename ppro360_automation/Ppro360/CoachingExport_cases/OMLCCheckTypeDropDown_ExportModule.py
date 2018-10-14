'''
Created on Aug 25, 2017

@author: symbio
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.CoachingExportPage import CoachingExportPage
from public_method.Coach_Triad_General import Coach_Triad_General
import MySQLdb
from public_method import Gl
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.Deleteexistfile import Deleteexistfile
from public_method.Get_file import Get_file
from public_method.Get_CoachContent import Get_CoachContent



class OMLCCheckTypeDropDown_ExportModule(unittest.TestCase):


    def setUp(self):
        self.caseID="OMLCCheckTypeDropDown_ExportModule"
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.LCuserid=GetData.get_LCuserid()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
       
        
        #CoachExport file prefix
        self.filename_prefix="coaching_export"
        
        


    def tearDown(self):
        Gl.driver.quit()

    def test_OMLCCheckTypeDropDown_ExportModule(self):
        self.CheckTypeDropDown_ExportModule("L3")
        #self.CheckTypeDropDown_ExportModule("LC")
        #self.CheckTypeDropDown_ExportModule("L1")
    
    def CheckTypeDropDown_ExportModule(self,role):
        GetConfig=Get_configration_data()
        testLOBSITE_list=GetConfig.get_MultiRole_LOBSITEtoTest(self.caseID, role)
        GetAccount=Get_AllRoleAccountForTest()
        L=Login()
        Tablet=TabletHomepage()
        #CoachingExport=CoachingExportPage()
        CT=Coach_Triad_General()
        #Test several LOBs
        for i in range(0,len(testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=testLOBSITE_list[i].split(":")
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
                    print "************ Test",role,"**************"
                    coach_list=GetConfig.get_CoachingExportFormList(lobname)
                    #Step0:Login tablet system and find out a TL whose Agent has KPIt for testing
                    if role=="L3":
                        L.Login_tablet(tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                        Tablet.click_OM_coachingExportcircle()
                    elif role=="LC":
                        LCInfo=GetAccount.get_LCInfo(adminurl,lobname, sitename, self.OMuserid, self.OMpassword, self.LCuserid)
                        LCpassword=LCInfo["Password"]
                        L.Login_tablet(tableturl,lobname,sitename,self.LCuserid,LCpassword)
                        Tablet.click_LC_coachingExportcircle()
                    elif role=="L1":
                        TLInfo=GetAccount.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, "L1")
                        TLHrid=TLInfo["Hrid"]
                        TLPassword=TLInfo["Password"]
                        L.Login_tablet(tableturl,lobname,sitename,TLHrid,TLPassword)
                        Tablet.click_TL_coachingExportcircle()
                    
                    DropDownlist=CT.Get_typelist_CoachingExport()
                    print "DropDownlist:",DropDownlist
                    print "coach_list:",coach_list
                    if DropDownlist==[] and coach_list==[u'']:
                        DropDownlist=coach_list
                    print DropDownlist
                    print coach_list
                    assert DropDownlist==coach_list
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()