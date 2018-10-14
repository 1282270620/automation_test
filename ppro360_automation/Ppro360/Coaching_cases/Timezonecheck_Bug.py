'''
Created on Jan 18, 2017

@author: symbio
'''
import unittest
import time
from public_method.Login import Login
from Tablet_pages.Coachinghomepage import Coachinghomepage
#from test_pages.BasicInfoforCoaching import BasicInfoforCoaching
from public_method.Get_configration_data import Get_configration_data
from public_method import Gl
import xlrd
import public_method
from public_method.Deleteexistfile import Deleteexistfile
from Tablet_pages.TabletHomepage import TabletHomepage


class Timezonecheck_Bug(unittest.TestCase):


    def setUp(self):
        
        #Case ID
        self.caseID="Timezonecheck_Bug"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        #Others
        self.coachname="All"
        self.status="All"
        self.lobname="AOL"
        self.sitename="TUCSON"
        self.snnumber="AOL-TUC-SBS-000022"
        self.coach_loc="//*[@id='container']/div/section/div/div[2]/table/tbody/tr/td[1]"
        
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #Get Coach filename exported
        self.CoachfilenameExported_inExcel="coachfilenameExported"
        self.coachfileaddress=GetData.get_CoachfileExportedaddress(self.CoachfilenameExported_inExcel)
        
        
        
   


    def tearDown(self):
        public_method.Gl.driver.quit()


    def test_Timezonecheck_Bug(self):
        print self.caseID
        #Step1:Login tablet
        L=Login()
        L.Login_tablet(self.tableturl,self.lobname,self.sitename,self.OMuserid,self.OMpassword)
        time.sleep(Gl.waittime)
        #Step2:Enter coaching page
        Tablet=TabletHomepage()
        Tablet.click_coachingcircle()
        #Step3:Search the coaching
        time.sleep(Gl.waittime)
        C=Coachinghomepage()
        C.input_SN(self.snnumber)
        C.select_coachname(self.coachname)
        C.select_status(self.status)
        time.sleep(Gl.waittime)
        C.click_filterbutton()
        time.sleep(Gl.waittime)
        #Step4:Delete this file whose name include 'coach'
        #D=Deleteexistfile(self.downloadpath)
        D=Deleteexistfile()
        D.delete_coachfile(self.downloadpath)
        #Step5:Export this coaching
        C.click_exportbutton()
        time.sleep(2*Gl.waittime)
        #Step6:Read new coach file
        self.check_coachexported()

        
        
        
    def check_coachexported(self):
        coachdata=xlrd.open_workbook(self.coachfileaddress)
        table = coachdata.sheet_by_index(0)
        assert table.row_values(1)[0] == self.snnumber
        assert table.row_values(1)[6] == '2016/09/21'



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()