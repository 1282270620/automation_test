'''
Created on 2018/4/3

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from selenium import webdriver
import time 
from public_method import Gl

class LeaderAcademyCoachingLeaderScorespage(BasePage.Action):
    
    def __init__(self):
        self.datevalue_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/input"
        self.timebutton_path='//*[@id="container"]/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/span/span'
        self.back_loc=(By.XPATH,"//*[@id='container']/div/nav/a/div/div")
        self.timetopclick_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[2]"
        self.yeartopvalue_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]"
        self.smallleftbutton_path="//*[@id='container']/div/section/div/div/div[%d]/div[%d]/div[1]/div/div/div[2]/ul/li/div/div/table/thead/tr/th[1]"
        self.dayactivevalue_loc=(By.XPATH,"//*[@class='day active today']")
        self.bigleftbutton_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[1]/span"
        self.dayvalue_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.monthclick_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.yearclick_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.warnmessage_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div/p[2]")
        self.filterbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/div[3]/button")
        self.LeaderScorespage_path='//*[@id="container"]/div/section/section/a[%d]/div/div'
        self.tlname_path='//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[%d]/td[1]'
        self.pagedate_path='//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]/span'
        self.TLkpivalue_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]/td[%d]"
        self.TLHrid_path="//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]"
        #Add By Sabrina
        self.StartDatePicker_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[1]/div/div/div[2]/span/span"#d:1 for create,2 for Acknowledge
        self.EndDatePicker_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[2]/div/div/div[2]/span/span"#d:1 for create,2 for Acknowledge
        self.StartDateInput_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[1]/div/div/div[2]/input"#d:1 for create,2 for Acknowledge
        self.EndDateInput_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[2]/div/div/div[2]/input"#d:1 for create,2 for Acknowledge
        self.DayActiveToday=(By.CLASS_NAME,"day active today")
        self.CreatedDateInDatePicker_path="//*[@id='container']/div/section/div/div[1]/div[1]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]" #StartEndeindex,lineindex,dateindex
        self.AcknowledgeDateInDatePicker_path="//*[@id='container']/div/section/div/div[1]/div[2]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]" #StartEndeindex,lineindex,dateindex
        self.LeftArrow_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[1]/span"#DateTypeindex,StartEndeindex
        self.RightArrow_path="//*[@id='container']/div/section/div/div[1]/div[%d]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[3]/span"#DateTypeindex,StartEndeindex
    
    def Click_LeftArrowInDatePicker(self,DateTypeindex,StartEndeindex):
        '''DateTypeindex:1 for Created Date,2 for Acknowledge Date
           StartEndindex: 1 for Start,2 for End'''
        LeftArrow_loc=(By.XPATH,self.LeftArrow_path % (DateTypeindex,StartEndeindex))
        self.find_element(*LeftArrow_loc).click()
        time.sleep((Gl.waittime)/2)
    
    def Click_RightArrowInDatePicker(self,DateTypeindex,StartEndeindex):
        '''DateTypeindex:1 for Created Date,2 for Acknowledge Date
           StartEndindex: 1 for Start,2 for End'''
        RightArrow_loc=(By.XPATH,self.RightArrow_path % (DateTypeindex,StartEndeindex))
        self.find_element(*RightArrow_loc).click()
        time.sleep((Gl.waittime)/2)
        
        
    
    def Click_StartDate(self,WhichDate):#WhichDate:1 for create,2 for Acknowledge
        StartDate_loc=(By.XPATH,self.StartDatePicker_path % WhichDate)  
        self.find_element(*StartDate_loc).click()
    def Click_EndDate(self,WhichDate):#WhichDate:1 for create,2 for Acknowledge
        EndDate_loc=(By.XPATH,self.EndDatePicker_path % WhichDate)  
        self.find_element(*EndDate_loc).click()
        
    def Get_ClassValue_CreatedDateInDatePicker(self,StartEndeindex,lineindex,dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.CreatedDateInDatePicker_path % (StartEndeindex,lineindex,dateindex))
        return self.find_element(*DateInDatePicker_loc).get_attribute("class")
    def Get_ClassValue_AcknowledgeDateInDatePicker(self,StartEndeindex,lineindex,dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.AcknowledgeDateInDatePicker_path % (StartEndeindex,lineindex,dateindex))
        return self.find_element(*DateInDatePicker_loc).get_attribute("class")
        
    def Get_CreatedDateInDatePicker(self,StartEndeindex,lineindex,dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.CreatedDateInDatePicker_path % (StartEndeindex,lineindex,dateindex))
        return self.find_element(*DateInDatePicker_loc).text
    
    def Get_AcknowledgeDateInDatePicker(self,StartEndeindex,lineindex,dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.AcknowledgeDateInDatePicker_path % (StartEndeindex,lineindex,dateindex))
        return self.find_element(*DateInDatePicker_loc).text    
    
    
        
    def Select_CreatedDateInDatePicker(self,StartEndeindex,lineindex,dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.CreatedDateInDatePicker_path % (StartEndeindex,lineindex,dateindex))
        self.find_element(*DateInDatePicker_loc).click()
    def Select_AcknowledgeDateInDatePicker(self,StartEndeindex,lineindex,dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.AcknowledgeDateInDatePicker_path % (StartEndeindex,lineindex,dateindex))
        self.find_element(*DateInDatePicker_loc).click()
    def get_StartDateBoxContent(self,WhichDate):#WhichDate:1 for create,2 for Acknowledge
        StartDateBox_loc=(By.XPATH,self.StartDateInput_path % WhichDate)
        return self.find_element(*StartDateBox_loc).get_attribute("value")
    def Clear_StartDateBoxContent(self,WhichDate):#WhichDate:1 for create,2 for Acknowledge
        StartDateBox_loc=(By.XPATH,self.StartDateInput_path % WhichDate)
        self.find_element(*StartDateBox_loc).clear()
    def get_EndDateBoxContent(self,WhichDate):#WhichDate:1 for create,2 for Acknowledge
        EndDateBox_loc=(By.XPATH,self.EndDateInput_path % WhichDate)
        return self.find_element(*EndDateBox_loc).get_attribute("value")
    def Clear_EndDateBoxContent(self,WhichDate):#WhichDate:1 for create,2 for Acknowledge
        EndDateBox_loc=(By.XPATH,self.EndDateInput_path % WhichDate)
        self.find_element(*EndDateBox_loc).clear()
    
    
                       
        
    def get_EachkpivalueOfTL(self,TLindex,kpiindex):
        TLkpivaule_loc=(By.XPATH,self.TLkpivalue_path % (TLindex,kpiindex)) 
        return self.find_element(*TLkpivaule_loc).text
         
    def get_datevalu(self,int1,int2):#Created Date:(1,1/2),AcknowledgeDate:(2,1/2)
        self.datevalue_loc=(By.XPATH,self.datevalue_path %(int1,int2))
        return self.find_element(*self.datevalue_loc).get_attribute("value")   
        
    def click_filterbutton(self):
        self.find_element(*self.filterbutton_loc).click()
    
    def click_timebutton(self,int1,int2):
        self.timebutton_loc=(By.XPATH,self.timebutton_path %(int1,int2))
        self.find_element(*self.timebutton_loc).click()
        
    def click_back(self):
        self.find_element(*self.back_loc).click()
        time.sleep(Gl.waittime)
        
    def click_timetopclick(self,int1,int2):
        self.timetopclick_loc=(By.XPATH,self.timetopclick_path %(int1,int2))
        self.find_element(*self.timetopclick_loc).click()
        
    def get_yeartopvalue(self,int1,int2):
        self.yeartopvalue_loc=(By.XPATH,self.yeartopvalue_path %(int1,int2))
        return self.find_element(*self.yeartopvalue_loc).text
    
    def click_yeartopvalue(self,int1,int2):
        self.yeartopvalue_loc=(By.XPATH,self.yeartopvalue_path %(int1,int2))
        self.find_element(*self.yeartopvalue_loc).click()
     
    def click_smallleftbutton(self,int1,int2):
        self.smallleftbutton_loc=(By.XPATH,self.smallleftbutton_path %(int1,int2))
        self.find_element(*self.smallleftbutton_loc).click() 
    
    def click_dayactivevalue(self):
        self.find_element(*self.dayactivevalue_loc).click()
    
    def click_dayvalue(self,int1,int2,int3,int4):
        self.dayvalue_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4))
        self.find_element(*self.dayvalue_loc).click()
        
    def disabled_dayclick(self,int1,int2,int3,int4):
        self.dayvalue_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4))
        return self.find_element(*self.dayvalue_loc).get_attribute("class")
        
    def get_dayvalue(self,int1,int2,int3,int4):
        self.dayvalue_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4))
        return self.find_element(*self.dayvalue_loc).text
    
    def get_nowday(self,int1,int2,int3,int4):
        self.nowday_loc=(By.XPATH,self.dayvalue_path %(int1,int2,int3,int4))
        return self.find_element(*self.nowday_loc).get_attribute("class")   
        
    def click_bigleftbutton(self,int1,int2):
        self.bigleftbutton_loc=(By.XPATH,self.bigleftbutton_path %(int1,int2))  
        self.find_element(*self.bigleftbutton_loc).click()
        
    def click_monthclick(self,int1,int2,int3):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %(int1,int2,int3))
        self.find_element(*self.monthclick_loc).click()
        
    def get_monthvalue(self,int1,int2,int3):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %(int1,int2,int3))
        return self.find_element(*self.monthclick_loc).text
        
    def click_yearclick(self,int1,int2,int3):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %(int1,int2,int3))
        self.find_element(*self.yearclick_loc).click()
        
    def get_yearvalue(self,int1,int2,int3):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %(int1,int2,int3))
        return self.find_element(*self.yearclick_loc).text
    
    def get_warnmessage(self):
        return self.find_element(*self.warnmessage_loc).text
    
    def click_LeaderScorespage(self,int1):
        self.LeaderScorespage_loc=(By.XPATH,self.LeaderScorespage_path %int1)
        self.find_element(*self.LeaderScorespage_loc).click()
        
    def get_TLname(self,int1):
        self.tlname_loc=(By.XPATH,self.tlname_path %int1)
        return self.find_element(*self.tlname_loc).text
    def get_AllTLname_list(self):
        All=[]
        AllTLname=[]
        lineindex=1
        while self.Element_displayed(*(By.XPATH,self.tlname_path %lineindex)):
            TLaccount_loc=(By.XPATH,self.tlname_path %lineindex)
            TLname=self.find_element(*TLaccount_loc).text
            if TLname != "AVERAGE SCORE OF FORM":
                AllTLname.append(TLname)
            lineindex=lineindex+1
        All.append(AllTLname)
        All.append(lineindex-2)
        return All
    def get_TLHridWithL3Login(self,TLindex):#Add by Sabrina Guo,also is for L2
        TLHrid_loc=(By.XPATH,self.TLHrid_path % (TLindex))
        TLHrid=self.find_element(*TLHrid_loc).get_attribute("data-id")
        return TLHrid
    def get_anyTLvalueWithL3Login(self,TLindex,KPInumber):
        value_list=[]
        for kpiindex in range(2,KPInumber+2):
            #while self.Element_displayed(*(By.XPATH,self.tlvalue_path %(i,kpiindex))):
            tlvalue_loc=(By.XPATH,self.TLkpivalue_path %(TLindex,kpiindex))
            tlvalue=self.find_element(*tlvalue_loc).text
            value_list.append(tlvalue)
        return value_list
        
    
    def get_AllTLvalue_ByL3(self,TLnumber,KPInumber):#Add by Sabrina Guo,also is for L2
        AllTLValue_list={}
        for i in range(1,TLnumber+1):
            
            ''' kpiindex=2'''
            TLHrid=self.get_TLHridWithL3Login(i)
            value_list=self.get_anyTLvalueWithL3Login(i, KPInumber)
            '''
            value_list=[]
            for kpiindex in range(2,KPInumber+2):
            #while self.Element_displayed(*(By.XPATH,self.tlvalue_path %(i,kpiindex))):
                tlvalue_loc=(By.XPATH,self.TLkpivalue_path %(i,kpiindex))
                tlvalue=self.find_element(*tlvalue_loc).text
                value_list.append(tlvalue)
                #kpiindex=kpiindex+1'''
            AllTLValue_list[TLHrid]=value_list
        return AllTLValue_list 
    
    def get_pagedate(self,int1,int2):
        self.pagedate_loc=(By.XPATH,self.pagedate_path %(int1,int2))
        return self.find_element(*self.pagedate_loc).text
    
    
    def get_avgData(self,list_DataBase):
        index=0
        Sum_score=0
        for item in list_DataBase:
            if item !=None:
                index=index+1
                Sum_score=Sum_score+item
        avg=Sum_score/index
        return avg
            
        
    
    