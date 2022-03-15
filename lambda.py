# print((lambda x:x*2)(12))

'''x=lambda a,b:a+b
print(x(10,20))'''

'''double=lambda x:x*2
print(double(5))'''

'''def myfun(n):
    return lambda a:a*n
x=myfun(2)
print(x(5))'''

l=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:pow(x,3),l)))
