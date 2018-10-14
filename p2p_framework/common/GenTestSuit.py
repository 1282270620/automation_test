'''
Created on 2018年7月9日
@author: Administrator
'''
import unittest,os

def gen_test_suit(pattern):
    #定义测试套件
    testunit = unittest.TestSuite()
    #测试报告输入路径
    test_dir = os.path.join(os.path.dirname(os.path.abspath('.')),"testScripts")
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern=pattern, top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit
