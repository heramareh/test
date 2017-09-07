#encoding=utf-8
import mp3play
import requests, os, re

# content = requests.get("http://yinyueshiting.baidu.com/data2/music/e26fda35fa09c06340a237859a76443e/542059395/277161118800128.mp3?xcode=2880a1f4ff562bb7f4316fffb8ff8771")
# print content.json()
import time


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
    # TIME_AXIS_REGEXP = re.compile('\[\d+\:\d+\.\d+\]')
    # DEL_TIME_AXIS_REGEXP = re.compile('(\[\d+\:\d+\.\d+\])*(.*)')
    # content_sorted = []
    # for i in read_file(u"G:\music\火爆新歌\倍儿爽（Remix版）_大张伟.lrc"):
    #     for j in TIME_AXIS_REGEXP.findall(i):
    #         content_sorted.append(j + DEL_TIME_AXIS_REGEXP.findall(i)[0][1])
    # content_sorted.sort()
    # for k in content_sorted:
    #     print k
    url = "http://yinyueshiting.baidu.com/data2/music/e26fda35fa09c06340a237859a76443e/542059395/277161118800128.mp3?xcode=c9b11c6d023d4323a0cc505dc0621a48"
    import pygame
    # mp = Dispatch("WMPlayer.OCX")
    # tune = mp.newMedia(url)
    # mp.currentPlaylist.appendItem("G:\music\music\Breakdown_Jack Johnson.mp3")
    # mp.controls.play()
    pygame.mixer.init()
    track = pygame.mixer.music.load(url)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    time.sleep(20)
    pygame.mixer.music.stop()