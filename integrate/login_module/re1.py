# import re
# 
# str1 = "<unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[]>, <unittest.suite.TestSuite tests=[]>, <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<thinksns.t02_friendly_link.TestFriendlyLink testMethod=test_01>, <thinksns.t02_friendly_link.TestFriendlyLink testMethod=test_02>]>, <unittest.suite.TestSuite tests=[<thinksns.t03_publish_mood.TestPublishMood testMethod=test_01>]>, <unittest.suite.TestSuite tests=[<thinksns.t01_register.TestRegister testMethod=test_01>]>]>, <unittest.suite.TestSuite tests=[]>]>"
# str2 = re.match("tests=[", str1)
# print(str2)
import re
str1 = "<unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[]>, <unittest.suite.TestSuite tests=[]>, <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<thinksns.t02_friendly_link.TestFriendlyLink testMethod=test_01>, <thinksns.t02_friendly_link.TestFriendlyLink testMethod=test_02>]>, <unittest.suite.TestSuite tests=[<thinksns.t03_publish_mood.TestPublishMood testMethod=test_01>]>, <unittest.suite.TestSuite tests=[<thinksns.t01_register.TestRegister testMethod=test_01>]>]>, <unittest.suite.TestSuite tests=[]>]>"

m = re.search('<(.+?)testMethod=',str1)
#这里如果使用match将匹配不到任何字符串，因为match从第一个a开始匹配
if m is not None:
    print(m.group())

