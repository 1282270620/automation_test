'''
Created on 2018年4月15日

@author: Administrator
'''
import unittest
from interface_test_common import HTTPRequest

class TestIndex(unittest.TestCase):

    def setUp(self):
        # 实例化一个HTTP请求类
        self.hr = HTTPRequest()
        # 首页地址
        self.url = "http://192.168.0.102/"

    def test01(self):
        # 调用方法，访问首页
        response = self.hr.http_get(self.url)
        print(response)
        self.assertTrue('<a href="/Loan.html">我要投资</a>' in response)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()