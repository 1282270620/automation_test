'''
Created on 2018年9月13日

@author: Administrator
'''
from xml.dom.minidom import parse

def read_ipinfo():
    ip_dict = {}
    dom = parse("../config/Configration.xml")
    document = dom.documentElement
    
    ipinfo_list = document.getElementsByTagName("ipinfo")
    ip_list = ipinfo_list[0].getElementsByTagName("ip")
    port_list = ipinfo_list[0].getElementsByTagName("port")
    protocol_list = ipinfo_list[0].getElementsByTagName("protocol")
    
    ip = ip_list[0].childNodes[0].data
    port = port_list[0].childNodes[0].data
    protocol = protocol_list[0].childNodes[0].data

    ip_dict["ip"] = ip
    ip_dict["port"] = port
    ip_dict["protocol"] = protocol
    
    return ip_dict
def read_dbinfo():
    db_dict = {}
    dom = parse("../config/Configration.xml")

    document = dom.documentElement
    
    dbinfo_list = document.getElementsByTagName("dbinfo")
    dbname_list = dbinfo_list[0].getElementsByTagName("dbname")
    dbuser_list = dbinfo_list[0].getElementsByTagName("dbuser")
#     dbpassword_list = dbinfo_list[0].getElementsByTagName("dbpassword")
    
    dbname = dbname_list[0].childNodes[0].data
    dbuser = dbuser_list[0].childNodes[0].data
#     dbpassword = dbpassword_list[0].childNodes[0].data
    
    db_dict["dbname"] = dbname
    db_dict["dbuser"] = dbuser
#     db_dict["dbpassword"] = dbpassword
    
    return db_dict
      