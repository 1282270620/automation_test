x=1
def xxx(x):
    def foo1(func):
        def ww(*xx,**jj):
            print("foo1 xxxxxxxxxxxxxx") 
            print(x)
            print(func)
            func(*xx)
            print("foo1 zzzzzzzzzzzzzz") 
        return ww
    return foo1
    
# @xxx
# def foo2(a,b):
#     print(a+b) 
    
@xxx(x)
def foo3(a,b,c,d):
    print(a*b*c*d)
    
# foo2(1,2)
foo3(1,2,3,4)