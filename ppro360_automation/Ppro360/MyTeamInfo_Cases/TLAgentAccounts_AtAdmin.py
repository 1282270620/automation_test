'''
Created on 2018.2.12

@author: yalan.yin

'''
#coding=utf-8
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method import Gl
from AdminSystem_Pages.TLandAgentAccountsPage import TLandAgentAccountsPage
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from public_method.Get_MyTeamContent import Get_MyTeamContent
from public_method.Deleteexistfile import Deleteexistfile
import time
from public_method.TLandAgentAccount_PageNumber import TLandAgentAccount_PageNumber

class TLAgentAccounts_AtAdmin(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="TLAgentAccounts_AtAdmin"
        
        GetData=Get_configration_data()
        
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        self.UserRole="OM"
        self.PageTitle1='My Team'
        self.PageTitle2='Change Password'
        self.SettingButtonExisting='nav-btn-icon fa fa-cog'
        self.BackButtonExisting='nav-btn-text-inner'
        self.Titleexisting='text-center'
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #Myteam file prefix
        #self.filename="'"+lobname+"'_'"+sitename+"'_TLAndAgent"
        self.sheetname="L1 Agent Accounts"


    def tearDown(self):
        pass


    def test_TLAgentAccounts_AtAdmin(self):
        L=Login()
        GetConfig=Get_configration_data()
        AdminHome=AdminHomepage()
        TLandAgent=TLandAgentAccountsPage()
        Deletefile=Deleteexistfile()
        GetMyTeamContent=Get_MyTeamContent()
        TLandAgentPageNumber=TLandAgentAccount_PageNumber()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                Adminurl=GetConfig.get_Test_AdminUrl(lobname)
                ##GET THE CORRECT URL#####
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                    L.Login_admin(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    time.sleep(Gl.waittime)
                    #step13: verify Browse TL/Agent Accounts link shown
                    #print AdminHome.TLAgentAccounts_existing()
                    #assert AdminHome.TLAgentAccounts_existing()=='true'
                    #ENTER TLAgentaccount page
                    AdminHome.Enter_BrowseTLAgentAccounts()
                    # first delete the existing local tlandagent files
                    TotalTLandAgent_page_Dic=TLandAgentPageNumber.get_Total_PageandAgentnumber()
                    print(TotalTLandAgent_page_Dic)
                    TotalTLandAgentNumber_page=TotalTLandAgent_page_Dic['Total_TLandAgentnumber_Onpage']
                    print('total number:',TotalTLandAgentNumber_page)
                    total_pagenumber=TotalTLandAgent_page_Dic["total_pagenumber"]
                    print('total pagenumber:', total_pagenumber)
                    
                    if lobname=='UBER TRANSPORT VOICE':
                        filename='UBERTV'+"_"+sitename+"_L2L1AndAgent"
                        Deletefile.delete_TLandAgentAccountsFile(self.downloadpath)
                    elif lobname=='CENTURYLINK RETENTION':
                        filename='CENTURYLINKRET'+"_"+sitename+"_L2L1AndAgent" 
                        Deletefile.delete_TLandAgentAccountsFile(self.downloadpath)
                         
                    elif lobname not in ('UBER TRANSPORT VOICE','CENTURYLINK RETENTION'):
                        filename=lobname.replace(" ","")+"_"+sitename+"_L2L1AndAgent"#sitename.replace(" ","")
                        Deletefile.delete_TLandAgentAccountsFile(self.downloadpath)                        
                    #click export button
                    TLandAgent.click_ExportButton()
                
                    if total_pagenumber==1:
                        AllTLAgentInfoList_Adminpage=TLandAgent.get_TLandAgentInfoList_anypage()
                        allpageAgentlist=AllTLAgentInfoList_Adminpage
                        print('TLAgentInfo_onadminpage:',  allpageAgentlist)
                    elif total_pagenumber>1:
                        allpageAgentlist=[]
                        pageindex=total_pagenumber+3
                        for i in range(3,pageindex):
                            TLandAgent.click_Pagenumber(i)
                            AllTLAgentInfoList_Adminpage=TLandAgent.get_TLandAgentInfoList_anypage()
                            allpageAgentlist=allpageAgentlist+AllTLAgentInfoList_Adminpage
                            print('TLAgentInfo_onadminpage:',  allpageAgentlist) 
                            
                    
                    
                    #check tl and agent accounts in excel
                    print('=============================get TLandAgentAccounts from excel===============================')
                    print(filename)
                    filename_prefix=filename
                    sheetname=self.sheetname
                    TotaluserNumber=GetMyTeamContent.Get_TotalUserNumber(filename_prefix, sheetname)
                    print(TotaluserNumber)
                    Header_onpage=['Name','HR ID','Password','Title','Team','Activated Date']
                    Header_excel=GetMyTeamContent.Get_MyTeamHeader(filename_prefix, sheetname)
                    print("hearder_excel:", Header_excel)
                    assert Header_onpage==Header_excel
                    AllTLAgentInfo_excel=[]
                    for i in range(i,TotaluserNumber+1):
                        TLAgent_hrid_excel=GetMyTeamContent.Get_HRID(filename_prefix, sheetname)
                    print('tl hrid:', TLAgent_hrid_excel)
                    
                    OneUser=[]
                    for name in TLAgent_hrid_excel:
                        OneUser=[name, TLAgent_hrid_excel[name]]
                        AllTLAgentInfo_excel.append(OneUser)
                    print(AllTLAgentInfo_excel)
                    print('len(AllTLAgentInfo_Adminpage):',len(allpageAgentlist))
                    print('len(AllTLAgentInfo_excel):',len(AllTLAgentInfo_excel))
                    assert len(allpageAgentlist)==len(AllTLAgentInfo_excel)
                    for item in allpageAgentlist:
                        assert item in AllTLAgentInfo_excel                   
                
                    L.logout_admin()
                    
                    
                    
                    
                    
                    
                    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()