#encoding=utf-8
import string

# def my_split(str,split_str=''):
#     new_str = string.replace(str,split_str,' ')
#     list_s = []
#     s = ''
#     if split_str == '':
#         for i in str:
#             if i != ' ':
#                 s+=i
#             else:
#                 if s != '':
#                     list_s.append(s)
#                     s = ''
#         list_s.append(s)
#         return list_s
#     else:
#         length = len(split_str)
#         while split_str in str:
#             index = str.find(split_str)
#             list_s.append(str[:index])
#             str = str[index+length:]
#         list_s.append(str)
#         return list_s
#  
# a='aabbccbbdd'
# b='a bb   cc bdd'
# c='a bb   cc b d     d'
# print my_split(a,'bb')
# print my_split(b)
# print my_split(c,'  ')

# def split_string(str,split_str=" "):
#     tmp=""   #存储切割后的字符串
#     length=len(split_str)  #计算一下被切割字符串的长度
#     result=[]     #存储切割后的结果
#     i=0   #循环每一个字符需要用到的初始化变量i
#     while i<=len(str)-1:   #遍历str中的每一个字符
#         if str[i:i+length]==split_str:  #当前字符位置+length-1个的字符串是否等于切割字符串
#             result.append(tmp)   #触发了if条件，说明遍历到了切割字符串的位置，把之前的字符串写入到result中
#             tmp=""  #清空，用于下次累加               
#             i+=length   #跳过length个长度，以此实现跳过分割的字符串，来继续遍历
#         else:
#             tmp+=str[i]  #触发else条件，说明不是切割点，需要存到tmp中
#             i+=1   #加一后跳到下一个字符继续遍历
#      
#     result.append(tmp) #把最后的tmp添加到result中
#     return result
# 
# print split_string("aabbccbbdd","bb")
# print split_string("aa bcc bdd")
# print split_string("aa bcc b       dd")
# print split_string("aa bcc b       dd","   ")

# method1
# def is_str(s):
#     return True if isinstance(s,basestring) else False
# 
# method2(更严谨，兼容判断类（可以做字符串加操作的类实例）)
# def is_str(s):
#     try:
#         s + ''
#         return True
#     except Exception,e:
#         return False
# 
# class newstring():
#     def __init__(self, value):
#         self.value=value
#     def __str__(self):
#         return self.value
#     def __add__(self,other):
#         return str(self.value)+str(other)
# 
# print is_str("a")
# print "*"*20
# print is_str(u"a")
# print "*"*20
# print is_str(0)
# print "*"*20
# print is_str(newstring(0))
# print type(newstring(0).value)

#实现replace函数
# def my_replace(s,old_str,new_str):
#     length = len(old_str)
#     list_s=[]
#     while old_str in s:
#         index = s.find(old_str)
#         list_s.append(s[:index]+new_str)
#         s = s[index+length:]
#     list_s.append(s)
#     return ''.join(list_s)

#实现replace函数
# def my_replace(s,old_str,new_str,count=None):
#     length = len(old_str)
#     result=[]
#     num = 0
#     while old_str in s:
#         if num == count:
#             break
#         index = s.find(old_str)
#         result.append(s[:index])
#         s = s[index+length:]
#         num += 1
#     result.append(s)
#     return new_str.join(result)
#  
# s='abcdabcdabcdab'
# print my_replace(s,'ab','z')
# print my_replace(s,'ab','z',0)
# print my_replace(s,'ab','000',2)
# print my_replace(s,'ab','123',[1,2,3])

#遍历字符串存放到列表里
# s = 'gloryroad123GLORYROAD'
# print [x for x in s]
# print [s[i] for i in range(len(s))]
# print list(s)

# print [s[i] for i in range(1,len(s),2)]
# print [s[i] for i in range(len(s)) if i%2!=0]

#将一个字符串偶数位字符大小写转换
# def swap_even_index_letter(s):
#     result=[]
#     for i in range(0,len(s)):
#         if i % 2 == 0:
#             ascii_num = ord(s[i])
#             if ascii_num>=65 and ascii_num<=91:
#                 result.append(chr(ascii_num+32))
#             elif ascii_num>=97 and ascii_num<=122:
#                 result.append(chr(ascii_num-32))
#             else:
#                 result.append(s[i])
#         else:
#             result.append(s[i])
#     return ''.join(result)
# 
#将一个字符串偶数位字符大小写转换
# def swap_even_index_letter(str):
#     str="gloryroad"
#     str=list(str)
#     for i in range(0,len(str),2):
#         if ord(str[i])>97 and ord(str[i])<122:
#             str[i]=chr(ord(str[i])-32)
#         elif ord(str[i])>65 and ord(str[i])<90:
#             str[i]=chr(ord(str[i])+32)
# 
#     return "".join(str)

