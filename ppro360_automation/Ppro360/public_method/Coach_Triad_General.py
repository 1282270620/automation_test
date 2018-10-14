'''
Created on Feb 10, 2017

@author: Sabrina Guo
'''
import time
from public_method import Gl

from Tablet_pages.PerformancPage import PerformancePage
from Tablet_pages.Popupaddcoachpage import Popupaddcoachpage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from Tablet_pages.CoachingExportPage import CoachingExportPage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from public_method.HandleMySQL import HandleMySQL
from public_method.Get_CoachContent import Get_CoachContent

class Coach_Triad_General():
    '''
    classdocs
    '''
    def Get_CoachOrTriad_FromPopUpWindow(self):#New
        TotalNumber=0
        Disbaled_list=[]
        Enabled_list=[]
        All_list=[]
        PU2=Popupaddcoachpage()
        coachnameindex=1
        #print PU2.coachname_exsit(coachnameindex)
        while PU2.coachname_exsit(coachnameindex)==True:
            coachformname = PU2.get_coachname(coachnameindex)
            All_list.append(coachformname)
            if PU2.isornot_enable(coachnameindex)=="true":
                Disbaled_list.append(coachformname)
            else:
                Enabled_list.append(coachformname)
            coachnameindex=coachnameindex+1
            TotalNumber=TotalNumber+1    
            #time.sleep(Gl.waittime)        
        AllCoachOrTriadInfo={"Disabled_list":Disbaled_list,"Enabled_list":Enabled_list,"All_list":All_list,"TotalNumber":TotalNumber} 
        return AllCoachOrTriadInfo
    
    def Get_typelist(self):#New
        #dropdown_path="//*[@id='container']/div/section/div/div[1]/div[2]/div[1]/div/ul/li[%d]/a"
        dropdown_path="//*[@id='container']/div/section/div/div[1]/div/div[1]/div[3]/div/ul/li[%d]/a"
        
        time.sleep(Gl.waittime)
        Tc=Coachinghomepage()
        Tc.click_type()
        CoachingDropDownlist=[]
        coachnameindex=1
        Flag=True
        while Flag:
            coach_path=dropdown_path %coachnameindex
            Existflag=Tc.isElementExist(coach_path)
            if Existflag == True:
                coachingname=Tc.get_typename(coach_path)
                #print coachingname
                if coachingname == "":
                    break
                elif coachingname == "All":
                    coachnameindex=coachnameindex+1
                else:
                    CoachingDropDownlist.append(coachingname)
                    coachnameindex=coachnameindex+1
            else:
                Flag=False
        return CoachingDropDownlist
    
    def Get_typelist_CoachingExport(self):#New
        #dropdown_path="//*[@id='container']/div/section/div/div[1]/div[2]/div[1]/div/ul/li[%d]/a"
        dropdown_path="//*[@id='container']/div/section/div/div[1]/div/div[1]/div[2]/div/ul/li[%d]/a"
       
        time.sleep(Gl.waittime)
        CoachingExport=CoachingExportPage()
        CoachingExport.click_TypeBox()
        
        CoachingDropDownlist=[]
        coachnameindex=1
        Flag=True
        while Flag:
            coach_path=dropdown_path %coachnameindex
            Existflag=CoachingExport.isElementExist(coach_path)
            if Existflag == True:
                coachingname=CoachingExport.get_typename(coach_path)
                #print coachingname
                if coachingname == "":
                    break
                elif coachingname == "All":
                    coachnameindex=coachnameindex+1
                else:
                    CoachingDropDownlist.append(coachingname)
                    coachnameindex=coachnameindex+1
            else:
                Flag=False
        return CoachingDropDownlist
    
    def Add_AnyCoachOrTriad(self,coachformname):  
        PopCoach=Popupaddcoachpage()  
        coachnameindex=1
        while PopCoach.coachname_exsit(coachnameindex):
            if PopCoach.get_coachname(coachnameindex)==coachformname:
                PopCoach.select_coach(coachnameindex)
                PopCoach.add_coach()
            else:
                coachnameindex=coachnameindex+1
            
    
    def Click_triadcoach_firstTLofOM(self):
        P=PerformancePage()
        P.select_TLkpi()
        time.sleep(Gl.waittime)
        P.click_addTriadcoachbutton()
        
    def Click_coach_firstAgentofOM(self):#Old
        P=PerformancePage()
        P.select_Agentkpi()
        time.sleep(Gl.waittime)
        P.click_addcoachbutton()
        
    def Select_firstAgentofOM(self):#New
        P=PerformancePage()
        P.select_Agentkpi()
        time.sleep(Gl.waittime)
        P.click_addcoachbutton()
        
    def Click_coach_firstAgentofTL(self):
        P=PerformancePage()
        P.select_AgentofTLkpi()
        time.sleep(Gl.waittime)
        P.click_addcoachbutton()
        
    def Check_tittle(self,coachtype,Expectedpopuptittle):#Old
        PU=Popupaddcoachpage()
        tittle = PU.get_tittle()
        if coachtype == "triadcoaching":
            nu=23
        elif coachtype == "coaching":
            nu=17   
        tittle = tittle[0:nu]
        #------Only 0:17 is the expected tittle from CSV
        Expectedtittle=Expectedpopuptittle[0:nu]
        assert tittle == Expectedtittle
        
    def Get_AddWindow_title(self,coachtype):#New
        PU=Popupaddcoachpage()
        title = PU.get_title()
        if coachtype == "triadcoaching":
            nu=23
        elif coachtype == "coaching":
            nu=17   
        title = title[0:nu]
        return title
    
    def close_popupwindow(self):
        PU=Popupaddcoachpage()  
        PU.close_popup() 
    
    
    #****************************************
    def Check_WarningMessage_CoachingExport(self):
        CoachExport=CoachingExportPage()
        assert CoachExport.get_warningmessage()=="No available form could be exported."
        
    def Check_Header(self,LoginName,LoginRole,lobname,sitename): 
        Header=HeaderPage()
        print Header.get_loginName()
        print LoginName
        assert Header.get_loginName()==LoginName
        assert Header.get_loginRole()==LoginRole
        assert Header.get_loginLob()==lobname
        assert Header.get_loginSite()==sitename
    def Check_CoachingExportItemName(self):    
        CoachExport=CoachingExportPage()
        assert CoachExport.get_CoachItemName_other(1, 1)=="Coach Name"
        assert CoachExport.get_CoachItemName_other(2, 1)=="Employee Name"
        assert CoachExport.get_CoachItemName_time(1)=="Created Date"
        
        assert CoachExport.get_CoachItemName_other(1, 2)=="Type"
        assert CoachExport.get_CoachItemName_other(2, 2)=="Status"
        assert CoachExport.get_CoachItemName_time(2)=="Completed Date"
    def Check_CoachingExportFilterValue(self,CoachName,EmployeeName,Status,Type,Created_StartDate,Created_EndDate,Completed_StartDate,Completed_EndDate):
        CoachExport=CoachingExportPage()
        assert CoachExport.get_CoachItem_other_box(1, 1)==CoachName
        assert CoachExport.get_CoachItem_other_box(2,1)==EmployeeName
        assert CoachExport.get_CoachItem_time_box(1, 1)==Created_StartDate
        assert CoachExport.get_CoachItem_time_box(1, 2)==Created_EndDate
        
        assert CoachExport.get_CoachItem_other_box(1, 2)==Type
        assert CoachExport.get_CoachItem_other_box(2, 2)==Status
        assert CoachExport.get_CoachItem_time_box(2, 1)==Completed_StartDate
        assert CoachExport.get_CoachItem_time_box(2, 2)==Completed_EndDate
    
    
    def Check_CoachingItemName(self,lobname):
        CoachHome=Coachinghomepage()
        assert CoachHome.get_CoachItem_tittle_other(1, 1)=="SN"
        assert CoachHome.get_CoachItem_tittle_other(2, 1)=="HRID"
        assert CoachHome.get_CoachItem_tittle_time(1)=="Created Date"
        
        assert CoachHome.get_CoachItem_tittle_other(1, 2)=="Coach Name"
        assert CoachHome.get_CoachItem_tittle_other(2, 2)=="Employee Name"
        assert CoachHome.get_CoachItem_tittle_time(2)=="Completed Date"
        
        assert CoachHome.get_CoachItem_tittle_other(1, 3)=="Type"
        assert CoachHome.get_CoachItem_tittle_other(2, 3)=="Status"
        assert CoachHome.get_CoachItem_tittle_time(3)=="Acknowledge Date"
        
        if lobname != "AOL":
            assert CoachHome.get_CoachItem_tittle_other(3, 4)=="Call Recording Number"
            
    def Check_CoachFilterValue(self,CoachName,EmployeeName,Status,Type,Created_StartDate,Created_EndDate,Completed_StartDate,Completed_EndDate,Acknowledge_StartDate,Acknowledge_EndDate):
        CoachHome=Coachinghomepage()
        print CoachHome.get_CoachName(),CoachName
        assert CoachHome.get_CoachName()==CoachName
        assert CoachHome.get_EmployeeName()==EmployeeName
        assert CoachHome.get_status_selected()==Status
        assert CoachHome.get_typename_selected()==Type
        assert CoachHome.get_CreatedDate(1)==Created_StartDate
        assert CoachHome.get_CreatedDate(2)==Created_EndDate
        assert CoachHome.get_CompletedDate(1)==Completed_StartDate
        assert CoachHome.get_CompletedDate(2)==Completed_EndDate
        assert CoachHome.get_AcknowledgeDate(1)==Acknowledge_StartDate
        assert CoachHome.get_AcknowledgeDate(2)==Acknowledge_EndDate
        
    def Check_TotalCoachNumber_withDB(self,TotalCoachNumber_page,hostindex,lobname_database, sitename_database,dbuser,dbpassword,sql_coach):
        HMysql=HandleMySQL()
        TotalCoach_DB=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, dbuser, dbpassword, sql_coach)
        TotalCoachNumber_DB=TotalCoach_DB[0]
        print TotalCoachNumber_page
        print TotalCoachNumber_DB
        assert TotalCoachNumber_page==TotalCoachNumber_DB
    
    def Check_TotalCoachNumber_withExcel(self,TotalCoachNumber_page,filename_prefix, sheetname):
        GetCoachContent=Get_CoachContent()
        TotalCoachNumber_excel=GetCoachContent.Get_TotalCoachNumber(filename_prefix, sheetname)
        print TotalCoachNumber_page
        print TotalCoachNumber_excel
        assert TotalCoachNumber_page==TotalCoachNumber_excel
        #AllCoachNameList,
    def Check_AllCoachName_withDB(self,TotalCoachName_page,hostindex,lobname_database, sitename_database,dbuser,dbpassword,sql_OMLC,sql_TL):
        HMysql=HandleMySQL()
        Total_OMInfo=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, dbuser, dbpassword, sql_OMLC)
        Total_OM=[]
        print Total_OMInfo
        for i in range(0,len(Total_OMInfo[1])):
            OM_name=Total_OMInfo[1][i][0]+" "+Total_OMInfo[1][i][1]
            Total_OM.append(OM_name)
        print Total_OM
        if sql_TL!="":
            Total_TLInfo=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, dbuser, dbpassword, sql_TL)
            Total_TL=[]
            if Total_TLInfo[0]!=0:
                for i in range(0,len(Total_TLInfo[1])):
                    TL_name=Total_TLInfo[1][i][1]+" "+Total_TLInfo[1][i][2]
                    Total_TL.append(TL_name)
            TotalCoachName_DB=Total_OM+Total_TL
                
        else:
            TotalCoachName_DB=Total_OM
        time.sleep(2*Gl.waittime)
        print TotalCoachName_DB
        print TotalCoachName_page
        assert len(TotalCoachName_DB)==len(TotalCoachName_page)
        for item in TotalCoachName_DB:
            assert item in TotalCoachName_page
        
    def Check_AllEmployeeName_withDB(self,role,coachtype,TotalEmployeeName_page,hostindex, lobname_database, sitename_database, dbuser, dbpassword, sql_Employee):    
        HMysql=HandleMySQL()
        Total_EmployeeInfo=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, dbuser, dbpassword, sql_Employee)
        TotalEmployee_DB=[]
        print Total_EmployeeInfo[1]
        if coachtype=="Coaching":
            if role=="L3" or role=="LC" or role=="SVP":
                d=3
            elif role=="L1":
                d=5
            
        elif coachtype=="Triadcoaching":
            if role=="L3" or role=="LC" or role=="SVP":
                d=1
            elif role=="L1":
                pass
        for i in range(0,len(Total_EmployeeInfo[1])):
            Employee_name=Total_EmployeeInfo[1][i][d]+" "+Total_EmployeeInfo[1][i][d+1]
            print Employee_name
            TotalEmployee_DB.append(Employee_name)
        
        
            
        print "TotalEmployee_DB:"
        print TotalEmployee_DB
        print "TotalEmployeeName_page:"
        print TotalEmployeeName_page
        assert len(TotalEmployee_DB)==len(TotalEmployeeName_page)
        for item in TotalEmployee_DB:
            assert item in TotalEmployeeName_page
        #assert TotalEmployeeName_page==TotalEmployee_DB
    def Check_AllStatusValue_withStandardValue(self,TotalStatus_page):
        TotalStatus_Standard=["All","Incompleted","Planned","Ongoing","Completed","Acknowledged","Canceled"]
        print TotalStatus_page,TotalStatus_Standard
        assert TotalStatus_page==TotalStatus_Standard
        
    def Check_CoachListHeader_withStandardValue(self,CoachListHeader_List_page):
        CoachListHeader_List_Standard=["SN", "Coach Name",  "Employee Name","HRID", "Type", "Status","Video", "Created Date", "Completed Date", "Acknowledge Date","Satisfaction"]
        print CoachListHeader_List_page,CoachListHeader_List_Standard
        assert CoachListHeader_List_page==CoachListHeader_List_Standard
        
    def Check_CoachExportListHeader_withStandardValue(self,CoachListHeader_List_page):
        CoachListHeader_List_Standard=["SN", "Coach Name",  "Employee Name","Type", "Status", "Created Date", "Completed Date"]
        print CoachListHeader_List_page 
        print CoachListHeader_List_Standard 
        assert CoachListHeader_List_page==CoachListHeader_List_Standard    

