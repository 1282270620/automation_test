from urllib import request
import urllib


class HTTPRequest(object):
    '''
    此类提供关于HTTP基本请求的方法
    '''
    # 定义一个类属性，用于保存响应头内容（HTTPMessage格式）
    response_headers = None

    def __init__(self):
        pass
        
    def http_get(self,url,headers={},decode_tag=True):
        '''
        此方法提供最基本的Get请求功能
        '''
        # 实例化一个Request类，仅指明url地址和headers信息(相当于包装了一个请求)
        req = request.Request(url=url,headers=headers)
        # 发起一个HTTP请求（Get），并取得响应结果（相当于把上面包装的请求发出去）
        response = request.urlopen(req)
        # 得到所有的头部信息，并保存在类属性中
        self.response_headers = response.info()
        # 读取响应数据，注意格式为字节流
        response = response.read()
        # 需要解码时，再将得到的字节流解码为字符串
        if decode_tag:
            response = response.decode("utf-8")
        # 返回结果
        return response

    def http_post(self,url,data,headers={},urlencode_tag=True):
        '''
        此方法提供最基本的Get请求功能
        '''
        # 判断data数据是否需要进行urlencode编码，然后必须转成字节码才能发送出去
        if urlencode_tag:
            data = urllib.parse.urlencode(data).encode(encoding='utf_8')
        else:
            data = data.encode(encoding='utf_8')
        # 实例化一个Request类，仅指明url地址和headers信息(相当于包装了一个请求)
        req = request.Request(url=url,data=data,headers=headers)
        # 发起一个HTTP请求（变成POST），并取得响应结果（相当于把上面包装的请求发出去）
        response = request.urlopen(req)
        # 得到所有的头部信息，并保存在类属性中
        self.response_headers = response.info()
        # 读取响应数据，注意格式为字节流
        response = response.read()
        # 需要解码时，再将得到的字节流解码为字符串
        response = response.decode("utf-8")
        # 返回结果
        return response        
        
    def get_session(self):
        '''
        此方法提供解析出session的功能
        '''
        # 定义session信息起止的标记
        start_tag = "PHPSESSID="
        end_tag = ";"
        # 将头部信息的HTTPMessage对象保存为字符串格式
        headers_string = str(self.response_headers)
        # 先找到开始位置并进行截取
        start_pos = headers_string.find(start_tag)
        headers_string = headers_string[start_pos+len(start_tag):]
        # 再找到结束位置，并截取出session
        end_pos = headers_string.find(end_tag)
        session = headers_string[:end_pos]
        # 返回session内容
        return session
    
    def check_result(self,reponse,start_tag,end_tag,expect_result):
        '''
        此方法提供判断测试结果的功能
        '''
        # 进行异常捕捉，万一不符合规则则将结果完全返回
        try:
            # 先找到开始位置，并进行截取
            start_pos = reponse.find(start_tag)
            reponse = reponse[start_pos+len(start_tag):]
            # 再找到结束位置，并截取出session
            end_pos = reponse.find(end_tag)
            actual_result = reponse[:end_pos]
            # 进行结果的判断，并返回测试结果
            if expect_result == actual_result :
                return True
            else:
                return actual_result
        except:
            # 截取出现异常了，直接将内容全部返回
            return reponse
        
        