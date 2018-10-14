'''
Created on Apr 25, 2017

@author: symbio
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.CoachingExportPage import CoachingExportPage
import MySQLdb
from public_method import Gl
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.Deleteexistfile import Deleteexistfile
#from public_method.Get_file import Get_file
from public_method.Get_CoachContent import Get_CoachContent
from public_method.HandleMySQL import HandleMySQL
from public_method.Coaching_PublicFunction import Coaching_PublicFunction


class OM_FilterFunction_exportModule(unittest.TestCase):


    def setUp(self):
        self.caseID="OM_FilterFunction_exportModule"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.Adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.LCuserid=GetData.get_LCuserid()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Whose database name is special
        #self.lob_databasespecial=GetData.get_SpecialLobforDatabase()
        #Database info
        self.host=GetData.get_StageNodeHost(92)
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
       
        #CoachExport file prefix
        self.filename_prefix="coaching_export"
        
        self.sheetname="Sheet1"
        
        


    def tearDown(self):
        Gl.driver.quit()
        #pass


    def test_OM_FilterFunction_exportModule(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        GetAccount=Get_AllRoleAccountForTest()
        #CoachExportPage=CoachingExportPage()
        Deletefile=Deleteexistfile()
        GetCoachContent=Get_CoachContent()
        HMySQL=HandleMySQL()
        
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
                    coach_list=GetConfig.get_CoachingExportFormList(lobname)
                    database_name=HMySQL.Get_DatabaseName(lobname, sitename)
                    
                    '''Start to test........ '''
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    THomepage.click_OM_coachingExportcircle()
                    
                    #Step1:Case for Coaching Name="All"  Employee Name="All"  Type=select one form    Other option 'All'
                    '''1.Coaching Name="All"  Employee Name="All"  Type=select one form    Other option="All" '''
                    
                    coachname='All'
                    employeename='All'
                    Typename_list=coach_list
                    Statusname='All'
                    
                    
                    
                    #Step1.3:get total_coachnumber from database
                    #Connect to database
                    conn=MySQLdb.connect(self.host,self.dbuser,self.dbpassword,database_name)
                    cursor=conn.cursor()
                    conn.autocommit(True)
                    #Step1.1:Get total_coachnumber from tablet
                    print Typename_list
                    for Typename in Typename_list:
                        
                        #Step1.0:Delete coaching_export file
                        Deletefile.delete_coachfile(self.downloadpath)
                        Total_coachnumber_tablet_1=self.Filter_combination(coachname, employeename, Typename, Statusname)
                    #Step1.2:Get total_coachnumber from excel
                        Total_coachnumber_excel_1=GetCoachContent.Get_TotalCoachNumber(self.filename_prefix, self.sheetname)
                        
                        
                        
                        
                    
                    #Execute sql
                        print Typename
                        type_id=str(int(GetConfig.get_CoachID(Typename)))
                        print "type_id:",type_id
                        sql_all="select * from coach where type="+type_id+" order by id desc;"
                        Total_coachnumber_database_1=cursor.execute(sql_all)
                        print Total_coachnumber_database_1
                        print Total_coachnumber_excel_1
                        assert Total_coachnumber_tablet_1==Total_coachnumber_database_1
                        assert Total_coachnumber_excel_1==Total_coachnumber_database_1
                        #Check if header is correct
                        
                        header_rows=int(GetConfig.get_FormDetailHeader_TotalRows(Typename))
                        print header_rows
                        '''
                        Headerlist_Actual=GetCoachContent.Get_CoachExcelHeader(self.filename_prefix, self.sheetname,header_rows)
                        '''
                        Headerlist_Actual=GetCoachContent.Get_CoachExcelHeader_Actual(self.filename_prefix, self.sheetname, header_rows)
                        
                        #Headerlist_Expected=GetConfig.get_FormDetailHeader(Typename)
                        Headerlist_Expected=GetConfig.get_anyFormHeaderList_InExcel(Typename)
                        print Headerlist_Actual
                        print Headerlist_Expected
                        assert Headerlist_Expected==Headerlist_Actual
                    
                    cursor.close()
                    conn.close()
                   
     
                    
    def Filter_combination(self,coachname, employeename, Typename, Statusname): 
        CoachingPublic=Coaching_PublicFunction()
        Cexport=CoachingExportPage()
        Cexport.select_CombinationConditions(coachname, employeename, Typename, Statusname)
        Cexport.click_Filter()
        Cexport.click_Export()
        #Step1.1:Get total_coachnumber from tablet
        #Total_coachnumber_tablet=Cexport.get_Total_coachnumber()
        Dic=CoachingPublic.get_Total_PageandCoachnumber()
        Total_coachnumber_tablet=Dic["Total_coachnumber_tablet"]
        return Total_coachnumber_tablet
    
    def Get_AnyattributeofAllCoach_tablet(self,Total_coachnumber_tablet):#attrindex=1:SN,attrindex=2:CoachName,attrindex=3:EmployeeName
        Cexport=CoachingExportPage()
        Attribute_All_Coach_tablet_Dic={}
        if Total_coachnumber_tablet==0:
            Attribute_All_Coach_tablet_Dic={}
        elif Total_coachnumber_tablet<=20:
            pagenumber=1
            pageindex=0
            coachindex=Total_coachnumber_tablet
            Attribute_All_Coach_tablet_Dic=self.Get_AnyattributeofEachCoach_tablet(pageindex,coachindex)
        elif Total_coachnumber_tablet>20:
            if Total_coachnumber_tablet % 20==0:
                pagenumber=Total_coachnumber_tablet/20
                for pageindex in range(1,pagenumber+1):
                    Cexport.click_Pagenumber(pageindex+2)
                    dic_page=self.Get_AnyattributeofEachCoach_tablet(pageindex,20)
                    Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_page.items())
            else:
                pagenumber_int=Total_coachnumber_tablet/20
                pagenumber_total=pagenumber_int+1
                coachnumber_lastpage=Total_coachnumber_tablet%20
                for pageindex in range(1,pagenumber_int+1):
                    Cexport.click_Pagenumber(pageindex+2)
                    dic_page=self.Get_AnyattributeofEachCoach_tablet(pageindex,20)
                    Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_page.items())
                Cexport.click_Pagenumber(pagenumber_total+2)
                dic_lastpage=self.Get_AnyattributeofEachCoach_tablet(pagenumber_total,coachnumber_lastpage)
                Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_lastpage.items())
        
        return Attribute_All_Coach_tablet_Dic
                
            
    def Get_AnyattributeofEachCoach_tablet(self,pageindex,coachnumber):
        Cexport=CoachingExportPage()
        Coach_tablet_Dic={}
        print "coachnumber=",
        print coachnumber
        for coachindex in range(1,coachnumber+1):
            print coachindex
            SNofCoach_tablet=Cexport.get_anyCoach_attribute(coachindex, 1)
            CoachNameofCoach_tablet=Cexport.get_anyCoach_attribute(coachindex, 2)
            EmployeeNameofCoach_tablet=Cexport.get_anyCoach_attribute(coachindex, 3)
            Info_EachCoach_List=[SNofCoach_tablet,CoachNameofCoach_tablet,EmployeeNameofCoach_tablet]
            key=pageindex*20+(coachindex-1)
            Coach_tablet_Dic[key]=Info_EachCoach_List
        return Coach_tablet_Dic

    
    
 
             
                    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()