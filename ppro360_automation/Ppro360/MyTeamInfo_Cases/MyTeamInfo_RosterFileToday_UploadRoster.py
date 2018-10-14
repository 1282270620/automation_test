'''
Created on 2018.4.13

@author: yalan.yin
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from public_method.Get_file import Get_file
import os
from AdminSystem_Pages.RosterHistoryPage import RosterHistoryPage
#import Gl
from fileinput import filename
from public_method.AdminSystem_Actions import AdminSystem_Actions
from AdminSystem_Pages.PerformanceUploadPage import PerformanceUploadPage
from AdminSystem_Pages.RosterUploadPage import RosterUploadPage

class MyTeamInfo_RosterFileToday_UploadRoster(unittest.TestCase):


    def setUp(self):
        Get_Config=Get_configration_data()
        self.VXI_LobSite_Dic=Get_Config.get_lobsiteDic_From_UploadTodayRosterLobs(1)
        self.AWS_LobSite_Dic=Get_Config.get_lobsiteDic_From_UploadTodayRosterLobs(2)
        
        self.AWS_Adminurl=Get_Config.get_AWS_AdminUrl()
        self.VXI_Adminurl=Get_Config.get_VXI_AdminUrl()
        
        #Get OM account
        OMaccount=Get_Config.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        self.filetype="roster"
        self.VXI_Directory=Get_Config.get_RostereFile_Directory("VXI")
        self.AWS_Directory=Get_Config.get_RostereFile_Directory("AWS")
        
    def test_AWS(self):
        LobSite_Dic=self.AWS_LobSite_Dic
        Adminurl=self.AWS_Adminurl
        print(LobSite_Dic)
        self.MyTeamInfo_RosterFileToday_UploadRoster(Adminurl,LobSite_Dic,self.AWS_Directory)
    def VXI(self):
        LobSite_Dic=self.VXI_LobSite_Dic
        Adminurl=self.VXI_Adminurl
        self.MyTeamInfo_RosterFileToday_UploadRoster(Adminurl,LobSite_Dic, self.VXI_Directory)

    def tearDown(self):
        pass

    def MyTeamInfo_RosterFileToday_UploadRoster(self,Adminurl,LobSite_Dic,filedir):
        L=Login()
        AdminHome=AdminHomepage()
        PerUpload=PerformanceUploadPage()
        RosterUpload=RosterUploadPage()
        RosterPage=RosterHistoryPage()
        AdminAction=AdminSystem_Actions()
        for key in LobSite_Dic:
            LobSite_list=LobSite_Dic[key]
            for item in LobSite_list:
                if item=="":
                    print(key+':T here is no any lob_site in this time tab.')
                else:
                    print(item)
                    lobsite=item.split("_")
                    #lobname=lobsite[0].upper()[1:]
                    lobname=lobsite[0].upper()
                    print(lobname)
                    sitename=lobsite[1].upper()
                    filepath=filedir+"\\"+item.lower().replace(" ","").replace("-","")+"\\"
                    print(filepath)
                    filename_list=os.listdir(filepath)
                    print("filename_list:",filename_list)
                    
                    #Roster file                    
                    rosterfilename=self.GetandModify_rosterDate_ToUpload(filename_list, filepath)
                    rosterfile_ToUpload=os.path.join(filepath,rosterfilename)
                    L.Login_admin(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    #Upload roster
                    AdminHome.Enter_RoserUpload()
                    RosterUpload.Click_BrowseFlie()
                    AdminAction.Upload_File(rosterfile_ToUpload)
                    Success_message_expected="You successfully uploaded ["+rosterfilename.lower()+"]"
                    Success_message_actual=PerUpload.get_upload_message()
                    print(Success_message_actual)
                    print(Success_message_expected)
                    assert Success_message_actual==Success_message_expected
                    #step 2-1) click browse upload history
                    RosterUpload.click_BrowseUploadHistory()
                    RosterPage.Click_anyRosterRecord(1)
                    assert RosterPage.is_CurrentActiveExist(1)=='active-text'
                    #step 2-2) click Download
                    RosterPage.Click_Download(1)
                    
                    
        
        
    def GetandModify_rosterDate_ToUpload(self,filename_list,filepath):   
        Get_Config=Get_configration_data()
        Getfile=Get_file()
        Date_Today=Get_Config.get_ServerCurrentDate().replace("-","")
        for item in filename_list:
            if "roster" in item:
                roster_filename=item
        new_roster_filename=roster_filename.replace("date",Date_Today)
        Getfile.CopyFile(filepath, roster_filename, new_roster_filename)
        print(new_roster_filename)
        
        return new_roster_filename
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()