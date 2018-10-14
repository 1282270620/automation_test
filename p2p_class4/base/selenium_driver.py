'''
Created on 2018年7月9日
@author: Administrator
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from base.read_config import get_browser_type,get_default_type
from base.read_config import get_timeout,get_default_speed,get_except_speed

class SeleniumDriver(object):
    def __init__(self,browser=None,type=None):
        # 检查浏览器的类型是否支持，若为空则直接使用默认浏览器
        self.check_browser(browser)
        # 得到webdriver
        self.driver = self.get_webdriver()
        # 设置相应的智能等待时间
        self.set_timeout()
        # 获取放慢速度
        if type is None:
            self.speed = get_default_speed()
        else:
            self.speed = get_except_speed()
    def set_timeout(self):
        timeout = get_timeout()
        # 设置元素识别超时时间
        self.driver.implicitly_wait(timeout)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout()
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout()
    def get_webdriver(self):
        # 根据浏览器的类型进行实例化，得到实例化后的对象
        if "chrome" == str.lower(self.browser):
            # 实例化Options对象，允许默认开启flash
            chromeOpitons = Options()
            prefs= {
                "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":1
            }
            chromeOpitons.add_experimental_option('prefs', prefs)
            driver = webdriver.Chrome(chrome_options=chromeOpitons)
        elif "firefox" == str.lower(self.browser):
            # 默认配置应该动态去获取（路径不变，文件名字可能会变）
            p = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\ff920jv6.default"
            profile = webdriver.FirefoxProfile(p)
            profile.set_preference("plugin.state.flash", 2)
            driver = webdriver.Firefox(profile) 
        elif "ie" == str.lower(self.browser):
            driver = webdriver.Ie()
        else:
            raise TypeError("获取驱动时，驱动类型未定义！！！")
        # 返回驱动变量
        return driver
    def check_browser(self):
        # 如果未指定浏览器的类型则从配置文件中读取浏览器的参数
        if browser:
            # 不为空，则需要判断是否支持该类型的浏览器
            browser = str.capitalize(browser)
            browser_type_list = get_browser_type()
            if browser in browser_type_list:
                self.browser = browser
            else:
                raise TypeError("不支持该类型的浏览器，请检查！！支持的浏览器类型为：{}".format(browser_type_list))            
        else:
            # 为空，则读取配置文件默认类型
            self.browser = get_defalut_browser()
    def open(self,base_url):
        # 调用webdriver真正相应的方法
        self.driver.get(base_url)  
        # 加个等待时间
        sleep(self.speed)
    def quit(self):
        # 调用webdriver真正相应的方法
        self.driver.quit()
        