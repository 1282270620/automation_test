'''
Created on Apr 25, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
class CoachingExportPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CoachName_dropdown_path="//*[@id='container']/div/section/div/div[1]/div/div[1]/div[1]/div/ul/li[%d]/a"
        
        self.CoachNameBox_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[1]/div/div/span")
        self.EmployeeNameBox_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[2]/div/div/span")
        self.EmployeeName_dropdown_path="//*[@id='container']/div/section/div/div[1]/div/div[2]/div[1]/div/ul/li[%d]/a"
        self.TypeBox_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div/div[1]/div[2]/div/span/span")
        self.TypeDownload_path="//*[@id='container']/div/section/div/div[1]/div/div[1]/div[2]/div/ul/li[%d]/a"
        
        self.StatusBox_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div/div[2]/div[2]/div/span")
        self.Status_dropdwon_path="//*[@id='container']/div/section/div/div[1]/div/div[2]/div[2]/div/ul/li[%d]/a"
        self.FilterButton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[4]/button")
        self.ExportButton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div/div[4]/button[2]")
        
        self.CoachItem_other_path="//*[@id='container']/div/section/div/div[1]/div/div[%d]/div[%d]/label"
        self.CoachItem_time_path="//*[@id='container']/div/section/div/div[1]/div/div[3]/div[%d]/div[1]/label" 
        self.CoachItem_Box_other_path="//*[@id='container']/div/section/div/div[1]/div/div[%d]/div[%d]/div/span"
        self.CoachItem_Box_time_path="//*[@id='container']/div/section/div/div[1]/div/div[3]/div[%d]/div[%d]/div/div/div[2]/input"
        self.WarnningMessage_loc="//*[@id='container']/div/div[2]/div/p[2]"
        self.CoachList_Header_path="//*[@id='container']/div/section/div/div[2]/table/thead/tr/th[%d]"
    
    def get_all_CoachListHeader(self):
        '''index:1~7'''
        GetText=Get_AnyText_ForNormal()
        CoachListHeader_List=GetText.Get_Text_ForLoop(1,self.CoachList_Header_path)
        return CoachListHeader_List
    def get_warningmessage(self):
        return self.find_element(*self.WarnningMessage_loc).text       
    def get_Type_download(self,index):
        TypeDownload_loc=(By.XPATH,self.TypeDownload_path % index)
        return self.find_element(*TypeDownload_loc).text
    def get_CoachItem_other_box(self,index1,index2):
        CoachItemBox_loc=(By.XPATH,self.CoachItem_Box_other_path % (index1,index2))
        return self.find_element(*CoachItemBox_loc).text
    def get_CoachItem_time_box(self,index1,index2):
        CoachItemBox_loc=(By.XPATH,self.CoachItem_Box_time_path % (index1,index2))
        return self.find_element(*CoachItemBox_loc).text
    
    def get_CoachItemName_other(self,index1,index2):    
        CoachItem_loc=(By.XPATH,self.CoachItem_other_path % (index1,index2))
        return (self.find_element(*CoachItem_loc).text)[:-1]
    
    def get_CoachItemName_time(self,index):    
        CoachItem_loc=(By.XPATH,self.CoachItem_time_path % index)
        return (self.find_element(*CoachItem_loc).text)[:-1]
    
    def click_CoachNameBox(self):
        self.find_element(*self.CoachNameBox_loc).click()
        time.sleep(Gl.waittime)
        
    def get_all_CoachName(self):
        '''index=1:Filter
           index=2:All'''   
        GetText=Get_AnyText_ForNormal()
        FirstCoachName_loc=(By.XPATH,self.CoachName_dropdown_path % 1)
        if self.Element_displayed(*FirstCoachName_loc)==True:
            CoachNameList=GetText.Get_Text_ForLoop(2,self.CoachName_dropdown_path)
        else:
            CoachNameList=GetText.Get_Text_ForLoop(3,self.CoachName_dropdown_path)
        print CoachNameList
        '''
        if CoachNameList[0]=="All":
            CoachNameList=CoachNameList[1:]
        else:
            CoachNameList=CoachNameList[2:]'''
        return CoachNameList    
    
    def select_CoachName(self,coachname):    
        CoachName_loc=(By.LINK_TEXT,coachname)
        self.find_element(*CoachName_loc).click()
        self.wait_loadingmask_disappear()
        
    def click_EmployeeNameBox(self):
        self.find_element(*self.EmployeeNameBox_loc).click()
        time.sleep(Gl.waittime)
    def get_all_EmployeeName(self):
        '''index=2:All
           index=1:Filter Box'''
        GetText=Get_AnyText_ForNormal()
        EmployeeNameList=GetText.Get_Text_ForLoop(3,self.EmployeeName_dropdown_path)
        return EmployeeNameList    
    def select_EmployeeName(self,employeename):
        EmployeeName_loc=(By.LINK_TEXT,employeename)
        self.find_element(*EmployeeName_loc).click()
        self.wait_loadingmask_disappear()
        
    def click_TypeBox(self):
        self.find_element(*self.TypeBox_loc).click()
        time.sleep(Gl.waittime)
        
    def select_Type(self,Typename):
        TypeName_loc=(By.LINK_TEXT,Typename)
        self.find_element(*TypeName_loc).click()
        self.wait_loadingmask_disappear()
        
    def click_StatusBox(self):
        self.find_element(*self.StatusBox_loc).click()
        self.wait_loadingmask_disappear()
    def get_all_StatusValue(self):
        GetText=Get_AnyText_ForNormal()  
        StatusList=GetText.Get_Text_ForLoop(1,self.Status_dropdwon_path)
        return StatusList    
    def select_Status(self,Statusname):
        StatusName_loc=(By.LINK_TEXT,Statusname)
        self.find_element(StatusName_loc).click()
        time.sleep(Gl.waittime)
        
    def select_Status_All(self):
        Status_All_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[2]/div[2]/div/ul/li[1]")
        self.find_element(*Status_All_loc)
        time.sleep(Gl.waittime)
        
    def select_CombinationConditions(self,coachname,employeename,Typename,Statusname):
        '''Not include create date and completed date '''
        if coachname!="":
            self.click_CoachNameBox()
            self.select_CoachName(coachname)
        if employeename!="":
            self.click_EmployeeNameBox()
            self.select_EmployeeName(employeename)
        if Typename!="":
            self.click_TypeBox()
            self.select_Type(Typename)
        if Statusname!="":
            self.click_StatusBox()
            if Statusname=="All":
                self.select_Status_All()
            else:
                self.select_Status(Statusname)
        
        
    
    def click_Filter(self):
        self.find_element(*self.FilterButton_loc).click()
        self.wait_loadingmask_disappear()
        
    def click_Export(self):
        self.find_element(*self.ExportButton_loc).click()
        time.sleep(5*Gl.waittime)
        
    def Pagenumber_exist(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH,("//*[@id='container']/div/section/div/nav/ul/li[%d]/a")%pageindex)
        flag=self.Element_displayed(*Pagenumber_loc)
        return flag
    def click_Pagenumber(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH,("//*[@id='container']/div/section/div/nav/ul/li[%d]/a")%pageindex)
        self.find_element(*Pagenumber_loc).click()
        time.sleep(Gl.waittime)
    def get_Pagenumber(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH,("//*[@id='container']/div/section/div/nav/ul/li[%d]/a")%pageindex)
        Pagenumber=self.find_element(*Pagenumber_loc).text
        return Pagenumber
    def get_typename(self,coachname_path):#Get type dropdown list
        coachname_loc=(By.XPATH,coachname_path)
        coachformname = self.find_element(*coachname_loc).text
        return coachformname
    def get_Total_pagenumber(self):
        pageindex=3
        if self.Pagenumber_exist(pageindex)==False:
            total_pagenumber=1
            last_pageindex=""
        else:
            while self.Pagenumber_exist(pageindex)==True:
                pageindex=pageindex+1
            last_pageindex=pageindex-3
            total_pagenumber=self.get_Pagenumber(last_pageindex)
        pagedic={'pagenumber':total_pagenumber,'pageindex':last_pageindex}
        return pagedic
            
    def get_Total_coachnumber(self):
        total_pagedic=self.get_Total_pagenumber()
        total_pagenumber=int(total_pagedic['pagenumber'])
        pageindex=total_pagedic['pageindex']
        if pageindex=="":
            Total_coachnumber_tablet=self.get_coachnumber_onepage()
        else:
            self.click_Pagenumber(pageindex)
            Total_coachnumber_tablet=20*(total_pagenumber-1)+self.get_coachnumber_onepage()
            
        return Total_coachnumber_tablet        

        
    
        
    def get_anyCoach_attribute(self,coachindex,attrindex):
        anyCoach_attribute_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[%d]")%(coachindex,attrindex))
        anyCoach_attribute=self.find_element(*anyCoach_attribute_loc).text
        return anyCoach_attribute
    
    def Coach_line_exist(self,coachindex):
        anyCoach_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[1]") % coachindex )
        flag=self.Element_displayed(*anyCoach_loc)
        return flag
    def get_coachnumber_onepage(self):
        coachindex=1
        if self.Coach_line_exist(coachindex)==False:
            coachindex=0
            return coachindex
        else:
            while self.Coach_line_exist(coachindex)==True:
                coachindex=coachindex+1
            return coachindex-1    
