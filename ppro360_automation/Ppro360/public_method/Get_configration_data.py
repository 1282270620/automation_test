'''
Created on Dec 20, 2016
@author: Sabrina Guo
'''
import xlrd
#import os
from public_method import Gl
from public_method.Get_file import Get_file
import getpass 
import pytz
import datetime
import calendar
class Get_configration_data():
    
    def __init__(self):
        self.Accountsheetname="Account"
        self.OMuserid="OMuserid"
        self.OMpwd="OMpassword"
        self.LCuserid="LCuserid"
        self.VPuserid="VPuserid"
        self.SVPuserid="SVPuserid"
        self.AdminOMuserid="AdminOMuserid"
        self.SVPpwd="SVPpassword"
        self.AdminURL="Adminurl"
        self.AWS_AdminURL="AWS_Adminurl"
        self.VXI_AdminURL="VXI_Adminurl"
        self.AWS_TabletURL="AWS_Tableturl"
        self.VXI_TabletURL="VXI_Tableturl"
        self.AWSLOBs="AWS_LOBs"
        self.VXILOBs="VXI_LOBs"
        self.TabletURL="Tableturl"
        self.CASE_LOBSITEsheetname="CASE-LOBSITE"
        self.BASE_CONFIGURATIONsheetname="BASE-CONFIGURATION"
        self.DATABASEsheetname="Database"
        self.AllLOBs="All-LOBs"
        self.LOBs_HaveNoLSACS="LOB-HasNoLACSandLACLSModule"
        self.TabletTitle="Tablet-Title"
        self.TabletVerion="Tablet-Version"
        self.coachsheetname="Coaching"
        self.triadcoachsheetname="TriadCoaching"
        self.coachexportsheetname="CoachingExport"
        self.coachtitle="coachpopuptitle"
        self.triadcoachtitle="triadcoachpopuptittle"
        self.coachIDsheetname="CoachingID"
        self.FormDetailHeadersheetname="FormDetailHeader"
        self.SAdminuserid='SuperAdminuserid'
        self.SAdminpwd='SuperAdminpassword'
        self.COACH_prefix="coachingform_"
        self.TRIADCOACH_ALL_prefix="triadcoachingform_all_"
        self.TRIADCOACH_DISABLED_prefix="triadcoachingform_disabled_"
        
        self.filename_prefix_inExcel="coaching_export_"
        
        self.FormCommonParameterSheetname="FormCommonParameter"
        self.CallRecordingNumber1_inExcel="Call_Recording_Number_1"
        self.CallRecordingNumber2_inExcel="Call_Recording_Number_2"
        self.Longtextboxesprefix1_inExcel="Long_text_boxes_prefix_1"
        self.Longtextboxesprefix2_inExcel="Long_text_boxes_prefix_2"
        self.Shorttextboxesprefix1_inExcel="Short_text_boxes_prefix_1"
        self.Shorttextboxesprefix2_inExcel="Short_text_boxes_prefix_2"
        
        self.PerformanceTimeForLOBsSheetname="PerformanceTimeForLOBs"
        self.UploadTodayRosterLobsSheetname='UploadTodayRosterLobs'
        self.TimeTab_Test_inExcel=["daily_report","weekly_report","current_month_report","last_month_report",\
                              "last_two_months_report","daily_report&current_month_report_other",\
                              "daily_report&current_month_report","last_two_months_report&current_month_report"]
        self.Date_Test_inExcel=['Today','Future']  #added for test upload today roster

        self.LobTimeConfigrationsheetname="LobTimeConfigration"
         
    def get_LocalCurrentTime(self):
        CurrentLocalTime=datetime.datetime.now()
        Current_Date=(str(CurrentLocalTime))[0:19]
        return Current_Date
    
    def get_ServerCurrentTime(self):
        tz=pytz.timezone('America/New_York') 
        CurrentServerTime=datetime.datetime.now(tz)
        return CurrentServerTime
    def get_ServerCurrentDate(self):
        CurrentServerTime=self.get_ServerCurrentTime()
        CurrentServerDate=CurrentServerTime.strftime("%Y-%m-%d")
        return CurrentServerDate


    
    def get_LastDate(self,days):
        CurrentServerTime=self.get_ServerCurrentTime()
        LastServerTime=CurrentServerTime-datetime.timedelta(days)
        LastDate=LastServerTime.strftime("%Y%m%d")
        return LastDate
    def get_FirstDayOfanyMonth(self,monthnumber):
        '''monthnumber:0-Current month
                       1-Last month
                       2-Last two month'''
        YM_list=self.get_anyMonth(monthnumber)
        Year_needed=YM_list[0]
        Month_needed=YM_list[1]
        if Month_needed<10:
            FirstDayOfanyMonth=str(Year_needed)+"0"+str(Month_needed)+"01"
        else:
            FirstDayOfanyMonth=str(Year_needed)+str(Month_needed)+"01"
        return FirstDayOfanyMonth
    
    def get_LastDayOfanyMonth(self,monthnumber):
        '''monthnumber:0-Current month
                       1-Last month
                       2-Last two month'''
        YM_list=self.get_anyMonth(monthnumber)
        Year_needed=YM_list[0]
        Month_needed=YM_list[1]
        monthRange = calendar.monthrange(Year_needed, Month_needed)
        lastday=str(monthRange[1])
        if Month_needed<10:
            LastDayOfanyMonth=str(Year_needed)+"0"+str(Month_needed)+lastday
        else:
            LastDayOfanyMonth=str(Year_needed)+str(Month_needed)+lastday
        return LastDayOfanyMonth
    
    def get_anyMonth(self,monthnumber):
        '''monthnumber:0-Current month
                       1-Last month
                       2-Last two month'''
        CurrentServerTime=self.get_ServerCurrentTime().strftime("%Y%m")
        Year=int(CurrentServerTime[0:4])
        Month=CurrentServerTime[4:6]
        if Month[0]=="0":
            Month_int=int(Month[1])
        else:
            Month_int=int(Month)
        
        if Month_int-monthnumber<=0:
            Month_needed=12+(Month_int-monthnumber)
            Year_needed=Year-1
        else:
            Month_needed=Month_int-monthnumber
            Year_needed=Year   
        if Month_needed<10:
            Month_needed="0"+str(Month_needed)
        YM_list=[Year_needed,Month_needed]
        return YM_list
    
    def get_TheDateOfLastAnyMonth(self,monthnumber,time_zone): 
        '''Today of any monthes ago.If it is "Local".'''
        LastAnyMonth_list=self.get_anyMonth(monthnumber)
        
        if time_zone=="Local":
            LocalCurrentDate=(self.get_LocalCurrentTime())[8:19]
        else:
            LocalCurrentDate=str(self.get_ServerCurrentDate())[8:19]
        LastAnyMonth_Date=str(LastAnyMonth_list[0])+'-'+str(LastAnyMonth_list[1])+'-'+LocalCurrentDate 
        return LastAnyMonth_Date
    
    def get_FutureDate(self,days):
        CurrentServerTime=self.get_ServerCurrentTime()
        TFutureServerTime=CurrentServerTime++ datetime.timedelta(days)
        FutureDate=TFutureServerTime.strftime("%Y%m%d")
        return FutureDate
    
    
        
    def get_Tablet_Title(self):
        Tablet_Title=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.TabletTitle)    
        return Tablet_Title
    def get_Tablet_Version(self):
        Tablet_Version=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.TabletVerion)
        return Tablet_Version
    
    def get_AllLOBs_list(self):
        AllLOBs_list=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.AllLOBs).split(",")
        return AllLOBs_list
    
    def get_AllSITEsForEachLOB_list(self,lobname):
        EachLOB_inExcel=lobname+"-SITES"
        AllSITEs_EachLOB_list=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, EachLOB_inExcel).split(",")
        return AllSITEs_EachLOB_list
    
    def get_LOBHasNoLSACS_list(self):
        LOBHasNoLSACS_list=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.LOBs_HaveNoLSACS).split(",")
        return LOBHasNoLSACS_list
    def get_sql_content(self,sheetname,itemname):  
        sql_query=self.get_data_needed(sheetname,itemname)
        return sql_query
    
    def get_SpecialLobforDatabase(self):
        SpecialLob_inExcel='Database-stagespeciallob'
        SpecialLob_list=self.get_data_needed(self.DATABASEsheetname, SpecialLob_inExcel).split(",")
        return SpecialLob_list
    def get_StageDatabaseHost(self):
        StageDatabaseHost_inExcel="Database-stagehost"
        StageDatabaseHost=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, StageDatabaseHost_inExcel)
        return StageDatabaseHost
    def get_StageNodeHost(self,nodeindex):
        StageNodeDatabaseHost_inExcel="Database-stagenodehost"+str(nodeindex)
        StageNodeDatabaseHost=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, StageNodeDatabaseHost_inExcel)
        return StageNodeDatabaseHost
    def get_StageDatabaseUser(self):
        StageDatabaseUser_inExcel="Database-stageuser"
        StageDatabaseUser=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, StageDatabaseUser_inExcel)
        return StageDatabaseUser
    def get_StageDatabasePassword(self):
        StageDatabasePassword_inExcel="Database-stagepassword"
        StageDatabasePassword=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, StageDatabasePassword_inExcel)
        return StageDatabasePassword
    
    
    def get_OMaccount(self):
        OMuserid=str(self.get_data_needed(self.Accountsheetname, self.OMuserid)).replace(".0","")
        OMpassword=str(self.get_data_needed(self.Accountsheetname, self.OMpwd)).replace(".0","")
        OMaccount={"OMuserid":OMuserid,"OMpassword":OMpassword}
        return OMaccount
    def get_SVPaccount(self):
        SVPuserid=str(self.get_data_needed(self.Accountsheetname, self.SVPuserid)).replace(".0","")
        SVPpassword=str(self.get_data_needed(self.Accountsheetname, self.SVPpwd)).replace(".0","")
        SVPaccount={"SVPuserid":SVPuserid,"SVPpassword":SVPpassword}
        return SVPaccount
        
    def get_LCuserid(self):
        LCuserid=str(self.get_data_needed(self.Accountsheetname, self.LCuserid)).replace(".0","")
        return LCuserid
    
    def get_AdminOMaccount(self):
        AdminOMuserid=str(self.get_data_needed(self.Accountsheetname, self.AdminOMuserid)).replace(".0","")
        OMpassword=str(self.get_data_needed(self.Accountsheetname, self.OMpwd)).replace(".0","")
        AdminOMaccount={"AdminOMuserid":AdminOMuserid,"OMpassword":OMpassword}
        return AdminOMaccount
    
    def get_SAdminaccount(self):
        SAdminuserid=str(self.get_data_needed(self.Accountsheetname, self.SAdminuserid)).replace(".0","")
        SAdminpassword=str(self.get_data_needed(self.Accountsheetname, self.SAdminpwd)).replace(".0","")
        AdminOMaccount={"SAdminuserid":SAdminuserid,"SAdminpassword":SAdminpassword}
        print(SAdminpassword)
        return AdminOMaccount
    
    
    def get_VPaccount(self):
        VPuserid=str(self.get_data_needed(self.Accountsheetname, self.VPuserid)).replace(".0","")
        OMpassword=str(self.get_data_needed(self.Accountsheetname, self.OMpwd)).replace(".0","")
        VPaccount={"VPuserid":VPuserid,"OMpassword":OMpassword}
        return VPaccount
    
    def get_AWSLOBs_list(self):
        AWSLOBs_list=(self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.AWSLOBs)).split(",")
        return AWSLOBs_list
    def get_VXILOBs_list(self):
        VXILOBs_list=(self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.VXILOBs)).split(",")
        return VXILOBs_list
    
    def get_AdminUrl(self):
        Adminurl=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.AdminURL)
        return Adminurl
    
    def get_AWS_AdminUrl(self):
        Adminurl=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.AWS_AdminURL)
        return Adminurl
    def get_VXI_AdminUrl(self):
        Adminurl=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.VXI_AdminURL)
        return Adminurl
    def get_AWS_TabletUrl(self):
        Adminurl=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.AWS_TabletURL)
        return Adminurl
    def get_VXI_TabletUrl(self):
        Adminurl=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.VXI_TabletURL)
        return Adminurl
    
    def get_Test_AdminUrl(self,lobname):
        AWSLOBs_list=self.get_AWSLOBs_list()
        VXILOBs_list=self.get_VXILOBs_list()
        if lobname in AWSLOBs_list:
            Adminurl=self.get_AWS_AdminUrl()
        elif lobname in VXILOBs_list:
            Adminurl=self.get_VXI_AdminUrl()
        return Adminurl
    def get_Test_Tablet(self,lobname):
        AWSLOBs_list=self.get_AWSLOBs_list()
        VXILOBs_list=self.get_VXILOBs_list()
        if lobname in AWSLOBs_list:
            tableturl=self.get_AWS_TabletUrl()
        elif lobname in VXILOBs_list:
            tableturl=self.get_VXI_TabletUrl()
        return tableturl
    def get_Test_Hostindex(self,lobname):
        AWSLOBs_list=self.get_AWSLOBs_list()
        VXILOBs_list=self.get_VXILOBs_list()
        AWS_hostindex=93
        VXI_hostindex=92
        if lobname in AWSLOBs_list:
            hostindex=AWS_hostindex
        elif lobname in VXILOBs_list:
            hostindex=VXI_hostindex
        return hostindex
        
    
    
    def get_TabletUrl(self):
        Tableturl=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.TabletURL)
        return Tableturl
    
    def get_LOBSITEtoTest(self,caseID):
        #TestLOBSITE_title=caseID+"_LOBSITE"
        TestLOBSITE_inExcel=caseID
        print("****")
        print(TestLOBSITE_inExcel,)
        print("****")
        LOBSITElist=self.get_data_needed(self.CASE_LOBSITEsheetname, TestLOBSITE_inExcel).split(",")
        return LOBSITElist 
    
    def get_MultiRole_LOBSITEtoTest(self,caseID,role):
        TestLOBSITE_inExcel=caseID
        print("****",)
        print(TestLOBSITE_inExcel,)
        print("****")
        LOBSITElist=self.get_MultiRole_data(self.CASE_LOBSITEsheetname, TestLOBSITE_inExcel, role).split(",")
        return LOBSITElist 
        
    def get_AddCoachingFormTitle(self):
        title=self.get_data_needed(self.coachsheetname, self.coachtitle)
        return title
    def get_AddTriadCoachingFormTitle(self):
        title=self.get_data_needed(self.triadcoachsheetname, self.triadcoachtitle)
        return title
    def get_CoachingExportFormList(self,lobname):
        testcoach_inExcel=self.COACH_prefix+lobname
        coach_list=self.get_data_needed(self.coachexportsheetname, testcoach_inExcel).split(",")
        return coach_list
    def get_CoachingFormList(self,lobname):
        testcoach_inExcel=self.COACH_prefix+lobname
        coach_list=self.get_data_needed(self.coachsheetname, testcoach_inExcel).split(",")
        return coach_list
    
    def get_CoachID(self,Typename):
        testcoachId_inExcel=Typename
        coachID=self.get_data_needed(self.coachIDsheetname, testcoachId_inExcel)
        return coachID
    
    def get_TriadCoachingFormAllList(self,lobname):
        testAlltriadcoach_inExcel=self.TRIADCOACH_ALL_prefix+lobname
        triadcoach_list=self.get_data_needed(self.triadcoachsheetname,testAlltriadcoach_inExcel).split(",")
        return triadcoach_list
    def get_TriadCoachingFormDisabledList(self,lobname):
        testDisabledtriadcoach_inExcel=self.TRIADCOACH_DISABLED_prefix+lobname
        triadcoachDisabled_list=self.get_data_needed(self.triadcoachsheetname, testDisabledtriadcoach_inExcel).split(",")
        return triadcoachDisabled_list
    def get_DefaultDownloadPath(self):
        CurrentUser=getpass.getuser()
