'''
此模块提供执行数据库相关操作的办法
'''
from .read_config import read_ipinfo,read_dbinfo
import pymysql

def execute_sql(sql):
    # 读取配置信息
    ip = read_ipinfo().get("ip")
    db_dict = read_dbinfo()
    # 连接数据库p2p3
    db =pymysql.connect(ip, db_dict.get("dbuser"), 
                        db_dict.get("dbpasswd"),db_dict.get("dbname"))
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchall() 方法获取所有数据
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    # 返回数据
    return data