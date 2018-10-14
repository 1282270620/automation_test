'''
Created on 2018年6月28日
@author: Administrator
'''
import xml.dom.minidom as XDM
import os

class XmlHandler(object):
    @classmethod
    def get_xml(cls,key="login"):
        relative_path = os.path.dirname(os.path.abspath("."))
        filepath = os.path.join(relative_path,"config","config.xml")
        dom = XDM.parse(filepath) 
        para_dict = {}
        root = dom.documentElement
        url_node = root.getElementsByTagName("url")[0]
        para_dict["url"] = url_node.firstChild.data
        url_node = root.getElementsByTagName("burl")[0]
        para_dict["burl"] = url_node.firstChild.data
        
        if key == "login":
            itemlist = root.getElementsByTagName("login")[0]
            para_dict["username"] = itemlist.getAttribute("username")
            para_dict["password"] = itemlist.getAttribute("passwd")
        elif key == "logon":
            itemlist = root.getElementsByTagName("logon")[0]
            para_dict["username"] = itemlist.getAttribute("username")
            para_dict["password"] = itemlist.getAttribute("passwd")
        elif key == "loc":
            itemlist = root.getElementsByTagName("loc")[0]
            para_dict["username"] = itemlist.getAttribute("username")
            para_dict["password"] = itemlist.getAttribute("passwd")
        mysqllist = root.getElementsByTagName("mysql")[0]
        para_dict["host"] = mysqllist.getAttribute("host")
        para_dict["root"] = mysqllist.getAttribute("user")
        para_dict["passwd"] = mysqllist.getAttribute("passwd")
        para_dict["db"] = mysqllist.getAttribute("db")
        para_dict["charset"] = mysqllist.getAttribute("charset")  
        return para_dict
if __name__ == "__main__":
    list1 = XmlHandler.get_xml("login")
    print(list1)