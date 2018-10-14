'''
Created on 2018年6月28日

@author: Administrator
'''
import xml.dom.minidom as XDM
import gzip,cStringIO,os

class xmlHandler(object):
    def __init__(self):
        pass
    def dom_parser(self,gz):
        vs_cnt = 0
        str_s = ''
        file_io = cStringIO.StringIO()
        xm = gzip.open(gz,"rb")
        print("已读入：%s.\n解析中："%(os.path.abspath(gz)))
        doc = XDM.parseString(xm.read())
        bulkPmMrDataFile = doc.documentElement
        #读入子元素
        enbs = bulkPmMrDataFile.getElementsByTagName("eNB")
        measurements = enbs[0].getElementsByTagName("measurement")
        objects = measurements[0].getElementsByTagName("object")
        #写入csv文件
        for object in objects:
            vs = object.getElementsByTagName("v")
            vs_cnt += len(vs)
            for v in vs:
                file_io.write(enbs[0].getAttribute("id")+' '+object.getAttribute("id")+' '+\
                object.getAttribute("MmeUeS1apId")+' '+object.getAttribute("MmeGroupId")+' '+object.getAttribute("MmeCode")+' '+\
                object.getAttribute("TimeStamp")+' '+v.childNodes[0].data+'\n')  #获取文本值
        str_s = (((file_io.getvalue().replace(' \n','\r\n')).replace(' ',',')).replace('T',' ')).replace('NIL','')
        xm.close()
        file_io.close()
        return (str_s,vs_cnt)
        
