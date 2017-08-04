#encoding=utf-8

# '''打印2000-3000之间被7整除但不被5整除的数，以逗号分隔'''
# lista=[]
# for num in xrange(2000,3001):
#     if num % 7 == 0 and not(num % 5 == 0):
#         lista.append(str(num))
# print ','.join(lista)

# import string
#   
# '''输出9*9口诀表'''
# for x in xrange(1,10):
#     for y in xrange(1,x+1):
#         print string.ljust("%d*%d = " %(y,x) + str(y*x), 10),
#     print

# '''计算1 - 1/2 + 1/3 - 1/4 + … + 1/99 - 1/100 + …
# 直到最后一项的绝对值小于10的-5次幂为止
# '''
# num = 0
# for i in xrange(1,10**5+1):
#     if i % 2 == 1:
#         num += 1.0/i
#     else:
#         num -= 1.0/i
# print num

# '''编程将类似“China”这样的明文译成密文，密码规律是：用字母表中原来
# 的字母后面第4个字母代替原来的字母，不能改变其大小写，如果超出了字母
# 表最后一个字母则回退到字母表中第一个字母
# '''
# def encryption(s):
#     lista = []
#     for i in s:
#         num = ord(i)
#         if (num >= 65 and num <= 86) or (num >= 97 and num <= 118):
#             lista.append(chr(num+4))
#         elif (num >= 87 and num <= 90) or (num >= 119 and num <= 122):
#             lista.append(chr(num-22))
#         else:
#             lista.append(i)
#     return ''.join(lista)
# import string
# print string.letters+string.digits
# print encryption(string.letters+string.digits)

# '''输出以下如下规律的矩阵
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
# '''
# import string
# import copy
#  
# def get_matrix(num):
#     lista = range(1,num+1)
#     row_list = copy.copy(lista)
#     for i in xrange(num):
#         for each in row_list:
#             print string.ljust(str(each),4),
#         print
#         row_list = map(lambda x,y:x+y,lista,row_list)
#   
# get_matrix(5)

# '''对一个列表求和，如列表是[4, 3, 6]，
# 求和结果是 [4, 7, 13]，
# 每一项的值都等与该项的值加上前一项的值
# '''
# import copy
#  
# lista = [4,3,6,12,5,9]
# result_list = copy.copy(lista)
# for i in range(1,len(lista)):
#     result_list[i] = result_list[i-1] + lista[i]
# print "result_list =",result_list
#
# result_list = []
# for i in range(1,len(lista)+1):
#     result_list.append(sum(lista[:i]))
# print "result_list =",result_list

# '''一个字符串 list，
# 每个元素是 1 个 ip，
# 输出出现次数最多的 ip'''
# str_list = ['1.1.1.1','1.1.1.1','1.1.1.2','1.1.1.1','1.1.1.3','10.2.21.10','10.2.21.10','10.2.21.10','10.2.23.24','10.2.21.32']
# str_dict = dict.fromkeys(str_list)
# for i in str_dict.keys():
#     str_dict[i] = str_list.count(i)
# number_max = max(str_dict.values())
# for key,value in str_dict.items():
#     if value == number_max:
#         print u'出现次数最多的ip：',key,u'，出现次数',value,u'次'

# '''打印100以内的素数'''
# import math
# for num in xrange(2,101):
#     for i in xrange(1,int(math.sqrt(num)+1)):
#         if num % i == 0 and i!=1:
#             break
#         if i == int(math.sqrt(num)):
#             print num,

# '''实现一个简易版的计算器，
# 功能要求：加、减、乘、除，
# 支持多数同时进行计算
# '''
# def calculator(expressions):
#     operator = ['+','-','*','/']
#     if expressions.find('+') > -1:
#         L = expressions.rsplit('+',1)[0].strip()
#         R = expressions.rsplit('+',1)[1].strip()
#         return calculator(L)+calculator(R)
#     elif expressions.find('-') > 0 and expressions[expressions.find('-')-1] not in operator:
#         L = expressions.rsplit('-',1)[0].strip()
#         R = expressions.rsplit('-',1)[1].strip()
#         return calculator(L)-calculator(R)
#     elif expressions.find('*') > -1:
#         L = expressions.rsplit('*',1)[0].strip()
#         R = expressions.rsplit('*',1)[1].strip()
#         return calculator(L)*calculator(R)
#     elif expressions.find('/') > -1:
#         L = expressions.rsplit('/',1)[0].strip()
#         R = expressions.rsplit('/',1)[1].strip()
#         return calculator(L)/calculator(R)
#     else:
#         return float(expressions)
#  
# s = '-2.0/-3.0*-3+-4'
# print calculator(s)
# print eval(s)

