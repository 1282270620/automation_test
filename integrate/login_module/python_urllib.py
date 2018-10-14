
from bs4 import BeautifulSoup
import random,urllib
import urllib.parse
from urllib import request

def idcard_6first():#随机获取一个身份证号前6位
    urll="http://www.360doc.com/content/12/0917/16/1888675_236595612.shtml" #身份证前6位网址
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req=request.Request(url=urll,headers=headers)
    response=request.urlopen(req)       #打开网站
    page=response.read()               #读取内容
    page_info = page.decode('UTF-8','ignore')    #保存类型
    soup = BeautifulSoup(page_info, 'html.parser')
    b=soup.find_all('span',lang="EN-US",style="FONT-WEIGHT: normal; FONT-SIZE: 12pt; FONT-FAMILY: 宋体; mso-bidi-font-family: 宋体; mso-font-kerning: 0pt")
   # c=b.find_all('span',lang="EN-US")
    id=random.choice(b[4:])
    return id.string


#urllib库包含四个模块
# 1. request ： 它是最基本的 HTTP 请求模块，可以用来模拟发送请求 。 就像在浏览器里输入网址然后回车一样，只需要给库方法传入 URL 以及额外的参数，就可以模拟实现这个过程了 。
# 2. error ： 异常处理模块，如果出现请求错误 ， 我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止 。
# 3. parse ： 一个工具模块，提供了许多 URL 处理方法，比如拆分、解析 、 合并等 。
# 4. robot parser ：主要是用来识别网站的 robots.txt 文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。

#urllib.request用Request类来表示你做出的HTTP请求。它的最简形式就是只指定你需要访问的url。Request对象调用urlopen方法会为这个请求返回一个响应对象。这个响应是一个类文件对象

def url():
    response=urllib.request.urlopen('http://www.baidu.com')    
    print(type(response))        #<class 'http.client.HTTPResponse'>  模拟浏览器的一个请求发起过程
       
    #print(response.getcode() )
    #print(response.status)      #响应的状态码
    #print(response.getheaders())  
    #print(response.info())       #响应的头信息
    #print(response.getheader('Bdqid'))
    #print(response.geturl())
    page=response.read()   #返回网页的内容
    print(type(page))
    print(page)
    #print(page.decode('utf-8'))

#urllib.request.urlopen(url,data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
# data 参数是可选的 。 如果要添加该参数，它是字节流编码格式的内容，即 bytes 类型，
# 则需要通过 bytes（方法转化。 另外，如果传递了这个参数，则它的请求方式就不再是 GET 方式，而是 POST 方式 。
def post():
    data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding="utf8")
    response=urllib.request.urlopen('http://httpbin.org/post',data=data) 
    print(response.read())
    print(response.info())

#timeout 参数用于设置超时时间，单位为秒，意思就是如果请求超 出 了设置的这个时间， 还没有得到响应 ， 就会抛出异常
def timeout():
    response=urllib.request.urlopen('http://www.baidu.com',timeout=0.1)
  
# class urllib. request. Request (ur1, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# 1.第一个参数 ur l 用于请求 URL ， 这是必传参数，其他都是可选参数 。
# 2.第二个参数 data 如果要传，必须传 bytes（字节流）类型的。如果它是字典,可以先用urllib.parse模块里的 urlencode（)编码 。
# 3.第三个参数 headers 是一个字典，它就是请求头，我们可以在构造请求时通过 headers 参数直接构造，也可以通过调用请求实例的 add_header（）方法添加 。
# 添加请求头最常用的用法就是通过修改 User-Agent 来伪装浏览器，默认的 User-Agent 是Python-urllib  
# 4.第四个参数 origin_req_host 指的是请求方的 host 名称或者 IP 地址。
# 5.第五个参数unverifiable 表示这个请求是否是无法验证的，默认是 False ，意思就是说用户没有足够权限来选择接收这个请求的结果。例如，我们请求一个 HTML 文档中的图片，但是我们没有向动抓取图像的权限，这时 unverifiable 的值就是 True 。
# 6.第六个参数 method 是一个字符串 ，用来指示请求使用的方法，比如 GET 、 POST 和 PUT 等 。
def header():  #防爬虫
    urll="http://www.360doc.com/content/12/0917/16/1888675_236595612.shtml" #身份证前6位网址
    #headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req=request.Request(url=urll)
    response=request.urlopen(req)       #打开网站
    print(response.status)
    print(response.read().decode('utf-8'))
    

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener    
def daili():   #代理登陆没成功

    proxy_handler = ProxyHandler({
    'http':'http://77.85.169.149:8080'
    })
    opener = build_opener(proxy_handler)
    try:
        response = opener.open('https://www.baidu.com')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)
#daili()
def headers():      #post登陆p2p
    urll="http://172.31.31.108/Logo/logings.html" 
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
              }
    #data = bytes(urllib.parse.urlencode({'username':'xiaoli','password':'123456'}),encoding="utf8")
    req=request.Request(url=urll,headers=headers)
    response=request.urlopen(req)       #打开网站
    print(response.info())
    print(response.read().decode('utf-8'))

#headers()
def center(): #直接登陆，提示请先登陆
    urll="http://172.31.31.108/Center.html" 
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
              }
  
    req=request.Request(url=urll,headers=headers,method='GET')
    response=request.urlopen(req)       #打开网站
    print(response.info())
    print(response.read().decode('utf-8'))
#center()

    
import http.cookiejar,urllib.request
def cookie():    #获取cookie自己查看获得7个
    
    cookie = http.cookiejar.CookieJar()
    handler = urllib .request.HTTPCookieProcessor (cookie)
    opener = urllib.request.build_opener(handler )
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name+'='+item.value)
#cookie()   
def filecookie(): #将cookie保存下来
    filename= 'cookies.txt'
#    cookie = http.cookiejar.MozillaCookieJar(filename)
    cookie = http.cookiejar. LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)
#filecookie() 
def read_cookie(): #保存cookie信息，并登陆到中心页面
    filename= 'cookies.txt'
#    cookie = http.cookiejar.MozillaCookieJar(filename)
    cookie = http.cookiejar. LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    urll="http://172.31.31.108/Logo/logings.html" 
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
              }
    data = bytes(urllib.parse.urlencode({'username':'xiaoli','password':'123456'}),encoding="utf8")
    req=request.Request(url=urll,data=data,headers=headers,method='POST')
    try:
        response=opener.open(req)
        page=response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)
    cookie.save(ignore_discard=True, ignore_expires=True)
    print(cookie)
    get_url="http://172.31.31.108/Center.html"
    get_request = urllib.request.Request(get_url, headers=headers)
    get_response = opener.open(get_request)
    print(get_response.read().decode('utf-8'))
    
def get_cookie():  #用保存的cookie到其他页面
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request .HTTPCookieProcessor(cookie)
    opener = urllib .request.build_opener(handler)
    response= opener.open('http://172.31.31.108/Center/approve/autonym.html')
    print(response.read().decode('utf-8'))
get_cookie() 


    
    