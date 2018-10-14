'''
Created on 2018年7月9日
@author: Administrator
'''
import requests

host = "https://passport.cnblogs.com/user/signin"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
body1 = {"username":"借鉴六颗","password":"1282270620@qq.com"}
'''
s = requests.session()
r1 = requests.get(host,data=body1,headers=header)
print(r1.text)
'''
s = requests.session()
r = s.get(host, headers=header,verify=False)
print(s.cookies)
# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()

c.set('.CNBlogsCookie', '这里是抓到的')  # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies','这里是抓到的')  # 填上面抓包内容
c.set('AlwaysCreateItemsAsActive',"True")
c.set('AdminCookieAlwaysExpandAdvanced',"True")
s.cookies.update(c)
print(s.cookies)

# 登录成功后保存编辑内容
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=header, verify=False)

# 保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"这是3111",
        "Editor$Edit$EditorBody":"<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$tbEnryPassword":"",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(url2, data=body, verify=False)
print(r.content)