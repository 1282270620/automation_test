''' 
Created on 2018-8-3

@author: hanyang.dong

pip install image
pip install pyautogui

set configration_FormCommonParameter_upload_file_path/name/downloadpath...


'''
import unittest
import time
from public_method import Gl
from public_method.Login import Login
from public_method.Get_configration_data import Get_configration_data
from public_method.Get_configration_data_OtherAccount import Get_configration_data_OtherAccount
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from CoachingAndTriadCoaching_Pages.Coaching_Otherfrom_Pages import Coaching_Otherfrom_Pages
from Tablet_pages.PerformancPage import PerformancePage
import os

class OtherForm_PlannedToCompleted(unittest.TestCase):
    def setUp(self):
        #Case ID
        self.caseID="OtherForm_PlannedToCompleted"
        
        GetConfData=Get_configration_data()  
        GetConfDataOA=Get_configration_data_OtherAccount()
        
        self.role_LC=GetConfData.get_LCuserid()
        self.role_OM=GetConfData.get_OMaccount()
        self.role_L2="L2"
        self.role_TL="L1"
        
        self.Call_Recording_Number_1=GetConfDataOA.get_Call_Recording_Number_1()
        
        self.testLOBSITE_list=GetConfData.get_LOBSITEtoTest(self.caseID)
    def test_OtherForm_PlannedToCompleted(self):
        #TSSGP=TabletSystemSwitchGroupPage()
        GetConfData=Get_configration_data()
        #GetConfDataOA=Get_configration_data_OtherAccount()
        Getaccount=Get_AllRoleAccountForTest()
        GetConfDataOA=Get_configration_data_OtherAccount()
        COP=Coaching_Otherfrom_Pages()
        PfP=PerformancePage()
                
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag = GetConfData.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]

                ##GET THE CORRECT URL#####
                adminurl=GetConfData.get_Test_AdminUrl(lobname)
                tableturl=GetConfData.get_Test_Tablet(lobname)
                
                #######Get lob database name########
                #get each site which in this lob
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename = site_list[n]
                    GetConfData.print_StartTest_message(lobname, sitename)
                    
                    loginID = [self.role_LC,self.role_OM,self.role_L2,self.role_TL]
                    x=0
                    if lobname == "AOL": x=1
                    for b in range(x,len(loginID)):
                        L=Login()
                        if self.role_LC == loginID[b]:
                            login_info = Getaccount.get_LCInfo(adminurl, lobname, sitename,self.role_OM["OMuserid"], self.role_OM["OMpassword"], self.role_LC)
                        elif self.role_OM == loginID[b]:
                            login_info = {"Hrid":self.role_OM["OMuserid"],"Password":self.role_OM["OMpassword"]}
                        else:
                            login_info = Getaccount.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.role_OM["OMuserid"], self.role_OM["OMpassword"], loginID[b])
                        
                        print 'login:',tableturl,lobname,sitename,login_info["Hrid"],login_info["Password"]
                        L.Login_tablet(tableturl,lobname,sitename,login_info["Hrid"],login_info["Password"])
                        
                        ##step_start...
                        COP.click_Performance()
                        if loginID[b]==self.role_TL:

                            COP.click_AgentFirstKPI_L1()
                        else:

                            COP.click_TL2Testerlist()
                            COP.click_AgentFirstKPI()
                        PfP.click_addcoachbutton()
                        
                        #COP.click_Otherform()
                        allformlist=COP.get_allformlist()
                        for c in range(0,len(allformlist)):
                            if allformlist[c]=='Other': 
                                COP.click_needclicktheform(c+1)
                                break
                            
                            
                        COP.click_AddButton()
                        print 'AddedMessage:',COP.get_SuccessfullyAddedMessage()
                        assert COP.get_SuccessfullyAddedMessage() == 'Coaching Added'
                        if loginID[b]==self.role_TL:
                            Agent_HRid=COP.get_FirstAgentuserid_L1()
                        else:
                            Agent_HRid=COP.get_FirstAgentuserid()
                        print 'Agent_HRid:',Agent_HRid
                        COP.click_BackButton()
                        COP.click_Coaching()
                        PlannedSN=COP.get_CoachingPlannedSN()
                        COP.click_ThisCoaching()
                        
                        assert COP.get_title() == 'Coaching - Other'
                        #check Button==disabled
                        assert COP.get_CompleteCoachingButton()
                        
          
                        #login
                        L.logout_tablet()
                        AgentInfo=Getaccount.get_TLandAgentInfofromAdmin(adminurl,lobname,sitename,self.role_OM["OMuserid"], self.role_OM["OMpassword"],Agent_HRid)
                        Agent_password=AgentInfo["Password"]
                        print lobname,sitename,Agent_HRid,Agent_password
                        L.Login_tablet(tableturl,lobname,sitename,Agent_HRid,Agent_password)

                        COP.click_Coaching()
                        COP.click_ThisCoaching()
                        Planned_list=[]
                        Planned_list.append(COP.get_shortinput(1,1))
                        Planned_list.append(COP.get_shortinput(1,2))
                        Planned_list.append(COP.get_shortinput(1,3))
                        Planned_list.append(COP.get_shortinput(2,1))
                        Planned_list.append(COP.get_shortinput(2,2))
                        Planned_list.append(COP.get_shortinput(2,3))
                        Planned_list.append(COP.get_shortinput(3,1))
                        Planned_list.append(COP.get_shortinput(3,2))
                        if lobname != "AOL":Planned_list.append(COP.get_shortinput(3,3))
                        if lobname != "AOL":assert COP.get_CallRecordingNumber()
                        assert COP.get_CompletedDate()
                        if lobname == "AOL":assert COP.shortinput_disabled(3,2)
                        else:assert COP.shortinput_disabled(3,3)
                        KPIlist=COP.get_lenKPIlist()
                        nositedict={'BLUE':1,'ISM':1,'ISM SERVICE':1,'ISM HFC':1}
                        if nositedict.has_key(lobname):assert COP.get_KPIlists(4,2)=='fa fa-check-square'
                        else:assert COP.get_KPIlists(5,2)=='fa fa-check-square'
                        
                        d=3
                        while (d < len(KPIlist)):
                            #COP.click_KPIlists(d)
                            if nositedict.has_key(lobname):assert COP.get_KPIlists(4,d)=='fa fa-uncheck'
                            else:assert COP.get_KPIlists(5,d)=='fa fa-uncheck'
                            d += 1;
                        
                        L.logout_tablet()
                        L.Login_tablet(tableturl,lobname,sitename,login_info["Hrid"],login_info["Password"])
                        COP.click_Coaching()
                        COP.click_ThisCoaching()
                        if lobname != "AOL":COP.input_CallRecordingNumber(self.Call_Recording_Number_1)
                        
                        if nositedict.has_key(lobname):
                            if loginID[b]==self.role_TL:
                                COP.click_KPIlists(4,2)
                            else:
                                COP.click_KPIlists(3,2)
                            if loginID[b]==self.role_TL:
                                COP.click_KPIlists(4,len(KPIlist))
                            else:    
                                COP.click_KPIlists(3,len(KPIlist))
                        else:
                            if loginID[b]==self.role_TL:
                                COP.click_KPIlists(5,2)
                            else:
                                COP.click_KPIlists(4,2)
                            if loginID[b]==self.role_TL:
                                COP.click_KPIlists(5,len(KPIlist))
                            else:    
                                COP.click_KPIlists(4,len(KPIlist))
                            
                        COP.click_BrowseFile()
                        
                        COP.uploadfile_loc_1()
                        print COP.get_Uploadsuccess()
                        assert COP.get_Uploadsuccess() == 'Upload Success'
                        COP.click_downloadfile()
                        print GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1(),os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1())
                        assert os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1())==True
                        os.remove(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1())
                        
                        
                        assert COP.get_UpdateAttachment()=='Update Attachment'
                        assert COP.get_Coachstatus()=='Ongoing'
                        #downloadsuccess
                        COP.click_UpdateAttachment()
                        COP.click_BrowseFile_popup()
                        COP.uploadfile_loc_2()
                        print COP.get_Uploadsuccess()
                        assert COP.get_Uploadsuccess()=='Upload Success'
                        
                        print COP.get_Nowfilename(),GetConfDataOA.get_upload_file_name_2()
                        assert COP.get_Nowfilename()==GetConfDataOA.get_upload_file_name_2()
                        COP.click_CompleteCoaching_button()
                        COP.click_CompleteCoaching_yse_button_loc()
                        
                        COP.click_SearchStatus()
                        COP.click_SearchCompleted()
                        COP.click_Filter_button()
                        time.sleep(Gl.waittime*3)
                        CompletedSN=COP.get_CoachingCompletedSN()
                        print PlannedSN,CompletedSN
                        assert  PlannedSN== CompletedSN
                        assert COP.get_CoachingCompletedStatus()=='Completed'
                        COP.click_ThisCoaching()
                        assert COP.get_Coachstatus()=='Completed'
                        
                        if lobname != "AOL":assert COP.get_CallRecordingNumberValue()==''
                    
                        if lobname == "AOL":assert COP.get_shortinput_text(3,2)==''
                        else:assert COP.get_shortinput_text(3,3)==''
                        e=2
                        while (e < len(KPIlist)-1):
                            if nositedict.has_key(lobname):
                                if loginID[b]==self.role_TL:
                                    assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                                else:
                                    assert COP.get_KPIlists(3,e)=='fa fa-uncheck'
                                    
                                if loginID[b]==self.role_TL:
                                    assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                                else:
                                    assert COP.get_KPIlists(3,e)=='fa fa-uncheck'
                                e += 1;
                            else:
                                if loginID[b]==self.role_TL:
                                    assert COP.get_KPIlists(5,e)=='fa fa-uncheck'
                                else:
                                    assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                                    
                                if loginID[b]==self.role_TL:
                                    assert COP.get_KPIlists(5,e)=='fa fa-uncheck'
                                else:
                                    assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                                e += 1;
                        if nositedict.has_key(lobname):
                            if loginID[b]==self.role_TL:
                                assert COP.get_KPIlists(4,len(KPIlist))=='fa fa-check-square'
                            else:
                                assert COP.get_KPIlists(3,len(KPIlist))=='fa fa-check-square'
                        else:
                            if loginID[b]==self.role_TL:
                                assert COP.get_KPIlists(5,len(KPIlist))=='fa fa-check-square'
                            else:
                                assert COP.get_KPIlists(4,len(KPIlist))=='fa fa-check-square'
                       
                        Completed_list=[]
                        Completed_list.append(COP.get_shortinput(1,1))
                        Completed_list.append(COP.get_shortinput(1,2))
                        Completed_list.append(COP.get_shortinput(1,3))
                        Completed_list.append(COP.get_shortinput(2,1))
                        Completed_list.append(COP.get_shortinput(2,2))
                        Completed_list.append(COP.get_shortinput(2,3))
                        Completed_list.append(COP.get_shortinput(3,1))
                        Completed_list.append(COP.get_shortinput(3,2))
                        if lobname != "AOL":Completed_list.append(COP.get_shortinput(3,3))
                        print Completed_list
                        print Planned_list
                        for g in range(0,len(Completed_list)):
                            if g==1:
                                assert Completed_list[g]=='Completed'
                            elif g==5:
                                assert Completed_list[g]==Planned_list[g-3]
                            else:
                                assert Completed_list[g]==Planned_list[g]
                        
                        assert COP.get_printbutton()=='Print'
                        assert COP.get_backbutton()=='Back'
                        COP.click_downloadfile()
                        print GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2(),os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2())
                        assert os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2())==True
                        os.remove(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2())
                        
                        
                        ##step_end.
                        L.logout_tablet()
                        print lobname,sitename,loginID[b],'pass'
                        
                    GetConfData.print_EndTest_message(lobname, sitename)
                        
