'''
Created on Feb 12, 2018

@author: symbio
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from public_method.Get_file import Get_file
import os
import time
import Gl
from fileinput import filename
from public_method.AdminSystem_Actions import AdminSystem_Actions
from AdminSystem_Pages.PerformanceUploadPage import PerformanceUploadPage
from AdminSystem_Pages.RosterUploadPage import RosterUploadPage
class UploadPerformanceFileToDoTest(unittest.TestCase):


    def setUp(self):
        Get_Config=Get_configration_data()
        self.VXI_LobSite_Dic=Get_Config.get_LobsiteDic_From_PerformanceTimeForLOBs(1)
        self.AWS_LobSite_Dic=Get_Config.get_LobsiteDic_From_PerformanceTimeForLOBs(2)
        
        self.AWS_Adminurl=Get_Config.get_AWS_AdminUrl()
        self.VXI_Adminurl=Get_Config.get_VXI_AdminUrl()
        
        #Get OM account
        OMaccount=Get_Config.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        self.filetype="performance"
        self.VXI_Directory=Get_Config.get_PerformanceFile_Directory("VXI")
        self.AWS_Directory=Get_Config.get_PerformanceFile_Directory("AWS")


    def tearDown(self):
        pass
    def AWS(self):
        LobSite_Dic=self.AWS_LobSite_Dic
        Adminurl=self.AWS_Adminurl
        print LobSite_Dic
        self.UploadPerformanceFileToDoTest(Adminurl,LobSite_Dic,self.AWS_Directory)
    def test_VXI(self):
        LobSite_Dic=self.VXI_LobSite_Dic
        Adminurl=self.VXI_Adminurl
        self.UploadPerformanceFileToDoTest(Adminurl,LobSite_Dic, self.VXI_Directory)

    
        
    def UploadPerformanceFileToDoTest(self,Adminurl,LobSite_Dic,filedir):
        L=Login()
        AdminHome=AdminHomepage()
        PerUpload=PerformanceUploadPage()
        RosterUpload=RosterUploadPage()
        AdminAction=AdminSystem_Actions()
        Getfile=Get_file()
        for key in LobSite_Dic:
            LobSite_list=LobSite_Dic[key]
            for item in LobSite_list:
                if item=="":
                    print key+':There is no any lob_site in this time tab.'
                else:
                    print item
                    lobsite=item.split("_")
                    #lobname=lobsite[0].upper()[1:]
                    lobname=lobsite[0].upper()
                    print lobname
                    sitename=lobsite[1].upper()
                    filepath=filedir+"\\"+item.lower().replace(" ","").replace("-","")+"\\"
                    print filepath
                    filename_list=os.listdir(filepath)
                    print "filename_list:",filename_list
                    newfilename_list=[]
                    if key=="daily_report":
                        print key,":",LobSite_Dic[key]
                        newfilename_list=self.GetandModify_yesterday_filename(filename_list, filepath)
                    elif key=="weekly_report":
                        newfilename_list=self.GetandModify_weekly_filename(filename_list, filepath)

                    elif key=="last_two_months_report":
                        newfilename_list=self.GetandModify_LastTwoMonth_filename(filename_list, filepath)
                        
                    elif key=="last_two_months_report&current_month_report":
                        newfilename_list=self.GetandModify_LastTwoMonth_filename(filename_list, filepath)+self.GetandModify_currentmonth_filename(filename_list, filepath)
                    elif key=="last_month_report":
                        newfilename_list=self.GetandModify_LastMonth_filename(filename_list, filepath)
                    elif key=="daily_report&current_month_report_other":
                        newfilename_list=self.GetandModify_yesterday_filename(filename_list, filepath)
                    elif key in ("current_month_report","daily_report&current_month_report"):
                        newfilename_list=self.GetandModify_currentmonth_filename(filename_list, filepath)
                    
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
                    print Success_message_actual
                    print Success_message_expected
                    assert Success_message_actual==Success_message_expected
                    
                    
                    #Upload Performance
                    print newfilename_list
                    for item in newfilename_list:
                        filename=os.path.join(filepath,item)
                        AdminHome.Enter_PerformanceUpload()
                        PerUpload.Click_BrowseFlie()
                        print filename
                        print "It starts to upload file:"+item
                        AdminAction.Upload_File(filename)
                        #Step3: Waiting for uploading#Step3: Waiting for uploading
                        '''
                        while PerUpload.get_progressbar()!="icon-view success":
                            print PerUpload.get_progressbar()
                            time.sleep(Gl.waittime)'''
                        time.sleep(10*Gl.waittime)
                        while PerUpload.get_upload_message()=="Data is being processed...":
                            time.sleep(Gl.waittime)
                        Success_message_expected="You successfully uploaded ["+item.lower()+"]"
                        Success_message_actual=PerUpload.get_upload_message()
                        print Success_message_expected
                        print Success_message_actual
                        assert Success_message_actual==Success_message_expected
                        
                    for item in newfilename_list:
                        Getfile.DeleteFile(filepath, item)        
   
                    
    def GetandModify_yesterday_filename(self,filename_list,filepath): 
        Get_Config=Get_configration_data() 
        Getfile=Get_file()    
        newfilename_list=[]
        YesterdayDate=Get_Config.get_LastDate(1)
        file_needupload_list=self.get_filename_needupload(filename_list, "date1", "")
        print file_needupload_list
        print len(file_needupload_list)
        for item in file_needupload_list[0]:
            print item
            newfilename=item.replace("date1",YesterdayDate)
            newfilename_list.append(newfilename)
            Getfile.CopyFile(filepath, item, newfilename)  
        print "Yesterday filename:",newfilename_list
        return newfilename_list     
    def GetandModify_weekly_filename(self,filename_list,filepath): 
        Get_Config=Get_configration_data() 
        Getfile=Get_file()
        '''Yesterday performance files' name has been modified and get all file name'''
        yesterday_newfilename_list=self.GetandModify_yesterday_filename(filename_list, filepath)
        TheDayBeforeYesterdayDate=Get_Config.get_LastDate(2)
        TheDayBeforeYesterday_newfilename_list=[]
        file_needupload_list=self.get_filename_needupload(filename_list, "date2", "")
        print "****file_needupload_list****:",file_needupload_list
        for item in file_needupload_list[0]:
            newfilename=item.replace("date2",TheDayBeforeYesterdayDate)
            TheDayBeforeYesterday_newfilename_list.append(newfilename)
            Getfile.CopyFile(filepath, item, newfilename)  
        newfilename_list=yesterday_newfilename_list+TheDayBeforeYesterday_newfilename_list
        print "Weekly filename:",newfilename_list
        return newfilename_list  
    
    def GetandModify_currentmonth_filename(self,filename_list,filepath):
        Get_Config=Get_configration_data() 
        Getfile=Get_file()
        FirstDay_CurrentMonth_newfilename_list=[]
        '''Yesterday and weekly performance files' name has been modified and get all file name'''
        yesterdayandweekly_newfilename_list=self.GetandModify_weekly_filename(filename_list, filepath)
        print "yesterdayandweekly_newfilename_list:",yesterdayandweekly_newfilename_list
        FirstDay_CurrentMonth=Get_Config.get_FirstDayOfanyMonth(0)
        print "FirstDay_CurrentMonth:",FirstDay_CurrentMonth
        file_needupload_list=self.get_filename_needupload(filename_list, "date3", "")
        for item in file_needupload_list[0]:
            newfilename=item.replace("date3",FirstDay_CurrentMonth)
            FirstDay_CurrentMonth_newfilename_list.append(newfilename)
            Getfile.CopyFile(filepath, item, newfilename) 
        print "FirstDay_CurrentMonth_newfilename_list:",FirstDay_CurrentMonth_newfilename_list
        newfilename_list= yesterdayandweekly_newfilename_list+FirstDay_CurrentMonth_newfilename_list
        print "CurrentMonth filename:",newfilename_list
        return newfilename_list
    def GetandModify_LastMonth_filename(self,filename_list,filepath): 
        Get_Config=Get_configration_data() 
        Getfile=Get_file()
        FirstDay_newfilename_list=[]
        LastDay_newfilename_list=[]
        FirstDay_lastMonth=Get_Config.get_FirstDayOfanyMonth(1)
        LastDay_lastMonth=Get_Config.get_LastDayOfanyMonth(1)
        file_needupload_list=self.get_filename_needupload(filename_list, "date3", "date1")
        for item in file_needupload_list[0]:
            if "date3" in item:
                newfilename=item.replace("date3",FirstDay_lastMonth)
                FirstDay_newfilename_list.append(newfilename)
                Getfile.CopyFile(filepath, item, newfilename)
        for item in file_needupload_list[1]:
            if "date1" in item:
                newfilename=item.replace("date1",LastDay_lastMonth)
                LastDay_newfilename_list.append(newfilename)
                Getfile.CopyFile(filepath, item, newfilename)
                
        newfilename_list=FirstDay_newfilename_list+LastDay_newfilename_list
        print "LastMonth filename:",newfilename_list
        return newfilename_list
        
    def GetandModify_LastTwoMonth_filename(self,filename_list,filepath): 
        Get_Config=Get_configration_data() 
        Getfile=Get_file()
        FirstDay_newfilename_list=[]
        LastDay_newfilename_list=[]
        FirstDay_lasttwoMonth=Get_Config.get_FirstDayOfanyMonth(2)
        LastDay_lasttwoMonth=Get_Config.get_LastDayOfanyMonth(2)
        file_needupload_list=self.get_filename_needupload(filename_list, "date2", "date3")
        for item in file_needupload_list[0]:
            if "date2" in item:
                newfilename=item.replace("date2",FirstDay_lasttwoMonth)
                FirstDay_newfilename_list.append(newfilename)
                Getfile.CopyFile(filepath, item, newfilename)
        for item in file_needupload_list[1]:
            if "date3" in item:
                newfilename=item.replace("date3",LastDay_lasttwoMonth)
                LastDay_newfilename_list.append(newfilename)
                Getfile.CopyFile(filepath, item, newfilename)
                
        newfilename_list=FirstDay_newfilename_list+LastDay_newfilename_list
        print "LasttwoMonth filename:",newfilename_list
        return newfilename_list


    def GetandModify_rosterDate_ToUpload(self,filename_list,filepath):
        Get_Config=Get_configration_data()
        Getfile=Get_file()
        FirstDay_lastThreeMonth=Get_Config.get_FirstDayOfanyMonth(2)
        for item in filename_list:
            if "roster" in item:
                roster_filename=item
        new_roster_filename=roster_filename.replace("date",FirstDay_lastThreeMonth)
        Getfile.CopyFile(filepath, roster_filename, new_roster_filename)
        print new_roster_filename
        
        return new_roster_filename
        
        

    def get_filename_needupload(self,filename_list,date_1,date_2):
        file_needupload_list=[]
        file_needupload_1_list=[]
        file_needupload_2_list=[]
        if date_1 !="":
            for item in filename_list:
                if date_1 in item and "roster" not in item:
                    file_needupload_1_list.append(item)
        file_needupload_list.append(file_needupload_1_list)
        if date_2 !="":
            for item in filename_list:
                if date_2 in item and "roster" not in item:
                    file_needupload_2_list.append(item)
        file_needupload_list.append(file_needupload_2_list)
        return file_needupload_list
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()