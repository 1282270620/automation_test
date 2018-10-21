from Tablet_pages import BasePage
from selenium.webdriver.common.by import By

class Satisfaction_Page(BasePage.Action):
    def __init__(self):
        self.info = []
        self.Name_AverageRate = (By.XPATH,'//*[@id="container"]/div/section/div/table/tbody')
        self.overall_average = (By.XPATH,'//*[@id="container"]/div/section/div/h3[1]')

    def Get_allavrageRate(self):
        if self.find_element(*self.Name_AverageRate) == None:
            return self.info
        else:
            content = self.find_element(*self.Name_AverageRate).text
            print 'content:',content
            self.info = content.split("\n")
            return self.info
    def Get_overall_average(self):
        print 'self.overall_average:',self.overall_average
        OverallAverageofmysite = self.find_element(*self.overall_average).text
        Overall = OverallAverageofmysite.split(':')[1]
        return Overall