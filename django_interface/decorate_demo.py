'''import unittest,time
import ddt
from selenium import webdriver

def method_test(func):
    for i in range(2):
        try:
            print("method_test")
            obj = func()
            print(dir(obj))
            obj.setUp()
            obj.test_demo()
            obj.tearDown()
        except exception:
            print("e") 
    
@method_test
class demo_test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        time.sleep(3)
        print("setUp")
    def tearDown(self):
        self.driver.quit()
        print("tearDown")
    def test_demo(self):
        self.assertEqual(1,2)
        print("test_demo")


import unittest,paramunittest,time
@paramunittest.parametrized(
    {"user": "admin", "psw": "123", "result": "true"},
    {"user": "admin1", "psw": "1234", "result": "true"},
    {"user": "admin2", "psw": "1234", "result": "true"},
    {"user": "admin3", "psw": "1234", "result": "true"},
    {"user": "admin4", "psw": "1234", "result": "true"},
    {"user": "admin5", "psw": "1234", "result": "true"},
    {"user": "admin6", "psw": "1234", "result": "true"},
    {"user": "admin7", "psw": "1234", "result": "true"},
    {"user": "admin8", "psw": "1234", "result": "true"},
    {"user": "admin9", "psw": "1234", "result": "true"},
    {"user": "admin10", "psw": "1234", "result": "true"},
    {"user": "admin11", "psw": "1234", "result": "true"},
)

class TestDemo(unittest.TestCase):
    def setParameters(self, user, psw, result):
        #这里注意了，user, psw, result三个参数和前面定义的字典一一对应
        print(user,psw,result)
        self.user = user
        self.psw = psw
        self.result = result

    def testcase(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("期望结果：%s " % self.result)
        time.sleep(0.5)
        self.assertTrue(self.result == "true")
'''
'''
# _*_ coding:utf-8 _*_
import csv,unittest #导入csv模块
from time import sleep
from selenium import webdriver
from parameterized import parameterized, param#导入parameterized
class baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#类中最先执行
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()  # 最大化窗口
        cls.driver.implicitly_wait(10)  # 隐式等待
    @classmethod
    def tearDownClass(cls): #类中最后执行
        cls.driver.quit()

    #开始使用parameterized
    @parameterized.expand([
        ("selenium","selenium_百度搜索"), #此处为file.csv中的数据
        ("selenium2","selenium2_百度搜索"),
        ("selenium3","selenium3_百度搜索"),
        ("webdriver","webdriver_百度搜索"),
    ])
    def test_search(self,search_str,assrt_str):#接收上面的两个参数'''
# _*_ coding:utf-8 _*_
import unittest #导入csv模块
from time import sleep
from selenium import webdriver
from parameterized import parameterized, param#导入parameterized
param_test = [
        {"selenium","selenium_百度搜索"}, #此处为file.csv中的数据
        {"selenium2","selenium2_百度搜索"},
        {"selenium3","selenium3_百度搜索"},
        {"webdriver","webdriver_百度搜索"},
    ]
class baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#类中最先执行
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()  # 最大化窗口
        cls.driver.implicitly_wait(10)  # 隐式等待
    @classmethod
    def tearDownClass(cls): #类中最后执行
        cls.driver.quit()

    #开始使用parameterized
    @parameterized.expand(param_test)
    def test_search(self,search_str,assrt_str):#接收上面的两个参数
        print("测试开始拉----------")
        print(search_str,assrt_str)
        print("测试结束-----------")
        self.assertNotEqual(search_str,assrt_str)
if __name__ == "__main__": #如果直接执行将执行以下代码，调用不执行以下代码
    unittest.main()

