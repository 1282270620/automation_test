'''
Created on 2017.10.10

@author: yalan.yin
'''
import unittest
from Performance_Cases_DBS.Get_PerformanceData_Expected_DBS import Get_PerformanceData_Expected_DBS
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.OutlierPage import OutlierPage

class DBS_Outlier_TL(unittest.TestCase):


    def setUp(self):
        self.caseID="DBS_Outlier_TL"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #TL2's name
        ''' Name='Tl1 Test' '''
        self.TL_name='Tl1 Test'
        self.TL_userid='300012'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for DBS
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
       


    def tearDown(self):
        Gl.driver.quit()
        


    def test_DBS_Outlier_TL(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        Outlier=OutlierPage()
        
        #Get Goal Expected
        #GetPData_Expected=Get_PerformanceData_Expected()
        GetPData_Expected=Get_PerformanceData_Expected_DBS()
        
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
                    
                    #Get TL2's account
                    #L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    #THomepage.click_Myteaminfocircle()
                    #lineindex=Get_account.Get_lineindex(self.TL_userid)
                    #TL1_Info=Get_account.Get_MyTeamInfo(lineindex)
                    TL1_Info=Get_account.get_TLandAgentInfofromAdmin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.TL_userid)
                    TL1_name=TL1_Info['Name']
                    TL1_password=TL1_Info['Password']
                    #L.logout_tablet()
                    if TL1_name!=self.TL_name:
                        print "!!!!!!!!!!TL1 is not incorrect, please check it!!!!!!!!!"
                    else:
                        #Step0.1:All data has been ready manually
                        #Step0.3:Login with OM to do upload work
                        L.Login_tablet(self.tableturl, lobname, sitename, self.TL_userid, TL1_password)
                        THomepage.click_TL_outliercircle()
                        for ywm in range(0,len(self.tablist)):
                            Ppage.click_timetab_performance(ywm+1)
                            
                            print "*********************Start********************",
                            print self.tablist[ywm],
                            print "is in testing:"
                            time.sleep(Gl.waittime)
                        
                            Agentname_First_Top20=Outlier.get_anyKPIofTop20(1, 1)
                            Achieve_First_Top20=Outlier.get_anyKPIofTop20(1, 2)
                            
                            Agentname_Second_Top20=Outlier.get_anyKPIofTop20(2, 1)
                            Achieve_Second_Top20=Outlier.get_anyKPIofTop20(2,2)
                            
                            Agentname_Third_Top20=Outlier.get_anyKPIofTop20(3, 1)
                            Achieve_Third_Top20=Outlier.get_anyKPIofTop20(3, 2)
                            
                            Agentname_First_Bottom20=Outlier.get_anyKPIofBottom20(1, 1)
                            Achieve_First_Bottom20=Outlier.get_anyKPIofBottom20(1, 2)
                            
                            Agentname_Second_Bottom20=Outlier.get_anyKPIofBottom20(2, 1)
                            Achieve_Second_Bottom20=Outlier.get_anyKPIofBottom20(2, 2)
                            
                            Agentname_Third_Bottom20=Outlier.get_anyKPIofBottom20(3, 1)
                            Achieve_Third_Bottom20=Outlier.get_anyKPIofBottom20(3, 2)
                            if self.tablist[ywm]=="LastTwoMonth":
                                '''TOP20:Agent9.Agent10,Agent11
                                   BOTTON20:Agent9.Agent10,Agent11'''
                                Expected_Top1=GetPData_Expected.get_DBS_Performance_Data_Expected(132)
                                Expected_Top2=GetPData_Expected.get_DBS_Performance_Data_Expected(133)
                                Expected_Top3=GetPData_Expected.get_DBS_Performance_Data_Expected(134)
                                Expected_Bottom1=GetPData_Expected.get_DBS_Performance_Data_Expected(132)
                                Expected_Bottom2=GetPData_Expected.get_DBS_Performance_Data_Expected(133)
                                Expected_Bottom3=GetPData_Expected.get_DBS_Performance_Data_Expected(134)
                            elif self.tablist[ywm]=="LastMonth":
                                '''TOP20:Agent9.Agent3,Agent7
                                   BOTTON20:Agent6,Agent4,Agent10'''
                                Expected_Top1=GetPData_Expected.get_DBS_Performance_Data_Expected(115)
                                Expected_Top2=GetPData_Expected.get_DBS_Performance_Data_Expected(109)
                                Expected_Top3=GetPData_Expected.get_DBS_Performance_Data_Expected(113)
                                Expected_Bottom1=GetPData_Expected.get_DBS_Performance_Data_Expected(112)
                                Expected_Bottom2=GetPData_Expected.get_DBS_Performance_Data_Expected(110)
                                Expected_Bottom3=GetPData_Expected.get_DBS_Performance_Data_Expected(116)
                            elif self.tablist[ywm]=="Yesterday":
                                '''TOP20:Agent11.Agent3,Agent7
                                   BOTTON20:Agent2,Agent6,Agent4'''
                                Expected_Top1=GetPData_Expected.get_DBS_Performance_Data_Expected(15)
                                Expected_Top2=GetPData_Expected.get_DBS_Performance_Data_Expected(7)
                                Expected_Top3=GetPData_Expected.get_DBS_Performance_Data_Expected(11)
                                Expected_Bottom1=GetPData_Expected.get_DBS_Performance_Data_Expected(6)
                                Expected_Bottom2=GetPData_Expected.get_DBS_Performance_Data_Expected(10)
                                Expected_Bottom3=GetPData_Expected.get_DBS_Performance_Data_Expected(8)
                            elif self.tablist[ywm]=="Week-to-Date":
                                '''TOP20:Agent3,Agent7,Agent1.
                                   BOTTON20:Agent2,Agent6,Agent4'''
                                Expected_Top1=GetPData_Expected.get_DBS_Performance_Data_Expected(62)
                                Expected_Top2=GetPData_Expected.get_DBS_Performance_Data_Expected(66)
                                Expected_Top3=GetPData_Expected.get_DBS_Performance_Data_Expected(60)
                                Expected_Bottom1=GetPData_Expected.get_DBS_Performance_Data_Expected(61)
                                Expected_Bottom2=GetPData_Expected.get_DBS_Performance_Data_Expected(65)
                                Expected_Bottom3=GetPData_Expected.get_DBS_Performance_Data_Expected(63)
                            elif self.tablist[ywm]=="Month-to-Date":
                                '''TOP20:Agent9,Agent3,Agent7
                                   BOTTON20:Agent6,Agent4,Agent10'''
                                Expected_Top1=GetPData_Expected.get_DBS_Performance_Data_Expected(90)
                                Expected_Top2=GetPData_Expected.get_DBS_Performance_Data_Expected(84)
                                Expected_Top3=GetPData_Expected.get_DBS_Performance_Data_Expected(88)
                                Expected_Bottom1=GetPData_Expected.get_DBS_Performance_Data_Expected(87)
                                Expected_Bottom2=GetPData_Expected.get_DBS_Performance_Data_Expected(85)
                                Expected_Bottom3=GetPData_Expected.get_DBS_Performance_Data_Expected(91)
                            print Agentname_First_Top20
                            print Expected_Top1['Name'][0] 
                            assert Agentname_First_Top20==Expected_Top1['Name'][0]
                            assert Achieve_First_Top20==Expected_Top1["Achiev"][0]
                            
                            assert Agentname_Second_Top20==Expected_Top2['Name'][0]
                            assert Achieve_Second_Top20==Expected_Top2["Achiev"][0]
                            
                            assert Agentname_Third_Top20==Expected_Top3['Name'][0]
                            assert Achieve_Third_Top20==Expected_Top3["Achiev"][0]
                            
                            assert Agentname_First_Bottom20==Expected_Bottom1['Name'][0]
                            assert Achieve_First_Bottom20==Expected_Bottom1["Achiev"][0]
                            
                            print Agentname_Second_Bottom20,Expected_Bottom2['Name'][0]
                            assert Agentname_Second_Bottom20==Expected_Bottom2['Name'][0]
                            assert Achieve_Second_Bottom20==Expected_Bottom2["Achiev"][0]
                            
                            assert Agentname_Third_Bottom20==Expected_Bottom3['Name'][0]
                            assert Achieve_Third_Bottom20==Expected_Bottom3["Achiev"][0]
                        L.logout_tablet()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()