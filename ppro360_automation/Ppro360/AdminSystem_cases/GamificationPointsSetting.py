import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from AdminSystem_Pages.GamificationPointsSettingPage import GamificationPointsSettingPage

class GamificationPointsSetting(unittest.TestCase):
    def setUp(self):
        #caseID
        self.caseID = "GamificationPointsSetting"
        GetConfData = Get_configration_data()

        #Get OM account
        OMaccount = GetConfData.get_OMaccount()
        self.OMuserid = OMaccount["OMuserid"]
        self.OMpwd = OMaccount["OMpassword"]

        #Get all lobs from CSV
        self.testLOBSITE_list = GetConfData.get_LOBSITEtoTest(self.caseID)
    def tearDown(self):
        Gl.driver.quit()
        pass
    def test_GamificationPointsSetting(self):
        GetConfData = Get_configration_data()
        Log = Login()
        GamPoint = GamificationPointsSettingPage()

        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag = GetConfData.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                
                ##GET THE CORRECT URL#####
                adminurl=GetConfData.get_Test_AdminUrl(lobname)
                
                #get each site which in this lob
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename = site_list[n]
                    GetConfData.print_StartTest_message(lobname, sitename)
                    
                    #Login Admin and navigate to Performance Data module
                    Log.Login_admin(adminurl, lobname, sitename, self.OMuserid, self.OMpwd)
                    GamPoint.enter_GamificationPointSetting()
                    
                    #set daily conditions and check
                    expcetedDaily,lengthDaily = GamPoint.set_Conditions(3,"KPI Value",">","0.5","1","DAILY")
                    GamPoint.assert_SetCondition("DAILY", expcetedDaily, lengthDaily)
                    
                    #set weekly conditions and check
                    expcetedWeekly_st,lengthWeekly_st = GamPoint.set_Conditions(3,"Increase %",">","1","2","WEEKLY")
                    GamPoint.assert_SetCondition("WEEKLY", expcetedWeekly_st, lengthWeekly_st)
                    expcetedWeekly_nd,lengthWeekly_nd = GamPoint.set_Conditions(4,"Decrease Value","<","100","3","WEEKLY")
                    GamPoint.assert_SetCondition("WEEKLY", expcetedWeekly_nd, lengthWeekly_nd)
                    
                    #set monthly conditions and check
                    expcetedMonthly_st,lengthMonthly_st = GamPoint.set_Conditions(3,"Target %",">=","1","4","MONTHLY")
                    GamPoint.assert_SetCondition("MONTHLY", expcetedMonthly_st, lengthMonthly_st)
                    expcetedMonthly_nd,lengthMonthly_nd = GamPoint.set_Conditions(5,"Decrease %","<=","90","5","MONTHLY")
                    GamPoint.assert_SetCondition("MONTHLY", expcetedMonthly_nd,lengthMonthly_nd)
                    expcetedMonthly_rd,lengthMonthly_rd = GamPoint.set_Conditions("Coaching","Acknowledged",">=","3","6","MONTHLY")
                    GamPoint.assert_SetCondition("MONTHLY", expcetedMonthly_rd,lengthMonthly_rd)
                    
                    Log.logout_admin()
                    GetConfData.print_EndTest_message(lobname, sitename)
                