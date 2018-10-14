'''
Created on 2018年7月2日
@author: Administrator
'''
from pageObject.BasePage import BasePage
from selenium.webdriver.common.by import By

class MyAccount(BasePage):
    my_account = (By.XPATH,"/html/body/div[1]/div/div/div/ul/li[5]/a")      #我的账户元素定位
    tender_loan = (By.XPATH,"/html/body/div[3]/div[1]/div[1]/dl[1]/dd[4]/a")        #我投标的借款元素定位
    per_page_display = (By.XPATH,"//*[@id='DataTables_Table_0_length']/label/select")   #每页显示数元素定位
    search = (By.XPATH,"//*[@id='DataTables_Table_0_filter']/label/input")      #搜索框元素定位
    title_content = (By.XPATH,".//*[@id='DataTables_Table_0']/tbody/tr/td[1]/a")     #标题元素定位 
    type_content = (By.XPATH,".//*[@id='DataTables_Table_0']/tbody/tr[1]/td[2]")     #类型元素定位
    row_content = (By.XPATH,"//*[@id='DataTables_Table_0']/tbody/tr/td[1]/a")
    def into_tender_loan(self):
        self.click(self.my_account)
        self.click(self.tender_loan)
        self.log.info("--进入我投标的借款页面")
    def search_tender_info(self,value):
        self.input_values(self.search,value)
        self.log.info("--搜索框中输入内容")
        title = self.find_element(self.title_content).text
        type = self.find_element(self.type_content).text
        content = title + type
        self.log.info("--返回我的投标借款内容")
        return content
    def get_info_bid(self):
        total = []
        bidder = []
        self.select_list(self.per_page_display, "100")
        title_ele = self.find_elements(self.row_content)
        row = len(title_ele)
        for i in range(1,row+1):
            loc = "//*[@id='DataTables_Table_0']/tbody/tr["+str(i)+"]/td"
            self.repay_info = (By.XPATH,loc)
            elements = self.find_elements(self.repay_info)
            repay_info = []
            flag = 0
            for element in elements:
                if flag == 0: 
                    repay_info.append(element.text)
                else:
                    break
                flag = flag + 1
            total.append(repay_info[0])
        self.log.info("--获取货款列表信息")
        total.sort()
        return total