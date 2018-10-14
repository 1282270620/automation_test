'''
Created on 2018年6月28日
@author: Administrator
'''
import pymysql
from utils.parserXML import XmlHandler
dict_info = XmlHandler.get_xml()

def get_verifycode(session):
    sql = "select code from ds_verifyCode where session='"+session+"' order by id desc limit 0,1"
    verifycode = execute_sql(sql)[0][0]
    sql_delete = 'truncate table ds_verifyCode'
    execute_sql(sql_delete)
    return verifycode
def execute_sql(sql):
    db = pymysql.connect(host=dict_info["host"],user=dict_info["root"],passwd=dict_info["passwd"],db=dict_info["db"],charset=dict_info["charset"]) 
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data
def get_bid(value_tit='title',value_state='state',value_type='type'):
    bid_info = []
    pledge = ["质押标"]
    mortgage = ["抵押标"]
    dic = ["已流标"]
    sql = "select "+value_tit+" from ds_borrowing"
    info_tits = execute_sql(sql)
    sql_state = "select "+value_state+" from ds_borrowing"
    info_states = execute_sql(sql_state)
    sql_type = "select "+value_type+" from ds_borrowing"
    info_types = execute_sql(sql_type)
    for info_tit,info_state,info_type in zip(info_tits,info_states,info_types):
        info_tit = list(info_tit)
        info_type = list(info_type)
        info_state = list(info_state)
        if info_state[0] == 1 and info_type[0] == 1:
            info_state[0] = "抵押标"
            mortgage.append(info_tit[0])
        if info_state[0] == 1 and info_type[0] == 2:
            info_state[0] = "质押标"
            pledge.append(info_tit[0])
        if info_state[0] == 4:
            info_state[0] = "已流标"
            dic.append(info_tit[0])         
    bid_info.append(pledge)
    bid_info.append(mortgage)
    bid_info.append(dic)
    return bid_info
if __name__ == "__main__":
    test = get_bid()
    print(test)

