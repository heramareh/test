#encoding=utf-8

'''深浅拷贝'''
'''
浅拷贝，只拷贝第一层元素
深拷贝，不管有多少层都会拷贝
'''
# import copy
# a=[1,2,[3,4]]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# 
# print 'a id:',id(a)
# print 'b id:',id(b)
# print 'c id:',id(c)
# print 'd id:',id(d)
# 
# print '*'*20
# 
# a.append(6)
# a[2].append(5)
# a[0]=7
# print a
# print b
# print c
# print d

'''两个元组合并成一个新元组'''
# tup1=(12,34,56)
# tup2=('abc','xyz')
# lista=[]
# for i in tup1:
#     lista.append(i)
# for i in tup2:
#     lista.append(i)
# print tuple(lista)
# print tup1+tup2

'''统计元组的元素个数'''
# tup1=(12,34,56)
# count = 0
# for i in tup1:
#     count+=1
# print count

'''遍历序列的子元素，如果是序列则输出子元素'''
# def iterate_sequence_subitem(s):
#     for i in s:
#         if isinstance(i,(list,tuple)):
#             for j in i:
#                 print j,
#             print
# 
# a=[1,2,3,(4,5,6),[7,8,9],(10,11)]
# iterate_sequence_subitem(a)

# def get_key(d,value):
#     for k,v in d.items():
#         if v == value:
#             print k,v
# 
# d = {'name': 'Heram', 'sex': 'male','age':18,'aa':18}
# get_key(d,18)

# def get_value_by_key(d,key):
#     if d.has_key(key):
#         print d[key]

''''1 图书馆可以有多本书，每本书有个作者，我需要统计一共有多少本书，有多少个作者
2 查看所有的作者清单，和书名清单
3 查看书名和作者的对应关系'''
# def get_count_books():
#     return len(d.keys())
# 
# def get_count_author():
#     return len(set(d.values()))
# 
# def get_all_authorname():
#     return list(set(d.values()))
# 
# def get_all_bookname():
#     return d.keys()
# 
# def get_author_book():
#     for k,v in d.iteritems():
#         print k+"'s author:",v
# 
# d={'python':'zhangsan','java':'lisi','php':'wangwu','c++':'wangwu'}
# print 'count_books:',get_count_books()
# print 'count_author:',get_count_author()
# print 'bookname:',get_all_bookname()
# print 'authorname:',get_all_authorname()
# get_author_book()

# user={'user3':'ab','user2':'cde','user1':'d'} 
# print user.items()
# sort=sorted(user.iteritems(),key=lambda e:e[1][-1])   #排序
# print sort
# print type(sort)
# for item in sort:
#     print "%s= %s"  %(item[0],item[1])

# s='fwegfrwegro34o3gjr'
# print s[0]+s[-1]+s[1:5]

# import time
# def my_sum(n):
#     start_time = time.time()
#     i = iter(range(1,n+1))
#     sum = 0
#     while True:
#         try:
#             sum += i.next()
#         except StopIteration:
#             break
#     end_time = time.time()
#     
#     return 'my_sum:',sum,end_time-start_time
# 
# def my_sum2(n):
#     start_time = time.time()
# #     sum = 0
# #     for i in xrange(1,n+1):
# #         sum += i
#     sum2 = sum(xrange(1,n+1))
#     end_time = time.time()
#     
#     return 'my_sum2',sum2,end_time-start_time
# 
# n=10000000
# print my_sum(n)
# print my_sum2(n)
