#encoding=utf-8

# def get_str_length(s):
#     num = 0
#     for i in s:
#         num += 1
#     return num
# 
# print get_str_length('abcde')


# import string
# import time
# 
# def isLower(s):
#     "判断字符是否是小写"
#     if s in string.ascii_lowercase:
#         return True
#     else:
#         return False
# 
# def isUpper(s):
#     "判断字符是否是大写"
#     if s in string.ascii_uppercase:
#         return True
#     else:
#         return False
# 
# def my_swapcase(s):
#     """函数_文档字符串：
#         将字符串中的字符大小写转换"""
#     start_time = time.time()
#     newList = []
#     for i in s:
#         time.sleep(1)
#         if isLower(i):
#             newList.append(chr(ord(i)-32))
#         elif isUpper(i):
#             newList.append(chr(ord(i)+32))
#         else:
#             newList.append(i)
#     end_time = time.time()
#     print u'用时：',end_time - start_time
#     return ''.join(newList)
# 
# print my_swapcase('adbd2342VFSE')
# print my_swapcase.__doc__
# help(my_swapcase)

# def changeNum(n):
#     n = 10
# #     n += 1
#     print u'自定义函数中的n =',n
#     print id(n)
# 
# # def changeNum():
# #     global num
# #     num += 1
# #     print u'自定义函数中的n =',num
# #     print id(num)
# 
# 
# num = 10
# # changeNum(num)
# changeNum(num)
# print u'函数调用后的num =',num
# print id(num)


# import copy
# 
# def changeList(list1) :
#     list1.append('newStr')
#     print u"函数中的list1：",list1
#     print id(list1)
# 
# #定义list1
# list1 = [1,2,3]
# print u"调用函数前的list1: ",list1
# changeList(copy.copy(list1))
# print u"调用函数后的list1：",list1
# print id(list1)


# def add_end(L=None):
#     if L == None:
#         L = []
#         L.append('END')
#         print 'id(L)=',id(L)
#         return L
#     else:
#         L.append('END')
#         print 'id(L)=',id(L)
#         return L
# 
# print add_end([1, 2, 3]) #调用正常
# print add_end(['x', 'y', 'z']) #调用正常
# print add_end()#调用正常
# print add_end()#调用不正常
# print add_end()#调用不正常

# import math
# def my_abs(num):
#     if isinstance(num,(int,float)):
#         if num < 0:
#             return -num
#         else:
#             return num
#     elif isinstance(num,complex):
#         return math.sqrt(num.real**2+num.imag**2)
#     else:
#         return False
# 
# lista=[10,-10,0,'a',10.23,-10.23,1+2j]
# for each in lista:
#     print my_abs(each)


# def my_sum(a,b,c):
#     return a*100+b*10+c
# 
# # print my_sum(3,c=1,b=2)
# print my_sum(a=1,3,4)



# def say(times = 1, message):
#     print message * times
# say('gloryroad!')
# say(u'万岁！', 3)


# def func(x, y=3, z=8):
#     print 'x is', x
#     print 'y is', y
#     print 'z is', z
# 
# func(3, 7)
# print "-"*30
# func(25, z=24)
# print "-"*30
# func(z=50, x=100)


# def my_sum(operandA,operandB):
#     return float(operandA)+float(operandB)
# 
# def substract(operandA,operandB):
#     return float(operandA)-float(operandB)
# 
# 
# def multiple(operandA,operandB):
#     return float(operandA)*float(operandB)
# 
# def divide(operandA,operandB):
#     return float(operandA)/float(operandB)
# 
# print "10+5=",my_sum(10,5)
# print "10-5=",substract(10,5)
# print "10*5=",multiple(10,5)
# print "10/5=",divide(10,5)
# print "10/0=",divide(10,0)


# def func(a,b):
#     return a,b
# 
# print func(1,2)

# def my_sum(*nums):
#     if nums == ():
#         return
#     else:
#         sum = 0
#         for i in nums:
#             sum += i
#         return sum
# 
# print my_sum()
# print my_sum(1,21,31.8,41)

# def func(*args):
#     print type(args)
#     print args
# 
# func(1,2,3)


# def my_sum(**nums):
#     if nums == {}:
#         return
#     else:
#         sum = 0
#         for value in nums.values():
#             sum += value
#         return sum
# 
# print my_sum()
# print my_sum(a=1,b=-3,c=4.5)


# def my_sum(a,b=3,*args,**kw):
#     print 'a =',a
#     print 'b =',b
#     print 'args =',args
#     print 'kw =',kw
#     sum = a+b
#     for i in args:
#         sum += i
#     for value in kw.values():
#         sum += value
#     return sum


# def my_sum(a,b=3,*args,**kw):
#     print 'a =',a
#     print 'b =',b
#     print 'args =',args
#     print 'kw =',kw
# 
# my_sum(2,4,5,6,7,{'e':9},c=13,d=0)
# my_sum(2)


# def make_repeater(n):
#     return lambda s: s*n
# twice = make_repeater(2)
# 
# help(twice)
# print twice
# print twice('word')
# print twice(5)


# lista = ['a','adc','elephant']
# print map(len, lista)


# def my_sum(x,y):
#     return x+y
#  
# lista = range(1,10,2)
# listb = range(2,11,2)
# print lista
# print listb
# print map(my_sum, lista, listb)


# #定义大于5小于10的函数
# def guolvhanshu(num):
#     if num>5 and num<10:
#         return num
#  
# #定义一个序列
# seq=(12,50,8,17,65,14,9,6,14,5)
#  
# #使用filter函数
# result=filter(guolvhanshu,seq)
#  
# #(8,9,6)
# print result


# import string
# def delete_lowercase(s):
#     if s in string.uppercase:
#         return s
# 
# result = filter(delete_lowercase,"fsaeFES")
# print result


