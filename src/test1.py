# encoding=utf-8
import os

def rename(path, newname, count):
    u'''批量修改文件名'''
    filenames = os.listdir(path)  # 获取目录下所有文件和文件夹
    for filename in filenames:
        if os.path.isdir(os.path.join(path, filename)):  # 检验给出的路径是一个文件还是目录，如果是目录跳过本次循环执行下一次循环
            continue
#       filetype = filename.split('.')[1]    #获取文件后缀名
#        print filetype
        for i in xrange(1, count):
            if filename.find('E' + str(i).zfill(2)) > -1:  # 关键字查找
                os.rename(os.path.join(path, filename), os.path.join(path, newname + u'第' + str(i) + u'集' + '.' + 'mkv'))  # 修改文件名
                break
            else:
                continue

# path = u'H:\迅雷下载\吸血鬼日记第一季'
newname = u'纸牌屋第四季' 
path = u'F:\\迅雷下载\\' + newname
count = 24
rename(path, newname, count)