# s = 'gloryroad123GLORYROAD'
# print swap_even_index_letter(s)

# s='abcdefg'
# print s[:3]+'C'+s[3:]

# s1='abcdefgcc'
# s2=''
# flag = True
# for i in s1:
#     if flag and i=='c':
#         s2+='f'
#         flag = False
#     else:
#         s2+=i
# print s2

#1-1000里包含3的有多少个数字
# count = 0
# for i in range(1,1001):
#     if '3' in str(i):
#         print i
#         count += 1
# print 'count:',count

#找到字符串中包含子串的所有索引值存到一个列表里
# def my_findall(s,child_str):
#     index_list = []
#     start = 0
#     length = len(child_str)
#     while True:
#         index = s.find(child_str,start)
#         if index == -1:
#             break
#         index_list.append(index)
#         start = index + length
#     return index_list
# 
# s='abdseabaaadcdeab'
# print my_findall(s,'a')

# s= 'I am a boy,and handsome!'
# print s.split()

#读取文件，返回文件内容行数跟内容总字符数
# def get_file_lines_count(filepath):
#     with open(filepath,'r') as f:
#         l = f.read()
#     print 'lines:',len(l.splitlines())
#     print 'count:',len(''.join(l.splitlines()))
# 
# get_file_lines_count(r'e:\text.txt')

# import string
# rule = string.maketrans('123','abc')
# print '112233grg'.translate(rule)
# print '11wqd2233grg123'.translate(rule,'grwdx')

# str = "this is string example....wow!!!"
# str = str.encode('base64','strict')
# print "Encoded String: " + str;
# print "Decoded String: " + str.decode('base64','strict')

'''1、将一个正整数分解质因数'''
# def get_primenumber(n):
#     primenumber_list = []
#     i = 2
#     while True:
#         if i == n:
#             primenumber_list.append(i)
#             break
#         if n % i == 0:
#             primenumber_list.append(i)
#             n = n / i
#         else:
#             i +=1
#     return list(set(primenumber_list))
# 
# print get_primenumber(12)
# print get_primenumber(8)
# print get_primenumber(7)

'''2、一个字符串中，分别输出奇数坐标字符或偶数坐标字符，奇数坐标的一行，偶数坐标的一行'''
s = 'abcdefg'
# print s[::2]+'\n'+s[1::2]

'''3、统计字符串中的字母、数字、其他字符个数'''
# def count_alpha_digit_other(s):
#     alpha = []
#     digit = []
#     other = []
#     for i in s:
#         if i.isalpha():
#             alpha.append(i)
#         elif i.isdigit():
#             digit.append(i)
#         else:
#             other.append(i)
#     print 'alpha',''.join(alpha),'count:',len(alpha)
#     print 'digit:',''.join(digit),'count:',len(digit)
#     print 'other:',''.join(other),'count:',len(other)
# 
# s = 'fwei4u3h33ognwv#*$)#@(%&$(THO'
# count_alpha_digit_other(s)

'''4、有一个已经排好序的列表。现输入一个数，要求按原来的规律将它插入列表中'''
# method1
# def my_insert(lista,n):
#     index = 0
#     lista.insert(0,n)
#     if lista[1]<=lista[len(lista)-1]:
#         for i in xrange(1,len(lista)):
#             if lista[index]<lista[i]:
#                 break
#             else:
#                 lista[index],lista[i]=lista[i],lista[index]
#                 index=i
#     else:
#         for i in xrange(1,len(lista)):
#             if lista[index]>lista[i]:
#                 break
#             else:
#                 lista[index],lista[i]=lista[i],lista[index]
#                 index=i
#     return lista
# method2
# def my_insert(lista,n):
#     lista.append(n)
#     if lista[0]<=lista[len(lista)-1]:
#         return sorted(lista)
#     else:
#         return sorted(lista,reverse=True)
# la=[2,5,7,9,10,34,35]
# lb=[34,21,21,21,19,15,7]
# n=21
# print my_insert(la,n)
# print my_insert(lb,n)

'''5、统计名字列表中，各名字的首字母在名字列表中出现的次数'''
# def count_first_letter_in_namelist(namelist):
#     first_letter_list = []
#     for i in namelist:
#         first_letter_list.append(i[0].upper())
#     first_letter_dict = dict.fromkeys(first_letter_list)
#     for i in sorted(first_letter_dict.keys()):
#         first_letter_dict[i]=first_letter_list.count(i)
#         print 'letter:',i,', count:',first_letter_dict[i]
# 
# la=['kobe','jordan','lily','lilei','hanmeimei','xiaoming','laowang','tudou','xihongshi','jidan','zhangsan','lisi','wangwu']
# count_first_letter_in_namelist(la)

