'''
Created on Jan 13, 2017

@author: symbio
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
import time
from public_method import Gl
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
class Coachinghomepage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #Item tittle
        
        self.coachingItem_tittle_other_path="//*[@id='container']/div/section/div/div[1]/div/div[%d]/div[%d]/label"
        self.coachingItem_tittle_time_path="//*[@id='container']/div/section/div/div[1]/div/div[3]/div[%d]/div[1]/label"
                                                                
        #Item input box
        self.SN_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[1]/div[1]/input")
        self.CoachName_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[1]/div[2]/div/span")
        self.EmployeeName_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[2]/div[2]/div/span")
        self.coachnameselect_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[1]/div[2]/div/span/span")
        self.statusselect_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div/div[2]/div[3]/div/span")
        self.filterbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[1]/div[4]/button")
        self.exportbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div/div[4]/button[2]")
        self.CreatedDateBox_path="//*[@id='container']/div/section/div/div[1]/div/div[3]/div[1]/div[%d]/div/div/div[2]/input"
        self.CompletedDateBox_path="//*[@id='container']/div/section/div/div[1]/div/div[3]/div[2]/div[%d]/div/div/div[2]/input"
        self.AcknowledgeDateBox_path="//*[@id='container']/div/section/div/div[1]/div/div[3]/div[3]/div[%d]/div/div/div[2]/input"
        #self.type_loc=(By.XPATH,"(//span[@type='button'])[3]")
        self.type_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div/div[1]/div[3]/div/span")
        
        #container > div > div.loading-mask.hide,"
        self.statuschangedWarning_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div/p[1]")
        self.anyAttributeOfCoach_path="//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[%d]"
        
        self.CoachName_dropdown_path="//*[@id='container']/div/section/div/div[1]/div/div[1]/div[2]/div/ul/li[%d]/a"
        self.EmployeeName_dropdown_path="//*[@id='container']/div/section/div/div[1]/div/div[2]/div[2]/div/ul/li[%d]/a"
        self.Status_dropdwon_path="//*[@id='container']/div/section/div/div[1]/div/div[2]/div[3]/div/ul/li[%d]/a"
        self.CoachList_Header_path="//*[@id='container']/div/section/div/div[2]/table/thead/tr/th[%d]"
        
    def get_all_CoachListHeader(self):
        '''index:1~9'''
        GetText=Get_AnyText_ForNormal()
        CoachListHeader_List=GetText.Get_Text_ForLoop(1,self.CoachList_Header_path)
        return CoachListHeader_List
    def get_all_StatusValue(self):
        GetText=Get_AnyText_ForNormal()  
        StatusList=GetText.Get_Text_ForLoop(1,self.Status_dropdwon_path)
        return StatusList
    
    
    def get_all_EmployeeName(self):
        '''index=1:All
           index=2:Filter Box'''
        GetText=Get_AnyText_ForNormal()
        EmployeeNameList=GetText.Get_Text_ForLoop(3,self.EmployeeName_dropdown_path)
        return EmployeeNameList
    
    def get_EmployeeName_Nofilter(self):  
        '''index=1:All'''
        GetText=Get_AnyText_ForNormal()
        EmployeeNameList=GetText.Get_Text_ForLoop(2,self.EmployeeName_dropdown_path)
        return EmployeeNameList
    
    def get_all_CoachName(self):
        '''index=1:All'''   
        GetText=Get_AnyText_ForNormal()
        CoachNameList=GetText.Get_Text_ForLoop(2,self.CoachName_dropdown_path)
        return CoachNameList
       
   
    
           
    def get_CoachItem_tittle_other(self,d1,d2):#d1-di ji ge,d2-di ji ceng
        coachingItem_tittle_other_loc=(By.XPATH,self.coachingItem_tittle_other_path % (d1,d2))
        return (self.find_element(*coachingItem_tittle_other_loc).text)[:-1]
    def get_CoachItem_tittle_time(self,d):
        coachingItem_tittle_time_loc=(By.XPATH,self.coachingItem_tittle_time_path % d)
        return (self.find_element(*coachingItem_tittle_time_loc).text)[:-1]
       
        
    def input_SN(self,SNnumber):
        self.find_element(*self.SN_loc).send_keys(SNnumber)    
        
    def click_coachnamebox(self):
        self.find_element(*self.CoachName_loc).click()
    def select_coachname(self,coachname):
        coachname_loc=(By.LINK_TEXT,coachname)
        self.find_element(*self.coachnameselect_loc).click()
        self.find_element(*coachname_loc).click()
        time.sleep(5*Gl.waittime)
        
    def click_type(self):
        self.find_element(*self.type_loc).click()
        time.sleep(Gl.waittime)
    def get_typename_selected(self):
        typename=self.find_element(*self.type_loc).text
        return typename
    def get_CoachName(self):
        coachname=self.find_element(*self.CoachName_loc).text
        return coachname
    
    def get_typename(self,coachname_path):#Get type dropdown list
        coachname_loc=(By.XPATH,coachname_path)
        coachformname = self.find_element(*coachname_loc).text
        return coachformname   
    
    def click_EmployeeNamebox(self):
        self.find_element(*self.EmployeeName_loc).click()
    def get_EmployeeName(self):
        employeename=self.find_element(*self.EmployeeName_loc).text    
        return employeename
        
        
    def get_eachtextOfanycoachline(self,coach_path):
        coach_loc=(By.XPATH,coach_path)
        coach_text = self.find_element(*coach_loc).text
        return coach_text
    
    def click_statusbox(self):
        self.find_element(*self.statusselect_loc).click()
    def select_status(self,status):
        status_loc=(By.LINK_TEXT,status)
        self.find_element(*self.statusselect_loc).click()
        self.find_element(*status_loc).click()
        time.sleep(Gl.waittime)
    def get_status_selected(self):
        status=self.find_element(*self.statusselect_loc).text
        return status
    
        
    def get_CreatedDate(self,index):
        '''index=1:Start;index=2:End'''
        CreatedDate_loc=(By.XPATH,self.CreatedDateBox_path % index)
        return self.find_element(*CreatedDate_loc).text
    def get_CompletedDate(self,index):
        '''index=1:Start;index=2:End'''
        CompletedDate_loc=(By.XPATH,self.CompletedDateBox_path % index)
        return self.find_element(*CompletedDate_loc).text
    def get_AcknowledgeDate(self,index):
        '''index=1:Start;index=2:End'''
        AcknowledgeDate_loc=(By.XPATH,self.AcknowledgeDateBox_path % index)
        return self.find_element(*AcknowledgeDate_loc).text
    def click_filterbutton(self):
        self.find_element(*self.filterbutton_loc).click()
        self.wait_loadingmask_disappear()
    
    def click_exportbutton(self):
        self.find_element(*self.exportbutton_loc).click()
        self.wait_loadingmask_disappear()
    '''   
    def click_eachcoach(self,eachcoach_path):
        self.find_element(*(By.XPATH,eachcoach_path)).click()
        time.sleep(Gl.waittime)'''
        
    def click_eachcoach(self,coachindex):
        anyCoach_SN_loc=(By.XPATH,self.anyAttributeOfCoach_path % (coachindex,1))
        self.find_element(*anyCoach_SN_loc).click()
        self.wait_loadingmask_disappear()
        
        
    def click_Pagenumber(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH,("//*[@id='container']/div/section/div/nav/ul/li[%d]/a")%pageindex)
        self.find_element(*Pagenumber_loc).click()
        self.wait_loadingmask_disappear()
    
    def Coach_line_exist(self,coachindex):
        anyCoach_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[1]") % coachindex )
        flag=self.Element_displayed(*anyCoach_loc)
        return flag 
    def Pagenumber_exist(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH,("//*[@id='container']/div/section/div/nav/ul/li[%d]/a")%pageindex)
        flag=self.Element_displayed(*Pagenumber_loc)
        return flag 
    def get_Pagenumber(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH,("//*[@id='container']/div/section/div/nav/ul/li[%d]/a")%pageindex)
        Pagenumber=self.find_element(*Pagenumber_loc).text
        return Pagenumber
    
        
    def get_StatusChangedWarning(self):
        return self.find_element(*self.statuschangedWarning_loc).text
    
        
    def get_SpecialPage_index(self,Star_pageindex,End_pageindex,pagename):
        '''Last_button:Star_pageindex=6,End_pageindex=9
           Next_button:Star_pageindex=5,End_pageindex=8'''
        NormalPagenumber_path="//*[@id='container']/div/section/div/nav/ul/li[%d]/a"
        SpecialPagenumber_path=NormalPagenumber_path+"/span"
        for pageindex in range(Star_pageindex,End_pageindex+1):
            Pagenumber_loc=(By.XPATH,SpecialPagenumber_path % pageindex)
            if self.Element_displayed(*Pagenumber_loc)==True:
                if self.find_element(*Pagenumber_loc).text==pagename:
                    SpecialPage_pageindex=pageindex
                    #print "get_SpecialPage_index=",SpecialPage_pageindex
                    return SpecialPage_pageindex
  
    
    def get_anyCoach_attribute(self,coachindex,attrindex):
        anyCoach_attribute_loc=(By.XPATH,self.anyAttributeOfCoach_path %(coachindex,attrindex))
        flag=self.Element_displayed(*anyCoach_attribute_loc)
        if flag==True:
            anyCoach_attribute=self.find_element(*anyCoach_attribute_loc).text
        else:
            anyCoach_attribute="None"
        return anyCoach_attribute