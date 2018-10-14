'''
Created on 2017/03/17

@author: luming.zhao
'''


from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
import time
from public_method import Gl


class SalesQuickHit(BasePage.Action):


    def __init__(self):
       
        self.calendar_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/span/span")
        
        self.date_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/div/div[2]/ul/li/div/div/table/tbody/tr/td[3]")
        
        self.tactic_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/input")
        self.TacticTtle_path=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[2]/label')
        self.CallDateTime_input_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[1]/div/div/div[2]/input')
        self.CallDateTime_selection_loc=(By.CSS_SELECTOR, "span.glyphicon.glyphicon-calendar")
        self.TheFirstTimeofCallDateTime_select_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[1]/td[1]')
        #self.anyDateTimeOfCall_path='//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[%d]/td[%d]'
        self.anyDateTimeOfCall_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[%d]/td[%d]"
        
        self.FirstThreelongtextbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/table/tbody/tr[13]/td/div/textarea'
        self.SecondThreelongtextbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/table/tbody/tr[%d]/td/div/textarea'
        self.Seventhlongtextbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[10]/div/textarea'
        self.LastFourlongtextbox_path='//*[@id="container"]/div/section/div/form/div[2]/table/tbody/tr[%d]/td[2]/div/textarea'
        
    def select_ObservationReason(self,reasonindex): #reasonindex=1, 2, 3
        self.ObservationReason_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/div/div[%d]/label' %reasonindex) 
                                              
        self.find_element(*self.ObservationReason_loc).click()             
    def get_ObservationReasonStatus(self,reasonstatusindex): #reasonstatusindex=1,2,3
        self.ObservationReasonStatus_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/div/div[%d]/i' %reasonstatusindex)     
        ObservationReasonStatus=self.find_element(*self.ObservationReasonStatus_loc).get_attribute('class')
        return ObservationReasonStatus
   
        
    def input_CallDateTime (self,text):  
        self.find_element(*self.CallDateTime_input_loc).send_keys(text)
        time.sleep(Gl.waittime)
    
    def get_CallDateTime (self):
        return self.find_element(*self.CallDateTime_input_loc).get_attribute('value')
    def CallDateTime_disabled(self):
        flag=self.find_element(*self.CallDateTime_input_loc).get_attribute('disabled')
        return flag  
    
    def select_ThefirstTimeOfCallDateTime(self):
        self.find_element(*self.CallDateTime_selection_loc).click()
        self.find_element(*self.CallDateTime_selection_loc).click()
        time.sleep(Gl.waittime)    
        
    def select_anyDateTimeOfCall(self,lineindex,dateindex):#lineindex is from 1 to 6;dateindex is from 1 to 7
        self.find_element(*self.CallDateTime_selection_loc).click()
        #anyDateTimeOfCall_loc=(By.XPATH,self.anyDateTimeOfCall_path % (lineindex,dateindex))
        anyDateTimeOfCall_loc=(By.XPATH, self.anyDateTimeOfCall_path % (lineindex,dateindex))
        
        self.find_element(*anyDateTimeOfCall_loc).click()
        time.sleep(Gl.waittime) 
      
      
        
    def input_tactic (self,text):
        self.find_element(*self.tactic_loc).clear()
        self.find_element(*self.tactic_loc).send_keys(text)
    def get_tactic (self):
        return self.find_element(*self.tactic_loc).get_attribute('value')
        
    def get_TacticTitle (self):
        self.TacticTitle_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[2]/div[2]/label')
        #TacticTitle_loc=(By.XPATH, self.TacticTtle_path)
        return self.find_element(*self.TacticTitle_loc).text
    
    def tactic_disabled(self):
        flag=self.find_element(*self.tactic_loc).get_attribute('disabled')
        return flag
    
    def input_FirstThreelongtextbox (self,text,boxindex):   #boxindex=4, 5, 6
        #self.FirstThreelongtextbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[%d]/table/tbody/tr[13]/td/div/textarea' %boxindex) 
        FirstThreelongtextbox_loc=(By.XPATH,self.FirstThreelongtextbox_path % boxindex)
        self.find_element(*FirstThreelongtextbox_loc).clear()
        self.find_element(*FirstThreelongtextbox_loc).send_keys(text)
    def get_FirstThreelongtextbox(self,boxindex): #boxindex=4, 5, 6
        FirstThreelongtextbox_loc=(By.XPATH,self.FirstThreelongtextbox_path % boxindex)
        return self.find_element(*FirstThreelongtextbox_loc).text
          
    def FirstThreelongtextbox_disabled(self,boxindex): #boxindex=4, 5, 6
        FirstThreelongtextbox_loc=(By.XPATH,self.FirstThreelongtextbox_path % boxindex)
        flag=self.find_element(*FirstThreelongtextbox_loc).get_attribute('disabled')
        return flag
    def input_SecondThreelongtextbox (self, text, boxindex, lineindex):   #boxindex=7, 8, 9  lineindex=5, 4, 8
        SecondThreelongtextbox_loc=(By.XPATH, self.SecondThreelongtextbox_path %(boxindex,lineindex))        
        self.find_element(*SecondThreelongtextbox_loc).clear()
        self.find_element(*SecondThreelongtextbox_loc).send_keys(text)
    def get_SecondThreelongtextbox (self, boxindex, lineindex):   #boxindex=7, 8, 9  lineindex=5, 4, 8
        self.SecondThreelongtextbox_loc=(By.XPATH, self.SecondThreelongtextbox_path %(boxindex,lineindex))
        return self.find_element(*self.SecondThreelongtextbox_loc).text   
        
    def SecondThreelongtextbox_disabled(self,boxindex,lineindex):#boxindex=7, 8, 9  lineindex=5, 4, 8
        SecondThreelongtextbox_loc=(By.XPATH, self.SecondThreelongtextbox_path %(boxindex,lineindex))
        flag=self.find_element(*SecondThreelongtextbox_loc).get_attribute('disabled')
        return flag
    
    def input_Seventhlongtextbox (self,text):
        Seventhlongtextbox_loc=(By.XPATH, self.Seventhlongtextbox_path)
        self.find_element(*Seventhlongtextbox_loc).clear()
        self.find_element(*Seventhlongtextbox_loc).send_keys(text)
    def Seventhlongtextbox_disabled(self):
        Seventhlongtextbox_loc=(By.XPATH, self.Seventhlongtextbox_path)
        flag=self.find_element(*Seventhlongtextbox_loc).get_attribute('disabled')
        return flag
    def get_Seventhlongtextbox (self):
        self.Seventhlongtextbox_loc=(By.XPATH, self.Seventhlongtextbox_path)
        return self.find_element(*self.Seventhlongtextbox_loc).text
    
    def input_LastFourlongtextbox (self,text,boxindex): #boxindex=2, 3, 5, 6
        LastFourlongtextbox_loc=(By.XPATH, self.LastFourlongtextbox_path %boxindex)
        self.find_element(*LastFourlongtextbox_loc).clear()
        self.find_element(*LastFourlongtextbox_loc).send_keys(text)
    def LastFourlongtextbox_disabled(self,boxindex):
        LastFourlongtextbox_loc=(By.XPATH, self.LastFourlongtextbox_path %boxindex)
        flag=self.find_element(*LastFourlongtextbox_loc).get_attribute('disabled')
        return flag
    def get_LastFourlongtextbox (self,boxindex): #boxindex=2, 3, 5, 6
        self.LastFourlongtextbox_loc=(By.XPATH, self.LastFourlongtextbox_path %boxindex)
        return self.find_element(*self.LastFourlongtextbox_loc).text
    
    def get_FristSevenlongtextboxTitle (self,titleindex): #titleindex=4, 5, 6, 7, 8, 9, 10
        FristSevenlongtextboxTitle_loc=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[%d]/label' %titleindex)
        return self.find_element(*FristSevenlongtextboxTitle_loc).text
    
    def get_LastTwolongtextboxTitle(self,titleindex): #titleindex=1, 4
        LastTwolongtexttitle_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/table/tbody/tr[%d]/th/label' %titleindex)
        return self.find_element(*LastTwolongtexttitle_loc).text
    
    def click_RadioButtonAtSectionOne (self,buttonindex,Buttontypeindex):
        #buttonindex=2, 3, 4, 6, 7, 8, 10, 11, 12  Buttontypeindex=1=yes  buttontypeindex=2=no  buttontypeindex=3=na   
        self.RadioButtonAtSectionOne_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[4]/table/tbody/tr[%d]/td[2]/div/div[%d]/label') %(buttonindex,Buttontypeindex))
        self.find_element(*self.RadioButtonAtSectionOne_loc).click()
    def get_RadioButtonAtSectionOneStatus(self,buttonindex,Buttontypeindex):
        RadioButtonAtSectionOnStatus_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[4]/table/tbody/tr[%d]/td[2]/div/div[%d]/i') %(buttonindex,Buttontypeindex))
        return self.find_element(*RadioButtonAtSectionOnStatus_loc).get_attribute('class')
    
        
    def click_RadioButtonAtSectionTwo (self,buttonindex,Buttontypeindex): #buttonindex=2, 3, 4, 5, 7, 8, 9, 11, 12 Buttontypeindex=1=yes  buttontypeindex=2=no  buttontypeindex=3=na 
        self.RadioButtonAtSectionTwo_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[5]/table/tbody/tr[%d]/td[2]/div/div[%d]/label') %(buttonindex,Buttontypeindex))
        self.find_element(*self.RadioButtonAtSectionTwo_loc).click()
    def get_RadioButtonAtSectionTwoStatus(self,buttonindex,Buttontypeindex):  #buttonindex=2, 3, 4, 5, 7, 8, 9, 11, 12 Buttontypeindex=1=yes  buttontypeindex=2=no  buttontypeindex=3=na 
        RadioButtonAtSectionTwoStatus_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[5]/table/tbody/tr[%d]/td[2]/div/div[%d]/i')  %(buttonindex,Buttontypeindex))
        return self.find_element(*RadioButtonAtSectionTwoStatus_loc).get_attribute('class') 
    
      
    def click_RadioButtonAtSectionThree(self,buttonindex,Buttontypeindex): #buttonindex=2, 3, 5, 6, 7, 9, 10, 11, 12 Buttontypeindex=1=yes  buttontypeindex=2=no  buttontypeindex=3=na 
        RadioButtonAtSectionThree_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td[2]/div/div[%d]/label') %(buttonindex,Buttontypeindex))
        self.find_element(*RadioButtonAtSectionThree_loc).click()
    def get_RadioButtonAtSectionThreeStatus(self,buttonindex,Buttontypeindex):
        RadioButtonAtSectionThreeStatus_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td[2]/div/div[%d]/i') %(buttonindex,Buttontypeindex))
        return self.find_element(*RadioButtonAtSectionThreeStatus_loc).get_attribute('class')
   
    
        
    def click_RadioButtonAtSectionFour (self, buttonindex,Buttontypeindex): #buttonindex=2,3, 4 Buttontypeindex=1=yes  buttontypeindex=2=no  buttontypeindex=3=na
        RadioButtonAtSectionFour_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[7]/table/tbody/tr[%d]/td[2]/div/div[%d]/label') %(buttonindex,Buttontypeindex))
        self.find_element(*RadioButtonAtSectionFour_loc).click()
    def get_RadioButtonAtSectionFourStatus(self,buttonindex,Buttontypeindex):
        RadioButtonAtSectionFourStatus_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[7]/table/tbody/tr[%d]/td[2]/div/div[%d]/i') %(buttonindex,Buttontypeindex))
        return self.find_element(*RadioButtonAtSectionFourStatus_loc).get_attribute('class') 
    
       
    def click_RadioButtonAtSectionFive (self, buttonindex,Buttontypeindex): #buttonindex=2,3   Buttontypeindex=1=yes  buttontypeindex=2=no  buttontypeindex=3=na
        RadioButtonAtSectionFive_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[8]/table/tbody/tr[%d]/td[2]/div/div[%d]/label') %(buttonindex,Buttontypeindex))
        self.find_element(*RadioButtonAtSectionFive_loc).click()
    def get_RadioButtonAtSectionFiveStatus(self,buttonindex,Buttontypeindex):
        RadioButtonAtSectionFiveStatus_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[8]/table/tbody/tr[%d]/td[2]/div/div[%d]/i') %(buttonindex,Buttontypeindex))
        return self.find_element(*RadioButtonAtSectionFiveStatus_loc).get_attribute('class')  
    
       
    def click_RadioButtonAtSectionSix (self, buttonindex,Buttontypeindex): #buttonindex=1, 2, 3, 4, 5, 6, 7   Buttontypeindex=1=yes  buttontypeindex=2=no  buttontypeindex=3=na
        RadioButtonAtSectionSix_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[9]/table/tbody/tr[%d]/td[2]/div/div[%d]/label') %(buttonindex,Buttontypeindex))
        self.find_element(*RadioButtonAtSectionSix_loc).click()
    def get_RadioButtonAtSectionSixStatus(self,buttonindex,Buttontypeindex):
        RadioButtonAtSectionFiveStatus_loc=(By.XPATH, ('//*[@id="container"]/div/section/div/form/div[2]/div[9]/table/tbody/tr[%d]/td[2]/div/div[%d]/i') %(buttonindex,Buttontypeindex))
        return self.find_element(*RadioButtonAtSectionFiveStatus_loc).get_attribute('class') 
    
    