from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl

class GamificationPointsSettingPage(BasePage.Action):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.GimficationPoint_path = "li.reward.ng-scope"
        self.Setting_path = 'Setting'
        #the element label of  Conditions
        self.ConditionSection_path = 'div[type="%s"] div div:nth-of-type(1)'
    
        self.ConditionSectionKPI_path = 'div[type="%s"] div div:nth-of-type(1) div ul li:nth-of-type(%d)'
        self.Coachingespecial_path = 'div[type="%s"] div div:nth-of-type(1) div ul li a[data-name="%s"]'

        self.CoditionsCondition_path = 'div[type="%s"] div div:nth-of-type(2)'
        self.ConditionsConditionsKPI_path = 'div[type="%s"] div div:nth-of-type(2) div ul li a[data-name="%s"]'
        
        self.ConditionsRelationship_path = 'div[type="%s"] div div:nth-of-type(3)'
        self.ConditionsRelationshipSelect_path = 'div[type="%s"] div div:nth-of-type(3) div ul li a[data-id="%s"]'
        
        self.ConditionsTarget_path = 'div[type="%s"] div div:nth-of-type(4) input'
        self.ConditionsPoints_path = 'div[type="%s"] div div:nth-of-type(5) input'
    
        self.Conditionadd_path = 'div[type="%s"] div div:nth-of-type(6) a'
        self.Conditioninfo_path = "html body div:nth-of-type(2) div div:nth-of-type(2) div div:nth-of-type(%d) div table tbody tr:nth-of-type(%d)"
    ####Every action on the page####
    def click_GimficationPoint(self):
        self.GimficationPoint = (By.CSS_SELECTOR,self.GimficationPoint_path)
        self.find_element(*self.GimficationPoint).click()   
            
    def click_Setting(self):
        self.Setting = (By.LINK_TEXT,self.Setting_path)
        self.find_element(*self.Setting).click()
    
    def click_ConditionsSection(self,date):
        self.ConditionSection = (By.CSS_SELECTOR,self.ConditionSection_path %(date))
        self.find_element(*self.ConditionSection).click()
        
    def select_ConditionSectionKPI(self,date,sectionindex):
        if sectionindex == "Coaching":
            self.ConditionSectionKPI = (By.CSS_SELECTOR,self.Coachingespecial_path % (date,sectionindex))
        else:
            self.ConditionSectionKPI = (By.CSS_SELECTOR,self.ConditionSectionKPI_path % (date,sectionindex))
        self.find_element(*self.ConditionSectionKPI).click()
        
    def click_ConditionCondition(self,date):
        self.CoditionsCondition = (By.CSS_SELECTOR,self.CoditionsCondition_path % (date))
        self.find_element(*self.CoditionsCondition).click()
    
    def click_ConditionConditionKPI(self,date,conditionKPI):
        self.ConditionsConditionsKPI = (By.CSS_SELECTOR,self.ConditionsConditionsKPI_path % (date,conditionKPI))
        self.find_element(*self.ConditionsConditionsKPI).click()
    
    def click_ConditionRelationship(self,date):
        self.ConditionsRelationship = (By.CSS_SELECTOR,self.ConditionsRelationship_path % (date))
        self.find_element(*self.ConditionsRelationship).click()
    
    def click_ConditionRelationshipSelect(self,date,relationshipindex):
        self.ConditionsRelationshipSelect = (By.CSS_SELECTOR,self.ConditionsRelationshipSelect_path % (date,relationshipindex))
        self.find_element(*self.ConditionsRelationshipSelect).click()
        
    def input_ConditionTarget(self,date,target):
        self.ConditionsTarget = (By.CSS_SELECTOR,self.ConditionsTarget_path % (date))
        self.Input_text(target,*self.ConditionsTarget)
        
    def input_ConditionPoints(self,date,points):
        self.ConditionsPoints = (By.CSS_SELECTOR,self.ConditionsPoints_path % (date))
        self.Input_text(points,*self.ConditionsPoints)
    
    def click_addsetting(self,date):
        self.Conditionadd = (By.CSS_SELECTOR,self.Conditionadd_path % (date))
        self.find_element(*self.Conditionadd).click()
        
    #Nabigate to the Gamification module
    def enter_GamificationPointSetting(self):
        self.click_GimficationPoint()
        self.click_Setting()

    #Get Condition info
    def get_setConditionData(self,date,length):
        if date == "DAILY":
            data = 2
        elif date == "WEEKLY":
            data = 4
        elif date == "MONTHLY":
            data = 6
        i = 1
        con = (By.CSS_SELECTOR,self.Conditioninfo_path % (data,i))
        while self.Element_displayed(*con) == True:   
            i = i + 1
            Conditioninfo = self.find_element(*con).text
            con = (By.CSS_SELECTOR,self.Conditioninfo_path % (data,i))
            Conditioninfolist = Conditioninfo.split(" Edit")[0]
        Conditionlist = Conditioninfolist.split(" ")[-length:]
        return Conditionlist

            
    #Set  Condition
    def set_Conditions(self,sectionindex,conditionKPI,relationshipindex,target,points,date):
        #Set Section
        self.click_ConditionsSection(date)
        if date == "Coaching":
            self.select_ConditionSectionKPI(date, sectionindex)
        else:
            self.select_ConditionSectionKPI(date,sectionindex)
        time.sleep(Gl.waittime)
        #Set Condition
        self.click_ConditionCondition(date)
        self.click_ConditionConditionKPI(date,conditionKPI)
        time.sleep(Gl.waittime)
        #Set Relationship
        self.click_ConditionRelationship(date)
        self.click_ConditionRelationshipSelect(date,relationshipindex)
        time.sleep(Gl.waittime)
        #Set target and points
        self.input_ConditionTarget(date,target)
        self.input_ConditionPoints(date,points)
        #Add set condition
        self.click_addsetting(date)
        #refresh window
        self.refresh_window()
        
        #get value of expected
        expected = conditionKPI.split(" ")
        expected.append(relationshipindex)
        if expected[1] == "%":
            targetfloat = "%.2f" % float(target)
            expected.append(str(targetfloat)+"%")
        else:
            expected.append(target)
        expected.append(points)
        length = len(expected)
        return expected,length
    
    #the method of assert
    def assert_SetCondition(self,date,expected,length):
        actual = self.get_setConditionData(date,length)
        assert expected == actual
        print("%s conditions set successful!"%(date))



        
    

        
        
        