#         downloadpath='C:\Users\\'+CurrentUser+'\\'+'Downloads\\'
        downloadpath=r'C:\Users\Administrator\Downloads\\'
        return downloadpath
    def get_CoachfileExportedaddress(self,filenameExported_inExcel):
        downloadpath=self.get_DefaultDownloadPath()
        coachfileaddress=downloadpath+self.get_data_needed(self.BASE_CONFIGURATIONsheetname, filenameExported_inExcel)
        return coachfileaddress
    def get_CoachExportfile_prefix(self):
        CoachExportfilename_prefix=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.filename_prefix_inExcel)
        return  CoachExportfilename_prefix
    def get_PerformanceFile_Directory(self,platform):
        '''platform in [AWS,VXI]'''
        Directory_inExcel=platform+"-PerformanceFile-Directory"
        Directory=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, Directory_inExcel)
        return Directory
        
    def get_FormCommonParameter(self):
        CallRecordingNumber1=self.get_data_needed(self.FormCommonParameterSheetname,self.CallRecordingNumber1_inExcel)
        CallRecordingNumber2=self.get_data_needed(self.FormCommonParameterSheetname,self.CallRecordingNumber2_inExcel)
        Longtextboxesprefix1=self.get_data_needed(self.FormCommonParameterSheetname,self.Longtextboxesprefix1_inExcel)
        Longtextboxesprefix2=self.get_data_needed(self.FormCommonParameterSheetname,self.Longtextboxesprefix2_inExcel)
        Shorttextboxesprefix1=self.get_data_needed(self.FormCommonParameterSheetname,self.Shorttextboxesprefix1_inExcel)
        Shorttextboxesprefix2=self.get_data_needed(self.FormCommonParameterSheetname,self.Shorttextboxesprefix2_inExcel)
        
        FormCommonParameter={"CallRecordingNumber1":CallRecordingNumber1,"CallRecordingNumber2":CallRecordingNumber2,
                             "Longtextboxesprefix1":Longtextboxesprefix1,"Longtextboxesprefix2":Longtextboxesprefix2,
                             "Shorttextboxesprefix1":Shorttextboxesprefix1,"Shorttextboxesprefix2":Shorttextboxesprefix2}
        return FormCommonParameter
    def get_LobsiteDic_From_PerformanceTimeForLOBs(self,column): 
        '''column: 1-VXI
                   2-AWS'''
        Lobsite_Dic={}
        for item in self.TimeTab_Test_inExcel:
            lobsite_list=self.get_data_needed_anyColumn(self.PerformanceTimeForLOBsSheetname, item, column).split(",")
            Lobsite_Dic[item]=lobsite_list
        return Lobsite_Dic
    
    def get_lobsiteDic_From_UploadTodayRosterLobs(self,column): #added for test upload today roster
        Lobsite_Dic={}
        for item in self.Date_Test_inExcel:
            lobsite_list=self.get_data_needed_anyColumn(self.UploadTodayRosterLobsSheetname, item, column).split(",")
            Lobsite_Dic[item]=lobsite_list
        return Lobsite_Dic 
    def get_RostereFile_Directory(self,platform):
        '''platform in [AWS,VXI]'''
        Directory_inExcel=platform+"-RosterFile-Directory"
        Directory=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, Directory_inExcel)
        return Directory
    
    #Get data from database configuration file,this method is for the special lobs
    def get_DatabaseName_ByLobName(self,lobname):
        Testfilename=Gl.DatabaseConfigfilename
        sheetname='LOB_DataBaseName'
        testitem=lobname
        DataBaseName=self.get_data_FromExcel(Testfilename, sheetname, testitem)
        return DataBaseName
    #Get data from database configuration file,this method is for the special sites
    def get_DatabaseName_BySiteName(self,sitename):
        Testfilename=Gl.DatabaseConfigfilename
        sheetname='Site_DataBaseName'
        testitem=sitename
        DataBaseName=self.get_data_FromExcel(Testfilename, sheetname, testitem)
        return DataBaseName
    #Get all special lobs
    def get_Allspeciallobs_ByDataBase(self):
        Testfilename=Gl.DatabaseConfigfilename
        sheetname='Special_lobsite'
        testitem='Special_Lob'
        AllSpecialLobs_list=(self.get_data_FromExcel(Testfilename, sheetname, testitem)).split(",")
        return AllSpecialLobs_list
    def get_Allspecialsites_ByDataBase(self):
        Testfilename=Gl.DatabaseConfigfilename
        sheetname='Special_lobsite'
        testitem='Special_Site'
        AllSpecialSites_list=(self.get_data_FromExcel(Testfilename, sheetname, testitem)).split(",")
        return AllSpecialSites_list
        
    
    
    def get_Lobtime_From_LobTimeConfig(self,lob_site):
        LobSite_inExcel=lob_site
        Timetab=self.get_data_needed(self.LobTimeConfigrationsheetname, LobSite_inExcel)
        return Timetab
    
    def get_data_needed(self,sheetname,testitem): 
        #global dataneeded
        
        G=Get_file()
        Configurationfile=G.Get_fileaddress(Gl.configrationfilename)
        print(Configurationfile)
        Cdata=xlrd.open_workbook(Configurationfile)
        table = Cdata.sheet_by_name(sheetname)
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            if item == testitem:
                dataneeded=table.row_values(i)[1]
        return dataneeded
    
    
    def get_data_FromExcel(self,Testfilename,sheetname,testitem):#Can read data from any file
        G=Get_file()
        Testfile=G.Get_fileaddress(Testfilename)
        Cdata=xlrd.open_workbook(Testfile)
        table = Cdata.sheet_by_name(sheetname)
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            if item == testitem:
                dataneeded=table.row_values(i)[1]
        return dataneeded
    
    def get_data_needed_anyColumn(self,sheetname,testitem,column): 
        global dataneeded
        G=Get_file()
        Configurationfile=G.Get_fileaddress(Gl.configrationfilename)
        Cdata=xlrd.open_workbook(Configurationfile)
        table = Cdata.sheet_by_name(sheetname)
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            print("item:",item)
            print("testitem:",testitem)
            if item == testitem:
                dataneeded=table.row_values(i)[column]
        return dataneeded
    def get_FormDetailHeader_TotalRows(self,Typename):
        testType_inExcel=Typename
        FormDetailHeader_rows=int(self.get_data_needed_anyColumn(self.FormDetailHeadersheetname, testType_inExcel,1))
        return FormDetailHeader_rows 
    def get_anyFormHeaderList_InExcel(self,Typename):
        G=Get_file()
        Configurationfile=G.Get_fileaddress(Gl.configrationfilename)
        Cdata=xlrd.open_workbook(Configurationfile)
        table = Cdata.sheet_by_name(self.FormDetailHeadersheetname)
        nrows=table.nrows
        header_rows=self.get_FormDetailHeader_TotalRows(Typename)
        header_list=[]
        testitem=Typename
        #flag=False
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            if item == testitem:
                for a in range(i, i+header_rows):
                    source_list=table.row_values(a)
                    del source_list[0]
                    del source_list[0]
                    #print "len(source_list):",len(source_list)
                    #print source_list
                    if a==i:
                        b=0
                        while source_list[b]!="Acknowledged Date":
                            b=b+1
                            if b>=len(source_list):
                                break
                        
                    
                    
                        
                                                    
                        
                    source_list=source_list[0:b+1]
                    
                    header_list=header_list+source_list
        return header_list
    
    def get_MultiRole_data(self,sheetname,testitem,role): 
        global dataneeded
        role_list=Gl.role_list
        G=Get_file()
        Configurationfile=G.Get_fileaddress(Gl.configrationfilename)
    
        Cdata=xlrd.open_workbook(Configurationfile)
        table = Cdata.sheet_by_name(sheetname)
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0] 
            if item == testitem:
                for roleindex in range(0,len(role_list)):
                    if role==role_list[roleindex]:
                        dataneeded=table.row_values(i)[roleindex+1]      
        return dataneeded
        
    
    
    
    
    
    #******************Below is some print message************************************
    def get_LOBSITE_STATUS(self,lobsitestring):
        Flag=True
        if lobsitestring=="":#No any configuration for LOB-SITE in LOB-SITE sheet
            print("!!!There is empty for LOBSITE configuration!!!Pleach check out it!!!")
            Flag=False
        elif ":" not in lobsitestring:#The format of LOB-SITE is not correct in LOB-SITE sheet
            print("!!!The format is not correct for LOB-site!!!Pleach check out it!!!")
            Flag=False
        else:
            lobsite_list=lobsitestring.split(":")
            if lobsite_list[0]=="":#No lob is set in LOB-SITE sheet
                print("!!!There is no any lob for test, please check out it!!!")
                Flag=False
            elif lobsite_list[1]=="":#No site is set in LOB-SITE sheet
                print("!!!There is no any site for test, please check out it!!!")
                Flag=False
        return Flag
           
    def print_StartTest_message(self,lobname,sitename):   
        print("Start to test",)
        print(lobname,)
        print("---",)
        print(sitename) 

    def print_EndTest_message(self,lobname,sitename):
        print("**End to test ",)
        print(lobname,)
        print("---",)
        print(sitename,)
        print(": test ok!!")
        print("*")
        print("*")
        print("*")
    #******************Above is some print message************************************
