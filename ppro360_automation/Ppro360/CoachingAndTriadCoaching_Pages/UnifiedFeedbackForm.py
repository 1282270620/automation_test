'''
Created on 20170707

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class UnifiedFeedbackForm(BasePage.Action):
    
    
    def __init__(self):
         
        
        self.shortinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[%d]/div/input"
        self.shortinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[%d]/label"
        self.totalpoint_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[18]/div/div[2]")
        self.datebox_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div/div/div[2]/input")
        self.timebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/span/span")
        self.dayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        self.hourbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div/div/div[2]/ul/li[2]/span/span")
        self.backbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div/div/div[2]/ul/li[1]/span/span")
        self.pointchoose_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/div/div[1]/div[%d]/div[2]/div[%d]/i"
        self.pointrecieved_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/div/div[2]"
        self.observationnotes_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.observationnotes_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        self.chooseclick_path="//*[@id='container']/div/section/div/form/div[2]/div[19]/div/div[%d]/div[%d]/div/div[2]/div[%d]/i"
        self.longinput_path="//*[@id='container']/div/section/div/form/div[2]/div[20]/div/div[%d]/div/div/textarea"
        self.longinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[20]/div/div[%d]/div/label"
        self.midinput_path="//*[@id='container']/div/section/div/form/div[2]/div[20]/div/div[%d]/div[%d]/div/div/textarea "
        self.midinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[20]/div/div[%d]/div[%d]/div/label"
        self.bigleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th/span")
        self.bigrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]/span")
        self.monthandyearbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[2]")
        self.yearclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.monthclick_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td/span[%d]"
        self.smallleftarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th")
        self.smallrightarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/thead/tr/th[3]")
        self.ampmbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[2]/td[5]/button")
        self.houruparrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr/td/a/span")
        self.hourdownarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[3]/td/a/span")
        self.minuteuparrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr/td[3]/a/span")
        self.minutedownarrow_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[3]/td[3]/a/span")
        self.auditpurpose_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[1]/div/span")
        self.auditpurposechoose_path="//*[@id='container']/div/section/div/form/div[2]/div[4]/div[1]/div/ul/li[%d]/a "
        self.detractorbehavior_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/div/span")
        self.detractorbehaviorchoose_path="//*[@id='container']/div/section/div/form/div[2]/div[4]/div[2]/div/ul/li[%d]/a"
        
    def input_shortinput (self,lineindex,mid,text):
        self.shortinput_loc=(By.XPATH,self.shortinput_path %(lineindex,mid))
        self.Input_text(text,*self.shortinput_loc)
        
    def get_shortinput(self,lineindex,mid):
        self.shortinput_loc=(By.XPATH,self.shortinput_path %(lineindex,mid))
        return self.find_element(*self.shortinput_loc).get_attribute("value")
    
    def shortinput_disabled(self,lineindex,mid):
        self.shortinput_loc=(By.XPATH,self.shortinput_path %(lineindex,mid))
        flag=self.find_element(*self.shortinput_loc).get_attribute("disabled")
        return flag
    
    def get_shortinputBoxtitle(self,lineindex,mid):
        self.shortinput_title_loc=(By.XPATH,self.shortinput_title_path %(lineindex,mid))
        return self.find_element(*self.shortinput_title_loc).text
    
    def get_datebox(self):
        return self.find_element(*self.datebox_loc).get_attribute("value")
    
    def datebox_disabled(self):
        flag=self.find_element(*self.datebox_loc).get_attribute("disabled")
        return flag
    
    def click_timebutton(self):
        self.find_element(*self.timebutton_loc).click()
        
    def timebutton_disabled(self):
        flag=self.find_element(*self.timebutton_loc).get_attribute("disabled")
        return flag
    
    def click_dayclick (self,lineindex4,columnindex4):
        self.dayclick_loc=(By.XPATH,self.dayclick_path %(lineindex4,columnindex4))    
        self.find_element(*self.dayclick_loc).click()
        
    def click_hourbutton(self):
        self.find_element(*self.hourbutton_loc).click()
        
    def click_backbutton(self):
        self.find_element(*self.backbutton_loc).click()
        
    def click_pointchoose(self,moudle,line,column):
        self.pointchoose_loc=(By.XPATH,self.pointchoose_path %(moudle,line,column))
        self.find_element(*self.pointchoose_loc).click()
     
    def get_pointchoose(self,moudle,line,column):
        self.pointchoose_loc=(By.XPATH,self.pointchoose_path %(moudle,line,column))
        flag=self.find_element(*self.pointchoose_loc).get_attribute("class")
        return flag       
    
    def get_pointrecievedvalue(self,line):
        self.pointrecieved_loc=(By.XPATH,self.pointrecieved_path %line)
        return self.find_element(*self.pointrecieved_loc).text
    
    def get_totalpointvalue(self):
        return self.find_element(*self.totalpoint_loc).text
    
    def input_observationnotes (self,lineindex,text):
        self.observationnotes_loc=(By.XPATH,self.observationnotes_path %lineindex)
        self.Input_text(text,*self.observationnotes_loc)
        
    def get_observationnotes(self,lineindex):
        self.observationnotes_loc=(By.XPATH,self.observationnotes_path %lineindex)
        return self.find_element(*self.observationnotes_loc).get_attribute("value")
    
    def observationnotes_disabled(self,lineindex):
        self.observationnotes_loc=(By.XPATH,self.observationnotes_path %lineindex)
        flag=self.find_element(*self.observationnotes_loc).get_attribute("disabled")
        return flag
    
    def get_observationnotesBoxtitle(self,lineindex):
        self.observationnotes_title_loc=(By.XPATH,self.observationnotes_title_path %lineindex)
        return self.find_element(*self.observationnotes_title_loc).text
    
    def click_chooseclick (self,moduleindex,lineindex,columnindex):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(moduleindex,lineindex,columnindex))
        self.find_element(*self.chooseclick_loc).click()
        
    def get_chooseclick(self,moudle,line,column):
        self.chooseclick_loc=(By.XPATH,self.chooseclick_path %(moudle,line,column))
        flag=self.find_element(*self.chooseclick_loc).get_attribute("class")
        return flag
        
    def input_longinput (self,lineindex,text):
        self.longinput_loc=(By.XPATH,self.longinput_path %lineindex)
        self.Input_text(text,*self.longinput_loc)
        
    def get_longinput(self,lineindex):
        self.longinput_loc=(By.XPATH,self.longinput_path %lineindex)
        return self.find_element(*self.longinput_loc).get_attribute("value")
    
    def longinput_disabled(self,lineindex):
        self.longinput_loc=(By.XPATH,self.longinput_path %lineindex)
        flag=self.find_element(*self.longinput_loc).get_attribute("disabled")
        return flag
    
    def get_longinputBoxtitle(self,lineindex):
        self.longinput_title_loc=(By.XPATH,self.longinput_title_path %lineindex)
        return self.find_element(*self.longinput_title_loc).text
    
    
    def input_midinput (self,lineindex,mid,text):
        self.midinput_loc=(By.XPATH,self.midinput_path %(lineindex,mid))
        self.Input_text(text,*self.midinput_loc)
        
    def get_midinput(self,lineindex,mid):
        self.midinput_loc=(By.XPATH,self.midinput_path %(lineindex,mid))
        return self.find_element(*self.midinput_loc).get_attribute("value")
    
    def midinput_disabled(self,lineindex,mid):
        self.midinput_loc=(By.XPATH,self.midinput_path %(lineindex,mid))
        flag=self.find_element(*self.midinput_loc).get_attribute("disabled")
        return flag
    
    def get_midinputBoxtitle(self,lineindex,mid):
        self.midinput_title_loc=(By.XPATH,self.midinput_title_path %(lineindex,mid))
        return self.find_element(*self.midinput_title_loc).text   
          
    
    def click_bigleftarrow (self):
        self.find_element(*self.bigleftarrow_loc).click()
        
    def click_bigrightarrow (self):
        self.find_element(*self.bigrightarrow_loc).click()
    
    def click_monthandyearbutton (self):
        self.find_element(*self.monthandyearbutton_loc).click()

    def click_yearclick (self,lineindex5):
        self.yearclick_loc=(By.XPATH,self.yearclick_path %lineindex5)
        self.find_element(*self.yearclick_loc).click()
    
    def click_monthclick (self,lineindex6):
        self.monthclick_loc=(By.XPATH,self.monthclick_path %lineindex6)
        self.find_element(*self.monthclick_loc).click()
        
    def click_smallleftarrow (self):
        self.find_element(*self.smallleftarrow_loc).click()
        
    def click_smallrightarrow (self):
        self.find_element(*self.smallrightarrow_loc).click()
        
    def click_ampmbutton (self):
        self.find_element(*self.ampmbutton_loc).click()
    
    def click_houruparrow (self):
        self.find_element(*self.houruparrow_loc).click()
        
    def click_hourdownarrow (self):
        self.find_element(*self.hourdownarrow_loc).click()
        
    def click_minuteuparrow (self):
        self.find_element(*self.minuteuparrow_loc).click()
        
    def click_minutedownarrow (self):
        self.find_element(*self.minutedownarrow_loc).click()
        
        
    def click_auditpurpose(self):
        self.find_element(*self.auditpurpose_loc).click()
        
    def auditpurposevalue(self):
        return self.find_element(*self.auditpurpose_loc).text
    
    def auditpurpose_disabled(self):
        flag=self.find_element(*self.auditpurpose_loc).get_attribute("disabled")
        return flag
    
    def click_auditpurposechoose(self,lineindex):
        self.auditpurposechoose_loc=(By.XPATH,self.auditpurposechoose_path %lineindex)
        self.find_element(*self.auditpurposechoose_loc).click()
        
    def click_detractorbehavior(self):
        self.find_element(*self.detractorbehavior_loc).click()
        
    def detractorbehaviorvalue(self):
        return self.find_element(*self.detractorbehavior_loc).text
    
    def detractorbehavior_disabled(self):
        flag=self.find_element(*self.detractorbehavior_loc).get_attribute("disabled")
        return flag
    
    def click_detractorbehaviorchoose(self,lineindex):
        self.detractorbehaviorchoose_loc=(By.XPATH,self.detractorbehaviorchoose_path %lineindex)
        self.find_element(*self.detractorbehaviorchoose_loc).click()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
