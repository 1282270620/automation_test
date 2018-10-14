# 此模块提供读取配置文件相关操作
from xml.dom.minidom import parse

def read_ipinfo():
    # 定义用于存储ip信息的字典
    ip_dict = {}
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的ipinfo元素，注意返回类型为元素列表
    ipinfo_list = document.getElementsByTagName("ipinfo")
    # 整个配置文件中只有一个ipinfo，所以指定读取第一个，同样返回的是元素列表
    ip_list = ipinfo_list[0].getElementsByTagName("ip")
    port_list = ipinfo_list[0].getElementsByTagName("port")
    protocol_list = ipinfo_list[0].getElementsByTagName("protocol")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    ip = ip_list[0].childNodes[0].data
    port = port_list[0].childNodes[0].data
    protocol = protocol_list[0].childNodes[0].data
    # 返回ip及端口
    ip_dict["ip"] = ip
    ip_dict["port"] = port
    ip_dict["protocol"] = protocol
    return ip_dict

def read_dbinfo():
    # 定义用于存储db信息的字典
    db_dict = {}
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的dbinfo元素，注意返回类型为元素列表
    dbinfo_list = document.getElementsByTagName("dbinfo")
    # 整个配置文件中只有一个dbinfo，所以指定读取第一个，同样返回的是元素列表
    dbname_list = dbinfo_list[0].getElementsByTagName("dbname")
    dbuser_list = dbinfo_list[0].getElementsByTagName("dbuser")
    dbpasswd_list = dbinfo_list[0].getElementsByTagName("dbpasswd")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    dbname = dbname_list[0].childNodes[0].data
    dbuser = dbuser_list[0].childNodes[0].data
    dbpasswd = dbpasswd_list[0].childNodes[0].data
    # 返回ip及端口
    db_dict["dbname"] = dbname
    db_dict["dbuser"] = dbuser
    db_dict["dbpasswd"] = dbpasswd
    return db_dict

def get_ipinfo():
    # 先调用读取ip信息的方法
    ip_dict = read_ipinfo()
    protocol = ip_dict.get("protocol")
    ip = ip_dict.get("ip")
    port = ip_dict.get("port")
    # 返回ipinfo
    ipinfo = protocol+"://"+ip+":"+port
    return ipinfo

# print(read_ipinfo())
# print(read_dbinfo())
    