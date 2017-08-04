#encoding=utf-8

# def bianli(lista):
#     global listb
#     for i in lista:
#         if isinstance(i,(list,tuple)):
#             bianli(i)
#         else:
#             listb.append(i)
# 
# listb = []
# bianli([1,2,[3,[4,5,[6,7]]],8])
# print listb

# listb=[(1,5,3),(1,2,3,4),(2,54,6,3,2),(6,5)]
# 
# def L(t):
#     return t[-1]*5
# listb.sort(key=lambda x:x[-1]*5,reverse=True)
# print listb

# '''
# 1:增加新书
# 2：借书
# 3：还书
# 4：查看所有的书
# '''
# booklist=[]
# def add(name):
#     booklist.append(name)
# 
# def delete(name):
#     if name in booklist:
#         booklist.remove(name)
#         print u'借阅成功'
#     else:
#         print u'没有此书'
# 
# def count():
#     return len(booklist)
# 
# def name_list():
#     if count() == 0:
#         print u'目前图书馆没有书'
#     else:
#         print u'目前共有图书：',len(booklist),u'册'
#         for i in booklist.keyforms():
#             print i,':',booklist.count(i),u'册'
# 
# while 1:
#     print '''1:增加新书，2：借书，3：还书，4：查看共有多少书，5：查看所有书名'''
#     try:
#         n = int(raw_input('请输入要做的操作：'))
#         if n == 1:
#             name = raw_input('请输入要增加的书名：')
#             add(name)
#             print u'添加成功'
#         elif n == 2:
#             name = raw_input('请输入要借阅的书名：')
#             delete(name)
#         elif n == 3:
#             name = raw_input('请输入要归还的书名：')
#             add(name)
#             print u'归还成功'
#         elif n == 4:
#             print u'目前共有图书：',count(),u'册'
#         elif n == 5:
#             name_list()
#         else:
#             print u'输入有误，请重新输入'
#     except Exception,e:
#         print u'输入有误，请重新输入'

# def odd():
#     print 'step 1'
#     yield 1
#     print 'step 2'
#     yield 3
#     print 'step 3'
#     yield 5
# o = odd()
# print o.next()
# print o.next()
# print o.next()
# print o.next()
# for i in o:
#     print i   #可以遍历执行函数

# for i,value in enumerate(['a','b','c'],1):
#     print i,value

# import copy  
# a = [1, 2, 3, 4, ['a', 'b']] #原始对象  
#   
# b = a #赋值，传对象的引用  
# c = copy.copy(a) #对象拷贝，浅拷贝  
# d = copy.deepcopy(a) #对象拷贝，深拷贝  
#   
# a.append(5) #修改对象a  
# a[4].append('c') #修改对象a中的['a', 'b']数组对象  
#   
# print 'a = ', a  
# print 'b = ', b  
# print 'c = ', c  
# print 'd = ', d 
# import copy
# a = [1,2,3,['a','b','c']]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# a.append(4)
# a[3].append('d')
# print a
# print b
# print c
# print d

'''3 ：找到两个列表中不同的元素和相同元素'''
# def find(lista,listb):
#     list_difference=[]
#     list_equal=[]
#     for i in lista:
#         if i not in listb:
#             list_difference.append(i)
#         else:
#             list_equal.append(i)
#     for j in listb:
#         if j not in lista:
#             list_difference.append(j)
#     return list_difference,list_equal
#  
# a = [1,2,3,4,5,'a','b',['1','c']]
# b = [2,3,'b','d',['e','df']]
# difference,equal = find(a,b)
# print 'difference:',difference
# print 'equal:',equal

'''4：数字和字母混合的list中，
奇数位加1，偶数位加2'''
# lista=[1,2,3,4,2.34,2.32,1+2j,1+3j,'a','bc','ds3',34,2,'fer']
# for i in range(0,len(lista),2):
#     if isinstance(lista[i],(int,float,complex,long)):
#         lista[i] += 1
#     else:
#         lista[i] += '1'
# for i in range(1,len(lista),2):
#     if isinstance(lista[i],(int,float,complex,long)):
#         lista[i] += 2
#     else:
#         lista[i] += '2'
# print lista