'''6、字符替换
1）读入一个字符串
2）去掉字符串的前后空格
3）如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此类推
4）将字符串使用空格进行切分，存到一个列表，然后使用*号连接，并输出
5）把这些功能封装到一个函数里面，把执行结果作为返回值
'''
# def my_replace():
#     s = raw_input("input a str: ").strip(" ")
#     lista = []
#     for i in s:
#         if i.isdigit() and i !='0':
#             lista.append(chr(ord(i)+48))
#         else:
#             lista.append(i)
#     listb = ''.join(lista).split(" ")
#     for i in range(len(listb)):
#         if listb[i].isdigit() and listb[i] != '0':
#             listb[i] = chr(ord(i)+48)
#     return '*'.join(listb)
# 
# print my_replace()

'''7、找出字符串中出现次数最多的字符，并输出其出现的位置'''
# def find_the_most_chr(s):
#     d = dict.fromkeys(s,0)
#     for i in d.keys():
#         d[i] = s.count(i)
#     for key,value in d.items():
#         if value == max(d.values()):
#             print "the most chr:",key,
#             lista=[]
#             for j in range(len(s)):
#                 if s[j] == key:
#                     lista.append(j)
#             print ", index:",lista
# 
# s = 'aabbcdebf11223'
# find_the_most_chr(s)

'''8、找出一段句子中最长的单词及其索引位置，以字典返回'''
# def find_the_longest_words(s):
#     s1=''
#     for i in s:
#         if i == "'":
#             s1 += i
#             continue
#         if not i.isalpha():
#             s1 += ' '
#         else:
#             s1 += i
#     print s1
#     lista = s1.split()
#     print lista
#     d = dict.fromkeys(lista)
#     for i in d.keys():
#         d[i] = len(i)
#     longest = max(d.values())
#     for i in d.keys():
#         if d[i] != longest:
#             del d[i]
#     for i in d.keys():
#         index_list = []
#         index = 0
#         for j in range(s1.count(i)):
#             index = s1.find(i,index)
#             index_list.append(index)
#             index += longest
#         d[i] = index_list
#     return d
# 
# s = "There are moments necessarily necessarily  in life when you miss someone so much that you just want to pick them from your dreams and hug them for real!"
# print find_the_longest_words(s)

'''10、实现字符串的upper、lower以及swapcase方法'''
# def my_upper(s):
#     try:
#         if not isinstance(s, basestring):
#             raise Exception("expected a string")
#         lista = []
#         for i in range(len(s)):
#             if ord(s[i]) >=97 and ord(s[i]) <=122:
#                 lista.append(chr(ord(s[i])-32))
#             else:
#                 lista.append(s[i])
#         return ''.join(lista)
#     except Exception,e:
#         return "TypeError: " + str(e)
#  
# def my_lower(s):
#     try:
#         if not isinstance(s, basestring):
#             raise Exception("expected a string")
#         lista = list(s)
#         for i in range(len(lista)):
#             if lista[i] in string.uppercase:
#                 lista[i] = chr(ord(lista[i])+32)
#         return ''.join(lista)
#     except Exception,e:
#         return "TypeError: " + str(e)
#  
# def my_swapcase(s):
#     try:
#         if not isinstance(s, basestring):
#             raise Exception("expected a string")
#         lista = list(s)
#         for i in range(len(lista)):
#             if lista[i] in string.uppercase:
#                 lista[i] = chr(ord(lista[i])+32)
#             elif lista[i] in string.lowercase:
#                 lista[i] = chr(ord(lista[i])-32)
#         return ''.join(lista)
#     except Exception,e:
#         return "TypeError: " + str(e)
#  
# s = 'Hello World 123 !'
# print my_lower(123)
# print my_upper({})
# print my_swapcase(s)

'''11、实现字符串的find方法'''
# def my_find(s, sub, start=None, end=None):
#     try: 
#         if not isinstance(s, basestring) or not isinstance(sub, basestring):
#             raise Exception("expected a string")
#         length = len(sub)
#         # 特殊情况处理：sub为空时
#         if length == 0 and start <= len(s):
#             if start is None:
#                 return 0
#             else:
#                 return start
#         s1 = s[start:end]
#         for i in xrange(len(s1)):
#             if sub == s1[i:i+length]:
#                 if start == None:
#                     return i
#                 else:
#                     return i + start
#         return -1
#     except Exception,e:
#         return "TypeError: " + str(e)
# print my_find('12 3','',1)
