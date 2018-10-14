'''
Created on Jan 16, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method import Gl


#This class is the basic Info for all coaching or Triadcoaching.
class BasicInfoforCoaching(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.backbutton_loc=(By.XPATH,"//*[@id='container']/div/nav/a/div/div")
        self.SN_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[1]/div[1]/div/div/input")
        
        self.status_loc=(By.XPATH,"//*[@id='coach_status']")
        self.createdDate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[1]/div[3]/div/div/input")
        self.employeename_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[2]/div[1]/div/div/input")
        self.coachname_loc=(By.XPATH,"//*[@id='coach_title']")
        self.completedDate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[2]/div[3]/div/div/input")
        self.canceledDate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[2]/div[3]/div/div/input")
        
        self.employeeHrid_loc=(By.XPATH,"//*[@id='employee_hrId']")
        self.acknowledgedDate_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[3]/div[3]/div/div/input")
        self.callrecordingnumber_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[1]/div[3]/div[2]/div/div/input")
        
        
        self.KPIboxTitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[1]/label")
        self.anyKPIname_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/thead/tr/th[%d]"
        self.anyKPIname_path2="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/thead/tr[2]/th[%d]"#the second KPIname path
        self.anyKPI_Goal_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[1]/td[%d]"
        self.anyKPI_Site_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[2]/td[%d]"
        self.anyKPI_AgentOrTL_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[3]/td[%d]"
        self.anyKPI_AgentOfTL_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]"
        self.anyCheckBoxStatus_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i"
        self.anyCheckBoxStatus_AgentOfTL_path="//*[@id='container']/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[5]/td[%d]/i"
        self.button_path="//*[@id='container']/div/section/div/form/div[3]/a[%d]"
        
        self.AlertMessage_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div/p[2]")
                              
        
    
    
    '''Buttons:
                1="Print","Acknowledge Coaching","Back"
                2="Save and Continue Later","Back"
                3="Complete Coaching"
                4="Cancel Coaching"
                5="Quit Without Save"'''   
    def get_AlertMessage(self):
        return self.find_element(*self.AlertMessage_loc).text
    
    
    def get_ButtonName(self,index):
        button_loc=(By.XPATH,self.button_path % index)   
        return self.find_element(*button_loc).text
    
    def Button_Displayed(self,index):
        button_loc=(By.XPATH,self.button_path % index)
        return self.Element_displayed(*button_loc)
    def Button_disabled(self,index):
        button_loc=(By.XPATH,self.button_path % index)
        return self.find_element(*button_loc).get_attribute("disabled")
    def Click_Button(self,index):
        button_loc=(By.XPATH,self.button_path % index)   
        self.find_element(*button_loc).click()
        self.wait_loadingmask_disappear()
        #time.sleep(5*Gl.waittime)
        '''
        if self.find_element(*button_loc) in ["Complete Coaching","Acknowledge Coaching"]:
            time.sleep(5*Gl.waittime)
        else:
            time.sleep(Gl.waittime)'''
            
    
        
    '''Basic coach info'''    
    def input_callrecordingnumber(self,text):
        self.Input_text(text,*self.callrecordingnumber_loc)
        time.sleep(Gl.waittime)
        
    def callrecordingnumber_disabled(self):
        flag=self.find_element(*self.callrecordingnumber_loc).get_attribute("disabled")
        return flag
        
        
    def get_callrecordingnumber(self):
        callrecordingnumber=self.find_element(*self.callrecordingnumber_loc).get_attribute("value")
        return callrecordingnumber
        
    def get_SN(self):
        SN=self.find_element(*self.SN_loc).get_attribute("value")
        return SN
    
    def get_status(self):
        status=self.find_element(*self.status_loc).get_attribute("value")
        return status
    
    def get_createdate(self):
        createdate=self.find_element(*self.createdDate_loc).get_attribute("value")
        return createdate
    
    def get_canceleddate(self):
        return self.find_element(*self.canceledDate_loc).get_attribute("value")
    
    def get_employeename(self):
        employeename=self.find_element(*self.employeename_loc).get_attribute("value")
        return employeename
    
    def get_coachname(self):
        coachname=self.find_element(*self.coachname_loc).get_attribute("value")
        return coachname
        
    def get_completeddate(self):
        completeddate=self.find_element(*self.completedDate_loc).get_attribute("value")
        return completeddate
        
    def get_employeeHrid(self):
        employeeHrid=self.find_element(*self.employeeHrid_loc).get_attribute("value")
        return employeeHrid
        
    def get_acknowledgedDate(self):
        acknowledagedDate=self.find_element(*self.acknowledgedDate_loc).get_attribute("value")
        return acknowledagedDate
    
    '''KPI info of coaching'''
    def get_KPIboxTitle(self):
        KPIboxTitle=self.find_element(*self.KPIboxTitle_loc).text
        return KPIboxTitle
    def get_anyKPIname(self,index):#The index of KPI starts from 2
        anyKPIname_loc=(By.XPATH,self.anyKPIname_path % index)
        anyKPIname=self.find_element(*anyKPIname_loc).text
        return anyKPIname 
    def get_anyKPIname_second(self,KPIindex):##KPIindex is started from 2#The Second KPIname
        anyKPIname_loc=(By.XPATH,self.anyKPIname_path2 %KPIindex) 
        anyKPIname=self.find_element(*anyKPIname_loc).text
        return anyKPIname
    
    def get_KPIname_list(self,KPInumber):
        KPIname_list=[] 
        for index in range(2,KPInumber+1):
            anyKPIname=self.get_anyKPIname(index)
            KPIname_list.append(anyKPIname)  
        return KPIname_list  
    
    def get_KPIname_list_Double(self):
        KPIname_list1=[]
        KPIname_list2=[]
        KPInumber1=self.get_KPInumber()
        KPInumber2=self.get_KPInumber_Second()
        for index in range(2,KPInumber1+1):
            anyKPIname=self.get_anyKPIname(index)
            KPIname_list1.append(anyKPIname)
        for index in range(2,KPInumber2+1):
            anyKPIname=self.get_anyKPIname_second(index)
            KPIname_list2.append(anyKPIname)
        KPIname_list=KPIname_list1+KPIname_list2
        return KPIname_list
    
    
    
      
    def get_anyKPIofGoal(self,index):#The index of KPI starts from 1
        anyKPIofGoal_loc=(By.XPATH,self.anyKPI_Goal_path % index)
        anyKPIofGoal=self.find_element(*anyKPIofGoal_loc).text
        return anyKPIofGoal
    def get_KPIofGoal_list(self,KPInumber):
        KPIofGoal_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofGoal=self.get_anyKPIofGoal(index)
            KPIofGoal_list.append(anyKPIofGoal)  
        return KPIofGoal_list   
    def get_anyKPIofSite(self,index):#The index of KPI starts from 1
        self.anyKPI_Site_path1=self.anyKPI_Site_path+"/span"
        anyKPIofSite_loc_loc1=(By.XPATH,self.anyKPI_Site_path1 % index)
        anyKPIofSite_loc_loc2=(By.XPATH,self.anyKPI_Site_path % index)
        Ppage=PerformancePage()
        anyKPI_valueAndStatus_list=Ppage.Merge_ValueandStatusOfKPI(anyKPIofSite_loc_loc1, anyKPIofSite_loc_loc2, index)
        return anyKPI_valueAndStatus_list
    def get_KPIofSite_list(self,KPInumber):
        KPIofSite_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofSite=self.get_anyKPIofSite(index)
            KPIofSite_list.append(anyKPIofSite)  
        return KPIofSite_list  
    def get_KPIofTeam_list(self,KPInumber):
        KPIofTeam_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofTeam=self.get_anyKPIofAgentOrTL(index)
            KPIofTeam_list.append(anyKPIofTeam)  
        return KPIofTeam_list  
    def get_KPIofAgentOfTL_list(self,KPInumber):
        KPIofAgentOfTL_list=[]
        for index in range(1,KPInumber+1):
            anyKPIofAgent_TL=self.get_anyKPIofAgent_TL(index)
            KPIofAgentOfTL_list.append(anyKPIofAgent_TL)  
        return KPIofAgentOfTL_list 
    
    ''' 
    def get_anyKPIofAgentOrTL(self,index):#The index of KPI starts from 1
        anyKPIofAgentOrTL_loc=(By.XPATH,self.anyKPI_AgentOrTL_path % index)
        anyKPIofAgentOrTL=self.find_element(*anyKPIofAgentOrTL_loc).text
        return anyKPIofAgentOrTL'''
    def get_anyKPIofAgentOrTL(self,index):#Login with OM/LC to get
        self.anyKPI_AgentOrTL_path1=self.anyKPI_AgentOrTL_path+"/span"
        anyKPIofAgentOrTL_loc1=(By.XPATH,self.anyKPI_AgentOrTL_path1 % index)
        anyKPIofAgentOrTL_loc2=(By.XPATH,self.anyKPI_AgentOrTL_path % index)
        Ppage=PerformancePage()
        anyKPI_valueAndStatus_list=Ppage.Merge_ValueandStatusOfKPI(anyKPIofAgentOrTL_loc1, anyKPIofAgentOrTL_loc2, index)
        return anyKPI_valueAndStatus_list
    
    def get_anyKPIofAgent_TL(self,index):#Login with TL to get
        self.anyKPI_AgentOfTL_path1=self.anyKPI_AgentOfTL_path+"/span"
        anyKPIofAgentOfTL_loc1=(By.XPATH,self.anyKPI_AgentOfTL_path1 % index)
        anyKPIofAgentOfTL_loc2=(By.XPATH,self.anyKPI_AgentOfTL_path % index)
        Ppage=PerformancePage()
        anyKPI_valueAndStatus_list=Ppage.Merge_ValueandStatusOfKPI(anyKPIofAgentOfTL_loc1, anyKPIofAgentOfTL_loc2, index)
        return anyKPI_valueAndStatus_list
    
    
    def get_AllKPIsofAgentOrTL_list(self,KPInumber):
        KPIofAgentOrTL_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofAgentOrTL=self.get_anyKPIofAgentOrTL(index)
            KPIofAgentOrTL_list.append(anyKPIofAgentOrTL)  
        return KPIofAgentOrTL_list   
    def get_anyCheckBoxStatus(self,index):#The index of KPI starts from 2
        anyCheckBoxStatus_loc=(By.XPATH,self.anyCheckBoxStatus_path % index)
        anyCheckBoxStatus=self.find_element(*anyCheckBoxStatus_loc).get_attribute("class")
        return anyCheckBoxStatus
    def get_anyCheckBoxStatus_Agent(self,index):#The index of KPI starts from 2(Login with TL)
        anyCheckBoxStatus_loc=(By.XPATH,self.anyCheckBoxStatus_AgentOfTL_path % index)
        anyCheckBoxStatus=self.find_element(*anyCheckBoxStatus_loc).get_attribute("class")
        return anyCheckBoxStatus
    def click_anyKPIstatusofCheckBox(self,index):#The index of KPI starts from 2
        anyCheckBoxStatus_loc=(By.XPATH,self.anyCheckBoxStatus_path % index)
        self.find_element(*anyCheckBoxStatus_loc).click()
    def click_anyKPIstatusofCheckBox_Agent(self,index):#The index of KPI starts from 2(Login with TL)
        anyCheckBoxStatus_loc=(By.XPATH,self.anyCheckBoxStatus_AgentOfTL_path % index)
        self.find_element(*anyCheckBoxStatus_loc).click()
    def get_CheckBoxStatus_list(self,KPInumber):#Login with OM
        CheckBoxStatus_list=[] 
        for index in range(2,KPInumber+1):
            anyCheckBoxStatus=self.get_anyCheckBoxStatus(index)
            CheckBoxStatus_list.append(anyCheckBoxStatus)  
        return CheckBoxStatus_list 
    def get_CheckBoxStatus_Agent_list(self,KPInumber):#Login with TL
        CheckBoxStatus_list=[] 
        for index in range(2,KPInumber+1):
            anyCheckBoxStatus=self.get_anyCheckBoxStatus_Agent(index)
            CheckBoxStatus_list.append(anyCheckBoxStatus)  
        return CheckBoxStatus_list     
    
    def get_KPInumber(self):#For the first KPIname
        index=0
        flag=True
        while flag:
            KPInumber=index
            index=index+1 
            anyKPIofGoal_loc=(By.XPATH,self.anyKPIname_path % index)
            flag=self.Element_displayed(*anyKPIofGoal_loc) 
        return KPInumber
    def get_KPInumber_Second(self):#For two KPIname(BLUE,SPANISH,ISM)
        index=0
        flag=True
        while flag:
            KPInumber=index
            index=index+1 
            anyKPIname_loc=(By.XPATH,self.anyKPIname_path2 % index)
            flag=self.Element_displayed(*anyKPIname_loc) 
        return KPInumber
    def get_KPInumber_All(self):#For two KPIname(BLUE,SPANISH,ISM)
        index=0
        flag=True
        while flag:
            KPInumber=index
            index=index+1 
            anyKPI_loc=(By.XPATH,self.anyKPI_Goal_path% index)
                                   
            flag=self.Element_displayed(*anyKPI_loc) 
        return KPInumber



    
        
        
        
        
        