'''5：递归处理嵌套的list'''
# def bianli(lista):
#     for i in lista:
#         if not isinstance(i,list):
#             print i,
#         else:
#             bianli(i)
# alist=[1,2,3,4,['a','b','c'],'dsf',['s',[1,2,3]]]
# bianli(alist)

'''6:遍历list，
但是list中元素的数据类型不定，
有可能有嵌套的list，tuple，dict等'''
# def bianli(lista):
#     global result_list
#     for i in lista:
#         if isinstance(i,(list,tuple)):
#             bianli(i)
#         else:
#             result_list.append(i)
#  
# result_list=[]
# alist=[1,2,3,4,['a','b','c'],'dsf',['s',(1,2,3)]]
# bianli(alist)
# print result_list

'''7: 通过遍历list去掉重复部分'''
# def distinct(lista):
#     listb=[]
#     for i in lista:
#         if i not in listb:
#             listb.append(i)
#         else:
#             continue
#     return listb
#  
# alist=[1,1,1,1,1,1,[1,2,3],[1,2,3],'a','a','a','b','fse']
# print distinct(alist)

'''8：1个纯数字的list中，
分别输出奇数坐标字符或偶数坐标字符'''
# lista=[1,2,3,4,1.1,2.3,2.4,23,42,1+2j,2+34j]
# odd_number=[]
# even_number=[]
# for i in xrange(len(lista)):
#     if i % 2 == 0:
#         odd_number.append(str(lista[i]))
#     else:
#         even_number.append(str(lista[i]))
# print 'odd number:',odd_number
# print 'even number:',even_number

'''9：找到序列中最大的元素'''
# def my_max(s):
#     if isinstance(s,basestring):
#         s = list(s)
#     for i in range(len(s)-1):
#         if s[i]>s[i+1]:
#             s[i],s[i+1]=s[i+1],s[i]
#     return s[-1]
#  
# lista=[1,2,3,4,1.1,2.3,2.4,23,424,3,5,3,2]
# a='fweg423tg43gj3rg0vra9'
# print my_max(lista)
# print my_max(a)

'''10：返回列表中第二大元素'''
# def second_max(lista):
#     s = list(set(lista))
#     for i in xrange(0,2):
#         for j in xrange(len(s)-1-i):
#             if s[j]>s[j+1]:
#                 s[j],s[j+1]=s[j+1],s[j]
#     return s[-2]
# 
# lista=[1,2,3,23,21,1.1,2.3,2.4,23,23,3,5,3,21]
# print second_max(lista)

'''11：键盘读入一字符串，逆序输出'''
# print raw_input('input a str:')[::-1]

'''1、从键盘输入两个数，并比较其大小，直到输入e/E退出程序 '''
# while True:
#     try:
#         nums = raw_input('input num1,num2(e/E exit): ')
#         if nums in 'eE' and nums != '':
#             print 'exit!'
#             break
#         num1=float(nums.split(',',1)[0])
#         num2=float(nums.split(',',1)[1])
#         if num1 < num2:
#             print '%s < %s' %(str(num1).rstrip('.0'),str(num2).rstrip('.0'))
#         elif num1 == num2:
#             print '%s = %s' %(str(num1).rstrip('.0'),str(num2).rstrip('.0'))
#         else:
#             print '%s > %s' %(str(num1).rstrip('.0'),str(num2).rstrip('.0'))
#     except Exception,e:
#         print 'input error,please re input!'