# '''有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前20项之和
# '''
# def count_expression(n):
#     all_list = [1,2]
#     for index in xrange(2,n+1):
#         all_list.insert(index, all_list[index-1]+all_list[index-2])
#     return sum(map(lambda x,y:float(x)/y,all_list[1:],all_list[:-1]))
# 
# def count_expression(n):
#     numerator=2.0
#     denominator=1.0
#     sum=0
#     for i in range(n):
#         #print numerator,denominator
#         sum=sum+numerator/denominator
#         numerator,denominator=numerator+denominator,numerator
#     #print type(sum)
#     return sum
#
# print count_expression(20)

# s = 'I***LOVE***BEIJING'
# print '***'.join(s.split('***')[::-1])

# '''实心三角形'''
# import string
# def draw_solid_triangle(length):
#     '''draw a solid triangle'''
#     for i in xrange(1,length+1):
#         print string.center('*'*(2*i-1),2*length-1)
# 
# '''空心三角形'''
# import string
# def draw_hollow_triangle(length):
#     '''draw a hollow triangle'''
#     for i in xrange(1,length+1):
#         if i == 1:
#             print string.center('*',2*length-1)
#         elif i == length:
#             print string.center('*'+' *'*(i-1),2*length-1)
#         else:
#             print string.center('*'+' '*(2*(i-1)-1)+'*',2*length-1)
#             
# def print_hollow_triangle(n):
#     for i in range(n):
#         if i ==0:
#             print " "*20,"*"
#         elif i==n-1:
#             print " "*(20-i),'*'*(2*i+1) 
#             break
#         else:
#             print " "*(20-i),"*"+' '*(2*i-1)+"*" 
# 
# draw_hollow_triangle(4)
# print_hollow_triangle(5)

# 
# '''倒空心三角形'''
# import string
# def draw_upsidedown_triangle(length):
#     '''draw a upside down triangle'''
#     for i in xrange(length,0,-1):
#         if i == 1:
#             print string.center('*',2*length-1)
#         elif i == length:
#             print string.center('*'+' *'*(i-1),2*length-1)
#         else:
#             print string.center('*'+' '*(2*(i-1)-1)+'*',2*length-1)
# 
# length = 6
# draw_solid_triangle(length)
# draw_hollow_triangle(length)
# draw_upsidedown_triangle(length)

# '''画直角三角形（实心）'''
# def draw_solid_right_triangle(length):
#     """draw a solid right triangle"""
#     for i in xrange(1,length+1):
#         print '* '*i
# 
# '''画直角三角形（空心）'''
# def draw_hollow_right_triangle(length):
#     """draw a hollow right triangle"""
#     for i in xrange(1,length+1):
#         if i == 1:
#             print '*'
#         elif i == length:
#             print '* '*i
#         else:
#             print "*"+" "*(2*i-3)+"*"
#              
# draw_solid_right_triangle(5)
# draw_hollow_right_triangle(5)

# '''用*号输出字母C的图案'''
# def draw_letter_C(size):
#     """draw a letter C"""
#     for i in xrange(size,0,-1):
#         if i == size:
#             print ' '*i+'*'+' *'*i
#         else:
#             print ' '*i+'*'
#     for i in xrange(1,size+1):
#         if i == size:
#             print ' '*i+'*'+' *'*i
#         else:
#             print ' '*i+'*'
# draw_letter_C(5)

# '''打印N图案'''
# def draw_letter_N(size):
#     """draw a letter N"""
#     n = 2*size-3
#     for i in xrange(1,size+1):
#         m = 2*i-3
#         if i == 1 or i == size:
#             print '*'+' '*n+'*'
#         else:
#             print "*"+" "*m+"*"+" "*(n-m-1)+"*"
# 
# draw_letter_N(5)

# '''打印口图案'''
# def draw_square(length):
#     '''draw a square'''
#     if length == 1:
#         print '*'
#     else:
#         print '*'+' *'*(length-1)
#         for i in xrange(length-2):
#             print '*'+' '*(2*length-3)+'*'
#         print '*'+' *'*(length-1)
# 
# draw_square(5)

# '''打印H图案'''
# def draw_letter_H(size):
#     if size % 2 == 0:
#         print u"请输入一个奇数"
#     else:
#         for i in xrange(1,size+1):
#             if i == (size+1)/2:
#                 print " ".join("*"*((size-1)/2+2))
#             else:
#                 print "*"+" "*size+"*"
# 
# draw_letter_H(5)

