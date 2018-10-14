'''
Created on 2018.7.27

@author: yalan.yin
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
import time
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from AdminSystem_Pages.AddSitepage import AddSitepage

def test_method(fun):
    print(func)


@test_method
class AddNewSite(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="AddNewSite"
        GetData=Get_configration_data()
        
        #get superadmin account
        SAdminaccount=GetData.get_SAdminaccount()
        self.SAdminuserid=SAdminaccount['SAdminuserid']
        self.SAdminpassword=SAdminaccount['SAdminpassword']

        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #All-LOBs in configration file
        #self.AllLOBs="All-LOBs"
        self.LOB_lists=GetData.get_AllLOBs_list()


    def tearDown(self):
        pass


    def test_AddSite(self):
        GetConfig=Get_configration_data()
        ASP=AddSitepage()
        GetData=Get_configration_data()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                Adminurl=GetConfig.get_Test_AdminUrl(lobname)
                #GET THE CORRECT URL#####
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.#print_StartTest_message(lobname, sitename)
                    #Step4:Login admin system
                    L=Login()
                    L.Login_admin(Adminurl,lobname, sitename, self.SAdminuserid, self.SAdminpassword)
                    #Step2:Enter to OM account page
                    Admin=AdminHomepage()
                    Admin.Enter_AddSite()
                    SiteName='AUTO ADDED'
                    Sitenumber=ASP.get_Sitenumber()
                    Site=[]
                    #print "Sitenumber:",Sitenumber 
                    for i in range(1,Sitenumber+1):
                        #print i
                        #print ASP.Get_SiteNameinList(i)
                        ASP.Get_SiteNameinList(i)
                        Site.append(ASP.Get_SiteNameinList(i))
                    #print Site
                    for i in range(1, 100):
                        SiteName_new=SiteName+'00'+str(i)
                        if SiteName_new not in Site:
                            break
                    #print "SiteName_new:",SiteName_new
                    ASP.Input_SiteName(SiteName_new)
                    ASP.Click_AddButton()
                    time.sleep(3)
                    ASP.Click_YesButton()
                    VXIlobs=GetData.get_VXILOBs_list()
                    if lobname in VXIlobs:
                        time.sleep(7)
                    else:
                        time.sleep(20)
                    SiteOnPage=ASP.Get_SiteNameinList(1)
                    #print "SiteOnPage:", SiteOnPage
                    assert SiteOnPage==SiteName_new
                    L.logout_admin()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()