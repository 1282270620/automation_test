import os 
print("help.------------------------------------------------------")
#help(os)    #查看os模块帮助文档，里面详细的模块相关函数和使用方法
# 一、os.path介绍——获取路径
print("1.------------------------------------------------------")
#    1、os.path.abspath(path)        返回path规范化的绝对路径
print(os.path.abspath('.'))     #将相对路径转化为绝对路径
print(os.path.abspath(os.curdir))
print(os.path.abspath('..'))    #将相对路径的上级路径转化为据对路径
print(os.path.abspath(os.pardir))
print(os.path.abspath(__file__))    #获取当前文件的据对路径
print("2.------------------------------------------------------")
#    2.os.path.split(path)  将path分割成目录和文件名二元组返回
print(os.path.split(__file__))
print(__file__)
#    os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
dir = os.path.dirname(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
#    os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
file = os.path.basename(__file__)
print(os.path.basename(__file__))

#os.path.splitdrive(path) 返回（drivername，fpath）元组
#os.path.splitext(path) 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
print("3.------------------------------------------------------")
#    3.os.sep    输出操作系统特定的路径分隔符
print(os.sep)
filepath = dir + os.sep + file
print(filepath)
print(os.extsep)
print(os.path.normpath("E:\\Python/os"))
print(os.altsep)        #斜杠与os.sep相反

print("4.------------------------------------------------------")
#    4.os.getcwd()    获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())
print(os.getcwd().split())

print("5.------------------------------------------------------")
#    5.os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
#print(os.path.join(dir,file))

print("6.------------------------------------------------------")
#os.walk(top, topdown, onerror, followlinks)    遍历文件和目录，返回结果是一个元组类型,top:根节点，topdown=true 自顶而下的遍历;oneerror:没有值的时候，出现错误还会继续遍历;
'''
for root,alldir,curfile in os.walk("F:\\python"):
    print(root)    #返回当前的目录根节点
    print(alldir)    #当前结点的下的所有目录
    print(curfile)    #当前结点下的所有文件'''

print("8.------------------------------------------------------")
os.system('notepad')    #打开记事本
#os.system('pwd')
print("9.------------------------------------------------------")
os.path.normcase(path)
#    os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
#    os.path.isabs(path)  如果path是绝对路径，返回True
#    os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
#    os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
#os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间
#os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间
#os.path.getsize(path)返回path的文件的大小（字节）






