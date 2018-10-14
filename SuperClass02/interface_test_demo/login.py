'''
Created on 2018年4月15日

@author: Administrator
'''
import unittest
from interface_test_common import HTTPRequest,get_verify_code,get_ipinfo
from interface_test_common import InterfaceMainTest

class TestLogin(unittest.TestCase):
    # 定义类属性，用于保存验证码和session
    session = ""
    verify_code = ""

    def setUp(self):
        # 读取配置文件中的ip和端口信息
        ipinfo = get_ipinfo()
        # 实例化一个HTTP请求类
        self.hr = HTTPRequest()
        # 登录地址
        self.url = ipinfo+"/index.php/Logo/loging"
     
    def test_main(self):
        # 定义测试数据文件所在路径
        file_path = "../data/"+self.__class__.__name__+".xlsx"
        # 定义头部相关函数列表
        header_function_list = [get_verify_code]
        # 定义头部函数相关参数列表（二层列表）
        header_parameter_list=[[self.hr]]
        # 实例化主测类，并调用do_test方法执行测试
        main = InterfaceMainTest()
        # do_test方法第一个参数为数据文件地址，第二个参数为字典形式的可变形参
        main.do_test(file_path,self.login,header_function_list=header_function_list,
                     header_parameter_list=header_parameter_list)
        
        # 定义test_function,标准为5个参数：data,headers,start_tag,end_tag,expect_result 
        # 除此之外的参数往后放，按元组解包方式传参，且调用do_test方法时需指定test_parameter_list的值（列表）
    def login(self,data,headers,start_tag,end_tag,expect_result): 
        # 调用POST方法发送请求
        reponse = self.hr.http_post(self.url,data,headers)
        # 调用检查结果的方法
        result = self.hr.check_result(reponse, start_tag, end_tag, expect_result)
        # 返回测试结果
        return result


# if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#     lo = TestLogin()
#     lo.setUp()
#     data = {'username': 'test01', 'proving': '1940', 'password': 123456}
#     headers = {'Cookie': 'PHPSESSID=124efoufjviauu227qspd6brg7'}
#     start_tag = '<p class="green">'
#     end_tag = '</p>'
#     expect_result = '用户登录成功'
#     lo.login(data, headers, start_tag, end_tag, expect_result)