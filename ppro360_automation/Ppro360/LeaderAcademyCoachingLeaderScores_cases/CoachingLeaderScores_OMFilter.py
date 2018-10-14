'''
Created on Jun 28, 2018

@author: Sabrina Guo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Check_Tablet import Check_Tablet
from public_method.HandleMySQL import HandleMySQL
from Tablet_pages.LeaderAcademyCoachingLeaderScorespage import LeaderAcademyCoachingLeaderScorespage
#import time
from public_method.DatePicker_Method import DatePicker_Method


class CoachingLeaderScores_OMFilter(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="CoachingLeaderScores_OMFilter"
        
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
        #Info of configuration
        self.sqlsheetname="SQLs"
        self.sql_TLs_ByL3="Sql_TLs_ByL3_LeaderAcademyCoachingLeaderScorespage"
        self.sql_TLsValue_ByL3="Sql_KPIValueOfTLs_ByL3_LeaderAcademyCoachingLeaderScorespage"
        self.sql_AVGSCOREOFFORM_ByL3="Sql_AVGSCOREOFFORM_ByL3_LeaderAcademyCoachingLeaderScorespage"
        self.sql_TLsValue_createdAndacknowledge_ByL3="Sql_KPIValueOfTLs_CreatedAndAcknowledge_ByL3_LeaderAcademyCoachingLeaderScorespage"
        self.sql_AVGSCOREOFFORM_createdAndacknowledge_ByL3="Sql_AVGSCOREOFFORM_CreatedAndAcknowledge_ByL3_LeaderAcademyCoachingLeaderScorespage"
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
        #Gl.driver.quit()
        pass


    def test_CoachingLeaderScores_OMFilter(self):
        GetConfig=Get_configration_data()
        L=Login()
        Tablet=TabletHomepage()
        #CheckTablet=Check_Tablet()
        #HMysql=HandleMySQL()
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
                        #Step2:Check all TLs' KPI Value(Five months ago in created time)
                        #Get tls' kpi value of five months ago from page
                        #select LastFiveMonthDate in Start for created date
                        Current_Date=GetConfig.get_LocalCurrentTime()
                        LastFiveMonth_Date=GetConfig.get_TheDateOfLastAnyMonth(5, "Local")
                        CurrentMonth_need=Current_Date[5:7]
                        LastFiveMonth_need=LastFiveMonth_Date[5:7]
                        Date_need=Current_Date[8:10]
                        LACLS.Click_StartDate(1)
                        for i in range(0,5):
                            LACLS.Click_LeftArrowInDatePicker(1, 1)
                        LastFiveMonth_locationlist=DatePicker.get_DateLocation("Created_Date", 1, Date_need, LastFiveMonth_need)
                        LACLS.Select_CreatedDateInDatePicker(1, LastFiveMonth_locationlist[0], LastFiveMonth_locationlist[1])
                        #select current date  in End for created date
                        LACLS.Click_EndDate(1)
                        print Date_need, CurrentMonth_need
                        Current_locationlist=DatePicker.get_DateLocation("Created_Date", 2, Date_need, CurrentMonth_need)
                        LACLS.Select_CreatedDateInDatePicker(2, Current_locationlist[0], Current_locationlist[1])
                        LACLS.click_filterbutton()
                        #Get tls' kpi value from page
                        AllTLsName_FromPage=(LACLS.get_AllTLname_list())[0]
                        AllTLsName_FromPage.sort()
                        TLnumber=len(AllTLsName_FromPage)
                        AllTLsScores_FromPage=LACLS.get_AllTLvalue_ByL3(TLnumber, self.KPInumber)
                        DateType="created"
                        LastFiveMonth_need=LastFiveMonth_Date[:10]
                        CurrentDate_need=Current_Date[:10]
                        #Step2.1:Check  L1 row each coaching form score.
                        self.Check_TLVALUE(AllTLsScores_FromPage, DateType, LastFiveMonth_need,CurrentDate_need, hostindex, lobname, sitename)
                        
                        print AllTLsScores_FromPage
                        AllTLsKPIVaule_FromPage={}
                        for key in AllTLsScores_FromPage:
                            AllTLsKPIVaule_FromPage[key]=AllTLsScores_FromPage[key][:-1]
                        print AllTLsKPIVaule_FromPage
                        #Get tls' kpi value from database
                        LastFiveMonth_Date_need=LastFiveMonth_Date[:(LastFiveMonth_Date.find(" "))]
                        Current_Date_need=Current_Date[:(Current_Date.find(" "))]
                        #AVG SCORE OF FORM
                        #Get AVERAGE SCORE OF FORM from Page
                        AllAVGSCOREOFFOR=LACLS.get_anyTLvalueWithL3Login(TLnumber+1, self.KPInumber)
                        DateType="created"
                        #Step2.2:Check 'AVG SCORE OF FORM'
                        self.Check_AVGOFFORM(TLnumber, hostindex, lobname_database, sitename_database,DateType,LastFiveMonth_Date_need, Current_Date_need)
                                                
                        #Step2.3: Check AVG SCORE OF TL
                        self.Check_AVGOFTL(AllTLsScores_FromPage, AllTLsKPIVaule_FromPage)  
                        #Step2.4:Check the last column of 'AVERAGE SCORE OF FORM' and 'AVERAGE SCORE OF TL'
                        self.Check_AVGOFFORMANDTL(AllAVGSCOREOFFOR, AllTLsKPIVaule_FromPage)
                        
                        #Step3:Select acknowledge time(Three months ago in acknowledge time)
                        LACLS.click_back()
                        Tablet.Enter_LeadersAcademyCoachingLeaderScoresPage()
                        Monthindex=3
                        ThreeMonthAgo_Date=GetConfig.get_TheDateOfLastAnyMonth(Monthindex, "Local")
                        print ThreeMonthAgo_Date
                        LACLS.Click_StartDate(2)
                        for i in range(0,Monthindex):
                            LACLS.Click_LeftArrowInDatePicker(2, 1)
                        Month_need=ThreeMonthAgo_Date[5:7]
                        Date_need=ThreeMonthAgo_Date[8:10]
                        
                        print Month_need
                        print Date_need
                        ThreeMonthAgo_locationlist=DatePicker.get_DateLocation("Acknowledge_Date", 1, Date_need, Month_need)
                        print ThreeMonthAgo_locationlist
                        LACLS.Select_AcknowledgeDateInDatePicker(1, ThreeMonthAgo_locationlist[0], ThreeMonthAgo_locationlist[1])
                        print LACLS.get_StartDateBoxContent(2),ThreeMonthAgo_Date[0:ThreeMonthAgo_Date.find(" ")]
                        assert LACLS.get_StartDateBoxContent(2)==ThreeMonthAgo_Date[0:ThreeMonthAgo_Date.find(" ")]
                        
                        LACLS.Click_EndDate(2)
                        LACLS.Select_AcknowledgeDateInDatePicker(2, Current_locationlist[0], Current_locationlist[1])
                        print LACLS.get_EndDateBoxContent(2),Current_Date[0:Current_Date.find(" ")]
                        assert LACLS.get_EndDateBoxContent(2)==Current_Date[0:Current_Date.find(" ")]
                        
                        LACLS.click_filterbutton()
                        #Step3.1:Check TL row each coaching form score.
                        ThreeMonthAgo_Date_need=ThreeMonthAgo_Date[:(ThreeMonthAgo_Date.find(" "))]
                        Current_Date_need=Current_Date[:(Current_Date.find(" "))]
                        #Get tls' kpi value from page
                        AllTLsName_FromPage=(LACLS.get_AllTLname_list())[0]
                        AllTLsName_FromPage.sort()
                        TLnumber=len(AllTLsName_FromPage)
                        AllTLsScores_FromPage=LACLS.get_AllTLvalue_ByL3(TLnumber, self.KPInumber)
                        AllTLsKPIVaule_FromPage
                        #AllAVGSCOREOFFOR=LACLS.get_anyTLvalueWithL3Login(TLnumber+1, self.KPInumber)
                        DateType="acknowledge"
                        self.Check_TLVALUE(AllTLsScores_FromPage, DateType,ThreeMonthAgo_Date_need, Current_Date_need, hostindex, lobname, sitename)
                        
                        #Step3.2:Check row 'AVG SCORE OF FORM':
                        DateType="acknowledge"
                        AllAVGSCOREOFFOR=LACLS.get_anyTLvalueWithL3Login(TLnumber+1, self.KPInumber)
                        self.Check_AVGOFFORM(TLnumber, hostindex, lobname_database, sitename_database,DateType,ThreeMonthAgo_Date_need, Current_Date_need)
                        #Step3.3: Check AVG SCORE OF TL
                        AllTLsKPIVaule_FromPage=self.get_AllTLsKPIVaule_FromPage(AllTLsScores_FromPage)
                        self.Check_AVGOFTL(AllTLsScores_FromPage, AllTLsKPIVaule_FromPage)
                        #Step3.4:Check the last column of 'AVERAGE SCORE OF FORM' and 'AVERAGE SCORE OF TL'
                        self.Check_AVGOFFORMANDTL(AllAVGSCOREOFFOR, AllTLsKPIVaule_FromPage)
                        
                        #Step4:Select both created and acknowledge time(Six months ago in created and acknowledge time)
                        LACLS.click_back()
                        Tablet.Enter_LeadersAcademyCoachingLeaderScoresPage()
                        #select start date of created time (six month ago)
                        LACLS.Click_StartDate(1)
                        #Current_Date=GetConfig.get_LocalCurrentTime()
                        LastSixMonth_Date=GetConfig.get_TheDateOfLastAnyMonth(6, "Local")
                        #CurrentMonth_need=Current_Date[5:7]
                        LastSixMonth_need=LastSixMonth_Date[5:7]
                        #Date_need=Current_Date[8:10]
                        print Date_need, LastSixMonth_need
                        
                        #LACLS.Click_StartDate(1)
                        for i in range(0,6):
                            LACLS.Click_LeftArrowInDatePicker(1, 1)
                        LastSixMonth_locationlist=DatePicker.get_DateLocation("Created_Date", 1, Date_need, LastSixMonth_need)
                        print LastSixMonth_locationlist
                        LACLS.Select_CreatedDateInDatePicker(1, LastSixMonth_locationlist[0], LastSixMonth_locationlist[1])
                        print LACLS.get_StartDateBoxContent(1),LastSixMonth_Date[0:LastSixMonth_Date.find(" ")]
                        assert LACLS.get_StartDateBoxContent(1)==LastSixMonth_Date[0:LastSixMonth_Date.find(" ")]
                        
                        #select end date of created time (current date)
                        LACLS.Click_EndDate(1)
                        LACLS.Select_CreatedDateInDatePicker(2, Current_locationlist[0], Current_locationlist[1])
                        assert LACLS.get_EndDateBoxContent(1)==Current_Date[0:Current_Date.find(" ")]
                        
                        #select start date of acknowledge time (six month ago)
                        LACLS.Click_StartDate(2)
                        for i in range(0,6):
                            LACLS.Click_LeftArrowInDatePicker(2, 1)
                        LastSixMonth_locationlist=DatePicker.get_DateLocation("Acknowledge_Date", 1, Date_need, LastSixMonth_need)
                        print LastSixMonth_locationlist
                        LACLS.Select_AcknowledgeDateInDatePicker(1, LastSixMonth_locationlist[0], LastSixMonth_locationlist[1])
                        print LACLS.get_StartDateBoxContent(2),LastSixMonth_Date[0:LastSixMonth_Date.find(" ")]
                        assert LACLS.get_StartDateBoxContent(2)==LastSixMonth_Date[0:LastSixMonth_Date.find(" ")]
                        
                        #select end date of acknowledge time (current date)
                        LACLS.Click_EndDate(2)
                        LACLS.Select_AcknowledgeDateInDatePicker(2, Current_locationlist[0], Current_locationlist[1])
                        assert LACLS.get_EndDateBoxContent(2)==Current_Date[0:Current_Date.find(" ")]
                        
                        LACLS.click_filterbutton()
                        
                        
                        
                        #Step4.1:Check TL row each coaching form score.
                        SixMonthAgo_Date_need=LastSixMonth_Date[0:LastSixMonth_Date.find(" ")]
                        #Get tls' kpi value from page
                        AllTLsName_FromPage=(LACLS.get_AllTLname_list())[0]
                        AllTLsName_FromPage.sort()
                        TLnumber=len(AllTLsName_FromPage)
                        AllTLsScores_FromPage=LACLS.get_AllTLvalue_ByL3(TLnumber, self.KPInumber)
                        DateType=""#DateType="" means no change in sql
                        self.Check_TLVALUE(AllTLsScores_FromPage, DateType,SixMonthAgo_Date_need, Current_Date_need, hostindex, lobname, sitename)
                        #Step4.2:Check row 'AVG SCORE OF FORM':
                        AllTLsKPIVaule_FromPage={}
                        for key in AllTLsScores_FromPage:
                            AllTLsKPIVaule_FromPage[key]=AllTLsScores_FromPage[key][:-1]
                        print AllTLsKPIVaule_FromPage
                        self.Check_AVGOFFORM(TLnumber, hostindex, lobname_database, sitename_database,DateType,SixMonthAgo_Date_need, Current_Date_need)
                        #Step4.3: Check AVG SCORE OF TL
                        self.Check_AVGOFTL(AllTLsScores_FromPage, AllTLsKPIVaule_FromPage)
                        #Step4.4:Check the last column of 'AVERAGE SCORE OF FORM' and 'AVERAGE SCORE OF TL'
                        AllAVGSCOREOFFOR=LACLS.get_anyTLvalueWithL3Login(TLnumber+1, self.KPInumber)
                        self.Check_AVGOFFORMANDTL(AllAVGSCOREOFFOR, AllTLsKPIVaule_FromPage)
                        L.logout_tablet()
    def get_AllTLsKPIVaule_FromPage(self,AllTLsScores_FromPage):
        AllTLsKPIVaule_FromPage={}
        for key in AllTLsScores_FromPage:
            AllTLsKPIVaule_FromPage[key]=AllTLsScores_FromPage[key][:-1]
        print AllTLsKPIVaule_FromPage  
        return AllTLsKPIVaule_FromPage                 
                        
                        
    def Check_TLVALUE(self,AllTLsScores_FromPage,DateType,LastSixMonth_Date,Current_Date,hostindex, lobname, sitename):
        GetConfig=Get_configration_data()
        HMysql=HandleMySQL()
        CheckTablet=Check_Tablet()
        print AllTLsScores_FromPage
        AllTLsKPIVaule_FromPage={}
        for key in AllTLsScores_FromPage:
            AllTLsKPIVaule_FromPage[key]=AllTLsScores_FromPage[key][:-1]
        print AllTLsKPIVaule_FromPage
        #Step6.1.3:Get tls' kpi value from database      
        print LastSixMonth_Date
        print Current_Date
        if DateType=="":
            Sql_TLsValue_ByL3=GetConfig.get_sql_content(self.sqlsheetname, self.sql_TLsValue_createdAndacknowledge_ByL3).replace("LastSixMonth_Date",LastSixMonth_Date).replace("Current_Date",Current_Date)
        else:
            Sql_TLsValue_ByL3=GetConfig.get_sql_content(self.sqlsheetname, self.sql_TLsValue_ByL3).replace("DateType",DateType).replace("LastSixMonth_Date",LastSixMonth_Date).replace("Current_Date",Current_Date)
        print Sql_TLsValue_ByL3
        AllTLsKPIinf_DataBase=HMysql.Get_datafromDB(hostindex, lobname, sitename, self.dbuser, self.dbpassword, Sql_TLsValue_ByL3)
        AllTLsKPIinf=list(AllTLsKPIinf_DataBase[1])
        #print AllTLsKPIinf
        AllTLsKPIVaule_DataBase={}
        print AllTLsKPIinf
        for item in AllTLsKPIinf:
            tlinfo=list(item)
            tlhrid=tlinfo[0]
            tlkpivalue=tlinfo[1:self.KPInumber]
            for i in range(0,len(tlkpivalue)):
                if tlkpivalue[i]!=None:
                    tlkpivalue[i]=str(tlkpivalue[i])
            AllTLsKPIVaule_DataBase[tlhrid]=tlkpivalue
        print AllTLsKPIVaule_DataBase
        for key in AllTLsKPIVaule_FromPage:
            CheckTablet.CheckData_DataBaseAndPage(AllTLsKPIVaule_DataBase[key], AllTLsKPIVaule_FromPage[key])
                            
    
    def Check_AVGOFFORM(self,TLnumber,hostindex, lobname_database, sitename_database,DateType,ThreeMonthAgo_Date_need,Current_Date_need):
        LACLS=LeaderAcademyCoachingLeaderScorespage()
        GetConfig=Get_configration_data()
        HMysql=HandleMySQL()
        CheckTablet=Check_Tablet()
        AllAVGSCOREOFFOR=LACLS.get_anyTLvalueWithL3Login(TLnumber+1, self.KPInumber)
        AllAVGSCOREOFFORM_FromPage=AllAVGSCOREOFFOR[:-1]
        print "AllAVGSCOREOFFORM_FromPage:",AllAVGSCOREOFFORM_FromPage
        #Step3.2:Get AVERAGE SCORE OF FORM from DataBase
        if DateType=="":
            sql_AVGSCOREOFFORM_ByL3=GetConfig.get_sql_content(self.sqlsheetname, self.sql_AVGSCOREOFFORM_createdAndacknowledge_ByL3).replace("LastSixMonth_Date",ThreeMonthAgo_Date_need).replace("Current_Date",Current_Date_need)
        else:
            sql_AVGSCOREOFFORM_ByL3=GetConfig.get_sql_content(self.sqlsheetname, self.sql_AVGSCOREOFFORM_ByL3).replace("DateType",DateType).replace("LastSixMonth_Date",ThreeMonthAgo_Date_need).replace("Current_Date",Current_Date_need)
        print sql_AVGSCOREOFFORM_ByL3
        AllAVGSCOREOFFORM=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_AVGSCOREOFFORM_ByL3)
        print AllAVGSCOREOFFORM
        AllAVGSCOREOFFORM_DataBase=list(AllAVGSCOREOFFORM[1][0])
        for i in range(0,len(AllAVGSCOREOFFORM_DataBase)):
            AllAVGSCOREOFFORM_DataBase[i]=str(AllAVGSCOREOFFORM_DataBase[i])
        print "AllAVGSCOREOFFORM_DataBase:",AllAVGSCOREOFFORM_DataBase
        
        CheckTablet.CheckData_DataBaseAndPage(AllAVGSCOREOFFORM_DataBase, AllAVGSCOREOFFORM_FromPage)
                            
    
    def Check_AVGOFFORMANDTL(self,AllAVGSCOREOFFOR,AllTLsKPIVaule_FromPage):
        CheckTablet=Check_Tablet()
        TheLastValueOfTLAndForm_FromPage=AllAVGSCOREOFFOR[-1]
        print "TheLastValueOfTLAndForm_FromPage:",TheLastValueOfTLAndForm_FromPage
        #Step5.1 Get this value from Calculate
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
    def Check_AVGOFTL(self,AllTLsScores_FromPage,AllTLsKPIVaule_FromPage):
        CheckTablet=Check_Tablet()
        #Step4.1: Get AVG SCORE OF TL from page
        AVGSCOREOFTL_FromPage={}
        for key in AllTLsScores_FromPage:
            AVGSCOREOFTL_FromPage[key]=AllTLsScores_FromPage[key][-1]
        print "AVGSCOREOFTL_FromPage:",AVGSCOREOFTL_FromPage
        #Step4.2:AVG SCORE OF TL from Calculate  
        AVGSCOREOFTL_Calculate={}
        for key in AllTLsKPIVaule_FromPage:
            sum_AVG=0
            totalnumber=0
            for item in AllTLsKPIVaule_FromPage[key]:
                if item!='N/A':
                    totalnumber=totalnumber+1
                    sum_AVG=sum_AVG+float(item)
            print "sum_AVG:",sum_AVG
            print "totalnumber:",totalnumber
            
            #AVG=(sum_AVG/totalnumber)+0.0000000000000001 
            AVG=str(sum_AVG/totalnumber)+"00000000001"
            print AVG 
            #AVGSCOREOFTL_Calculate[key]= str(round((sum_AVG/totalnumber),2))
            AVGSCOREOFTL_Calculate[key]= str(round(float(AVG),2))
            
        print "AVGSCOREOFTL_Calculate:",AVGSCOREOFTL_Calculate
        for key in AVGSCOREOFTL_Calculate:
            CheckTablet.CheckData_DataBaseAndPage([AVGSCOREOFTL_Calculate[key]], [AVGSCOREOFTL_FromPage[key]])
          
         
        
        
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_CoachingLeaderScores_OMFilter']
    unittest.main()