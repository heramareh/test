#encoding=utf-8
'''一个长度15个字符的字符串，顺序读取字符，
第一次打印1一个，第二次打印2个，第三次打印三个。。。类推，如果到结尾，则从开头继续打印。
注意每个字符只打印一次'''
# def print_str_method1(s,n):
#     s1 = s
#     for i in range(1,n+1):
#         result = ''
#         for j in range(i):
#             result += s1[0]
#             s1 = s1[1:]
#             if s1 == '':
#                 s1 = s
#         print result
# 
# def print_str_method2(s,n):
#     s = s*(sum(range(1,n+1))/len(s)+1)
#     start = 0
#     for i in range(1,n+1):
#         print s[start:start+i]
#         start += i
#  
# print_str_method1('abc',7)
# print_str_method2('abc',7)

# s="abcefghijklmnop"
# j=0
# start=0
# for i in range(1,8):
#     if start+j<=len(s):
#         print s[start:start+j+1]
#         j=j+1
#         start=start+j
#     else:
#         tmp1=s[start:len(s)]
#         length=len(s)-start
#         start=0
#         tmp2=s[start:i-length]
#         start = i-length
#         j=j+1
#         print tmp1+tmp2

'''实现strip函数'''
# import string
# def my_strip(s,strip_str=None):
#     if strip_str == None:
#         length=len(s)
#         for i in range(len(s)):
#             if s[i] not in string.whitespace:
#                 start = i
#                 break
#         for j in range(len(s)):
#             if s[length-1-j] not in string.whitespace:
#                 end = length-j
#                 break
#         if start > end:
#             return ''
#         else:
#             return s[start:end]
#         
# s1 = "\t\r\n      a  bc \t\n"
# print my_strip(s1)

# def string_strip(source_str,strip_str=None):
#     space_letter_list=[" ","\n","\r","\t"]
#     letter_list=list(source_str)
#     if strip_str is None:
#         for index in range(len(letter_list)):
#             if letter_list[index] in space_letter_list:
#                 letter_list[index]=""
#             else:
#                 break
#         for index in range(-1,-len(letter_list),-1):
#             if letter_list[index] in space_letter_list:
#                 letter_list[index]=""
#             else:
#                 break
#     else:
#         for index in range(len(letter_list)):
#             if letter_list[index]==strip_str:
#                 letter_list[index]=""
#             else:
#                 break
#         for index in range(-1,-len(letter_list),-1):
#             if letter_list[index]==strip_str:
#                 letter_list[index]=""
#             else:
#                 break
#     return "".join(letter_list)    
#      
# print "'%s'" %string_strip("\t\r\n  a \r\n\t b  \t\r\n ")  
# print "'%s'" %string_strip("**a*b**","*")  