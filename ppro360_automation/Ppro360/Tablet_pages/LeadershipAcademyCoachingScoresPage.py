'''
Created on 20170707

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from selenium import webdriver
import time
from public_method import Gl

class LeadershipAcademyCoachingScoresPage(BasePage.Action):
    
    
    def __init__(self):
        
        self.datevalue_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/input"
        self.statusvalue_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[2]/div[2]/div/span")
        self.selectstatus_path="//*[@id='container']/div/section/div/div[1]/div[2]/div[2]/div/ul/li[%d]/a"
        self.back_loc=(By.XPATH,"//*[@id='container']/div/nav/a/div/div")
        self.timebutton_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/span/span"
        self.timetopclick_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[2]"
        self.yeartopvalue_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]"
        self.smallleftbutton_path="//*[@id='container']/div/section/div/div[%d]/div[%d]/div[%d]/div[1]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[1]"
        self.dayactivevalue_loc=(By.XPATH,"//*[@class='day active today']")
        self.bigleftbutton_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[1]/span"
        self.dayvalue_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.monthclick_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.yearclick_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div[%d]/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.filterbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[3]/button")
        self.warnmessage_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div/p[2]")
        self.disabledwarnmessagr_loc=(By.XPATH,"//*[@id='container']/div/div[2]")
        
        
        
        self.teamvalue_path="//*[@id='container']/div/section/div/div[2]/table/tbody/tr[%d]/td[%d]/span " #AGENT LOGIN
        self.agentvalue_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr/td[%d]/span"
        self.agentaccount_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[1]"
        self.agentname_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[1]"
        self.tlvalue_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]"#L3 LOGIN /span
        self.tlclick_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[1]"
        self.agentdate_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[%d]"#L3 LOGIN /span
        #Add by Sabrina Guo-Start
        self.TLnameWithL3Login_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[1]"#index start from 1
        self.AgentNameWithL3Login_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]/td[1]"#first %d=TLindex*2,first %d start from 1
        self.TLHridWithL3Login_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]"
        self.AgentHridWithL3Login_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td/table/tbody/tr[%d]"
        #Add by Sabrina Guo-End
    
    def get_TLHridWithL3Login(self,lineindex):#Add by Sabrina Guo
        TLHrid_loc=(By.XPATH,self.TLHridWithL3Login_path % lineindex)
        TLHrid=self.find_element(*TLHrid_loc).get_attribute("data-id")
        return TLHrid
    def get_AgentHridWithL3Login(self,lineindex1,lineindex2):#Add by Sabrina Guo
        AgentHrid_loc=(By.XPATH,self.AgentHridWithL3Login_path % (lineindex1,lineindex2))
        AgentHrid=self.find_element(*AgentHrid_loc).get_attribute("data-id")
        return AgentHrid
    
    
    def get_datevalu(self,int1,int2,int3):
        self.datevalue_loc=(By.XPATH,self.datevalue_path %(int1,int2,int3))
        return self.find_element(*self.datevalue_loc).get_attribute("value")
    
    
    
    def click_filterbutton(self):
        self.find_element(*self.filterbutton_loc).click()
    
    def click_status(self):
        self.find_element(*self.statusvalue_loc).click()
        
    def get_statusvalue(self):
        return self.find_element(*self.statusvalue_loc).text
    
    def get_StatusDropDownList(self):#Modify by Sabrina Guo
        self.click_status()
        StatusDropDownList=[]
        index=1
        while self.Element_displayed(*(By.XPATH,self.selectstatus_path%index)):
            status_dropdown_loc=(By.XPATH,self.selectstatus_path%index)
            status=self.find_element(*status_dropdown_loc).text
            StatusDropDownList.append(status)
            index=index+1
        return StatusDropDownList    
    def click_back(self):
        self.find_element(*self.back_loc).click()
    
    def click_selectstatus(self,line):
        self.selectstatus_loc=(By.XPATH,self.selectstatus_path %line)
        self.find_element(*self.selectstatus_loc).click()
        
        
    def click_timebutton(self,int1,int2,int3):
        self.timebutton_loc=(By.XPATH,self.timebutton_path %(int1,int2,int3))
        self.find_element(*self.timebutton_loc).click()
        
    def click_timetopclick(self,int1,int2,int3):
        self.timetopclick_loc=(By.XPATH,self.timetopclick_path %(int1,int2,int3))
        self.find_element(*self.timetopclick_loc).click()
        
    def get_yeartopvalue(self,int1,int2,int3):
        self.yeartopvalue_loc=(By.XPATH,self.yeartopvalue_path %(int1,int2,int3))
        return self.find_element(*self.yeartopvalue_loc).text
    
    def click_yeartopvalue(self,int1,int2,int3):
        self.yeartopvalue_loc=(By.XPATH,self.yeartopvalue_path %(int1,int2,int3))
        self.find_element(*self.yeartopvalue_loc).click()
     
    def click_smallleftbutton(self,int1,int2,int3):
        self.smallleftbutton_loc=(By.XPATH,self.smallleftbutton_path %(int1,int2,int3))
        self.find_element(*self.smallleftbutton_loc).click() 
    
    def click_dayactivevalue(self):
        self.find_element(*self.dayactivevalue_loc).click()
    
    def click_dayvalue(self,int1,int2,int3,int4,int5):
        self.dayvalue_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4,int5))
        self.find_element(*self.dayvalue_loc).click()
        
    def disabled_dayclick(self,int1,int2,int3,int4,int5):
        self.dayvalue_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4,int5))
        return self.find_element(*self.dayvalue_loc).get_attribute("class")
        
    def get_dayvalue(self,int1,int2,int3,int4,int5):
        self.dayvalue_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4,int5))
        return self.find_element(*self.dayvalue_loc).text
    
    def get_nowday(self,int1,int2,int3,int4,int5):
        self.nowday_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4,int5))
        return self.find_element(*self.nowday_loc).get_attribute("class")   
        
    def click_bigleftbutton(self,int1,int2,int3):
        self.bigleftbutton_loc=(By.XPATH,self.bigleftbutton_path %(int1,int2,int3))  
        self.find_element(*self.bigleftbutton_loc).click()
        
    def click_monthclick(self,int1,int2,int3,int4):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %(int1,int2,int3,int4))
        self.find_element(*self.monthclick_loc).click()
        
    def get_monthvalue(self,int1,int2,int3,int4):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %(int1,int2,int3,int4))
        return self.find_element(*self.monthclick_loc).text
        
    def click_yearclick(self,int1,int2,int3,int4):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %(int1,int2,int3,int4))
        self.find_element(*self.yearclick_loc).click()
        
    def get_yearvalue(self,int1,int2,int3,int4):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %(int1,int2,int3,int4))
        return self.find_element(*self.yearclick_loc).text
        
    def get_warnmessage(self):
        return self.find_element(*self.warnmessage_loc).text
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def get_Leadershippage_Teamandsite_value(self,siteindex,teamindex):
        self.teamvalue_loc=(By.XPATH,self.teamvalue_path %(siteindex,teamindex))
        flag=self.find_element(*self.teamvalue_loc).text
        return flag
        
        
    def get_Leadershippage_agent_value(self,agentindex):
        self.agentvalue_loc=(By.XPATH,self.agentvalue_path %agentindex)
        flag=self.find_element(*self.agentvalue_loc).text
        return flag
    
    def get_TL_Leadershippage_agentaccount(self,lineindex):
        self.agentaccount_loc=(By.XPATH,self.agentaccount_path %lineindex)
        flag=self.find_element(*self.agentaccount_loc).text
        return flag
    
    def get_TL_Leadershippage_AllAgentNames(self):#Add by Sabrina Guo: Get all Agents' name of TL with TL login
        AllAgentName_list=[]
        lineindex=1
        while self.Element_displayed(*(By.XPATH,self.agentaccount_path %lineindex)):
            agentaccount_loc=(By.XPATH,self.agentaccount_path %lineindex)
            agentname=self.find_element(*agentaccount_loc).text
            AllAgentName_list.append(agentname)
            lineindex=lineindex+1
        return AllAgentName_list
      
       
    
    def get_AllTLs_Leadershippage_ByL3(self):#Add By Sabrina Guo
        All=[]
        AllTL_list=[]
        lineindex=1
        while self.Element_displayed(*(By.XPATH,self.TLnameWithL3Login_path %lineindex)):
            TLaccount_loc=(By.XPATH,self.TLnameWithL3Login_path %lineindex)
            TLname=self.find_element(*TLaccount_loc).text
            AllTL_list.append(TLname)
            lineindex=lineindex+1
        All.append(AllTL_list)
        All.append(lineindex-1)
        return All
    def get_AllAgents_Leadershippage_ByL3(self,TLnumber,KPInumber):#Add By Sabrina Guo
        All_list=[]
        AllAgentNames_list=[]
        AllTheFirstThreeAgentValue={}
        for i in range(1,TLnumber+1):
            self.click_filterbutton()
            self.click_TLName_ByL3(i)
            lineindex1=i+1
            lineindex2=1
            #TheFirstThreeAgent_valuelist=[]
            while self.Element_displayed(*(By.XPATH,self.AgentNameWithL3Login_path %(lineindex1,lineindex2))):
                agentaccount_loc=(By.XPATH,self.AgentNameWithL3Login_path %(lineindex1,lineindex2))
                Agentname=self.find_element(*agentaccount_loc).text
                AgentHrid=self.get_AgentHridWithL3Login(lineindex1,lineindex2)
                AllAgentNames_list.append(Agentname)
                
                agentkpi_list=[]
                #EachAgent_value={}
                for kpiindex in range(2,KPInumber+2):
                    agentvalue_loc=(By.XPATH,self.agentdate_path%(lineindex1,lineindex2,kpiindex))
                    agentkpi_list.append(self.find_element(*agentvalue_loc).text)
                #EachAgent_value[AgentHrid]=agentkpi_list
                if lineindex2<=3:
                    AllTheFirstThreeAgentValue[AgentHrid]=agentkpi_list
                    #TheFirstThreeAgent_valuelist.append(EachAgent_value)     
                lineindex2=lineindex2+1
            #AllTheFirstThreeAgentValue_list.append(TheFirstThreeAgent_valuelist) 
        All_list.append(AllAgentNames_list) 
        All_list.append(AllTheFirstThreeAgentValue)
        return All_list
    
    def click_TLName_ByL3(self,lineindex):#Add By Sabrina Guo
        TLaname_loc=(By.XPATH,self.TLnameWithL3Login_path %lineindex)
        self.find_element(*TLaname_loc).click() 
        time.sleep(Gl.waittime)

    def get_Leadershippage_agentname(self,ab,lineindex):
        self.agentname_loc=(By.XPATH,self.agentname_path %(ab,lineindex))
        flag=self.find_element(*self.agentname_loc).text
        return flag
    #def get_Leadershippage_tl_value(self,siteindex,teamindex):
    def get_Leadershippage_tl_value(self,teamindex,kpiindex):#Get tl's kpi value in page with L3 LOGIN
        self.tlvalue_loc=(By.XPATH,self.tlvalue_path %(teamindex,kpiindex))
        flag=self.find_element(*self.tlvalue_loc).text
        return flag
    
    def get_AllTLvalue_ByL3(self,TLnumber,KPInumber):#Add by Sabrina Guo
        AllTLValue_list={}
        for i in range(1,TLnumber+1):
            value_list=[]
            kpiindex=2
            TLHrid=self.get_TLHridWithL3Login(i)
            for kpiindex in range(2,KPInumber+2):
            #while self.Element_displayed(*(By.XPATH,self.tlvalue_path %(i,kpiindex))):
                tlvalue_loc=(By.XPATH,self.tlvalue_path %(i,kpiindex))
                tlvalue=self.find_element(*tlvalue_loc).text
                value_list.append(tlvalue)
                #kpiindex=kpiindex+1
            AllTLValue_list[TLHrid]=value_list
        return AllTLValue_list 
    def get_Leadershippage_tl(self,index):
        self.tlclick_loc=(By.XPATH,self.tlclick_path %index)
        flag=self.find_element(*self.tlclick_loc).text
        return flag
    
    def click_Leadershippage_tl(self,index):
        self.tlclick_loc=(By.XPATH,self.tlclick_path %index)
        self.find_element(*self.tlclick_loc).click()
        
    def get_agentdate(self,index1,index2,index3):
        self.agentdate_loc=(By.XPATH,self.agentdate_path %(index1,index2,index3))
        flag=self.find_element(*self.agentdate_loc).text
        return flag
    

    

    
    
    

        
    
    