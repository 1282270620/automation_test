'''
Created on 2018年6月28日

@author: Administrator
'''

import  xml.dom.minidom as XMLDocument
import os

filepath = os.path.join(os.getcwd().split("utils")[0],"config","config.xml")

#打开xml文档
dom = XMLDocument.parse(filepath) #打开xml文档

#得到文档元素对象
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)

#获得子标签
bb = root.getElementsByTagName("maxid")
print(type(bb))
print(bb)

b = bb[0]
print(b.nodeName)
print(b.nodeValue)

#获取标签属性值
itemlist = root.getElementsByTagName("login")
print(itemlist)
item = itemlist[0]
print(item)
print(item.getAttribute("username"))
print(item.getAttribute("passwd"))
itemlist = root.getElementsByTagName("item")
print(itemlist)
itemlist1 = itemlist[1]
print(itemlist1.getAttribute("id"))
#获取标签之间的数据
itemlist = root.getElementsByTagName("caption")
item1 = itemlist[0]
print(item1.firstChild.data)
item2 = itemlist[1]
print(item2.firstChild.data)


'''
总结：minidom.parse(filename) 加载读取XML
doc.documentElement 获取文档对象
node.getAttribute(AttributeName) 获取XML节点属性值
node.getElementsByTagName(TagName) 获取XML节点对象集合
node.childNodes 返回子节点列表
node.childNodes[index].nodeValue 获取XML节点值
node.firstChild 访问第一节点。等价于childNodes[0]
'''

