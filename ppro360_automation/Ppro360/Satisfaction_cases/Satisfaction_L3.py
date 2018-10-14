import unittest 
from Tablet_pages.LoginTabletPage import LogintabletPage 
from public_method.Get_configration_data import Get_configration_data

class Satisfaction_L3(unittest.TestCase):
    def setUp(self):
        GetConfData = Get_configration_data()
        #Get VXI URL
        self.tabletURL = GetConfData.get_VXI_TabletUrl()
        print(self.tabletURL)
        self.adminURL = GetConfData.get_VXI_AdminUrl()
        print(self.adminURL)
        #Get L1 account
        self.L3account = GetConfData.get_OMaccount()
    def tearDown(self):
        #driver.quit()
        pass
    def test_Satisfaction_L1(self):
        Login = LogintabletPage()
        
        
        