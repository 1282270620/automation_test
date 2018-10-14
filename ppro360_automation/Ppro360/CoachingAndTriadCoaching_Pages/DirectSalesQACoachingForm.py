'''
Created on 20170307

@author: luming.zhao
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from MySQLdb.constants import FLAG
from operator import index
from __builtin__ import True
from pip._vendor.pyparsing import line


class DirectSalesQACoachingForm(BasePage.Action):

    def __init__(self):
        
        self.eachModule_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/table/tbody/tr[%d]/td[2]/div/div[%d]/label" 
        self.discover_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/table/tbody/tr[%d]/td[2]/div/div[%d]/label"
        self.transition_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/table/tbody/tr[%d]/td[2]/div/div[%d]/label"
        self.pitch_path="//*[@id='container']/div/section/div/form/div[2]/div[4]/table/tbody/tr[%d]/td[2]/div/div[%d]/i"
        self.overcome_path="//*[@id='container']/div/section/div/form/div[2]/div[5]/table/tbody/tr/td[2]/div/div[%d]/i"
        self.close_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/table/tbody/tr[%d]/td[2]/div/div[%d]/i"
        self.strengths_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/div/textarea")
        self.opportunities1_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[2]/td[2]/div/textarea")
        self.opportunities2_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[3]/td[2]/div/textarea")
        self.plan1_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[5]/td[2]/div/textarea")
        self.plan2_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[6]/td[2]/div/textarea")
        self.strengths_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[7]/label")
        self.opportunities_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[1]/th/label")
        self.plan_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/table/tbody/tr[4]/th/label")
         
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")

        
    #def select_eachModule(self,moduleindex,lineindex,buttonindex):
        #eachModule select 'yes' default 
        #eachModule_loc=(By.XPATH,self.eachModule_path %(moduleindex,lineindex,buttonindex))
        #self.find_element(*self.eachModule_loc).click()
    
    #def select_Discover(self,lineindex,buttonindex): 
        #lineindex just can be 1,2,3,4,5
        #buttonindex just can be 1,2,3
        #Discover_loc=(By.XPATH,self.Discover_path %(lineindex,buttonindex)) 
        #self.find_element(*Discover_loc).click()
        
    def select_discover(self,lineindex1,columnindex1):
        #lineindex just can be 1,2,3,4,5
        #buttonindex just can be 1,2,3
        self.discover_loc=(By.XPATH,self.discover_path %(lineindex1,columnindex1))
        self.find_element(*self.discover_loc).click()

    def discover_disabled(self,lineindex1,columnindex1):
        self.discover_loc=(By.XPATH,self.discover_path %(lineindex1,columnindex1) )
        flag=self.find_element(*self.discover_loc).get_attribute("disabled")
        return flag
    
    def get_discovertatus(self,lineindex1,columnindex1):
        self.discover_loc=(By.XPATH,self.discover_path %(lineindex1,columnindex1))
        checkstataus=self.find_element(*self.discover_loc).get_attribute("class")
        return checkstataus

        
    def select_transition(self,lineindex2,columnindex2): 
        #lineindex2 just can be 1,2
        #buttonindex2 just can be 1,2,3
        self.transition_loc=(By.XPATH,self.transition_path %(lineindex2,columnindex2))
        self.find_element(*self.transition_loc).click()
        
        
    def transition_disabled(self,lineindex2,columnindex2):
        self.transition_loc=(By.XPATH,self.transition_path %(lineindex2,columnindex2) )
        flag=self.find_element(*self.transition_loc).get_attribute("disabled")
        return flag
    
    def get_transitiontatus(self,lineindex2,columnindex2):
        self.transition_loc=(By.XPATH,self.transition_path %(lineindex2,columnindex2))
        checkstataus=self.find_element(*self.transition_loc).get_attribute("class")
        return checkstataus

        
    def select_pitch(self,lineindex3,buttonindex3): 
        #lineindex3 just can be 1,2,3,4,5,6,7,8
        #buttonindex3 just can be 1,2,3
        self.pitch_loc=(By.XPATH,self.pitch_path %(lineindex3,buttonindex3)) 
        self.find_element(*self.pitch_loc).click()
    
    def pitch_disabled(self,lineindex3,columnindex3):
        self.pitch_loc=(By.XPATH,self.pitch_path %(lineindex3,columnindex3) )
        flag=self.find_element(*self.pitch_loc).get_attribute("disabled")
        return flag
    
    def get_pitchtatus(self,lineindex3,columnindex3):
        self.pitch_loc=(By.XPATH,self.pitch_path %(lineindex3,columnindex3))
        checkstataus=self.find_element(*self.pitch_loc).get_attribute("class")
        return checkstataus

    
    def select_overcome(self,buttonindex): 
        #buttonindex just can be 1,2,3
        self.overcome_loc=(By.XPATH,self.overcome_path %buttonindex) 
        self.find_element(*self.overcome_loc).click()      
        
    def overcome_disabled(self,buttonindex):
        self.overcome_loc=(By.XPATH,self.overcome_path %buttonindex)
        flag=self.find_element(*self.overcome_loc).get_attribute("disabled")
        return flag
    
    def get_overcometatus(self,buttonindex):
        self.overcome_loc=(By.XPATH,self.overcome_path %buttonindex)
        checkstataus=self.find_element(*self.overcome_loc).get_attribute("class")
        return checkstataus   
           
        
    def select_close(self,lineindex4,buttonindex4): 
        #lineindex just can be 1,2,3
        #buttonindex just can be 1,2,3
        self.close_loc=(By.XPATH,self.close_path %(lineindex4,buttonindex4)) 
        self.find_element(*self.close_loc).click()
    
    def close_disabled(self,lineindex4,buttonindex4):
        self.close_loc=(By.XPATH,self.close_path %(lineindex4,buttonindex4))
        flag=self.find_element(*self.close_loc).get_attribute("disabled")
        return flag
    
    def get_closetatus(self,lineindex4,buttonindex4):
        self.close_loc=(By.XPATH,self.close_path %(lineindex4,buttonindex4))
        checkstataus=self.find_element(*self.close_loc).get_attribute("class")
        return checkstataus   
              
        
        
    def input_strengths(self,text):
        self.Input_text(text,*self.strengths_loc)
    def get_strengths(self):
        return self.find_element(*self.strengths_loc).get_attribute("value")
    def strengths__disabled(self):
        flag=self.find_element(*self.strengths_loc).get_attribute("disabled")
        return flag
    def get_strengthsBoxTitle(self):
        return self.find_element(*self.strengths_title_loc).text  
          
       
    def input_opportunities1(self,text):
        self.Input_text(text,*self.opportunities1_loc)
    def get_opportunities1(self):
        return self.find_element(*self.opportunities1_loc).get_attribute("value")
    def opportunities1__disabled(self):
        flag=self.find_element(*self.opportunities1_loc).get_attribute("disabled")
        return flag
    def get_opportunities1BoxTitle(self):
        return self.find_element(*self.opportunities_title_loc).text         
        
        
    def input_opportunities2(self,text):
        self.Input_text(text,*self.opportunities2_loc)
    def get_opportunities2(self):
        return self.find_element(*self.opportunities2_loc).get_attribute("value")
    def opportunities2__disabled(self):
        flag=self.find_element(*self.opportunities2_loc).get_attribute("disabled")
        return flag
    def get_opportunities2BoxTitle(self):
        return self.find_element(*self.opportunities_title_loc).text          
         
    def input_plan1(self,text):
        self.Input_text(text,*self.plan1_loc)
    def get_plan1(self):
        return self.find_element(*self.plan1_loc).get_attribute("value")
    def plan1__disabled(self):
        flag=self.find_element(*self.plan1_loc).get_attribute("disabled")
        return flag
    def get_plan1BoxTitle(self):
        return self.find_element(*self.plan_title_loc).text        
        
   
    def input_plan2(self,text):
        self.Input_text(text,*self.plan2_loc)
    def get_plan2(self):
        return self.find_element(*self.plan2_loc).get_attribute("value")
    def plan2__disabled(self):
        flag=self.find_element(*self.plan2_loc).get_attribute("disabled")
        return flag
    def get_plan2BoxTitle(self):
        return self.find_element(*self.plan_title_loc).text 
        
        
        
    def click_savebutton(self):
        self.find_element(*self.savebutton_loc).click()

        
        
        
        
        
        
        
        