# import string
# '''打印杨辉三角形
# 要求可以自定义行数'''
# def my_factorial(num):
#     '''n的阶乘'''
#     if num == 0:
#         return 1
#     else:
#         return reduce(lambda x,y:x*y,range(1,num+1),1)
#  
# def C(n, m):
#     '''C(n,m)'''
#     return my_factorial(n) / (my_factorial(n - m) * my_factorial(m))
#  
# def draw_pascal_triangle(rows):
#     """draw a Pascal's triangle"""
#     if rows == 1:
#         print "%d: " %1,
#         print 1
#     # last row
#     listb = []
#     for j in xrange(0,rows):
#         listb.append(str(C(rows-1,j)))
#     s = ' '.join(listb)
#     length = len(s)
#     for row in xrange(1,rows):
#         if row == 1:
#             print "%d: " %row,
#             print string.center("1",length)
#         if row == rows-1:
#             print "%d: " %(row+1),
#             print s
#         else:
#             lista = []
#             for j in xrange(0,row+1):
#                 lista.append(str(C(row,j)))
#             print "%d: " %(row+1),
#             print string.center(' '.join(lista),length)
#              
# draw_pascal_triangle(8)

# '''打印如图所示图案，
# 要求支持指定行数，
# 但行数必须是奇数行
# '''
# def draw_triangle(row):
#     if row % 2 ==1:
#         for i in xrange(1,((row+1)/2)+1):
#             print ' *'*(2*i-1)
#         for j in xrange(((row+1)/2)-1,0,-1):
#             print ' *'*(2*j-1)
#     else:
#         print u'不是奇数'
# 
# draw_triangle(5)
# draw_triangle(6)
# draw_triangle(7)

# '''要求实现一函数，
# 该函数用于求两个集合的差集，
# 结果集合中包含所有属于第一个集合
# 但不属于第二个集合的元素
# '''
# def get_difference_set(list_a,list_b):
#     list_c = []
#     for i in list_a:
#         if i in list_b:
#             continue
#         else:
#             list_c.insert(0,i)
#     return list_c
# list1 = [1,2,3,4,'abc','cde','a','b',(1,2,3),(12,4)]
# list2 = [1,2,'abc','a','c',32,(12,3),(12,4)]
# print get_difference_set(list1,list2)

# '''找出一段句子中最长的单词及其索引位置，
# 以list返回
# '''
# def get_the_longest_words(aString):
#     list_a = aString.split()
#     dict_a = {}
#     for i in list_a:
#         dict_a[i] = len(i)
#     longest = max(dict_a.values())
#     list_result = []
#     for word,length in dict_a.items():
#         if length == longest:
#             list_result.append(word)
#     return list_result
# 
# s = """And a youth said Speak to us of Friendship
# 
# Your friend is your needs answered
# 
# He is your field which you sow with love and reap with thanksgiving
# 
# And he is your board and your fireside 
# 
# For you come to him with your hunger and you seek him for peace 
# 
# When your friend speaks his mind you fear not the nay in your own mind, nor do you withhold the ay
# 
# And when he is silent your heart ceases not to listen to his heart 
# 
# For without words in friendship all thoughts all desires all expectations are born and shared with joy that is unacclaimed
# 
# When you part from your friend you grieve not
# 
# For that which you love most in him may be clearer in his absence as the mountain to the climber is clearer from the plain 
# 
# And let there be no purpose in friendship save the deepening of the spirit 
# 
# For love that seeks aught but the disclosure of its own mystery is not love but a net cast forth and only the unprofitable is caught 
# 
# And let your best be for your friend
# 
# If he must know the ebb of your tide let him know its flood also 
# 
# For what is your friend that you should seek him with hours to kill
# 
# Seek him always with hours to live 
# 
# For it is his to fill your need but not your emptiness
# 
# And in the sweetness of friendship let there be laughter and sharing of pleasures
# 
# For in the dew of little things the heart finds its morning and is refreshed"""
# 
# print get_the_longest_words(s)

# '''返回序列中的最大数'''
# def get_max(a):
#     if isinstance(a,basestring):
#         list_a = []
#         for i in a:
#             list_a.append(i)
#         return max(list_a)
#     elif isinstance(a,(list,tuple)):
#         return max(a)
#     else:
#         return 'Not sequence!'
# 
# print get_max('fwer42390fgFGWEROZh34thoi24cvsdnL')
# print get_max([1,2,3,4,5,'a','we','z','za'])
# print get_max((1,2,3,4,5,'a','we','z','za'))
# print get_max(u'你好哈哈哈分为若干非个人哦I高级肉在vsz')
# print get_max(123)
# print get_max({1:2,3:4})



















