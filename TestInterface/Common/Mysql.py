'''
Created on 2018年9月13日

@author: Administrator
'''
import pymysql
from Common.ReadConfigration import read_ipinfo,read_dbinfo

def execute_sql(sql):
    #ip = read_ipinfo()["ip"]
    ip = read_ipinfo().get("ip")
    db_dict = read_dbinfo()
    
    db = pymysql.connect(ip,db_dict.get("dbuser"),db_dict.get("dbpassword"),db_dict.get("dbname"))

    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    
    db.close()
    
    return data
execute_sql("select * from ds_user;")