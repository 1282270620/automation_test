#coding:utf-8
import pymysql
'''
Python3之后不再支持MySQLdb的方式进行访问mysql数据库；
可以采用pymysql的方式
连接方式：
    1、导包
        import pymysql
    2、打开数据库连接
        conn = pymysql.connect(host='10.*.*.*',user='root',password='123456',db='dingplus_self_dev',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
        备注：其中cursorclass=pymysql.cursors.DictCursor 可有可无，配置的是每个字段的展示方式，按照字典的形式进行展示（方便通过列名进行访问），默认元组形式。
    3、使用cursor()方法获取操作游标 
        cur = connection.cursor()
    4、SQL 查询语句
        sql = "SELECT * FROM table t where t.name='政协'"
    5、执行SQL语句
        cur.execute(sql)
    6、获取所有记录列表
        rows = cur.fetchall()
    7、输出
    8、关闭数据库连接
        connection.close()
'''
connection = pymysql.connect(host='10.*.*.*',
    user='root',
    password='123456',
    db='ddd',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

cur = connection.cursor()

sql = "SELECT * FROM plus_org t where t.name='政协'"
try:
    cur.execute(sql)
    results = cur.fetchall()

    for row in results:
        org_id = row['id']
        print(org_id)
except:
    print('Error:unable to fetch data')

connection.close()