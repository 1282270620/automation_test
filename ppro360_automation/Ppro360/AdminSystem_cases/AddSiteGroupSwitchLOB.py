'''
Created on 2018/8/1

@author: hanyang.dong
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Get_configration_data_OtherAccount import Get_configration_data_OtherAccount
#from VPSVPAccountManagement_Pages.Loblist_ForvpOrsvp import Loblist_ForvpOrsvp
from public_method.Login import Login
#import time
from AdminSystem_Pages.AdminSystemAddGroupPage import AdminSystemAddGroupPage
from Tablet_pages.TabletSystemSwitchGroupPage import TabletSystemSwitchGroupPage
from public_method.Check_Tablet import Check_Tablet



class AddSiteGroupSwitchLOB(unittest.TestCase):
    
    def setUp(self):
        #Case ID
        self.caseID="AddSiteGroupSwitchLOB"
        
        GetData=Get_configration_data()
        #Get URL 
        self.adminturl=GetData.get_AdminUrl()
        self.tableturl=GetData.get_TabletUrl()
        
        
        #Get SVP account
        SVPaccount=GetData.get_SVPaccount()
        self.SVPuserid=SVPaccount["SVPuserid"]
        self.SVPpassword=SVPaccount["SVPpassword"]
        
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        GetDataOA=Get_configration_data_OtherAccount()
        #Get SuperAdminaccount
        SuperAdminaccount=GetDataOA.get_SuperAdminaccount()
        self.SuperAdminuserid=SuperAdminaccount["SuperAdminuserid"]
        self.SuperAdminpassword=SuperAdminaccount["SuperAdminpassword"]
        
        #Get L2 account
        L2account=GetDataOA.get_L2account()
        self.L2userid=L2account["L2userid"]
        self.L2password=L2account["L2password"]
        
        #Get TL account
        TLaccount=GetDataOA.get_TLaccount()
        self.TLuserid=TLaccount["TLuserid"]
        self.TLpassword=TLaccount["TLpassword"]
        
        #Get Agent account
        Agentaccount=GetDataOA.get_Agentaccount()
        self.Agentuserid=Agentaccount["Agentuserid"]
        self.Agentpassword=Agentaccount["Agentpassword"]
        
        #Get LC userid
        self.LCuserid=GetData.get_LCuserid()
        #Get all lobs from Uber
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        
        
        
    def test_AddSiteGroup(self):
        #Add Group
        #TSSGP=TabletSystemSwitchGroupPage()
        #GetData=Get_configration_data()
        GetDataOA=Get_configration_data_OtherAccount()
        
        lobname_list=[]
        NeedclickLOBsname=[]
        for i in range(0,len(self.testLOBSITE_list)):

            each_LOBSITE=self.testLOBSITE_list[i].split(":")
            lobname_list.append(each_LOBSITE[0])
            NeedclickLOBsname.append('+ '+each_LOBSITE[0])
            sitename=each_LOBSITE[1]
            

        print 'lobname:',lobname_list
        print 'NeedclickLOBsname:',NeedclickLOBsname
        print 'sitename:',sitename

        
        L=Login()
        L.Login_admin(self.adminturl,lobname_list[0],sitename,self.SuperAdminuserid,self.SuperAdminpassword)
        
        
        #LOBlist_svp=Loblist_ForvpOrsvp()
        ASAGP=AdminSystemAddGroupPage()
        ASAGP.click_SwitchLoBConfig()
        ASAGP.click_Browse()
          
        
        #print 'YOUNGSTOWNGroup:',ASAGP.get_YOUNGSTOWNGroup()
        
        ASAGP.click_Add()
        ASAGP.get_alllobsInGroup()
        lobs_page_list=ASAGP.get_alllobsInGroup()
        lobs_config_list=GetDataOA.get_AllLOBs_list()
        
        list(lobs_config_list)
        lobs_page_list.sort()
        lobs_config_list.sort()
        lobs_config_list.remove('AOL')
        print lobs_page_list
        print lobs_config_list
        for e in range(0,len(lobs_page_list)):
            #print lobs_page_list[e]
            #print '+ '+lobs_config_list[e]
            assert '+ '+lobs_config_list[e]==lobs_page_list[e]
            
        print 'LOBList Check Done:Pass--------------------'
        ASAGP.input_GroupName('YOUNGSTOWN Group')
        
        lobs_page_list=ASAGP.get_alllobsInGroup()
        for a in range(0,len(NeedclickLOBsname)):
            for b in range(0,len(lobs_page_list)):
                if lobs_page_list[b]==NeedclickLOBsname[a]:
                    #print lobs_page_list[b]
                    #print NeedclickLOBs[a]
                    ASAGP.click_SwitchAddLOBGroup(b+1)
                    if lobs_page_list[b]==NeedclickLOBsname[0]:
                        LOB_site_list=ASAGP.get_dtvdssitesInGroup()
                        list(LOB_site_list)
                        print 'sitelist:',LOB_site_list
                        for c in range(0,len(LOB_site_list)):
                            if LOB_site_list[c]==sitename:
                                ASAGP.click_SwitchAddsiteGroup(c+1)
                    
        ASAGP.click_Add()
        print 'AddGroupDone-------------'    
        L.logout_admin()
    
    def test_SwitchLOB(self):
        TSSGP=TabletSystemSwitchGroupPage()
        L=Login()
        CT=Check_Tablet()
        loginID = [self.SVPuserid,self.OMuserid,self.L2userid,self.TLuserid,self.Agentuserid]
        loginpassword = [self.SVPpassword,self.OMpassword,self.L2password,self.TLpassword,self.Agentpassword]
        
        for z in range(0,4):
            L.Login_tablet(self.tableturl,'DTVDS','YOUNGSTOWN',loginID[z],loginpassword[z])
            if self.SVPuserid==loginID[z]:role='SVP'
            elif self.OMuserid==loginID[z]:role='L3'
            elif self.L2userid==loginID[z]:role='L2'
            elif self.TLuserid==loginID[z]:role='L1'
            else: role='Agent'
            print 'Check Account:',role+'---------------------'
            CT.Check_TabletHomepageCircle_ByRole('DTVDS',role)
            TSSGP.click_Setbutton()         
            TSSGP.click_SwitchLob(role)
            TSSGP.click_Switchlist(role)
            
            loblist=TSSGP.get_alllobsInGroup(role)
            print loblist
            for e in range(2,len(loblist)+1):
                
                TSSGP.click_Switchlists(e,role)
                TSSGP.click_Switchbutton(role)
                print 'check site:',role,loblist[e-1]+'------------------'
                CT.Check_TabletHomepageCircle_ByRole(loblist[e-1],role)
                
                TSSGP.click_Setbutton()         
                TSSGP.click_SwitchLob(role)     #Switchlob
                TSSGP.click_Switchlist(role)
                
            TSSGP.click_Switchlob_cancel_loc(role)
            L.logout_tablet()
        print 'ALL Done -------------- '    
        
    


if __name__ == '__main__':
    unittest.main()