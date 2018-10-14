'''
Created on Jun 16, 2018

@author: Sabrina Guo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Check_Tablet import Check_Tablet
from public_method.HandleMySQL import HandleMySQL
from Tablet_pages.LeaderAcademyCoachingLeaderScorespage import LeaderAcademyCoachingLeaderScorespage
import time
from public_method.DatePicker_Method import DatePicker_Method
class CoachingLeaderScores_OMDefault(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="CoachingLeaderScores_OMDefault"
        
        GetData=Get_configration_data()
        
        
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.role="L3"
        #Get LOBs have no LSACS
        self.LOBs_NoLSACS_list=GetData.get_LOBHasNoLSACS_list()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Get AWS LOBs
        self.AWSLOBs_list=GetData.get_AWSLOBs_list()
        #Get VXI LOBs
        self.VXILOBs_list=GetData.get_VXILOBs_list()
        #Info of configuration
        self.sqlsheetname="SQLs"
        self.sql_TLs_ByL3="Sql_TLs_ByL3_LeaderAcademyCoachingLeaderScorespage"
        self.sql_TLsValue_ByL3="Sql_KPIValueOfTLs_ByL3_LeaderAcademyCoachingLeaderScorespage"
        self.sql_AVGSCOREOFFORM_ByL3="Sql_AVGSCOREOFFORM_ByL3_LeaderAcademyCoachingLeaderScorespage"
        
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        self.KPInumber=11
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()


    def tearDown(self):
        pass


    def test_CoachingLeaderScores_OMDefault(self):
        GetConfig=Get_configration_data()
        L=Login()
        Tablet=TabletHomepage()
        CheckTablet=Check_Tablet()
        HMysql=HandleMySQL()
        LACLS=LeaderAcademyCoachingLeaderScorespage()
        DatePicker=DatePicker_Method()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                tableturl=GetConfig.get_Test_Tablet(lobname)
                hostindex=GetConfig.get_Test_Hostindex(lobname)
                ##GET THE CORRECT URL#####
                #######Get lob database name########
                if lobname in self.AllSpecialLobs_list:
                    lobname_database=GetConfig.get_DatabaseName_ByLobName(lobname)
                else:
                    lobname_database=lobname
                #######Get lob database name########
                if lobname in self.LOBs_NoLSACS_list:
                    print lobname," does not have LeadershipAcademyCoachingScores module."
                else:
                    #Get Site to test
                    site_list=each_LOBSITE[1].split("*")
                    for n in range(0,len(site_list)):
                        sitename=site_list[n]
                        GetConfig.print_StartTest_message(lobname, sitename)
                        #######Get Site database name########
                        lob_site=lobname+':'+sitename
                        if lob_site in self.AllSpecialSites_list:
                            sitename_database=GetConfig.get_DatabaseName_BySiteName(lob_site)
                        else:
                            sitename_database=sitename
                        #######Get Site database name########
                        #Step1:Enter ''Leader Academy Coaching Leader Scores' with OM Login
                        L.Login_tablet(tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                        Tablet.Enter_LeadersAcademyCoachingLeaderScoresPage()
                        
                        #Step2:Check the date value
                        CheckTablet.Check_DefaltDateValue_LeadersAcademyCoachingLeaderScores()
                        #Step3:Check all TLs
                        #Step3.1:Get all TLs from DataBase
                        sql_TLs_ByL3=GetConfig.get_sql_content(self.sqlsheetname, self.sql_TLs_ByL3)
                        AllTLsInfo_DataBase=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_TLs_ByL3)
                        print AllTLsInfo_DataBase
                        AllTLsAccount_DataBase=list(AllTLsInfo_DataBase[1])
                        AllTLsName_DataBase=[]
                        for item in AllTLsAccount_DataBase:
                            name=item[1]+" "+item[2]
                            AllTLsName_DataBase.append(name)
                        AllTLsName_DataBase.sort()
                        print AllTLsName_DataBase
                        #Step3.2:Get all TLs from Page
                        AllTLsName_FromPage=(LACLS.get_AllTLname_list())[0]
                        AllTLsName_FromPage.sort()
                        print AllTLsName_FromPage
                        
                        CheckTablet.CheckData_DataBaseAndPage(AllTLsName_DataBase, AllTLsName_FromPage)
                        
                        #Step4:Check all TLs' KPI Value
                        #Step4.1:Get tls' kpi value from page
                        TLnumber=len(AllTLsName_FromPage)
                        AllTLsScores_FromPage=LACLS.get_AllTLvalue_ByL3(TLnumber, self.KPInumber)
                        print AllTLsScores_FromPage
                        AllTLsKPIVaule_FromPage={}
                        for key in AllTLsScores_FromPage:
                            AllTLsKPIVaule_FromPage[key]=AllTLsScores_FromPage[key][:-1]
                        #AllTLsKPIVaule_FromPage=AllTLsScores_FromPage[1][:-1]
                        print AllTLsKPIVaule_FromPage
                        #Step4.2:Get tls' kpi value from database
                        Current_Date=GetConfig.get_LocalCurrentTime()
                        LastSixMonth_Date=GetConfig.get_TheDateOfLastAnyMonth(6, "Local")
                        print LastSixMonth_Date
                        print Current_Date
                        Sql_TLsValue_ByL3=GetConfig.get_sql_content(self.sqlsheetname, self.sql_TLsValue_ByL3).replace("DateType","acknowledge").replace("LastSixMonth_Date",LastSixMonth_Date).replace("Current_Date",Current_Date)
                        AllTLsKPIinf_DataBase=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, Sql_TLsValue_ByL3)
                        AllTLsKPIinf=list(AllTLsKPIinf_DataBase[1])
                        #print AllTLsKPIinf
                        AllTLsKPIVaule_DataBase={}
                        print AllTLsKPIinf
                        for item in AllTLsKPIinf:
                            tlinfo=list(item)
                            tlhrid=tlinfo[0]
                            tlkpivalue=tlinfo[1:self.KPInumber]
                            #Avg=LACLS.get_avgData(tlkpivalue)
                            #tlkpivalue.append(Avg)
                            for i in range(0,len(tlkpivalue)):
                                if tlkpivalue[i]!=None:
                                    tlkpivalue[i]=str(tlkpivalue[i])
                            AllTLsKPIVaule_DataBase[tlhrid]=tlkpivalue
                        print AllTLsKPIVaule_DataBase
                        for key in AllTLsKPIVaule_FromPage:
                            CheckTablet.CheckData_DataBaseAndPage(AllTLsKPIVaule_DataBase[key], AllTLsKPIVaule_FromPage[key])
                            
                        #Step5:Check AVERAGE SCORE OF FORM
                        #Step5.1:Get AVERAGE SCORE OF FORM from Page
                        AllAVGSCOREOFFOR=LACLS.get_anyTLvalueWithL3Login(TLnumber+1, self.KPInumber)
                        AllAVGSCOREOFFORM_FromPage=AllAVGSCOREOFFOR[:-1]
                        print "AllAVGSCOREOFFORM_FromPage:",AllAVGSCOREOFFORM_FromPage
                        #Step5.2:Get AVERAGE SCORE OF FORM from DataBase
                        LastSixMonth_Date_need=LastSixMonth_Date[:(LastSixMonth_Date.find(" "))]
                        Current_Date_need=Current_Date[:(Current_Date.find(" "))]
                        print LastSixMonth_Date_need
                        print Current_Date_need
                        sql_AVGSCOREOFFORM_ByL3=GetConfig.get_sql_content(self.sqlsheetname, self.sql_AVGSCOREOFFORM_ByL3).replace("DateType","acknowledge").replace("LastSixMonth_Date",LastSixMonth_Date_need).replace("Current_Date",Current_Date_need)
                        AllAVGSCOREOFFORM=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_AVGSCOREOFFORM_ByL3)
                        print AllAVGSCOREOFFORM
                        AllAVGSCOREOFFORM_DataBase=list(AllAVGSCOREOFFORM[1][0])
                        for i in range(0,len(AllAVGSCOREOFFORM_DataBase)):
                            AllAVGSCOREOFFORM_DataBase[i]=str(AllAVGSCOREOFFORM_DataBase[i])
                        print "AllAVGSCOREOFFORM_DataBase:",AllAVGSCOREOFFORM_DataBase
                        
                        CheckTablet.CheckData_DataBaseAndPage(AllAVGSCOREOFFORM_DataBase, AllAVGSCOREOFFORM_FromPage)
                        
                        #Step6: Check AVG SCORE OF TL
                        #Step6.1: Get AVG SCORE OF TL from page
                        AVGSCOREOFTL_FromPage={}
                        for key in AllTLsScores_FromPage:
                            AVGSCOREOFTL_FromPage[key]=AllTLsScores_FromPage[key][-1]
                        print "AVGSCOREOFTL_FromPage:",AVGSCOREOFTL_FromPage
                        #Step6.2:AVG SCORE OF TL from Calculate  
                        AVGSCOREOFTL_Calculate={}
                        for key in AllTLsKPIVaule_FromPage:
                            sum_AVG=0
                            totalnumber=0
                            for item in AllTLsKPIVaule_FromPage[key]:
                                if item!='N/A':
                                    totalnumber=totalnumber+1
                                    sum_AVG=sum_AVG+float(item)
                                    
                            AVGSCOREOFTL_Calculate[key]= str(round((sum_AVG/totalnumber),2))
                        print "AVGSCOREOFTL_Calculate:",AVGSCOREOFTL_Calculate
                        for key in AVGSCOREOFTL_Calculate:
                            CheckTablet.CheckData_DataBaseAndPage([AVGSCOREOFTL_Calculate[key]], [AVGSCOREOFTL_FromPage[key]])
                                                
                        #Step7:Check the last column of 'AVERAGE SCORE OF FORM' and 'AVERAGE SCORE OF TL'
                        #Step7.1 Get this value from page
                        TheLastValueOfTLAndForm_FromPage=AllAVGSCOREOFFOR[-1]
                        print "TheLastValueOfTLAndForm_FromPage:",TheLastValueOfTLAndForm_FromPage
                        #Step7.1 Get this value from Calculate
                        #TheLastValueOfTLAndForm_Calculate
                        sum_AVGFORM=0
                        Tnumber=0
                        for key in AllTLsKPIVaule_FromPage:
                            for item in AllTLsKPIVaule_FromPage[key]:
                                if item !='N/A':
                                    Tnumber=Tnumber+1
                                    sum_AVGFORM=sum_AVGFORM+float(item)
                        TheLastValueOfTLAndForm_Calculate=str(round((sum_AVGFORM/Tnumber),2))
                        print "TheLastValueOfTLAndForm_Calculate:",TheLastValueOfTLAndForm_Calculate
                        CheckTablet.CheckData_DataBaseAndPage([TheLastValueOfTLAndForm_Calculate], [TheLastValueOfTLAndForm_FromPage])
                        Current_Date=GetConfig.get_LocalCurrentTime()                        
                        print Current_Date
                        #Step8:Check Created Date picker and Filter
                        Month_need=Current_Date[5:7]
                        Date_need=Current_Date[8:10]
                        LACLS.Click_StartDate(1)
                        print LACLS.Get_CreatedDateInDatePicker(1, 5, 2)
                        Current_location_list=DatePicker.get_DateLocation("Created_Date", 1, Date_need, Month_need)
                        print Current_location_list
                        LACLS.Select_CreatedDateInDatePicker(1, Current_location_list[0], Current_location_list[1])
                        print LACLS.get_StartDateBoxContent(1),(GetConfig.get_LocalCurrentTime())[0:10]
                        #Step8.1:Can select any start date<=today:=today
                        assert LACLS.get_StartDateBoxContent(1)==(GetConfig.get_LocalCurrentTime())[0:10]
                        
                        Monthindex=7
                        SevenMonthAgo_Date=GetConfig.get_TheDateOfLastAnyMonth(Monthindex, "Local")
                        print SevenMonthAgo_Date
                        LACLS.Click_StartDate(1)
                        for i in range(0,Monthindex):
                            LACLS.Click_LeftArrowInDatePicker(1, 1)
                        Month_need=SevenMonthAgo_Date[5:7]
                        Date_need=SevenMonthAgo_Date[8:10]
                        print Date_need
                        SevenMonthAgo_locationlist=DatePicker.get_DateLocation("Created_Date", 1, Date_need, Month_need)
                        print SevenMonthAgo_locationlist
                        LACLS.Select_CreatedDateInDatePicker(1, SevenMonthAgo_locationlist[0], SevenMonthAgo_locationlist[1])
                        #Step8.1:Can select any start date<=today:<today
                        assert LACLS.get_StartDateBoxContent(1)==SevenMonthAgo_Date[0:10]
                        #Step8.2: Check warning message with No End date
                        LACLS.click_filterbutton()                        
                        Actual_Message=LACLS.get_warnmessage()
                        print Actual_Message
                        CheckTablet.Check_WarningMessageNoEndDate_LeadersAcademyCoachingLeaderScores("Created_Date",Actual_Message)
                        time.sleep(3)
                        #Step8.3: Check warning message with more than 6 months
                        LACLS.Click_EndDate(1)
                        LACLS.Select_CreatedDateInDatePicker(2, Current_location_list[0], Current_location_list[1])
                        LACLS.click_filterbutton()
                        Actual_Message=LACLS.get_warnmessage()
                        print Actual_Message
                        CheckTablet.Check_WarningMessageOfMoreThanSixMonth_LeadersAcademyCoachingLeaderScores("Created_Date",Actual_Message)
                        #Step8.4: End Date can not ealier than start date
                        EalierDay_locationlist=DatePicker.get_DateLocatioEarlierThanSpecifiedDate(SevenMonthAgo_locationlist)
                        LACLS.Click_EndDate(1)
                        for i in range(0,Monthindex):
                            LACLS.Click_LeftArrowInDatePicker(1, 2)
                        Actual_classvalue=LACLS.Get_ClassValue_CreatedDateInDatePicker(2, EalierDay_locationlist[0], EalierDay_locationlist[1])
                        CheckTablet.Check_DateDisabled_LeadersAcademyCoachingLeaderScores(Actual_classvalue)
                        LACLS.Select_CreatedDateInDatePicker(2, SevenMonthAgo_locationlist[0], SevenMonthAgo_locationlist[1])#Cancel the window of datepicker
                        time.sleep(1)
                        
                        #Step9: Check Acknowledge Date picker and filter
                        LACLS.Click_StartDate(2)
                        #Step9.1:Can select any start date<=today:=today
                        LACLS.Select_AcknowledgeDateInDatePicker(1, Current_location_list[0], Current_location_list[1])
                        print LACLS.get_StartDateBoxContent(2),(GetConfig.get_LocalCurrentTime())[0:10]
                        assert LACLS.get_StartDateBoxContent(2)==(GetConfig.get_LocalCurrentTime())[0:10]
                        #Step9.1:Can select any start date<=today:<today
                        LACLS.Click_StartDate(2)
                        for i in range(0,Monthindex):
                            LACLS.Click_LeftArrowInDatePicker(2, 1)
                        print SevenMonthAgo_locationlist
                        LACLS.Select_AcknowledgeDateInDatePicker(1, SevenMonthAgo_locationlist[0], SevenMonthAgo_locationlist[1])
                        print LACLS.get_StartDateBoxContent(2),SevenMonthAgo_Date[0:10]
                        assert LACLS.get_StartDateBoxContent(2)==SevenMonthAgo_Date[0:10]
                        #Step9.2:Check warning message with No End date
                        LACLS.click_filterbutton()                        
                        Actual_Message=LACLS.get_warnmessage()
                        print Actual_Message
                        CheckTablet.Check_WarningMessageNoEndDate_LeadersAcademyCoachingLeaderScores("Acknowledge_Date",Actual_Message)
                        time.sleep(3)
                        #Step9.3:Check warning message with more than 6 months
                        LACLS.Click_EndDate(2)
                        #LACLS.Select_CreatedDateInDatePicker(2, Current_location_list[0], Current_location_list[1])
                        LACLS.Select_AcknowledgeDateInDatePicker(2, Current_location_list[0], Current_location_list[1])
                        LACLS.click_filterbutton()
                        Actual_Message=LACLS.get_warnmessage()
                        print Actual_Message
                        CheckTablet.Check_WarningMessageOfMoreThanSixMonth_LeadersAcademyCoachingLeaderScores("Acknowledge_Date",Actual_Message)
                        
                            
                            
                        
                        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_CoachingLeaderScores_OMDefault']
    unittest.main()