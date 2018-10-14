# 所有接口测试基类，提供基本结构
from interface_test_common import read_test_case_data
from openpyxl import Workbook
import time

class InterfaceMainTest(object):
    '''
    此类为接口测试基类，定义接口测试时的结构模型
    '''
    def __init__(self):
        # 总数据变量
        self.test_data = []
        # 用例编号及参数位置
        self.case_number = ""
        self.case_number_pos = None
        # 头部信息及参数位置
        self.headers = {}
        self.headers_param = []
        self.headers_pos = []
        # 正文数据及参数位置
        self.datas = {}
        self.datas_param = []
        self.datas_pos = []
        # 截取开始标签及参数位置
        self.start_tag = ""
        self.start_tag_pos = None
        # 截取结束标签及参数位置
        self.end_tag = ""
        self.end_tag_pos = None
        # 期望结果及参数位置
        self.expect_result = ""
        self.expect_result_pos = None
        # 测试执行结果及参数位置
        self.test_result = ""
        self.test_result_pos = None
        # 备注说明及参数位置
        self.remark = ""
        self.remark_pos = None
        # 实例化一个Excel对象
        self.wb = Workbook()
        # 找到当前活动的sheet
        self.sheet = self.wb.active
    
    def do_test(self,file_path,test_function,**dynamic_dict):
        '''
        此方法提供执行测试动作的功能
        参数说明：
        file_path:数据文件所在位置
        test_function:测试时的方法，也就是接口测试正文内容
        **dynamic_dict:可变形参，动态传入关于header的方法和参数内容，和关于data的方法和参数内容
                                                                    方法名、参数列表、数据文件中的位置三者顺序必须一致！！！！
                                    测试方法补充参数列表：'test_parameter_list'=[arg1,arg2,....]                        
                                    头部内容：'header_function_list'=[fun1,fun2,fun3,...],'header_parameter_list'=[[arg1,arg2,arg3,...],[arg1,arg2,arg3,...],...]
                                            方法名列表：[fun1,fun2,fun3,...]
                                            参数列表：[[arg1,arg2,arg3,...],[arg1,arg2,arg3,...],...]
                                    数据内容：'data_function_list'=[fun1,fun2,fun3,...],'data_parameter_list'=[[arg1,arg2,arg3,...],[arg1,arg2,arg3,...],...]
                                            方法名列表：[fun1,fun2,fun3,...]
                                            参数列表：[[arg1,arg2,arg3,...],[arg1,arg2,arg3,...],...]                   
        '''
        # 读取测试数据
        data_dict = read_test_case_data(file_path)
        print("data_dict列表的值为：{}".format(data_dict))
        param_list = data_dict.get('param_list')
        total_list = data_dict.get('total_list')
        print("param_lsit列表的值为：{}".format(param_list))
        print("total_list列表的值为：{}".format(total_list))
        # 解析数据，计算接口测试模型中各属性的位置
        for param in param_list:
            # 得到元素在列表中的位置
            pos = param_list.index(param)
            # 得到用例编号的位置
            if "用例编号" == param:
                self.case_number_pos = pos
            # 得到头部信息
            if "头部：" in param:
                self.headers_pos.append(pos)
                # 得到头部参数名字
                value = param.split("头部：")[1]
                self.headers_param.append(value)
                # 中断后续判断，继续寻找
                continue
            # 得到参数信息
            if "参数：" in param:
                self.datas_pos.append(pos)
                # 得到数据参数名字
                value = param.split("参数：")[1]
                self.datas_param.append(value)
                # 中断后续判断，继续寻找
                continue
            # 得到截取开始标签位置
            if "截取开始标签" == param:
                self.start_tag_pos = pos
            # 得到截取结束标签位置
            if "截取结束标签" == param:
                self.end_tag_pos = pos
            # 得到预期结果位置
            if "预期结果" == param:
                self.expect_result_pos = pos
            # 得到执行结果位置
            if "执行结果" == param:
                self.test_result_pos = pos
            # 得到备注的位置
            if "备注" == param:
                self.remark_pos = pos
        print("self.headers_pos的值为：{}".format(self.headers_pos))
        print("self.headers_param的值为：{}".format(self.headers_param))
        print("self.datas_pos的值为：{}".format(self.datas_pos))
        print("self.datas_param的值为：{}".format(self.datas_param))
        # 根据位置，开始循环进行测试
        for data_list in total_list:
            print("data_list的值为：{}".format(data_list))
            # 初始化各参数的值，主要是为头部和参数部分赋值判断时提供基础，后面如果已经存在值则不赋值
            self.init_parameter()
            # 得到用例编号
            self.case_number = data_list[self.case_number_pos]
            self.test_data.append(self.case_number)
            print("self.case_number信息的值为：{}".format(self.case_number))
            # 循环拼接头部内容，以得到头部信息
            for header_pos in self.headers_pos:
                # 取到此时头部的位置，然后取出数据列表中对应的值
                temp_pos = self.headers_pos.index(header_pos)
                header_param = self.headers_param[temp_pos]
                header_value = data_list[header_pos]
                print("header_value信息的值为：{}".format(header_value))
                # 如果头部值是动态内容，则会调用动态方法，否则则使用固定值
                if "*动态*" == header_value:
                    # 先判断头部是否已经赋值，若未赋值则调用函数处理
                    if self.headers.get(header_param) == None :
                        # 先获取到动态字典中头部方法的列表，并找到对应的头部方法
                        header_function_list = dynamic_dict.get('header_function_list')
                        header_function = header_function_list[temp_pos]
                        # 找到对应的参数
                        header_parameter_list = dynamic_dict.get('header_parameter_list')
                        header_parameter = header_parameter_list[temp_pos]
                        # 进行调用,并取得返回值
                        header_value = header_function(*header_parameter)
                        # 对返回值进行判断，如果返回的是字符串则直接赋值，如果返回的是字典，则需另外处理
                        if type(header_value) is str :
                            # 存入参数列表中
                            self.headers[header_param] = header_value
                        elif type(header_value) is dict :
                            # 如果是字典，则需要解析
                            header_dict = header_value["header"]
                            datas_dict = header_value["data"]
                            # 循环进行处理，如果data或header中参数未赋值则进行赋值，如果已经赋值则不处理
                            for header in header_dict.keys():
                                # 头部参数有值则不会修改，无值则修改
                                self.headers.setdefault(header,header_dict.get(header))
                            for data in datas_dict.keys():
                                # 正文参数同理
                                self.datas.setdefault(data,datas_dict.get(data))
                        else:
                            raise TypeError("do_test中使用头部方法返回类型不正确！！！")
                else:
                    # 否则就按固定值处理
                    self.headers[header_param] = header_value
            self.test_data.append(self.headers)
            print("self.headers信息的值为：{}".format(self.headers))
            # 循环拼接参数部分，以得到参数信息
            for data_pos in self.datas_pos:
                # 取到此时头部的位置，然后取出数据列表中对应的值
                temp_pos = self.datas_pos.index(data_pos)
                data_param = self.datas_param[temp_pos]
                data_value = data_list[data_pos]
                # 如果头部值是动态内容，则会调用动态方法，否则则使用固定值
                if "*动态*" == data_value:
                    # 先判断参数是否已经赋值，若未赋值则调用函数赋值
                    if self.datas.get(data_param) == None :
                        # 先获取到动态字典中头部方法的列表，并找到对应的头部方法
                        data_function_list = dynamic_dict.get('data_function_list')
                        data_function = data_function_list[temp_pos]
                        # 找到对应的参数
                        data_parameter_list = dynamic_dict.get('data_parameter_list')
                        data_parameter = data_parameter_list[temp_pos]
                        # 进行调用,并取得返回值
                        data_value = data_function(*data_parameter)
                        # 存入参数列表中
                        self.datas[data_param] = data_value
                else:
                    # 否则就按固定值处理
                    self.datas[data_param] = data_value
            self.test_data.append(self.datas)
            # 得到截取开始标签信息
            self.start_tag = data_list[self.start_tag_pos]
            self.test_data.append(self.start_tag)
            # 得到截取结束标签信息
            self.end_tag = data_list[self.end_tag_pos]
            self.test_data.append(self.end_tag)
            # 得到预期结果信息
            self.expect_result = data_list[self.expect_result_pos]
            self.test_data.append(self.expect_result)
            # 得到执行结果信息
            self.test_result = data_list[self.test_result_pos]
            self.test_data.append(self.test_result)
            # 得到备注信息
            self.remark = data_list[self.remark_pos]
            self.test_data.append(self.remark)
            print("self.test_data测试数据为：{}".format(self.test_data))
            # 调用测试方法完成测试，并进行异常捕捉，出现异常则记录信息
            try:
                # 得到补充的测试参数列表
                test_parameter_list = dynamic_dict.get('test_parameter_list')
                # 如果test_parameter_list为空
                if test_parameter_list == None:
                    # 默认传参方式传递
                    result = test_function(self.datas,self.headers,self.start_tag,self.end_tag,self.expect_result)
                else:
                    # 包括其他参数，则按元组解包赋值
                    result = test_function(self.datas,self.headers,self.start_tag,self.end_tag,self.expect_result,*test_parameter_list)
                # 如果测试结果不为True则均为不正常
                if result is True:
                    # 结果成功
                    self.test_result = "执行成功"
                    data_list[self.test_result_pos] = self.test_result
                else:
                    # 结果失败
                    data_list[self.test_result_pos] = "执行失败"
                    raise AssertionError("执行结果跟期望结果不一致，期望结果为{}，实际结果为{}".format(self.expect_result,result))
            except AssertionError as ae:
                data_list[self.remark_pos] = str(ae)[:32000]
            except Exception as e:
                # 执行测试出现异常，则抛出异常
                data_list[self.test_result_pos] = "执行异常"
                data_list[self.remark_pos] = str(e)[:32000]
                print("执行测试时，出现异常了，异常信息为{}".format(str(e)))
            # 测试完成后，开始记录测试结果，先得到列数字母
            col_list = self.get_col_list(param_list)
            print("测试完成后，data_list的值为：{}".format(data_list))
            # 循环写表头
            for col in col_list:
                self.sheet[col+'1'] = param_list[col_list.index(col)]
            # 循环进行赋测试用例的值
            for col in col_list:
                pos = total_list.index(data_list)+2
                self.sheet[col+str(pos)] = data_list[col_list.index(col)]
        # 测试完成保存，Excel文件
        report_path = self.get_report_excel(file_path)
        self.wb.save(report_path)
    
    def get_col_list(self,param_lsit):
        # 得到由大写字母组成的列表，对于测试数据的列而言应该够了
        col_list = []
        param_lsit_length = len(param_lsit)
        # 循环取出列所在位置
        for i in range(65, 65+param_lsit_length):
            col_list.append(chr(i))
        # 返回列表
        return col_list
    
    def get_report_excel(self,file_path):
        # 得到报告文件
        file_name = file_path.split("/")[-1]
        pos = file_name.find(".")
        # 得到时间名字
        time_str = time.strftime("%Y-%m-%d %H%M%S",time.localtime())
        report_path = "../result/"+file_name[:pos]+time_str+file_name[pos:]
        # 返回报告文件路径
        return report_path
        
    def init_parameter(self):
        # 初始化参数的值
        # 总数据变量
        self.test_data = []
        # 用例编号及参数位置
        self.case_number = ""
        # 头部信息及参数位置
        self.headers = {}
        # 正文数据及参数位置
        self.datas = {}
        # 截取开始标签及参数位置
        self.start_tag = ""
        # 截取结束标签及参数位置
        self.end_tag = ""
        # 期望结果及参数位置
        self.expect_result = ""
        # 测试执行结果及参数位置
        self.test_result = ""
        # 备注说明及参数位置
        self.remark = ""
        
if __name__ == "__main__":
    main = InterfaceMainTest()
    col_list = main.get_col_list([1,2,3,4,5,6,7,8,9,10])  
    print(col_list)         
            
            