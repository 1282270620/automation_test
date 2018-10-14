'''
Created on Apr 24, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
from Performance_Cases_SPANISH.Get_PerformanceData_Expected_SPANISH import Get_PerformanceData_Expected_SPANISH
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.OutlierPage import OutlierPage


class SPANISH_Outlier_TL(unittest.TestCase):


    def setUp(self):
        self.caseID="SPANISH_Outlier_TL"
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
        self.TL_userid='321170'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for SPANISH
        self.tablist=Gl.Less_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
       


    def tearDown(self):
        Gl.driver.quit()


    def test_SPANISH_Outlier_TL(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        Outlier=OutlierPage()
        
        #Get Goal Expected
        #GetPData_Expected=Get_PerformanceData_Expected()
        GetPData_Expected=Get_PerformanceData_Expected_SPANISH()
        
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
                            if self.tablist[ywm]=="LastTwoMonth":#date2
                                '''TOP20:Agent11.Agent9,Agent10
                                   BOTTON20:Agent11,Agent9,Agent10'''
                                Expected_Top1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(93)
                                Expected_Top2=GetPData_Expected.get_SPANISH_Performance_Data_Expected(89)
                                Expected_Top3=GetPData_Expected.get_SPANISH_Performance_Data_Expected(91)
                                Expected_Bottom1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(93)
                                Expected_Bottom2=GetPData_Expected.get_SPANISH_Performance_Data_Expected(89)
                                Expected_Bottom3=GetPData_Expected.get_SPANISH_Performance_Data_Expected(91)
                            if self.tablist[ywm]=="LastMonth":#date1
                                '''TOP20:Agent8.Agent7,Agent3
                                   BOTTON20:Agent4,Agent6,Agent1'''
                                Expected_Top1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(20)
                                Expected_Top2=GetPData_Expected.get_SPANISH_Performance_Data_Expected(18)
                                Expected_Top3=GetPData_Expected.get_SPANISH_Performance_Data_Expected(10)
                                Expected_Bottom1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(12)
                                Expected_Bottom2=GetPData_Expected.get_SPANISH_Performance_Data_Expected(16)
                                Expected_Bottom3=GetPData_Expected.get_SPANISH_Performance_Data_Expected(6)
                            elif self.tablist[ywm]=="Month-to-Date":#date3
                                '''TOP20:Agent8,Agent11,Agent9
                                   BOTTON20:Agent11,Agent9,Agent10'''
                                Expected_Top1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(106)
                                Expected_Top2=GetPData_Expected.get_SPANISH_Performance_Data_Expected(112)
                                Expected_Top3=GetPData_Expected.get_SPANISH_Performance_Data_Expected(108)
                                Expected_Bottom1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(112)
                                Expected_Bottom2=GetPData_Expected.get_SPANISH_Performance_Data_Expected(108)
                                Expected_Bottom3=GetPData_Expected.get_SPANISH_Performance_Data_Expected(110)
                            print Agentname_First_Top20
                            print Expected_Top1['Name'][0] 
                            assert Agentname_First_Top20==Expected_Top1['Name'][0]
                            assert Achieve_First_Top20==Expected_Top1["Achiev"][0]
                            
                            print Agentname_Second_Top20,Expected_Top2['Name'][0]
                            assert Agentname_Second_Top20==Expected_Top2['Name'][0]
                            assert Achieve_Second_Top20==Expected_Top2["Achiev"][0]
                            
                            assert Agentname_Third_Top20==Expected_Top3['Name'][0]
                            assert Achieve_Third_Top20==Expected_Top3["Achiev"][0]
                            
                            assert Agentname_First_Bottom20==Expected_Bottom1['Name'][0]
                            assert Achieve_First_Bottom20==Expected_Bottom1["Achiev"][0]
                            
                            assert Agentname_Second_Bottom20==Expected_Bottom2['Name'][0]
                            assert Achieve_Second_Bottom20==Expected_Bottom2["Achiev"][0]
                            
                            assert Agentname_Third_Bottom20==Expected_Bottom3['Name'][0]
                            assert Achieve_Third_Bottom20==Expected_Bottom3["Achiev"][0]
                        L.logout_tablet()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_SPANISH_Outlier_TL']
    unittest.main()