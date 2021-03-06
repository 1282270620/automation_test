'''
Created on 2018年7月9日
@author: Administrator
'''
# 此模块提供异常重试和日志记录修饰符的方法
import traceback
from .logs import log

def log_decorator(log_path):
    '''
            此方法提供日志记录和异常重试判断的功能
    '''
    def decorator(func):
        def f(*arg):
            log(log_path, "{} 正在执行中~~~~~".format(func.__name__))
            try:
                t = func(*arg)
            except AssertionError as e:
                log(log_path, "{} 正在执行过程中断言失败：{}".format(func.__name__,str(e)))
            except Exception as e:
                log(log_path, "{} 正在执行过程中出异常了：{}".format(func.__name__,traceback.format_exc()))
                # 捕捉其他异常，先得到类的全路径
                class_name = arg[0].__class__
                # 调用方法解析出模块名和类名
                m_name,c_name = get_module_and_class(str(class_name))
                # 导包，导入模块名
                module = __import__(m_name)
                # 通过模块对象和类名得到实际的类
                AClass = getattr(module, c_name)
                # 进行重试
                try:
                    AClass.setUpClass(type="xx")
                    func(*arg)
                    AClass.tearDown()
                except Exception as e:
                    print(str(e))
            else:
                log(log_path, "{} 执行完成~~~~~".format(func.__name__))
                return t
        return f
    return decorator
def get_module_and_class(class_name):
    '''
            此方法通过处理得到类的全路径，然后解析出模块名和类名，形参格式如：<class 'p2p.test002_demo.TestDemo'>
    '''
    # 通过切割语法处理，得到模块名和类名
    tmp_list = str.split(class_name,".")
    module_name = tmp_list[-2]
    class_name = tmp_list[-1][:-2]
    # 返回参数
    return module_name,class_name