'''2、请写一个函数，
第一个参数为一个字母，另外一个参数为一个数字n，
请返回这个字母后的第n个字母，
如果达到字母表的末尾，则从头开始选取字母'''
# import string
# def get_letter(letter,n):
#     index = string.lowercase.index(letter.lower())
#     if letter in string.lowercase:
#         return (string.lowercase*((index+n)/26+1))[index+n]
#     else:
#         return (string.uppercase*((index+n)/26+1))[index+n]
#           
# letter='a'
# n=26
# print get_letter(letter,n)

'''3、分别输出字符串中奇数坐标和偶数坐标的字符 '''
# s = 'vfwrefg324tf'
# print 'odd_string: ',s[::2]
# print 'even_string: ',s[1::2]

'''4、打印杨辉三角形
要求可以自定义行数'''
# def my_factorial(n):
#     u'''n的阶乘'''
#     if n ==0 or n == 1:
#         return 1
#     return n * my_factorial(n-1)
#    
# def C(n, m):
#     return my_factorial(n) / (my_factorial(n - m) * my_factorial(m))
#    
# def draw_pascal_triangle(rows):
#     for row in xrange(rows):
#         print '  '*(rows-row-1),
#         for i in xrange(row+1):
#             print str(C(row,i)).ljust(3,' '),
#         print
#    
# draw_pascal_triangle(12)

'''5、将一个多重嵌套的列表的元素进行互换，
存到另一个同等维度的嵌套列表中，
例如：[[1,2,3],[4,5,6]]
互换后变成[[1,4],[2,5],[3,6]] '''
# method1
# def transposition(lista):
#     listb=[]
#     for col in xrange(len(lista)):
#         listc=[]
#         for row in xrange(len(lista[0])):
#             listc.append(lista[row][col])
#         listb.append(listc)
#     return listb
#   
# lista=[[1,2,3],[4,5,6],[7,8,9]]
# print transposition(lista)
# 
# method2
# print eval(str(eval('zip('+str(lista)[1:-1]+')')).replace('(','[').replace(')',']'))

'''6、有一个3 x 4的矩阵，
要求编程求出其中值最大的那个元素的值，
以及其所在的行号和列号，
矩阵可以通过嵌套列表来模拟'''
# def my_max(lista):
#     n = lista[0][0]
#     for row in xrange(len(lista)):
#         for col in xrange(len(lista[0])):
#             if n < lista[row][col]:
#                 n = lista[row][col]
#                 r = row+1
#                 c = col+1
#     return n,r,c
# lista = [[2,5,3,56],[5,4,32,2],[5,7,8,4]]
# print u'最大值：',my_max(lista)[0]
# print u'行号：',my_max(lista)[1],u'列号：',my_max(lista)[2]

'''7、递归实现列表求和'''
# def my_sum(lista):
#     if len(lista) == 1:
#         return lista[0]
#     return lista[0]+my_sum(lista[1:])
#  
# lista=[1,2,3,4,5]
# print my_sum(lista)

'''8、打印斐波拉契数列前n项'''
# def fibonacci_sequence(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)
#  
# n=8
# print u'斐波拉契数列前%d项:' %n
# print ', '.join([str(fibonacci_sequence(i)) for i in xrange(1,n+1)])

'''9、检查ipV4的有效性，有效则返回True，否则返回False'''
# def is_ipv4(ip):
#     try:
#         lista = ip.split('.')
#         if len(lista) != 4:
#             return False
#         for i in xrange(4):
#             lista[i] = int(lista[i])
#         if lista[0]<=0 or lista[0]>255:
#             return False
#         for i in lista[1:3]:
#             if i<0 or i>255:
#                 return False
#         if lista[3]<=0 or lista[3]>254:
#             return False
#         else:
#             return True
#     except Exception,e:
#         return False
#  
# while 1:
#     ip = raw_input('ip: ')
#     print is_ipv4(ip)

