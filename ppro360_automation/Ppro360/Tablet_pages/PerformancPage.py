'''
Created on Jan 3, 2017

@author: symbio
'''
import sys 
#from _multiprocessing import flags
sys.path.append("\test_cases") 
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
#Three tab: Yesterday, WTD, MTD
#FOR OM
class PerformancePage(BasePage.Action):
    '''
    This performance page has 3 tabs(Yesterday, Week-To-Date, Month-To-Date) or 1 tab (Month-To-Date).
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #1-lasttwomonth,2-lastmonth,3-ytd,4-wtd,5-mtd
        #1-lasttwomonth,2-lastmonth,3-mtd
        self.timetab_path="//*[@id='container']/div/section/div/div[1]/ul/li[%d]"
        
        self.mtd_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[5]")
        self.wtd_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[4]")
        self.ytd_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[3]")
        self.lastmonth_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[2]")
        self.lasttwomonth_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[1]")
        #The first kpi for the first TL
 
        self.FirstTLkpi_loc=(By.XPATH,"//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr/td[2]")
        self.FirstTLkpi_unselect_loc=(By.XPATH,"//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr/td[2]/i")
        self.addTriadcoachbutton_loc=(By.LINK_TEXT,"Add Triad Coaching Form")
        #The first kpi for the first agent of the first TL (OM LOGIN)
        self.FisrtTL_loc=(By.CSS_SELECTOR,"i.icon-arrow-up")
        self.FisrtagentofOMkpi_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]")
        self.FisrtagentofOMkpi_unselect_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/i")
        
        self.addcoachbutton_loc=(By.LINK_TEXT,"Add Coaching Form")
        self.addcoachOrtriadcoach_messeage_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div/p[1]")
        #The first kpi for the first agent(TL LOGIN)
        self.FirstagentofTLkpi_loc=(By.XPATH,"//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr/td[2]")
        self.FirstagentofTLkpi_unselect_loc=(By.XPATH,"//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr/td[2]/i")
        
        self.anyKPIname_path="//*[@id='container']/div/section/div/div[2]/table/thead/tr/th[%d]"#The first kPIname path
        self.anyKPIname_path2="//*[@id='container']/div/section/div/div[2]/table/thead/tr[2]/th[%d]"#The second first KPIname path
        self.anyKPIname_second_path="//*[@id='container']/div/section/div/div[2]/table/thead/tr[2]/th[%d]"
        self.anyKPIofAgentForOM_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[%d]/td[%d]"#All agent's kipi of the first TL of OMd1=angentindex,d2=kipindex
        self.anyKPIofAgentForTL_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]"#the first agent of TL:d1=angentindex,d2=kipindex
        self.anyAgentName_TL_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[1]"
        
        
        
        #Back button
        self.Backbutton_loc=(By.XPATH,"//*[@id='container']/div/nav/a/div/div")
    
    def click_mtd(self):
        self.find_element(*self.mtd_loc).click()
        time.sleep(Gl.waittime)
        
    def click_wtd(self):
        self.find_element(*self.wtd_loc).click()
        time.sleep(Gl.waittime)
        
    def click_ytd(self):
        self.find_element(*self.ytd_loc).click()
        time.sleep(Gl.waittime)
    
    def click_timetab_performance(self,index):
        '''1-lasttwomonth,2-lastmonth,3-ytd,4-wtd,5-mtd;
           1-lasttwomonth,2-lastmonth,3-mtd'''
        print index
        timetab_loc=(By.XPATH,self.timetab_path % index)
        self.find_element(*timetab_loc).click()
        self.wait_loadingmask_disappear()
    def get_timetab_text_performance(self,index):
        '''1-lasttwomonth,2-lastmonth,3-ytd,4-wtd,5-mtd;
           1-lasttwomonth,2-lastmonth,3-mtd'''
        timetab_text_path=self.timetab_path+"/span"
        timetab_text_loc=(By.XPATH,timetab_text_path % index)
        print timetab_text_loc
        timetab_text=self.find_element(*timetab_text_loc).text
        return timetab_text
        
        
    
    
       
##################Below is to get any cell value or click  any button#######################################
    def get_KPInumber(self):#For the first KPIname
        index=0
        flag=True
        while flag:
            KPInumber=index
            index=index+1 
            anyKPIname_loc=(By.XPATH,self.anyKPIname_path % index)
            flag=self.Element_displayed(*anyKPIname_loc) 
        return KPInumber
    def get_KPInumber_Second(self):#For two KPIname(BLUE,SPANISH,ISM)
        index=0
        flag=True
        while flag:
            KPInumber=index
            index=index+1 
            anyKPIname_loc=(By.XPATH,self.anyKPIname_second_path % index)
            flag=self.Element_displayed(*anyKPIname_loc) 
        return KPInumber
    
    def get_KPInumber_All(self):#For two KPIname(BLUE,SPANISH,ISM)
        index=0
        flag=True
        while flag:
            KPInumber=index
            index=index+1 
            anyKPI_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[1]/td[%d]")% index)
            flag=self.Element_displayed(*anyKPI_loc) 
        return KPInumber
    def get_anyKPIname(self,KPIindex):##KPIindex is started from 2#The first KPIname
        anyKPIname_loc=(By.XPATH,self.anyKPIname_path %KPIindex) 
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
    def get_KPIname_list_Second(self,KPInumber):
        KPIname_list=[]
        for index in range(1,KPInumber+1):
            anyKPIname=self.get_anyKPIname_second(index)
            KPIname_list.append(anyKPIname)
        return KPIname_list
    def get_anyKPIindex(self,KPInumber,KPIName):
        for index in range(2,KPInumber+1):
            anyKPIname_loc=(By.XPATH,self.anyKPIname_path % index)
            if self.find_element(*anyKPIname_loc)==KPIName:
                anyKPIindex=index
            return  anyKPIindex 
    def get_anyAgentindex(self,AgentName):
        lineindex=1
        flag=True
        while flag==True:
            AgentName_loc=(By.XPATH,self.anyAgentName_TL_path % lineindex)
            if self.find_element(*AgentName_loc).text==AgentName:
                Agent_lineindex=lineindex
                break
            else:
                lineindex=lineindex+1
                flag=self.Element_displayed(*AgentName_loc)
        return Agent_lineindex
    
    
    def get_anyGoalValue(self,Goalindex): ##Goalindex is started from 2
        anyGoalValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[1]/td[%d]/span") %Goalindex)
        anyGoalValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[1]/td[%d]") %Goalindex)
        flag=self.isElementExist(*anyGoalValue_loc1)
        #print flag
        if flag==True:
            anyGoalValue=self.find_element(*anyGoalValue_loc1).text
        else:
            anyGoalValue=self.find_element(*anyGoalValue_loc2).text
        return anyGoalValue
    
    def get_AllKPIsofGoal_list(self,KPInumber):
        KPIofGoal_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofGoal=self.get_anyGoalValue(index)
            KPIofGoal_list.append(anyKPIofGoal)  
        return KPIofGoal_list   
    
    def get_anyKPIValueOfTotal(self,lineindex,Kpiindex):##For SITE:Siteindex is started from 2;#For Achievement for other role
        ''' Site:lineindex=2'''
        anyKPIValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[%d]/span") % (lineindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[%d]") % (lineindex, Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST
    def get_anyKPIValueOfTotal_doubleKPI(self,lineindex,Kpiindex):##For SITE:Siteindex is started from 2;#For Achievement for other role
        ''' Site:lineindex=2'''
        anyKPIValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[%d]/span/span") % (lineindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[%d]") % (lineindex, Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST
    
    def get_AllKPIsofSite_list(self,KPInumber):
        KPIofSite_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofSite=self.get_anyKPIValueOfTotal(2, index)
            KPIofSite_list.append(anyKPIofSite)  
        return KPIofSite_list  
    def get_AllKPIsofTeam_list(self,KPInumber):
        SecondLine_Tittle=self.get_anyKPIValueOfTotal(2, 1)
        print "SecondLine_Tittle:",SecondLine_Tittle
        KPIofTeam_list=[]
        if SecondLine_Tittle[0]=="Site":
            Team_lineindex=3
        elif SecondLine_Tittle[0]=="Team":
            Team_lineindex=2
        for index in range(1,KPInumber+1):
            anyKPIofSite=self.get_anyKPIValueOfTotal(Team_lineindex, index)
            KPIofTeam_list.append(anyKPIofSite)
        return KPIofTeam_list    
    def get_AllKPIsofAgentForOM_list(self,KPInumber):
        KPIofAgentForOM_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofAgentForOM=self.get_anyKPIofAgent_OM(1, 1,index)
            KPIofAgentForOM_list.append(anyKPIofAgentForOM)  
        return KPIofAgentForOM_list   
    def get_AllKPIsofTL_list(self,KPInumber):
        KPIofTL_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofTL=self.get_anyKPIofTL(1,index)
            KPIofTL_list.append(anyKPIofTL)  
        return KPIofTL_list  
    def get_AllKPIsofAgent_TL_list(self,KPInumber,Agentindex):
        KPIofAgent_TL_list=[] 
        for index in range(1,KPInumber+1):
            anyKPIofAgent=self.get_anyKPIofAgent_TL(Agentindex,index)
            KPIofAgent_TL_list.append(anyKPIofAgent)  
        return KPIofAgent_TL_list 

    def get_anyKPIofTL(self,TLindex,Kpiindex):
        anyKPIValue_loc1=(By.XPATH,("//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]/span") %(TLindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]") %(TLindex,Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST
    def get_anyKPIofTL_doubleKPI(self,TLindex,Kpiindex):
        anyKPIValue_loc1=(By.XPATH,("//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]/span/span") %(TLindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//div[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]") %(TLindex,Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST
    def get_anyKPIofAgent_OM(self,TLindex,Agentindex,Kpiindex):#FOR TL&AGENT:
        anyKPIValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[%d]/span") %(TLindex+1,Agentindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[%d]") %(TLindex+1,Agentindex,Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST 
    def get_anyKPIofAgent_OM_doubleKPI(self,TLindex,Agentindex,Kpiindex):#FOR TL&AGENT:
        anyKPIValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[%d]/span/span") %(TLindex+1,Agentindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[%d]") %(TLindex+1,Agentindex,Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST 
    def get_anyKPIofAgent_TL(self,Agentindex,Kpiindex):
        anyKPIValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]/span") %(Agentindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]") %(Agentindex,Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST 
    def get_anyKPIofAgent_TL_doubleKPI(self,Agentindex,Kpiindex):
        anyKPIValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]/span/span") %(Agentindex,Kpiindex))
        anyKPIValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]") %(Agentindex,Kpiindex))
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST 
    
    def get_anyKPIofAgent_Agent(self,Kpiindex):
        anyKPIValue_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr/td[%d]/span") % Kpiindex)
        anyKPIValue_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr/td[%d]") % Kpiindex)
        anyKPI_LIST=self.Merge_ValueandStatusOfKPI(anyKPIValue_loc1, anyKPIValue_loc2, Kpiindex)
        return anyKPI_LIST
    
    
    
    def Merge_ValueandStatusOfKPI(self,anyKPIValue_loc1,anyKPIValue_loc2,Kpiindex):
        if Kpiindex==1:
            anyKPIValue=self.find_element(*anyKPIValue_loc2).text
            anyKPI_LIST=[anyKPIValue,'']
        elif self.find_element(*anyKPIValue_loc2).text != 'N/A':
            anyKPIValue=self.find_element(*anyKPIValue_loc2).text
            if "\nTrendAdd Coaching Form" in anyKPIValue:
                anyKPIValue=anyKPIValue.replace("\nTrendAdd Coaching Form","")
            anyKPIStatus=self.find_element(*anyKPIValue_loc1).get_attribute('class')
            anyKPI_LIST=[anyKPIValue,anyKPIStatus]
        else:
            anyKPIValue=self.find_element(*anyKPIValue_loc2).text
            anyKPI_LIST=[anyKPIValue,'']  
        return anyKPI_LIST
    
    def TL_line_exist(self,lineindex):
        anyTL_name_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[1]") % lineindex)
        flag=self.Element_displayed(*anyTL_name_loc)
        return flag 
    def Agent_line_exist_OM(self,TLindex,Agentindex):
        anyAgent_name_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[1]")%(TLindex+1,Agentindex))
        flag=self.Element_displayed(*anyAgent_name_loc)
        return flag
    
    def Agent_line_exist_TL(self,Agentindex):
        anyAgent_name_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[1]")%Agentindex)
        flag=self.Element_displayed(*anyAgent_name_loc)
        return flag
    
    
   
   
    
    
    def unfold_anyTL(self,TLindex):
        eachTLline_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[1]/i") %TLindex)
        self.find_element(*eachTLline_loc).click()
        time.sleep(Gl.waittime)
    def get_anyTL_hrid(self,TLindex):
        eachTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*eachTL_loc).get_attribute("data-id")
               
    def select_TLkpi(self):
        self.find_element(*self.FirstTLkpi_loc).click()  
    def unselect_TLkpi(self):
        self.find_element(*self.FirstTLkpi_unselect_loc).click()
        
    def select_AnyKpiOfAgent_OM(self,MaxKPIindex):#the KPIindex is from 2 to start.MaxKPIindex=KPInumber+1
        self.unfold_anyTL(1)
        #self.find_element(*self.FisrtTL_loc).click()
        time.sleep(Gl.waittime)
        if MaxKPIindex>=2:
            FisrtagentofOM_Lastkpi_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[%d]") %MaxKPIindex)
            FisrtagentofOM_Lastkpi_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[%d]/span") %MaxKPIindex)
            if self.Element_displayed(*FisrtagentofOM_Lastkpi_loc2)==True:
                self.find_element(*FisrtagentofOM_Lastkpi_loc2).click()
            else:
                self.find_element(*FisrtagentofOM_Lastkpi_loc1).click()
            for KPIindex in range(2,MaxKPIindex):              
                FisrtagentofOM_anykpi_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[%d]") %KPIindex)
                FisrtagentofOM_anykpi_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[%d]/span") %KPIindex)
                
                if self.Element_displayed(*FisrtagentofOM_anykpi_loc2)==True:
                    self.find_element(*FisrtagentofOM_anykpi_loc2).click()
                else:
                    self.find_element(*FisrtagentofOM_anykpi_loc1).click()
        else:
            FisrtagentofOM_anykpi_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[%d]") %KPIindex)
            FisrtagentofOM_anykpi_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[%d]/span") %KPIindex)
            
            if self.Element_displayed(*FisrtagentofOM_anykpi_loc2)==True:
                self.find_element(*FisrtagentofOM_anykpi_loc2).click()
            else:
                self.find_element(*FisrtagentofOM_anykpi_loc1).click()
        self.wait_loadingmask_disappear()
        
    def select_AnyKpiOfAgent_TL(self,MaxKPIindex,KPIindex):#the KPIindex is from 2 to start.MaxKPIindex=KPInumber+1
        #self.unfold_anyTL(1)
        #self.find_element(*self.FisrtTL_loc).click()
        time.sleep(Gl.waittime)
        if MaxKPIindex>=2 and MaxKPIindex==KPIindex:
            
            FisrtagentofTL_Lastkpi_loc1=(By.XPATH,self.anyKPIofAgentForTL_path %(1,MaxKPIindex))
            FisrtagentofTL_Lastkpi_loc2=(By.XPATH,(self.anyKPIofAgentForTL_path+"/span") %(1,MaxKPIindex))
            if self.Element_displayed(*FisrtagentofTL_Lastkpi_loc2)==True:
                self.find_element(*FisrtagentofTL_Lastkpi_loc2).click()
            else:
                self.find_element(*FisrtagentofTL_Lastkpi_loc1).click()
            for KPIindex in range(2,MaxKPIindex):              
                FisrtagentofTL_anykpi_loc1=(By.XPATH,self.anyKPIofAgentForTL_path %(1,KPIindex))
                FisrtagentofTL_anykpi_loc2=(By.XPATH,(self.anyKPIofAgentForTL_path+"/span") %(1,KPIindex))
                
                if self.Element_displayed(*FisrtagentofTL_anykpi_loc2)==True:
                    self.find_element(*FisrtagentofTL_anykpi_loc2).click()
                else:
                    self.find_element(*FisrtagentofTL_anykpi_loc1).click()
        else:
            FisrtagentofTL_anykpi_loc1=(By.XPATH,self.anyKPIofAgentForTL_path %(1,KPIindex))
            FisrtagentofTL_anykpi_loc2=(By.XPATH,(self.anyKPIofAgentForTL_path+"/span") %(1,KPIindex))
            
            if self.Element_displayed(*FisrtagentofTL_anykpi_loc2)==True:
                self.find_element(*FisrtagentofTL_anykpi_loc2).click()
            else:
                self.find_element(*FisrtagentofTL_anykpi_loc1).click()
        self.wait_loadingmask_disappear()
    def select_AnyKpiOfTL(self,MaxKPIindex):#the KPIindex is from 2 to start.MaxKPIindex=KPInumber+1
        for KPIindex in range(2,MaxKPIindex+1):
            FisrtTL_anykpi_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[1]/td[%d]") %KPIindex)
            FisrtTL_anykpi_loc2=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[1]/td[%d]/span") %KPIindex)
            if self.Element_displayed(*FisrtTL_anykpi_loc2)==True:
                self.find_element(*FisrtTL_anykpi_loc2).click()
                 
            else:
                self.find_element(*FisrtTL_anykpi_loc1).click()
        time.sleep(Gl.waittime)   
    
    def select_Agentkpi(self):
        self.find_element(*self.FisrtTL_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.FisrtagentofOMkpi_loc).click()
    def unselect_Agentkpi(self):   
        self.find_element(*self.FisrtagentofOMkpi_unselect_loc).click()
    def select_AgentofTLkpi(self):
        self.find_element(*self.FirstagentofTLkpi_loc).click()
    
    def unselect_AgentofTLkpi(self):
        self.find_element(*self.FirstagentofTLkpi_unselect_loc).click()
        
        
    def click_addTriadcoachbutton(self):
        self.find_element(*self.addTriadcoachbutton_loc).click()
    
        
    def click_addcoachbutton(self):
        self.find_element(*self.addcoachbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def click_backbutton(self):
        self.find_element(*self.Backbutton_loc).click()
        self.wait_loadingmask_disappear()
        #time.sleep(Gl.waittime)
    
    def TriadcoachNotexist(self):
        Flag=False
        if self.isElementExist(*self.addTriadcoachbutton_loc) == False:
            Flag=True
            return Flag
        else:
            return Flag
            
    
    def get_FirstAgentofAnyTL_hrid(self,TLindex):
        Agentindex=TLindex+1
        #eachFisrtAgent_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tr[1]") %Agentindex)
        eachFisrtAgent_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[1]") %Agentindex)
        return self.find_element(*eachFisrtAgent_loc).get_attribute("data-id")
    def FisrtAgent_Notexist(self,TLindex):
        Agentindex=TLindex+1
        eachFisrtAgent_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tr[1]") %Agentindex)
        Flag=False
        if self.isElementExist(eachFisrtAgent_loc)==True:
            Flag=True
            return Flag
        else:
            return Flag
        
    def get_messageOfaddCoachOrtriad(self):
        return self.find_element(*self.addcoachOrtriadcoach_messeage_loc).text   
        