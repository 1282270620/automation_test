# 此模块提供验证码相关功能
from interface_test_common import execute_sql
from .read_config import get_ipinfo

def get_verify_code(http_request):
    '''
    此方法会去获取验证码
    '''
    # 读取配置文件中的ip和端口信息
    ipinfo = get_ipinfo()
    # 定义验证码接口的地址
    verify_url = ipinfo+"/index.php/Public/verify/"
    # 发送一个Get请求，去获取验证码
    http_request.http_get(verify_url,decode_tag=False)
    # 调用获取session的方法
    session = http_request.get_session()
    # 定义查询验证码的SQL语句
    sql = "SELECT code FROM ds_verifycode where session='"+session+ \
    "' ORDER BY id DESC LIMIT 0,1;"
    # 调用执行sql语句的方法
    verify_code = execute_sql(sql)[0][0]
    # 定义接口测试固定参数格式
    data_dict = {}
    data_dict["header"]={"Cookie":"PHPSESSID="+session}
    data_dict["data"]={"proving":verify_code}
    # 返回字典内容（固定格式）
    return data_dict