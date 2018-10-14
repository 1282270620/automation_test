'''
Created on 2018年6月28日
@author: Administrator
'''
from pageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from utils.mysql import get_verifycode
import os

'''
    发布抵押标页面元素定位，及相关页面元素操作，继承BasePage基类
'''

class PledgePage(BasePage):
    myloan_page = (By.XPATH,"/html/body/div[1]/div/div/div/ul/li[3]/a")    #我要借款元素定位    
    release_mortgage = (By.XPATH,"/html/body/div[1]/div/div/div/ul/li[3]/ul/li[2]/a")       #发布抵押标元素定位
    title = (By.XPATH,".//input[@class='span3']")     #标题元素定位
    annual_interest_rate = (By.XPATH,".//input[@class='span1']")      #年利率元素定位
    usage_of_loan = (By.XPATH,".//select[@class='span2' and @name='use']")     #借款用途元素定位
    statistical_unit = (By.XPATH,".//*[@id='uniform-undefined']/span")     #统计单位元素定位
    term_of_loan = (By.ID,"deadline")       #借款期限元素定位
    repayment_menthod = (By.XPATH,".//select[@class='span2' and @name='way']")      #还款方式元素定位
    effective_time = (By.XPATH,".//select[@name='valid']")      #有效时间元素定位
    password_state = (By.XPATH,".//*[@id='uniform-undefined']/span")        #密码状态元素定位
    passwd_state_close = (By.XPATH,".//td/label[1]/div[@id='uniform-undefined']/span")      #密码状态关元素定位
    passwd_state_open = (By.XPATH,".//td/label[2]/div[@id='uniform-undefined']/span")       #密码状态开元素定位
    password = (By.XPATH,".//*[@id='pass']")        #密码输入框元素定位
    minimum_bids = (By.XPATH,".//select[@name='min']")      #最低投标金额元素定位
    maximize_bids = (By.XPATH,".//select[@name='max']")      #最高投标金额元素定位
    loan_amount = (By.XPATH,".//input[@name='money']")      #借款金额元素定位
    bid_award_none = (By.XPATH,".//td/label[@class='radio']/div/span")     #投标奖项元素定位(无)
    bid_award_quota = (By.XPATH,".//div[1]/label[@class='radio']/div/span")       #投标奖励元素定位(按奖金额奖励)
    bid_award_num = (By.XPATH,".//*[@id='reward_1']")       #投标奖金额度输入框定位
    bid_award_proportion = (By.XPATH,".//div[2]/label[@class='radio']/div/span")        #投标奖励元素定位(按奖金比例奖励)
    bid_award_proport = (By.XPATH,".//*[@id='reward_1']")       #投标奖金比例输入框
    data_uploading= (By.XPATH,".//*[@id='file_goods']")     #资料上传元素定位
    frame_content = (By.CLASS_NAME,"ke-content")        #纤细说明输入框元素定位
    verify_code = (By.XPATH,"html/body/div[3]/div/form/div[2]/input")       #验证码输入框元素定位
    confirm_submit = (By.XPATH,"/html/body/div[3]/div/form/div[2]/button")     #确认提交
    login_out = (By.XPATH,"/html/body/div[1]/div/div/div/ul/li[10]/a")      #退出元素定位
    
    #切换到我要借款/发布抵押标
    def into_myloan(self):
        self.click(self.myloan_page)
        self.log.info("--进入我要借款页面")
        self.click(self.release_mortgage)
        self.log.info("--进入发布抵押标页面")
        
    #定位输入框，输入内容
    def send_content(self,title,interest_rate,loan_amount):
        self.input_values(self.title, title)      #输入主题内容
        self.log.info("--输入主题内容")
        self.input_values(self.annual_interest_rate,interest_rate)   #输入年利率  
        self.log.info("--输入年利率")
        self.input_values(self.loan_amount,loan_amount)     #输入借款金额
        self.log.info("--输入借款金额")
#        self.input_values("html",detail_description)       #输入详细说明

    #选择下拉选项option
    def select_option(self, usage_value, term_value, repay_value, effe_value, min_value, max_value):
        self.select_list(self.usage_of_loan, usage_value)     #选择借款用途
        self.log.info("--选择借款内容")
        self.select_list(self.term_of_loan,term_value)      #选择借款期限
        self.log.info("--选择借款类型")
        self.select_list(self.repayment_menthod, repay_value)        #选择还款方式
        self.log.info("--选择还款类容")
        self.select_list(self.effective_time, effe_value)       #选择有效时间
        self.log.info("--选择有效时间")
        self.select_list(self.minimum_bids, min_value)      #选择最低投标金额
        self.log.info("--选择最低投标金额")
        self.select_list(self.maximize_bids, max_value)     #选择最高投标金额
        self.log.info("--选择最高投标金额")
    #选择密码标状态
    def passwd_status(self, option, passwd):
        if option == "关":
            self.click(self.passwd_state_close)
            self.log.info("--密码状态：关")
        else:
            self.click(self.passwd_state_open)
            self.input_values(self.password, passwd)
            self.log.info("--密码状态：开，并输入密码")
    #选择投标奖励选项
    def  operate_bidaward(self, option, quota, proportion):
        if option == "无":
            self.click(self.bid_award_non)
            self.log.info("--投标奖励：无")
        elif option == "比例":
            self.click(self.bid_award_quota)
            self.input_values(self.bid_award_num, quota)
            self.log.info("--投标奖励：按比例奖励")
        else:
            self.click(self.bid_award_proportion)
            self.input_values(self.bid_award_proport, proportion)
            self.log.info("--投标奖励，按金额奖励")
    def input_frame(self,para = "阿什顿发嗲建立开放的时刻"):
        self.switchframe()
        self.input_values(self.frame_content, para)
        self.switchdefault()
    def input_verifycode(self,driver):
        cookie_list = driver.get_cookies()
        sessID = driver.get_cookie("PHPSESSID")
        verify_code = get_verifycode(sessID["value"])
        self.input_values(self.verify_code,verify_code)
        self.log.info("--获取并输入验证码")
    def submit_pledge(self):
        self.click(self.confirm_submit)
        self.log.info("--点击“确认投标”按钮")
    def logon_out(self):
        self.click(self.login_out)
        self.log.info("--点击“退出”按钮")
