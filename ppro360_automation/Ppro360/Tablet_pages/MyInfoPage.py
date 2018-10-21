from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class MyInfoPage(BasePage.Action):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.PersonalInfo_loc = (By.CSS_SELECTOR,'#container div section div div.fixed-left-200 div div:nth-child(1) a')
        self.PointsHistoryButton_loc = (By.CSS_SELECTOR,'#container div section div div.fixed-left-200 div div:nth-child(2) a')
        self.TitleMyInfoPosition = (By.CSS_SELECTOR,'#container div nav div span')
        self.TabletColunms_path = '#container div section div div.fixed-main div table thead tr th:nth-child(%d)'
        self.PointsHistroy_path = '#container div section div div.fixed-main div table tbody tr:nth-child(%d) td:nth-child(%d)'
    
    def click_PointsHistory(self):
        self.find_element(*self.PointsHistoryButton_loc).click()
        
    def get_ColorofPersonalInfo(self):
        element_color = self.find_element(*self.PersonalInfo_loc)
        colorRGB = element_color.value_of_css_property('color')
        return colorRGB
    
    def get_ColorofPointsHistory(self):
        element_color = self.find_element(*self.PointsHistoryButton_loc)
        colorRGB = element_color.value_of_css_property('color')
        return colorRGB
    
    def get_TitleMyInfoPosition(self):
        element_position = self.find_element(*self.TitleMyInfoPosition)
        titlePosition = element_position.value_of_css_property('text-align')
        return titlePosition
    
    def get_TabletColunms(self):
        index = 1
        TabletColunms_list=[]
        TabletColunms = (By.CSS_SELECTOR,self.TabletColunms_path % index)
        while self.Element_displayed(*TabletColunms) == True:
            TabletColunms_list.append(self.find_element(*TabletColunms).text)
            index = index + 1
            TabletColunms = (By.CSS_SELECTOR,self.TabletColunms_path % index)
        return TabletColunms_list
    
    def get_PointHistoryTablet(self):
        index = 1
        PointsHistory_list=[]
        pointshistory_loc = (By.CSS_SELECTOR,self.PointsHistroy_path % (index,1))
        while self.Element_displayed(*pointshistory_loc) == True:
            subindex = 1
            PointsHistory = []
            while self.Element_displayed(*pointshistory_loc) == True:
                PointsHistory.append(self.find_element(*pointshistory_loc).text)
                subindex = subindex + 1
                pointshistory_loc = (By.CSS_SELECTOR,self.PointsHistroy_path % (index,subindex))
            PointsHistory_list.append(PointsHistory)
            index = index + 1
            pointshistory_loc = (By.CSS_SELECTOR,self.PointsHistroy_path % (index,1))
        PointsHistory_list=sorted(PointsHistory_list)
        return PointsHistory_list