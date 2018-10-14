'''
Created on 2018年7月2日

@author: Administrator
'''
from time import sleep
import jpype
import time
from utils.parserXML import XmlHandler

dict_info = XmlHandler.get_xml()

class DefineFlash(object):
    @classmethod
    def init_method(self,driver,path,url=dict_info["url"]):
        '''
                    该方法提供设置flash为允许的功能
        '''
        self.url = url
        # 定义所需图片在项目中的位置
        self.picture_path = path+r"\testData"
        # 打开flash的设置页
        driver.get("chrome://settings/content/flash")
        sleep(2)
        # 定义jvm的路径及jar的路径
        jvm_path = r"C:\Program Files\Java\jdk1.8.0_151\jre\bin\server\jvm.dll"
        jar_path = "-Djava.class.path=" + "C:\mydemo\sikulixapi.jar"
        # 启动JVM
        jpype.startJVM(jvm_path,jar_path)
#        print(jpype.isJVMStarted())
        # 得到Screen类和Pattern类
        Screen = jpype.JClass("org.sikuli.script.Screen")
        self.Pattern = jpype.JClass("org.sikuli.script.Pattern")
        # 实例化Screen类
        self.screen = Screen()
    @classmethod
    def set_flash(self):
        picture_path = self.picture_path
        # 先定义添加图片的路径，然后进行适当的偏移
        add_path = picture_path+r"\add.png"
        sleep(2)
        offset_Path = self.Pattern(add_path).targetOffset(300,0)
        print(self.Pattern(add_path).getSimilar())
        self.screen.click(offset_Path)
        sleep(2)
        # 输入网址
        url_path = picture_path+r"\url.png"
        self.screen.type(url_path,self.url)
        # 点击添加
        add_ok_path = picture_path+r"\add_ok.png"
        self.screen.click(add_ok_path)
    @classmethod
    def upload_picture(self):
        picture_path = self.picture_path
        # 先定义添加图片的路径，然后进行适当的偏移
        add_path = picture_path+r"\select_png.png"
        sleep(2)
        offset_Path = self.Pattern(add_path).targetOffset(0,0)
        print(self.Pattern(add_path).getSimilar())
        self.screen.click(offset_Path)
        sleep(2)
        url_path = picture_path+r"\upload.png"
        self.screen.type(url_path,r"C:\mydemo\p2p_framework\testData\testpicture.jpg")
        # 点击添加
        open_path = picture_path+r"\upload_image\open.png"
        offset_Path = self.Pattern(add_path).targetOffset(0,0)
        self.screen.click(open_path)
        time.sleep(5)
    @classmethod
    def del_method(self):
        # 关闭JVM
        jpype.shutdownJVM()
        sleep(1)