'''10、检测密码强度
c1 : 长度>=8
c2: 包含数字和字母
c3: 其他可见的特殊字符
强：满足c1,c2,c3
中: 只满足任一2个条件
弱：只满足任一1个或0个条件'''
# import string
# def check_pwd(pwd):
#     n = 0
#     if len(pwd) >= 8:
#         n += 1
#     flag1 = False
#     flag2 = False
#     for i in pwd:
#         if not flag1 and i in string.letters:
#             flag1 = True
#         if not flag2 and i in string.digits:
#             flag2 = True
#         if flag1 and flag2:
#             n += 1
#             break
#     for i in pwd:
#         if i in string.punctuation:
#             n += 1
#             break
#     if n <= 1:
#         return u'弱'
#     elif n == 2:
#         return u'中'
#     else:
#         return u'强'
#  
# while 1:
#     print check_pwd(raw_input('input password: '))

'''11、返回列表中第二大元素'''
# method5
# def get_second_max(s):
#     lista = list(set(s))
#     for i in xrange(2):
#         for j in xrange(len(lista)-1-i):
#             if lista[j]>lista[j+1]:
#                 lista[j],lista[j+1]=lista[j+1],lista[j]
#     return lista[-2]
#   
# s=[1,3,23,4,32,2,4,23,13,1,32,4,2,31,3]
# print get_second_max(s)
#  
# a=[1,2,3,4,4,5,5,5,6,6,6]
#  
# method1
#  
# max_value=max(a)
# while 1:
#     if max_value in a:
#         a.remove(max_value)
#     else:
#         break
#   
# print max(a)
#  
# method2
#  
# a=[1,2,3,4,4,5,5,5,6,6,6]
# a.sort()
#   
# for i in a[::-1]:
#     if i!=max(a):
#         print i
#         break
#  
# method3
#  
# a=[2,5,8,8,0,5]
# b=set(a)
# b.remove(max(b))
# print max(b)
#  
# method4
#  
# sorted(set(a))[-2]

'''12、已知一字符串列表list1 = ['a','b','c','d', 'e', 'f', 'g']，
对序列的任一子序列list1[start, end]中的元素进行排列组合，
有多少种不同的组合，请分别输出。
（start >= 0, end < len(list1)）'''
# result=[]
# def permutation(lista):
#     global result
#     if len(lista) == 1:
#         result.append(lista[0])
#         print result
#         del result[-1]
#     else:
#         for i in lista:
#             result.append(i)
#             listb = lista[:]
#             listb.remove(i)
#             permutation(listb),
#             del result[-1]
#  
# list1 = ['a','b','c','d', 'e', 'f', 'g']
# permutation(list1[2::2])

'''13、判断一个字符串是否为回文字符串
所谓回文字符串，就是一个字符串，从左到右读和从右到左读是完全一样的。
比如"level" 、 “aaabbaaa”'''
# def is_palindrome_str(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False
#  
# def is_palindrome_str(s):
#     return True if s == s[::-1] else False
# 
# print is_palindrome_str('agregf')
# print is_palindrome_str('aaabbaaa')
# print is_palindrome_str('level')

'''14、实现合并同类型的有序列表算法，要求不能有重复元素'''
# def merge(s1,s2):
#     t = str(type(s1))[7:-2]
#     s3 = str(set(s1+s2))
#     return t+'('+s3+')'
#  
# print eval(merge((1,2,3,4,5,'a','b'),(2,3,45,576,'a','c')))
# print eval(merge([1,2,3,4,5,'a'],[2,3,45,576,'a','c']))

# def merge(s1,s2):
#     return eval(str(type(s1))[7:-2]+'('+str(set(s1+s2))+')')
#   
# print merge((1,2,3,4,5,'a','b'),(2,3,45,576,'a','c'))
# print merge([1,2,3,4,5,'a'],[2,3,45,576,('a','c')])

