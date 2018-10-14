'''
Created on Jul 4, 2018

@author: Sabrina Guo
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Coach_Triad_General import Coach_Triad_General
import time

class CoachingTypeDropDown_OM(unittest.TestCase):


    def setUp(self):
        self.caseID="CoachingTypeDropDown_OM"
        GetData=Get_configration_data()
        

        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)




    def tearDown(self):
        #Gl.driver.quit()
        pass


    def test_CoachingTypeDropDown_OM(self):
        L=Login()
        THomepage=TabletHomepage()
        GetConfig=Get_configration_data()
        CT=Coach_Triad_General()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                tableturl=GetConfig.get_Test_Tablet(lobname)
                ##GET THE CORRECT URL#####
                coach_list=GetConfig.get_CoachingFormList(lobname)
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    time.sleep(Gl.waittime)
                    
                    L.Login_tablet(tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    THomepage.click_coachingcircle()
                    DropDownlist=CT.Get_typelist()
                    print "coach_list:",coach_list
                    print "DropDownlist:",DropDownlist
                    if coach_list==[u'']:
                        coach_list=[]
                    assert DropDownlist==coach_list
                    L.logout_tablet()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()