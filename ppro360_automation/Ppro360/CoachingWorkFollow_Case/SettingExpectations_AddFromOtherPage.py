'''
Created on 20170905

@author: luming.zhao
'''
import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
from Tablet_pages.PerformancPage import PerformancePage
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from CoachingAndTriadCoaching_Pages.BasicInfoforCoaching import BasicInfoforCoaching
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.OutlierPage import OutlierPage
from public_method.KPI_method import KPI_method
from public_method.HandleMySQL import HandleMySQL


class SettingExpectations_AddFromOtherPage(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="SettingExpectations_AddFromOtherPage"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.hostindex=92
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get coachpopuptittle
        self.title=GetData.get_AddCoachingFormTitle()
        
        #coaching or Triad coaching
        self.coachtype="coaching"  
        #Coachformname
        self.coachformname="Setting Expectations" 
        self.coachpagetitle="Coaching - "+self.coachformname
        self.Triadcoachpagetitle="Triad Coaching - "+self.coachformname
        self.KPIbox_title_yesterday="Coaching KPIs(Yesterday):"
        self.KPIbox_title_weektodate="Coaching KPIs(Week-To-Date):"
        self.KPIbox_title="Coaching KPIs(%s):"
        
        
        #CheckBox Status
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
    def SettingExpectations_AddFromOtherPage(self):
        self.AddFormfromdailyweeklyperformancepage()
        self.Addtriadcoachingformformdailyweeklyperformancepage()
        self.Addformfromoutlier()
    
    def AddFormfromdailyweeklyperformancepage(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        KPIMethod=KPI_method()
        HMysql=HandleMySQL()
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
                    
                    L=Login()
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        tablist=Gl.Multi_timetab
                    elif lobname in Gl.performancefor_3TimeTab_lob:
                        tablist=Gl.Less_timetab
                    else:
                        tablist=Gl.Old_timetab
                    tablist.pop()#Delete the last one(Month-To-Date)
                    
                    for ywm in range(0,len(tablist)):
                        Tablet.click_performancecircle()
                        if lobname in Gl.DoubleKPIname_lob:
                            KPInumber=Ppage.get_KPInumber_All()
                        else:
                            KPInumber=Ppage.get_KPInumber()
                        print ywm    
                        Ppage.click_timetab_performance(ywm+1)
                        KPIbox_title_AnyDate=self.KPIbox_title % Ppage.get_timetab_text_performance(ywm+1)
                        Ppage.unfold_anyTL(1)#unfold agent
                        KPIofAgentOrTL_FromPerformancePage_list=Ppage.get_AllKPIsofAgentForOM_list(KPInumber)
                        Ppage.unfold_anyTL(1)#fold agent
                        if tablist[ywm]=="Yesterday":
                            
                            Ppage.select_AnyKpiOfAgent_OM(KPInumber)#Select all KPIs to add  
                        else:
                            Ppage.select_AnyKpiOfAgent_OM(2)#Select one KPI to add
                        
                        print tablist[ywm],
                        print "is in testing:"
                        #Get all KPI Info from performance
                        if lobname in Gl.DoubleKPIname_lob:
                            KPInumber_Performance_First=Ppage.get_KPInumber()
                            KPInumber_Performance_Second=Ppage.get_KPInumber_Second()
                            KPInumber_Performance=Ppage.get_KPInumber_All()
                            KPIindexChecked_List_Performance=[KPInumber_Performance+1]
                            KPIname_FromPerformancePage_First_list=Ppage.get_KPIname_list(KPInumber_Performance_First)
                            KPIname_FromPerformancePage_Second_list=Ppage.get_KPIname_list(KPInumber_Performance_Second)
                            KPIname_FromPerformancePage_list=KPIname_FromPerformancePage_First_list+KPIname_FromPerformancePage_Second_list
                        else:
                            KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber)
                        KPIofGoal_FromPerformancePage_list=Ppage.get_AllKPIsofGoal_list(KPInumber)
                        KPIofSite_FromPerformancePage_list=Ppage.get_AllKPIsofSite_list(KPInumber)
                        #Ppage.select_AnyKpiOfAgent_OM(KPInumber)
                        Ppage.click_addcoachbutton()
                        TCoach.Add_AnyCoachOrTriad(self.coachformname)
                        Header.click_backbutton()
                        Tablet.click_coachingcircle()
                        #CoachHome.click_eachcoach(SN_path)
                        CoachHome.click_eachcoach(1)
                        #Get all KPI Info from Coaching Detail page
                        if lobname in Gl.DoubleKPIname_lob:
                            KPInumber_CoachDetail_First=BasicInfo.get_KPInumber()
                            KPInumber_CoachDetail_Second=BasicInfo.get_KPInumber_Second()
                            KPInumber_CoachDetail=BasicInfo.get_KPInumber_All()
                            KPIindexChecked_List_Performance=[KPInumber_CoachDetail+1]
                            KPIname_FromDetailPage_First_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail_First)
                            KPIname_FromDetailPage_Second_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail_Second)
                            KPIname_FromDetailPage_list=KPIname_FromDetailPage_First_list+KPIname_FromDetailPage_Second_list
                        
                        else:
                            KPInumber_CoachDetail=BasicInfo.get_KPInumber()
                            KPIname_FromDetailPage_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail)
                        KPIofGoal_FromDetailPage_list=BasicInfo.get_KPIofGoal_list(KPInumber_CoachDetail)
                        KPIofSite_FromDetailPage_list=BasicInfo.get_KPIofSite_list(KPInumber_CoachDetail)
                        KPIofAgentOrTL_FromDetailPage_list=BasicInfo.get_AllKPIsofAgentOrTL_list(KPInumber_CoachDetail)
                        #CheckBoxStatus_FromDetailPage_list=BasicInfo.get_CheckBoxStatus_list(KPInumber_CoachDetail)
                        #KPIboxTitle=BasicInfo.get_KPIboxTitle()
                        '''Check1&2:1.Enter the  form detail page with title 'Coaching - SettingExpectations'
                                  2.Show header name 'Coaching KPIs(Yesterday) or Coaching KPIs(Week-To-Date)'
                                  3.All KPI data of Goal, Site,Agent should be the same as those on the corresponding performance page.
                                  4.All KPIs are checked by default.'''
                        assert Header.get_HeaderTittle()==self.coachpagetitle
                        '''
                        print "KPIname_FromPerformancePage_list==KPIname_FromDetailPage_list"
                        print KPIname_FromPerformancePage_list
                        print KPIname_FromDetailPage_list
                        assert KPIname_FromPerformancePage_list==KPIname_FromDetailPage_list'''
                        if lobname in Gl.DoubleKPIname_lob:
                            Goal_index_Dic=KPIMethod.get_IndexOfTwovalue_list(KPIofGoal_FromPerformancePage_list)
                            Goal_SingleValue_index_list=Goal_index_Dic["SingleValue_index_list"]
                            Goal_TwoValue_index_list=Goal_index_Dic["TwoValue_index_list"]
                            for a1 in range(0,len(Goal_SingleValue_index_list)):
                                i=Goal_SingleValue_index_list[a1]
                                assert KPIofGoal_FromPerformancePage_list[i]==KPIofGoal_FromDetailPage_list[i]
                            for a2 in range(0,len(Goal_TwoValue_index_list)):
                                i=Goal_TwoValue_index_list[a2]
                                assert (KPIofGoal_FromPerformancePage_list[i].split("\n"))[1]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[0]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[1]
                        else:
                            assert KPIofGoal_FromPerformancePage_list==KPIofGoal_FromDetailPage_list
                        assert KPIofSite_FromPerformancePage_list==KPIofSite_FromDetailPage_list
                        print "KPIofAgentOrTL_FromPerformancePage_list==KPIofAgentOrTL_FromDetailPage_list:",KPIofAgentOrTL_FromPerformancePage_list,KPIofAgentOrTL_FromDetailPage_list
                        assert KPIofAgentOrTL_FromPerformancePage_list==KPIofAgentOrTL_FromDetailPage_list
                        if tablist[ywm]=="Yesterday":
                            
                            assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            for index in range(2,KPInumber_CoachDetail):
                                assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_CheckedStatus
                        else:
                            if tablist[ywm]=="LastTwoMonth":
                                print "BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate"
                                print BasicInfo.get_KPIboxTitle()
                                print KPIbox_title_AnyDate
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            elif tablist[ywm]=="LastMonth":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            elif tablist[ywm]== "Week-to-Date":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_CheckedStatus
                            for index in range(3,KPInumber_CoachDetail):
                                assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                        Header.click_backbutton()#Back to Coaching Home page
                        Header.click_backbutton()#Back to Tablet Home page
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                    #else:
                        #print lobname," only has one time tap!!!"                     
    def test_Addtriadcoachingformformdailyweeklyperformancepage(self): 
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        KPIMethod=KPI_method()
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
                    
                    L=Login()
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        tablist=Gl.Multi_timetab
                    elif lobname in Gl.performancefor_3TimeTab_lob:
                        tablist=Gl.Less_timetab
                    else:
                        tablist=Gl.Old_timetab
                    tablist.pop()#Delete the last one(Month-To-Date)
                    
                    for ywm in range(0,len(tablist)):
                        Tablet.click_performancecircle()
                        if lobname in Gl.DoubleKPIname_lob:
                            KPInumber=Ppage.get_KPInumber_All()
                        else:
                            KPInumber=Ppage.get_KPInumber()
                        print ywm    
                        Ppage.click_timetab_performance(ywm+1)
                        KPIbox_title_AnyDate=self.KPIbox_title % Ppage.get_timetab_text_performance(ywm+1)
                        Ppage.unfold_anyTL(1)#unfold agent
                        KPIofTL_FromPerformancePage_list=Ppage.get_AllKPIsofTL_list(KPInumber)
                        Ppage.unfold_anyTL(1)#fold agent
                        if tablist[ywm]=="Yesterday":
                            Ppage.select_AnyKpiOfAgent_OM(KPInumber)#Select all KPIs to add  
                        else:
                            Ppage.select_AnyKpiOfAgent_OM(2)#Select one KPI to add
                            
                        print tablist[ywm],
                        print "is in testing:"
                        #Get all KPI Info from performance
                        if lobname in Gl.DoubleKPIname_lob:
                            KPInumber_Performance_First=Ppage.get_KPInumber()
                            KPInumber_Performance_Second=Ppage.get_KPInumber_Second()
                            KPInumber_Performance=Ppage.get_KPInumber_All()
                            KPIindexChecked_List_Performance=[KPInumber_Performance+1]
                            KPIname_FromPerformancePage_First_list=Ppage.get_KPIname_list(KPInumber_Performance_First)
                            KPIname_FromPerformancePage_Second_list=Ppage.get_KPIname_list(KPInumber_Performance_Second)
                            KPIname_FromPerformancePage_list=KPIname_FromPerformancePage_First_list+KPIname_FromPerformancePage_Second_list
                        else:
                            KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber)
                        KPIofGoal_FromPerformancePage_list=Ppage.get_AllKPIsofGoal_list(KPInumber)
                        KPIofSite_FromPerformancePage_list=Ppage.get_AllKPIsofSite_list(KPInumber)
                        KPIofAgentOrTL_FromPerformancePage_list=Ppage.get_AllKPIsofAgentForOM_list(KPInumber)
                        Ppage.click_addcoachbutton()
                        TCoach.Add_AnyCoachOrTriad(self.coachformname)
                        Ppage.click_backbutton()
                        Tablet.click_coachingcircle()
                        #CoachHome.click_eachcoach(SN_path)
                        CoachHome.click_eachcoach(1)
                        #Get all KPI Info from Coaching Detail page
                        if lobname in Gl.DoubleKPIname_lob:
                            KPInumber_CoachDetail_First=BasicInfo.get_KPInumber()
                            KPInumber_CoachDetail_Second=BasicInfo.get_KPInumber_Second()
                            KPInumber_CoachDetail=BasicInfo.get_KPInumber_All()
                            KPIindexChecked_List_Performance=[KPInumber_CoachDetail+1]
                            KPIname_FromDetailPage_First_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail_First)
                            KPIname_FromDetailPage_Second_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail_Second)
                            KPIname_FromDetailPage_list=KPIname_FromDetailPage_First_list+KPIname_FromDetailPage_Second_list
                        
                        else:
                            KPInumber_CoachDetail=BasicInfo.get_KPInumber()
                            KPIname_FromDetailPage_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail)
                        
                        KPIofGoal_FromDetailPage_list=BasicInfo.get_KPIofGoal_list(KPInumber_CoachDetail)
                        KPIofSite_FromDetailPage_list=BasicInfo.get_KPIofSite_list(KPInumber_CoachDetail)
                        KPIofTL_FromDetailPage_list=BasicInfo.get_AllKPIsofAgentOrTL_list(KPInumber_CoachDetail)
                        #CheckBoxStatus_FromDetailPage_list=BasicInfo.get_CheckBoxStatus_list(KPInumber_CoachDetail)
                        #KPIboxTitle=BasicInfo.get_KPIboxTitle()
                        '''Check1&2:1.Enter the  form detail page with title 'Coaching - Accountability Conversation'
                                  2.Show header name 'Coaching KPIs(Yesterday) or Coaching KPIs(Week-To-Date)'
                                  3.All KPI data of Goal, Site,Agent should be the same as those on the corresponding performance page.
                                  4.All KPIs are checked by default.'''
                        assert Header.get_HeaderTittle()==self.coachpagetitle
                        #assert KPIname_FromPerformancePage_list==KPIname_FromDetailPage_list
                        if lobname in Gl.DoubleKPIname_lob:
                            Goal_index_Dic=KPIMethod.get_IndexOfTwovalue_list(KPIofGoal_FromPerformancePage_list)
                            Goal_SingleValue_index_list=Goal_index_Dic["SingleValue_index_list"]
                            Goal_TwoValue_index_list=Goal_index_Dic["TwoValue_index_list"]
                            for a1 in range(0,len(Goal_SingleValue_index_list)):
                                i=Goal_SingleValue_index_list[a1]
                                assert KPIofGoal_FromPerformancePage_list[i]==KPIofGoal_FromDetailPage_list[i]
                            for a2 in range(0,len(Goal_TwoValue_index_list)):
                                i=Goal_TwoValue_index_list[a2]
                                assert (KPIofGoal_FromPerformancePage_list[i].split("\n"))[1]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[0]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[1]
                        else:
                            assert KPIofGoal_FromPerformancePage_list==KPIofGoal_FromDetailPage_list
                        #assert KPIofGoal_FromPerformancePage_list==KPIofGoal_FromDetailPage_list
                        assert KPIofSite_FromPerformancePage_list==KPIofSite_FromDetailPage_list
                        print "KPIofTL_FromPerformancePage_list==KPIofAgentOrTL_FromDetailPage_list:",KPIofTL_FromPerformancePage_list,KPIofTL_FromDetailPage_list
                        #assert KPIofTL_FromPerformancePage_list==KPIofTL_FromDetailPage_list
                        if tablist[ywm]=="Yesterday":
                            assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            for index in range(2,KPInumber_CoachDetail):
                                assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_CheckedStatus
                        else:
                            if tablist[ywm]=="LastTwoMonth":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            elif tablist[ywm]=="LastMonth":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            elif tablist[ywm]== "Week-to-Date":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_AnyDate
                            assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_CheckedStatus
                            for index in range(3,KPInumber_CoachDetail):
                                assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus 
                        Header.click_backbutton()#Back to Coaching Home page
                        Header.click_backbutton()#Back to Tablet Home page
                    L.logout_tablet()               
                    GetConfig.print_EndTest_message(lobname, sitename)
    def Addformfromoutlier(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Outlier=OutlierPage()
        TCoach=Coach_Triad_General()
        Header=HeaderPage()
        Ppage=PerformancePage()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        KPIMethod=KPI_method()
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
                    GetTL=Get_AllRoleAccountForTest()
                    TLInfo=GetTL.get_TLInfoandAgentHridFromPerformance(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    TLHrid=TLInfo["TLHrid"]
                    TLPassword=TLInfo["TLPassword"]
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,TLHrid,TLPassword)
                    Tablet.click_TL_outliercircle()
                    KPInumber_Outlier=Outlier.get_KPInumber()
                    KPIName_list_InOutlier=Outlier.get_AllKPIname_List_Outlier(KPInumber_Outlier)
                    if lobname not in Gl.performancefor_MultiTimeTab_lob:
                    #if lobname in Gl.performancefor3time_lob:
                        tablist=Gl.Multi_timetab#
                        for ywm in range(0,len(tablist)):
                            if tablist[ywm]=="Yesterday":
                                Outlier.click_timetab_Outlier(3)
                                #select the third KPI to add this form
                                Outlier.click_anyKPIofTop20(1, 4)                               
                            elif tablist[ywm]=="Week-to-Date":
                                Outlier.click_timetab_Outlier(4)
                                #select all KPIs to add this form
                                for kpiindex in range(2,KPInumber_Outlier+1):
                                    Outlier.click_anyKPIofTop20(1, kpiindex)#The first Agent for TOP20
                            else:
                                if tablist[ywm]=="LastTwoMonth":
                                    Outlier.click_timetab_Outlier(1)
                                elif tablist[ywm]=="LastMonth":
                                    Outlier.click_timetab_Outlier(2)
                                elif tablist[ywm]=="Month-to-Date":
                                    Outlier.click_timetab_Outlier(5)
                                KPIname_Selected="ACHIEVEMENT"
                                KPIindex_outlier=Outlier.get_anyKPIindex_Outlier(KPInumber_Outlier, KPIname_Selected)
                                Outlier.click_anyKPIofTop20(1, KPIindex_outlier)
                                
                            print tablist[ywm],
                            print "is in testing:"
                            AgentName=Outlier.get_anyKPIofTop20(1, 1)
                            Outlier.click_addCoachButton()
                            TCoach.Add_AnyCoachOrTriad(self.coachformname)
                            Header.click_backbutton()
                            Tablet.click_performancecircle()
                            KPInumber_Performance=Ppage.get_KPInumber()
                            KPIindexChecked_List_Performance=[]
                            if tablist[ywm]=="Week-to-Date":
                                Ppage.click_timetab_performance(4)
                                KPIbox_title_weektodate=self.KPIbox_title % Ppage.get_timetab_text_performance(4)
                                for KPIindex in range(2,KPInumber_Performance+1):
                                    if Ppage.get_anyKPIname(KPIindex) in KPIName_list_InOutlier:
                                        KPIindexChecked_List_Performance.append(KPIindex)
                            elif tablist[ywm]=="Yesterday":
                                Ppage.click_timetab_performance(3)
                                KPIbox_title_yesterday=self.KPIbox_title % Ppage.get_timetab_text_performance(3)
                                for KPIindex in range(2,KPInumber_Performance+1):
                                    if Ppage.get_anyKPIname(KPIindex) == KPIName_list_InOutlier[2]:
                                        KPIindexChecked_List_Performance.append(KPIindex)
                            else:
                                if tablist[ywm]=="LastTwoMonth":
                                    Ppage.click_timetab_performance(1)
                                    KPIbox_title_LastTwoMonth=self.KPIbox_title % Ppage.get_timetab_text_performance(1)
                                elif tablist[ywm]=="LastMonth":
                                    Ppage.click_timetab_performance(2)
                                    KPIbox_title_LastMonth=self.KPIbox_title % Ppage.get_timetab_text_performance(2)
                                elif tablist[ywm]=="Month-to-Date":
                                    Ppage.click_timetab_performance(5)
                                    KPIbox_title_monthtodate=self.KPIbox_title % Ppage.get_timetab_text_performance(5)
                                for KPIindex in range(2,KPInumber_Performance+1):
                                    if Ppage.get_anyKPIname(KPIindex) == KPIname_Selected:
                                        KPIindexChecked_List_Performance.append(KPIindex)
                                
                            
                            Agent_lineindex=Ppage.get_anyAgentindex(AgentName)
                            
                            if lobname in Gl.DoubleKPIname_lob:
                                KPInumber=Ppage.get_KPInumber_All()
                                KPIname_FromPerformancePage_list=Ppage.get_KPIname_list_Double()
                                
                            else:
                                KPInumber=Ppage.get_KPInumber()
                                KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber)
                                
                            for i in range(0,len(KPIname_FromPerformancePage_list)):
                                if len(KPIname_FromPerformancePage_list[i])>12:
                                    if KPIname_FromPerformancePage_list[i][-12]=="(" and KPIname_FromPerformancePage_list[i][-1]==")":
                                        KPIname_FromPerformancePage_list[i]=KPIname_FromPerformancePage_list[i].replace(KPIname_FromPerformancePage_list[i][-13:],"")    
                          
                            #KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber_Performance)
                            KPIofGoal_FromPerformancePage_list=Ppage.get_AllKPIsofGoal_list(KPInumber_Performance)
                            KPIofSite_FromPerformancePage_list=Ppage.get_AllKPIsofSite_list(KPInumber_Performance)
                            KPIofTeam_FromPerformancePage_list=Ppage.get_AllKPIsofTeam_list(KPInumber_Performance)
                            KPIofAgent_FromPerformancePage_list=Ppage.get_AllKPIsofAgent_TL_list(KPInumber_Performance,Agent_lineindex)
                            
                            Header.click_backbutton()
                            Tablet.click_TL_coachingcircle()
                            
                            #CoachHome.click_eachcoach(SN_path)
                            CoachHome.click_eachcoach(1)
                            if lobname in Gl.DoubleKPIname_lob:
                                KPInumber_CoachDetail=BasicInfo.get_KPInumber_All()
                                KPIname_FromDetailPage_list=BasicInfo.get_KPIname_list_Double()
                            else:
                                KPInumber_CoachDetail=BasicInfo.get_KPInumber()
                                KPIname_FromDetailPage_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail)
                            
                            #KPInumber_CoachDetail=BasicInfo.get_KPInumber()
                            #KPIname_FromDetailPage_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail)
                            KPIofGoal_FromDetailPage_list=BasicInfo.get_KPIofGoal_list(KPInumber_CoachDetail)
                            KPIofSite_FromDetailPage_list=BasicInfo.get_KPIofSite_list(KPInumber_CoachDetail)
                            KPIofTeam_FromDetailPage_list=BasicInfo.get_KPIofTeam_list(KPInumber_CoachDetail)
                            KPIofAgentOfTL_FromDetailPage_list=BasicInfo.get_KPIofAgentOfTL_list(KPInumber_CoachDetail)
                            '''Check_Month-To-Date:
                                     1) Enter this form detail page with title 'Coaching -Commendation'
                                     2) Show header name 'Coaching KPIs(Month-To-Date)'
                                     3) All KPI data of Goal, Site,Agent should be the same as those on the corresponding performance page.
                                     4) The  KPIs achievement is checked by default.
                                     5)  Other KPIs are unchecked by default.
                               Check_Week-To-Date:
                                     1) Enter this form detail page with title 'Coaching -Commendation'
                                     2) Show header name 'Coaching KPIs(Week-To-Date)'
                                     3) All KPI data of Goal, Site,Agent should be the same as those on the corresponding performance page.
                                     4) The all KPIs  is checked by default.
                               Check_Yesterday:
                                     1) Enter this form detail page with title 'Coaching -Commendation'
                                     2) Show header name 'Coaching KPIs(Yesterday)'
                                     3) All KPI data of Goal, Site,Agent should be the same as those on the corresponding performance page.
                                     4) The  third KPI is checked by default.
                                     5) Other KPIs are unchecked by default.'''
                            assert Header.get_HeaderTittle()==self.coachpagetitle
                            if tablist[ywm]=="Yesterday":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_yesterday
                            elif tablist[ywm]=="Week-to-Date":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_weektodate
                            elif tablist[ywm]=="Month-to-Date":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_monthtodate
                            elif tablist[ywm]=="LastTwoMonth":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_LastTwoMonth
                            elif tablist[ywm]=="LastMonth":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_LastMonth
                            
                            assert KPIname_FromPerformancePage_list==KPIname_FromDetailPage_list
                            if lobname in Gl.DoubleKPIname_lob:
                                Goal_index_Dic=KPIMethod.get_IndexOfTwovalue_list(KPIofGoal_FromPerformancePage_list)
                                Goal_SingleValue_index_list=Goal_index_Dic["SingleValue_index_list"]
                                Goal_TwoValue_index_list=Goal_index_Dic["TwoValue_index_list"]
                                for a1 in range(0,len(Goal_SingleValue_index_list)):
                                    i=Goal_SingleValue_index_list[a1]
                                    assert KPIofGoal_FromPerformancePage_list[i]==KPIofGoal_FromDetailPage_list[i]
                                for a2 in range(0,len(Goal_TwoValue_index_list)):
                                    i=Goal_TwoValue_index_list[a2]
                                    assert (KPIofGoal_FromPerformancePage_list[i].split("\n"))[1]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[0]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[1]
                            else:
                                assert KPIofGoal_FromPerformancePage_list==KPIofGoal_FromDetailPage_list
                                                        
                            assert KPIofSite_FromPerformancePage_list==KPIofSite_FromDetailPage_list
                            assert KPIofTeam_FromPerformancePage_list==KPIofTeam_FromDetailPage_list
                            assert KPIofAgent_FromPerformancePage_list==KPIofAgentOfTL_FromDetailPage_list

                            for index in range(2,KPInumber_CoachDetail):
                                if index in KPIindexChecked_List_Performance:
                                    assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_CheckedStatus
                                else:
                                    assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                            Header.click_backbutton()
                            Header.click_backbutton()
                            Tablet.click_TL_outliercircle()
                    
                    else:#For those LOBs who Only have one timetab
                        tablist=Gl.Less_timetab
                        for ywm in range(0,len(tablist)):
                            if tablist[ywm]=="LastTwoMonth":
                                Outlier.click_timetab_Outlier(1)
                                KPIbox_title_LastTwoMonth=self.KPIbox_title % Ppage.get_timetab_text_performance(1)
                            elif tablist[ywm]=="LastMonth":
                                Outlier.click_timetab_Outlier(2)
                                KPIbox_title_LastMonth=self.KPIbox_title % Ppage.get_timetab_text_performance(2)
                            elif tablist[ywm]=="Month-to-Date":
                                Outlier.click_timetab_Outlier(3)
                                KPIbox_title_monthtodate=self.KPIbox_title % Ppage.get_timetab_text_performance(3)
                            print tablist[ywm],
                            print "is in testing:"
                            KPIname_Selected="ACHIEVEMENT"
                            KPIindex_outlier=Outlier.get_anyKPIindex_Outlier(KPInumber_Outlier, KPIname_Selected)
                            Outlier.click_anyKPIofTop20(1, KPIindex_outlier)
                            AgentName=Outlier.get_anyKPIofTop20(1, 1)
                            Outlier.click_addCoachButton()
                            TCoach.Add_AnyCoachOrTriad(self.coachformname)
                            Header.click_backbutton()
                            Tablet.click_performancecircle()
                            if tablist[ywm]=="LastTwoMonth":
                                Ppage.click_timetab_performance(1)
                            elif tablist[ywm]=="LastMonth":
                                Ppage.click_timetab_performance(2)
                            elif tablist[ywm]=="Month-to-Date":
                                Ppage.click_timetab_performance(3)
                            Agent_lineindex=Ppage.get_anyAgentindex(AgentName)
                            KPIindexChecked_List_Performance=[]
                            if lobname in Gl.DoubleKPIname_lob:
                                KPInumber_Performance_First=Ppage.get_KPInumber()
                                KPInumber_Performance_Second=Ppage.get_KPInumber_Second()
                                KPInumber_Performance=Ppage.get_KPInumber_All()
                                KPIindexChecked_List_Performance=[KPInumber_Performance+1]
                                KPIname_FromPerformancePage_First_list=Ppage.get_KPIname_list(KPInumber_Performance_First)
                                KPIname_FromPerformancePage_Second_list=Ppage.get_KPIname_list(KPInumber_Performance_Second)
                                KPIname_FromPerformancePage_list=KPIname_FromPerformancePage_First_list+KPIname_FromPerformancePage_Second_list
                                
                            else:
                                KPInumber_Performance=Ppage.get_KPInumber()
                                for KPIindex in range(2,KPInumber_Performance+1):
                                    if Ppage.get_anyKPIname(KPIindex) == KPIname_Selected:
                                        KPIindexChecked_List_Performance.append(KPIindex)
                                KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber_Performance)
                                
                            KPIofGoal_FromPerformancePage_list=Ppage.get_AllKPIsofGoal_list(KPInumber_Performance)
                            KPIofSite_FromPerformancePage_list=Ppage.get_AllKPIsofSite_list(KPInumber_Performance)
                            KPIofTeam_FromPerformancePage_list=Ppage.get_AllKPIsofTeam_list(KPInumber_Performance)
                            KPIofAgent_FromPerformancePage_list=Ppage.get_AllKPIsofAgent_TL_list(KPInumber_Performance,Agent_lineindex)
                            
                            Header.click_backbutton()
                            Tablet.click_TL_coachingcircle()
                            
                            #CoachHome.click_eachcoach(SN_path)
                            CoachHome.click_eachcoach(1)
                            #KPInumber_CoachDetail=BasicInfo.get_KPInumber()
                            #print KPInumber_CoachDetail
                            if lobname in Gl.DoubleKPIname_lob:
                                KPInumber_CoachDetail_First=BasicInfo.get_KPInumber()
                                KPInumber_CoachDetail_Second=BasicInfo.get_KPInumber_Second()
                                KPInumber_CoachDetail=BasicInfo.get_KPInumber_All()
                                KPIindexChecked_List_Performance=[KPInumber_CoachDetail+1]
                                KPIname_FromDetailPage_First_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail_First)
                                KPIname_FromDetailPage_Second_list=BasicInfo.get_KPIname_list(KPInumber_CoachDetail_Second)
                                KPIname_FromDetailPage_list=KPIname_FromDetailPage_First_list+KPIname_FromDetailPage_Second_list
                            else:
                                KPInumber_CoachDetail=BasicInfo.get_KPInumber()
                                KPIname_FromDetailPage_list=Ppage.get_KPIname_list(KPInumber_CoachDetail)
                            
                            
                            
                            KPIofGoal_FromDetailPage_list=BasicInfo.get_KPIofGoal_list(KPInumber_CoachDetail)
                            KPIofSite_FromDetailPage_list=BasicInfo.get_KPIofSite_list(KPInumber_CoachDetail)
                            KPIofTeam_FromDetailPage_list=BasicInfo.get_KPIofTeam_list(KPInumber_CoachDetail)
                            KPIofAgentOfTL_FromDetailPage_list=BasicInfo.get_KPIofAgentOfTL_list(KPInumber_CoachDetail)
                            
                            
                            Goal_index_Dic=KPIMethod.get_IndexOfTwovalue_list(KPIofGoal_FromPerformancePage_list)
                            Goal_SingleValue_index_list=Goal_index_Dic["SingleValue_index_list"]
                            Goal_TwoValue_index_list=Goal_index_Dic["TwoValue_index_list"]
                            Team_index_Dic=KPIMethod.get_IndexOfTwovalue_list(KPIofTeam_FromPerformancePage_list)
                            Team_SingleValue_index_list=Team_index_Dic["SingleValue_index_list"]
                            Team_TwoValue_index_list=Team_index_Dic["TwoValue_index_list"]
                            '''Check_Month-To-Date:
                                         1) Enter this form detail page with title 'Coaching -Commendation'
                                         2) Show header name 'Coaching KPIs(Month-To-Date)'
                                         3) All KPI data of Goal, Site,Agent should be the same as those on the corresponding performance page.
                                         4) The  KPIs achievement is checked by default.
                                         5)  Other KPIs are unchecked by default.'''
                            assert Header.get_HeaderTittle()==self.coachpagetitle
                            if tablist[ywm]=="Month-to-Date":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_monthtodate
                            elif tablist[ywm]=="LastTwoMonth":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_LastTwoMonth
                            elif tablist[ywm]=="LastMonth":
                                assert BasicInfo.get_KPIboxTitle()==KPIbox_title_LastMonth   
                            for a1 in range(0,len(Goal_SingleValue_index_list)):
                                i=Goal_SingleValue_index_list[a1]
                                assert KPIofGoal_FromPerformancePage_list[i]==KPIofGoal_FromDetailPage_list[i]
                            for a2 in range(0,len(Goal_TwoValue_index_list)):#the second value in performance = the second value in Coach detail page = the first value in coach detail page
                                i=Goal_TwoValue_index_list[a2]
                                assert (KPIofGoal_FromPerformancePage_list[i].split("\n"))[1]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[0]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[1]
                            
                            assert KPIofSite_FromPerformancePage_list==KPIofSite_FromDetailPage_list    
                                
                            for b1 in range(0,len(Team_SingleValue_index_list)):
                                i=Team_SingleValue_index_list[b1]
                                assert KPIofTeam_FromPerformancePage_list[i]==KPIofTeam_FromDetailPage_list[i]
                            for b2 in range(0,len(Team_TwoValue_index_list)):#Only the first value in Coach detail page = the second first in Performance page
                                i=Team_TwoValue_index_list[b2]
                                assert ((KPIofTeam_FromPerformancePage_list[i])[0].split("\n"))[0]==((KPIofTeam_FromDetailPage_list[i])[0].split("\n"))[0]
                            
                            assert KPIofAgent_FromPerformancePage_list==KPIofAgentOfTL_FromDetailPage_list
                            
                            #print "KPIindexChecked_List_Performance=",KPIindexChecked_List_Performance
                            for index in range(2,KPInumber_CoachDetail):
                                if index in KPIindexChecked_List_Performance:
                                    assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_CheckedStatus
                                else:
                                    assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                            Header.click_backbutton()
                            time.sleep(Gl.waittime)
                            Header.click_backbutton()
                            Tablet.click_TL_outliercircle()
                    
                            L.logout_tablet()  
                            GetConfig.print_EndTest_message(lobname, sitename)  
                            
    def get_IndexOfTwovalue_list(self,KPIlist):
        index_Dic={}
        SingleValue_index_list=[]
        TwoValue_index_list=[]
        for a in range(0,len(KPIlist)):
            if type(KPIlist[a])==list:
                if "\n" in KPIlist[a][0]:
                    TwoValue_index_list.append(a) 
                else:
                    SingleValue_index_list.append(a)
            else:
                if "\n" in KPIlist[a]:
                    TwoValue_index_list.append(a) 
                else:
                    SingleValue_index_list.append(a) 
        index_Dic["SingleValue_index_list"]=SingleValue_index_list
        index_Dic["TwoValue_index_list"]=TwoValue_index_list   
        return index_Dic 
                            
    
    def tearDown(self):
        #Gl.driver.quit()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()