'''15、有4个圆锥塔，
圆心分别为（20,20）、（-20,20）、（-20,-20）、（20，-20），
圆半径为10m，见下图。
这4个塔的高度为100m，塔以外无建筑物。
今输入任一点坐标，求该点的建筑高度（塔外的高度为0），
结果不需要特别精确，只需要考虑坐标为整数的情况'''
# import math
# def get_high(x,y):
#     d = math.sqrt((20-abs(x))**2+(20-abs(y))**2)
#     if d >= 10:
#         return 0
#     return (10-d)*100/10
#  
# def get_high(x,y):
#     d = math.sqrt((20-abs(x))**2+(20-abs(y))**2)
#     return 0 if d>=10 else (10-d)*100/10
# 
# print get_high(10,10)
# print get_high(-20,20)
# print get_high(-15,-15)
# print get_high(-30,20)

'''16、一个数如果恰好等于它的因子之和，这个数就称为完数，
例如6的因子为1,2,3，而6=1+2+3，因此6是完数，
编程找出1000之内的所有完数，
并按6 its factors are 1,2,3这样的格式输出'''
# def perfect_number(num):
#     for i in xrange(2,num+1):
#         lista = [str(j) for j in xrange(1,i) if i%j==0]
#         if eval('+'.join(lista)) == i:
#             print i,"its factors are",','.join(lista)
#  
# perfect_number(1000)

'''17、使用二分法实现在一个有序列表中查找指定的元素'''
# def find(lista,key):
#     n = len(lista)
#     index = n/2
#     while index >= 0 and index <n:
#         if key == lista[index]:
#             return index
#         elif key > lista[index]:
#             index = (n+index+1)/2
#         else:
#             index = (index-1)/2
#     return -1
#
# print find([1,2],1)
# print find([1,2],0)
# print find([1,2],3)
# print find([1,2,3,4,5,6,7],1)
# print find([1,2,3,4,5,6,7],4)
# print find([1,2,3,4,5,6,7],7)
# print find([1,2,3,4,5,6,7],0)
# print find([1,2,3,4,5,6,7],8)
# print find([1,2,3,4,5,6,7,8],1)
# print find([1,2,3,4,5,6,7,8],5)
# print find([1,2,3,4,5,6,7,8],8)
# print find([1,2,3,4,5,6,7,8],9)
# print find([1,2,3,4,5,6,7,8],0)

'''18、分离list1与list2中相同部分与不同部分'''
# def separate(list1,list2):
#     list3=[]
#     list4=[]
#     for i in list1:
#         if i in list2:
#             list3.append(i)
#         else:
#             list4.append(i)
#     for j in list2:
#         if j not in list1:
#             list4.append(j)
#     return set(list3),set(list4)
#  
# la=[1,2,3,4,5,9,9]
# lb=[1,2,5,6,7,8,9,10,10]
# print u'相同部分：%s\n不同部分：%s' % separate(la,lb)

'''19、找出一个多维数组的鞍点，即该位置上的元素在该行上最大，在该列上最小，也可能没有鞍点'''
# def find_saddle_point(arr):
#     points = []
#     for i in xrange(len(arr)):
#         cols = [j for j in xrange(len(arr[i])) if arr[i][j] == max(arr[i])]
#         for col in cols:
#             if arr[i][col] == min([arr[k][col] for k in xrange(len(arr))]):
#                 points.append(("row:%d," %(i+1)+"col:%d," %(col+1)+"value:"+str(arr[i][col])))
#     if len(points) == 0:
#         return
#     return points
#  
# arr=[[1,14,3,14],[5,8,7,8],[9,10,11,12]]
# print find_saddle_point(arr)

'''20、写一个函数，识别输入字符串是否是符合 python 语法的变量名'''
# import string
# import keyword
# def is_var(s):
#     s = s.strip()
#     if s in keyword.kwlist:
#         return False
#     if s == '' or s[0] not in string.letters+"_":
#         return False
#     for i in s[1:]:
#         if i not in string.letters+string.digits+"_":
#             return False
#     return True
#   
# while True:
#     print is_var(raw_input('input:'))