if __name__ == '__main__':
    unittest.main()
    
'''
class OtherForm_PlannedToCompleted(unittest.TestCase):
    def setUp(self):
        #Case ID
        self.caseID="OtherForm_PlannedToCompleted"
        
        GetConfData=Get_configration_data()
#         #Get URL 
#         self.adminturl=GetConfData.get_AdminUrl()
#         self.tableturl=GetConfData.get_TabletUrl()
        
        
        #Get OM account
        OMaccount=GetConfData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        GetConfDataOA=Get_configration_data_OtherAccount()
        #Get LCaccount
        LCaccount=GetConfDataOA.get_LCaccount()
        self.LCuserid=LCaccount["LCuserid"]
        self.LCpassword=LCaccount["LCpassword"]
        
        #Get L2 account
        L2account=GetConfDataOA.get_L2account()
        self.L2userid=L2account["L2userid"]
        self.L2password=L2account["L2password"]
        
        #Get TL account
        TLaccount=GetConfDataOA.get_TLaccount()
        self.role_TL=TLaccount["role_TL"]
        self.TLpassword=TLaccount["TLpassword"]
        
        self.Call_Recording_Number_1=GetConfDataOA.get_Call_Recording_Number_1()
        
        self.testLOBSITE_list=GetConfData.get_LOBSITEtoTest(self.caseID)
        
    def test_OtherForm_PlannedToCompleted(self):
        #get Lob_list And Site_list
        
    
        #TSSGP=TabletSystemSwitchGroupPage()
        GetConfData=Get_configration_data()
        #GetConfDataOA=Get_configration_data_OtherAccount()
        Getaccount=Get_AllRoleAccountForTest()
        GetConfDataOA=Get_configration_data_OtherAccount()
        COP=Coaching_Otherfrom_Pages()
        PfP=PerformancePage()
        
        
        lobname_list=[]
        sitename_list=[]
        for i in range(0,len(self.testLOBSITE_list)):
            
            each_LOBSITE=self.testLOBSITE_list[i].split(":")
            lobname_list.append(each_LOBSITE[0])
            sitename_list.append(each_LOBSITE[1])
        
        print 'lobname:',lobname_list
        print 'sitename:',sitename_list
        
        
        loginID = [self.LCuserid,self.OMuserid,self.L2userid,self.role_TL]
        loginpassword = [self.LCpassword,self.OMpassword,self.L2password,self.TLpassword]
        for a in range(0,len(lobname_list)):
            ##GET THE CORRECT URL#####
            self.adminturl=GetConfData.get_Test_AdminUrl(lobname_list[a])
            self.tableturl=GetConfData.get_Test_Tablet(lobname_list[a])
            
            x=0
            if lobname_list[a] == "AOL": x=1
            for b in range(x,len(loginID)):
                L=Login()
                print 'login:',self.tableturl,lobname_list[a],sitename_list[a],loginID[b],loginpassword[b]
                L.Login_tablet(self.tableturl,lobname_list[a],sitename_list[a],loginID[b],loginpassword[b])
                
                GetConfData.print_StartTest_message(lobname_list[a], sitename_list[a])
                ##step_start...
                COP.click_Performance()
                if loginID[b]==self.role_TL:
                    time.sleep(Gl.waittime)
                    COP.click_AgentFirstKPI_L1()
                else:
                    time.sleep(Gl.waittime)
                    COP.click_TL2Testerlist()
                    COP.click_AgentFirstKPI()
                PfP.click_addcoachbutton()
                
                #COP.click_Otherform()
                allformlist=COP.get_allformlist()
                for c in range(0,len(allformlist)):
                    if allformlist[c]=='Other': 
                        COP.click_needclicktheform(c+1)
                        break
                        
                COP.click_AddButton()
                print 'AddedMessage:',COP.get_SuccessfullyAddedMessage()
                assert COP.get_SuccessfullyAddedMessage() == 'Coaching Added'
                if loginID[b]==self.role_TL:
                    Agent_HRid=COP.get_FirstAgentuserid_L1()
                else:
                    Agent_HRid=COP.get_FirstAgentuserid()
                print 'Agent_HRid:',Agent_HRid
                COP.click_BackButton()
#                 time.sleep(1)
                COP.click_Coaching()
                PlannedSN=COP.get_CoachingPlannedSN()
#                 time.sleep(Gl.waittime)
                COP.click_ThisCoaching()
                
                assert COP.get_title() == 'Coaching - Other'
                #check Button==disabled
                assert COP.get_CompleteCoachingButton()
                
  
                #login
                L.logout_tablet()
                AgentInfo=Getaccount.get_TLandAgentInfofromAdmin(self.adminturl,lobname_list[a],sitename_list[a],self.OMuserid,self.OMpassword,Agent_HRid)
                #Agent_Name=AgentInfo["Name"]
                #Agent_hrid=AgentInfo["Hrid"]
                Agent_password=AgentInfo["Password"]
                print lobname_list[a],sitename_list[a],Agent_HRid,Agent_password
                L.Login_tablet(self.tableturl,lobname_list[a],sitename_list[a],Agent_HRid,Agent_password)
                #
                time.sleep(Gl.waittime)
                COP.click_Coaching()
#                 time.sleep(Gl.waittime)
                COP.click_ThisCoaching()
                Planned_list=[]
                Planned_list.append(COP.get_shortinput(1,1))
                Planned_list.append(COP.get_shortinput(1,2))
                Planned_list.append(COP.get_shortinput(1,3))
                Planned_list.append(COP.get_shortinput(2,1))
                Planned_list.append(COP.get_shortinput(2,2))
                Planned_list.append(COP.get_shortinput(2,3))
                Planned_list.append(COP.get_shortinput(3,1))
                Planned_list.append(COP.get_shortinput(3,2))
                if lobname_list[a] != "AOL":Planned_list.append(COP.get_shortinput(3,3))
                if lobname_list[a] != "AOL":assert COP.get_CallRecordingNumber()
                assert COP.get_CompletedDate()
                if lobname_list[a] == "AOL":assert COP.shortinput_disabled(3,2)
                else:assert COP.shortinput_disabled(3,3)
                KPIlist=COP.get_lenKPIlist()
                nositedict={'BLUE':1,'ISM':1,'ISM SERVICE':1,'ISM HFC':1}
                if nositedict.has_key(lobname_list[a]):assert COP.get_KPIlists(4,2)=='fa fa-check-square'
                else:assert COP.get_KPIlists(5,2)=='fa fa-check-square'
                
                d=3
                while (d < len(KPIlist)):
                    #COP.click_KPIlists(d)
                    if nositedict.has_key(lobname_list[a]):assert COP.get_KPIlists(4,d)=='fa fa-uncheck'
                    else:assert COP.get_KPIlists(5,d)=='fa fa-uncheck'
                    d += 1;
                
                L.logout_tablet()
                L.Login_tablet(self.tableturl,lobname_list[a],sitename_list[a],loginID[b],loginpassword[b])
#                 time.sleep(Gl.waittime)
                COP.click_Coaching()
#                 time.sleep(Gl.waittime)
                COP.click_ThisCoaching()
                if lobname_list[a] != "AOL":COP.input_CallRecordingNumber(self.Call_Recording_Number_1)
                
                if nositedict.has_key(lobname_list[a]):
                    if loginID[b]==self.role_TL:
                        COP.click_KPIlists(4,2)
                    else:
                        COP.click_KPIlists(3,2)
                    if loginID[b]==self.role_TL:
                        COP.click_KPIlists(4,len(KPIlist))
                    else:    
                        COP.click_KPIlists(3,len(KPIlist))
                else:
                    if loginID[b]==self.role_TL:
                        COP.click_KPIlists(5,2)
                    else:
                        COP.click_KPIlists(4,2)
                    if loginID[b]==self.role_TL:
                        COP.click_KPIlists(5,len(KPIlist))
                    else:    
                        COP.click_KPIlists(4,len(KPIlist))
                    
                COP.click_BrowseFile()
                
                COP.uploadfile_loc_1()
                print COP.get_Uploadsuccess()
                assert COP.get_Uploadsuccess() == 'Upload Success'
                COP.click_downloadfile()
                print GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1(),os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1())
                assert os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1())==True
                os.remove(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_1())
                
                
                assert COP.get_UpdateAttachment()=='Update Attachment'
                assert COP.get_Coachstatus()=='Ongoing'
                #downloadsuccess
                COP.click_UpdateAttachment()
                COP.click_BrowseFile_popup()
                COP.uploadfile_loc_2()
                print COP.get_Uploadsuccess()
                assert COP.get_Uploadsuccess()=='Upload Success'
                
#                 time.sleep(1)
                print COP.get_Nowfilename(),GetConfDataOA.get_upload_file_name_2()
                assert COP.get_Nowfilename()==GetConfDataOA.get_upload_file_name_2()
                COP.click_CompleteCoaching_button()
                COP.click_CompleteCoaching_yse_button_loc()
                
                COP.click_SearchStatus()
                COP.click_SearchCompleted()
                COP.click_Filter_button()
                time.sleep(Gl.waittime*3)
                CompletedSN=COP.get_CoachingCompletedSN()
                print PlannedSN,CompletedSN
                assert  PlannedSN== CompletedSN
                assert COP.get_CoachingCompletedStatus()=='Completed'
                COP.click_ThisCoaching()
#                 time.sleep(1)
                assert COP.get_Coachstatus()=='Completed'
                
                if lobname_list[a] != "AOL":assert COP.get_CallRecordingNumberValue()==''
            
                if lobname_list[a] == "AOL":assert COP.get_shortinput_text(3,2)==''
                else:assert COP.get_shortinput_text(3,3)==''
                e=2
                while (e < len(KPIlist)-1):
                    if nositedict.has_key(lobname_list[a]):
                        if loginID[b]==self.role_TL:
                            assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                        else:
                            assert COP.get_KPIlists(3,e)=='fa fa-uncheck'
                            
                        if loginID[b]==self.role_TL:
                            assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                        else:
                            assert COP.get_KPIlists(3,e)=='fa fa-uncheck'
                        e += 1;
                    else:
                        if loginID[b]==self.role_TL:
                            assert COP.get_KPIlists(5,e)=='fa fa-uncheck'
                        else:
                            assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                            
                        if loginID[b]==self.role_TL:
                            assert COP.get_KPIlists(5,e)=='fa fa-uncheck'
                        else:
                            assert COP.get_KPIlists(4,e)=='fa fa-uncheck'
                        e += 1;
                if nositedict.has_key(lobname_list[a]):
                    if loginID[b]==self.role_TL:
                        assert COP.get_KPIlists(4,len(KPIlist))=='fa fa-check-square'
                    else:
                        assert COP.get_KPIlists(3,len(KPIlist))=='fa fa-check-square'
                else:
                    if loginID[b]==self.role_TL:
                        assert COP.get_KPIlists(5,len(KPIlist))=='fa fa-check-square'
                    else:
                        assert COP.get_KPIlists(4,len(KPIlist))=='fa fa-check-square'
                #
                Completed_list=[]
                Completed_list.append(COP.get_shortinput(1,1))
                Completed_list.append(COP.get_shortinput(1,2))
                Completed_list.append(COP.get_shortinput(1,3))
                Completed_list.append(COP.get_shortinput(2,1))
                Completed_list.append(COP.get_shortinput(2,2))
                Completed_list.append(COP.get_shortinput(2,3))
                Completed_list.append(COP.get_shortinput(3,1))
                Completed_list.append(COP.get_shortinput(3,2))
                if lobname_list[a] != "AOL":Completed_list.append(COP.get_shortinput(3,3))
                print Completed_list
                print Planned_list
                for g in range(0,len(Completed_list)):
                    if g==1:
                        assert Completed_list[g]=='Completed'
                    elif g==5:
                        assert Completed_list[g]==Planned_list[g-3]
                    else:
                        assert Completed_list[g]==Planned_list[g]
                
                assert COP.get_printbutton()=='Print'
                assert COP.get_backbutton()=='Back'
                COP.click_downloadfile()
                print GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2(),os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2())
                assert os.path.exists(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2())==True
                os.remove(GetConfData.get_DefaultDownloadPath()+GetConfDataOA.get_upload_file_name_2())
                
                
                ##step_end.
                L.logout_tablet()
                print lobname_list[a],sitename_list[a],loginID[b],'pass'
                
                GetConfData.print_EndTest_message(lobname_list[a], sitename_list[a])
                
            
        
        
if __name__ == '__main__':
    unittest.main()
'''
