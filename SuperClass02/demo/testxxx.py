from interface_test_common import excel
class A():
#     a=1
    def __init__(self):
        self.a = 100
    def seta(self):
        print("seta")

class B(A):
#     a=100
    def setb(self,x):
        A.__init__(self)
#         self.a = x
#         print("setb")
        
class C(A):
#     a=333
    def setc(self,x):
        self.a = x
    def get(self):
        return self.a

class D():
    def get(self,path):
        xx = excel.read_test_case_data(path)
        print(xx)
    def setd(self,f):
        print(f(1))
        
def f(x):
    return x+1

d=D()
d.get("..\data\TestLogin.xlsx")
# b=B()
# b.setb(12222)
# c=C()
# c.setc(13333)
# c.get()
# print(b.a)
# print(c.a)
# print(b.a)
# d=D()
# d.setd(f)