'''
Created on 2017.6.28

@author: yalan.yin
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class ISMAgentWeeklyPerformanceReviewPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CallRecordingNumber_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/input')
        self.Feedback_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[6]/div[1]/textarea')
        self.OverallPerformanceScore_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[1]/input')
        self.WPRStatus_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[2]/div/span')
    
    def click_KPIcheckbox (self, checkboxorder):
        self.KPIcheckbox_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i' %checkboxorder)
        self.find_element (*self.KPIcheckbox_loc).click()  
    
    def input_CallRecordingNumber (self, CallRecordingNumber):
        self.find_element(*self.CallRecordingNumber_loc).clear()
        self.find_element(*self.CallRecordingNumber_loc).send_keys(CallRecordingNumber)
        
    def input_Feedback (self, inputtext):
        self.find_element(*self.Feedback_loc).clear()
        self.find_element(*self.Feedback_loc).send_keys(inputtext)
    
    def get_OverallPerformanceScore (self):
        return self.find_element(*self.OverallPerformanceScore_loc).text
        
    def click_WPRStatus (self):
        self.find_element(*self.WPRStatus_loc).click()
        
        #WSDIndex (1, 17)
    def click_WPRStatusDropdown (self, WSDIndex):
        self.WPRStatusDropdown_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[5]/div[2]/div/ul/li[%d]/a' %WSDIndex)
        self.find_element(*self.WPRStatusDropdown_loc).click()
        
    def input_PerformanceWeight (self, PWIndex, inputnumber):
        self.PerformanceWeight_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[%d]/td[2]/div/input' %PWIndex)
        self.find_element(*self.PerformanceWeight_loc).clear()
        self.find_element(*self.PerformanceWeight_loc).send_keys(inputnumber)
        
    def input_OtherKPIWeight (self, OWIndex, inputnumber):
        self.OtherKPIWeight_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[%d]/td[2]/div/input' %OWIndex)
        self.find_element(*self.OtherKPIWeight_loc).clear()
        self.find_element(*self.OtherKPIWeight_loc).send_keys(inputnumber)
        
        #PSIndex(1, 4)
    def get_PerformanceScore (self, PSIndex):
        self.PerformanceScore_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[%d]/td[6]/input' %PSIndex)
        return self.find_element(*self.PerformanceScore_loc).text
        
        #OSIndex(1, 5)
    def get_OtherKPIScore (self, OSIndex):
        self.OtherKPIScore_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[1]/td[6]/input' %OSIndex)
        return self.find_element(*self.OtherKPIScore_loc).text
     
        #PGIndex(1, 4)
    def get_PerformanceToGoal (self, PGIndex):
        self.PerformanceToGoal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[%d]/td[5]/input' %PGIndex)
        return self.find_element(*self.PerformanceToGoal_loc).text
        
        #OGIndex(1, 5)
    def get_OtherKPIToGoal (self, OGIndex): 
        self.OtherKPIToGoal_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[%d]/td[5]/input' %OGIndex)
        return self.find_element(*self.OtherKPIToGoal_loc).text
             
        #PGIndex(1, 3, 4)
    def input_PerformanceWTDGoalCRFT (self, inputnumber):
        self.PerformanceWTDGoalexceptAHT_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[1]/td[3]/div/input')
        self.find_element(*self.PerformanceWTDGoalexceptAHT_loc).clear()
        self.find_element(*self.input_PerformanceWTDGoalexceptAHT_loc).send_keys(inputnumber)
        
    def input_PerformanceWTDGoalAHT (self, inputnumber):
        self.PerformaneWTDGoalAHT_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[2]/td[3]/input')
        self.find_element(*self.PerformaneWTDGoalAHT_loc).clear()
        self.find_element(*self.PerformaneWTDGoalAHT_loc).send_keys(inputnumber)
    def input_PerformanceWTDGoalR7 (self, inputnumber):
        self.PerformanceWTDGoalR7_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[3]/td[3]/div/input')
    
    def input_PerformanceWTDGoalAbsoluteAttendance (self, inputnumber):
        self.PerformanceWTDGoalAbsoluteAttendance_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[4]/td[3]/div/input')
        self.find_element(*self.PerformanceWTDGoalAbsoluteAttendance_loc).clear()
        self.find_element(*self.PerformanceWTDGoalAbsoluteAttendance_loc).send_keys(inputnumber)
        
    def input_OtherKPIWTDGoalSalesBB (self, inputnumber):
        self.OtherWTDGoalSalesBB_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[1]/td[3]/input')
        self.find_element(*self.OtherKPIWTDGoalSalesBB_loc).clear()
        self.find_element(*self.OtherKPIWTDGoalSalesBB_loc).send_keys(inputnumber)
    
    def input_OtherKPIWTDGoalSalesWireless (self, inputnumber):
        self.OtherKPIWTDGoalSalesWireless_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[2]/td[3]/input')
        self.find_element(*self.OtherKPIWTDGoalSalesWireless_loc).clear()
        self.find_element(*self.OtherKPIWTDGoalSalesWireless_loc).send_keys(inputnumber)
        
    def input_OtherKPIWTDGoalVOC (self, inputnumber):
        self.OtherKPIWTDGoalVOC_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[3]/td[3]/div/input')
        self.find_element(*self.OtherKPIWTDGoalVOC_loc).clear()
        self.find_element(*self.OtherKPIWTDGoalVOC_loc).send_keys(inputnumber)
    
    def input_OtherKPIWTDGoalTransfer (self, inputnumber):
        self.OtherKPIWTDGoalTransfer_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[4]/td[3]/div/input')
        self.find_element(*self.OtherKPIWTDGoalTransfer_loc).clear()
        self.find_element(*self.OtherKPIWTDGoalTransfer_loc).send_keys(inputnumber)
    
    def input_OtherKPIWTDGoalZTP (self, inputnumber):
        self.OtherKPIWTDGoalZTP_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[5]/td[3]/input')
        self.find_element(*self.OtherKPIWTDGoalZTP_loc).clear()
        self.find_element(*self.OtherKPIWTDGoalZTP_loc).send_keys(inputnumber)        
        
        
    def input_PerformanceActualScoreCRFT (self, inputnumber):
        self.PerformanceActualScoreCRFT_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[1]/td[4]/div/input')
        self.find_element(*self.PerformanceActualScoreCRFT_loc).clear()
        self.find_element(*self.PerformanceActualScoreCRFT_loc).send_keys(inputnumber)
        
    def input_PerformanceActualScoreAHT (self, inputnumber):
        self.PerformanceActualScoreAHT_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[2]/td[4]/input')
        self.find_element(*self.PerformanceActualScoreAHT_loc).clear()
        self.find_element(*self.PerformanceActualScoreAHT_loc).send_keys(inputnumber)
        
    def input_PerformanceActualScoreR7 (self, inputnumber):
        self.PerformanceActualScoreR7_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[3]/td[4]/div/input')
        self.find_element(*self.PerformanceActualScoreR7_loc).clear()
        self.find_element(*self.PerformanceActualScoreR7_loc).send_keys(inputnumber)
        
    def input_PerformanceActualScoreAbsoluteAttendance (self, inputnumber):
        self.PerformanceActualScoreAbsoluteAttendance_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/table/tbody/tr[4]/td[4]/div/input')
        self.find_element(*self.PerformanceActualScoreAbsoluteAttendance_loc).clear()
        self.find_element(*self.PerformanceActualScoreAbsoluteAttendance_loc).send_keys(inputnumber)
        
    def input_OtherKPIActualScoreSalesBB (self, inputnumber):
        self.OtherKPIActualScoreSalesBB_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[1]/td[4]/input')
        self.find_element(*self.OtherKPIActualScoreSalesBB_loc).clear()
        self.find_element(*self.OtherKPIActualScoreSalesBB_loc).send_keys(inputnumber)
        
    def input_OtherKPIActualScoreSalesWireless (self, inputnumber):
        self.OtherKPIActualScoreSalesWireless_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[2]/td[4]/input')
        self.find_element(*self.OtherKPIActualScoreSalesWireless_loc).clear()
        self.find_element(*self.OtherKPIActualScoreSalesWireless_loc).send_keys(inputnumber)
        
    def input_OtherKPIActualScoreVOC (self, inputnumber):
        self.OtherKPIAcutalScoreVOC_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[3]/td[4]/div/input')
        self.find_element(*self.OtherKPIAcutalScoreVOC_loc).clear()
        self.find_element(*self.OtherKPIAcutalScoreVOC_loc).send_keys(inputnumber)
        
    def input_OtherKPIActualScoreTransfer (self, inputnumber):
        self.OtherKPIActualScoreTransfer_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[4]/td[4]/div/input')
        self.find_element(*self.OtherKPIActualScoreTransfer_loc).clear()
        self.find_element(*self.OtherKPIActualScoreTransfer_loc).send_keys(inputnumber)
        
    def input_OtherKPIActualScoreZTP (self, inputnumber):
        self.OtherKPIActualScoreZTP_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[4]/div/table/tbody/tr[5]/td[4]/input')
        self.find_element(*self.OtherKPIActualScoreZTP_loc).clear()
        self.find_element(*self.OtherKPIActualScoreZTP_loc).send_keys(inputnumber)
        
    
    
        
        
        
        
        
        
        
        
    