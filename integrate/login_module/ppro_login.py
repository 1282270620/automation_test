import requests

host = "https://github.com/login"

header = {
    "Host":"api.github.com",
    "Connection":"keep-alive",
    "Content-Length":"7434",
    "Origin":"https://github.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.4.3.17934",
    "Content-Type":"application/json",
    "Accept":"*/*",
    "Referer":"https://github.com/",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8"
}
data_para = {
    "commit":"Sign in",
    "utf8":"✓",
    "authenticity_token":"vra0H71XSIv5Lj5rc8cCfc+0Hnz6aZ16kaGfn9sIFnOEYvq575AQVKe0b04anbFjGX0wy3TrAj47cNLzdC7PgQ==",
    "login":"1282270620",
    "password":"1282270620@qq.com"
    }
res = requests.post(url=host, data=data_para, json=header)
print(res.text)