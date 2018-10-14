'''
Created on 2018年7月4日
@author: Administrator
'''
from xml.dom.minidom import Document
import os 
orderDict = {"name":"admin","tel":"123456","cnt":"code","value":"自动化测试"}
import xml.etree.ElementTree as ET
#创建根节点
a = ET.Element("root")
for k,v in orderDict.items():
    #创建子节点，并添加属性
    b = ET.SubElement(a,"sub1")
    b.attrib = orderDict
    #创建子节点，并添加数据
    c = ET.SubElement(a,"sub2")
    c.text = orderDict["value"]
      
#创建elementtree对象，写文件
tree = ET.ElementTree(a)
 
fp = os.path.join(os.getcwd().split("utils")[0],"config","writeConfig.xml")
print(fp)
tree.write(fp,encoding="utf8")
