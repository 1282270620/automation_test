'''
Created on 2018年6月28日
@author: Administrator
'''
from selenium.webdriver.common.by import By
from pageObject.BasePage import BasePage
from selenium import webdriver

'''
    登录功能封装，继承BasePage基类
'''

class LoginPage(BasePage):
    #前端登录元素定位
    login_username = (By.XPATH,".//input[@name='username']")    #账户输入框元素定位
    login_passwd = (By.XPATH,".//input[@name='password']")      #用户密码输入框元素定位
    login_submit = (By.XPATH,"/html/body/div[3]/form/div[4]/div/button")
    loc_button = (By.XPATH,".//div[@class='controls']/p[2]/button")       #登录按钮元素定位
    verifycode_loc = (By.XPATH,"/html/body/div[3]/div/div/div[1]/form/div[3]/div/label[1]/input")     #输入验证码    
    sign_in = (By.XPATH,".//a[@href='/Logo/login.html']")       #登陆界面元素定位
    click_verifycode = (By.XPATH,".//*[@id='verifyImg']")
    #后端登录元素定位
    logon_username = (By.XPATH,".//input[@name='name']")       #后台管理员账号元素定位
    logon_passwd = (By.XPATH,"html/body/div[2]/div/form/fieldset/div[3]/input")     #后台管理员密码元素定位
    verifycode_logon = (By.XPATH,"html/body/div[2]/div/form/fieldset/div[5]/input")     #后台验证码元素定位
    logon_botton = (By.XPATH,"html/body/div[2]/div/form/fieldset/p/button")      #登录按钮元素定位
    #前端登录功能
    def login_function(self, username, password):
        self.input_values(self.login_username, username)
        self.input_values(self.login_passwd, password)
        self.log.info("--输入用户名和密码")
        self.click(self.login_submit)
        self.log.info("--点击前端登陆，直接登陆")
    def into_login(self):
        self.click(self.sign_in)
        self.log.info("--点击登陆，进入登陆页面")
    def loc_function(self, username, password):
        self.input_values(self.login_username, username)
        self.input_values(self.login_passwd, password)
        self.log.info("--登录页面输入用户名和密码")
    def input_verifycode(self,verifycode):
        self.input_values(self.verifycode_loc, verifycode)
        self.log.info("--输入验证码")
        self.click(self.loc_button)
        self.log.info("--点击登陆按钮，用户登陆")
    #后端登录功能
    def logon_function(self, username, passwd):
        self.input_values(self.logon_username,username)
        self.input_values(self.logon_passwd,passwd)
        self.log.info("--后端管理员登陆页面，输入用户名和密码")
    def logon_verifycode(self, verifycode):
        self.input_values(self.verifycode_logon, verifycode)
        self.log.info("--后端页面，输入验证码")
        self.click(self.logon_botton)
        self.log.info("--点击后端登陆按钮")
if __name__ == "__main__":
    driver = webdriver.Firefox()
    LO = LoginPage(driver,"http://172.31.31.111")
    LO.open()
    LO.loc_function("admin","123456")
    LO.input_verifycode("1111")

    