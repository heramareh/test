#encoding=utf-8

import requests, os, re

# content = requests.get("http://yinyueshiting.baidu.com/data2/music/e26fda35fa09c06340a237859a76443e/542059395/277161118800128.mp3?xcode=2880a1f4ff562bb7f4316fffb8ff8771")
# print content.json()
def read_file(path):
    if not os.path.exists(path):
        print 'path : \'' + path + '\' not find.'
        return []
    content = ''
    try:
        with open(path, 'r') as fp:
            content += reduce(lambda x, y: x + y, fp)
    finally:
        fp.close()
    return content.split('\n')

def sort_lrc(content):
    TIME_AXIS_REGEXP = re.compile('\[\d+\:\d+\.\d+\]')
    DEL_TIME_AXIS_REGEXP = re.compile('(\[\d+\:\d+\.\d+\])*(.*)')
    content_sorted = []
    for i in content:
        for j in TIME_AXIS_REGEXP.findall(i):
            content_sorted.append(j + DEL_TIME_AXIS_REGEXP.findall(i)[0][1])
    content_sorted.sort()
    return content_sorted

if __name__ == "__main__":
    TIME_AXIS_REGEXP = re.compile('\[\d+\:\d+\.\d+\]')
    DEL_TIME_AXIS_REGEXP = re.compile('(\[\d+\:\d+\.\d+\])*(.*)')
    content_sorted = []
    for i in read_file(u"G:\music\火爆新歌\倍儿爽（Remix版）_大张伟.lrc"):
        for j in TIME_AXIS_REGEXP.findall(i):
            content_sorted.append(j + DEL_TIME_AXIS_REGEXP.findall(i)[0][1])
    content_sorted.sort()
    for k in content_sorted:
        print k