'''
Created on 2018年7月9日
@author: Administrator
'''
from common.GenTestSuit import gen_test_suit
from utils.HTMLTestRunner import HTMLTestRunner
import time,os

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%M")
    reportpath = os.path.join(os.path.dirname(os.path.abspath(".")),"report",now+"_result.html")
    suite = gen_test_suit("test*.py")
    fp = open(reportpath,"wb")
    runner = HTMLTestRunner(stream=fp, title="p2p网项目自动化测试报告", description="自动化脚本执行情况")
    runner.run(suite)
    fp.close()