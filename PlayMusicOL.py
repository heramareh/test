#encoding=utf-8
import copy
import random
import re
import threading
import traceback
import mp3play
import requests
import urllib
import os,sys
import time
reload(sys)
sys.setdefaultencoding("utf8")

channel_list_url = "http://fm.baidu.com/dev/api/?tn=channellist"
music_list_url = "http://fm.baidu.com/dev/api/?tn=playlist&format=json&id="
music_url = "http://music.baidu.com/data/music/fmlink?type=mp3&rate=320&songIds="
count = 0
def get_channel_list():
    channel_list = requests.get(channel_list_url).json()['channel_list']
    return channel_list

def get_music_list(channel_id):
    music_list = requests.get(music_list_url + channel_id).json()['list']
    return music_list

def get_music_info(music_id):
    global count
    try:
        content = requests.get(music_url + music_id).json()
        if content.has_key('data') and content['data']:
            music_info = content['data']['songList'][0]
            use_info = {}
            for i in ['songName', 'artistName', 'format', 'songLink', 'lrcLink', 'time']:
                use_info[i] = music_info[i]
            count += 1
            return use_info
        return None
    except:
        return None

def sort_lrc(content):
    TIME_AXIS_REGEXP = re.compile('\[\d+\:\d+\.\d+\]')
    DEL_TIME_AXIS_REGEXP = re.compile('(\[\d+\:\d+\.\d+\])*(.*)')
    content_sorted = []
    for i in content:
        for j in TIME_AXIS_REGEXP.findall(i):
            content_sorted.append(j + DEL_TIME_AXIS_REGEXP.findall(i)[0][1])
    content_sorted.sort()
    return content_sorted

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
    return sort_lrc(content.split('\n'))

class Lyrics:
    TIME_AXIS_REGEXP = re.compile('\[(\d+)\:(\d+)\.(\d+)\]')
    DEL_TIME_AXIS_REGEXP = re.compile('\[\d+\:\d+\.\d+\](.*)')

    def __init__(self, path):
        self.path = path
        self.stop = False

    def _get_time_diff(self, line):
        tm = map(lambda each: map(int, each), self.TIME_AXIS_REGEXP.findall(line))
        tm = map(lambda each: each[0] * 60 * 1000 + each[1] * 1000 + each[2], tm)
        return (tm[0], line)

    def _show_lyric(self, line):
        print line.decode()

    def static_lyric(self, lyrics):
        for line in lyrics:
            self._show_lyric(line)

    def dynamic_lyric(self, lyrics):
        for line in lyrics:
            try:
                time.sleep(float(line[0]) / 1000.0)
                if not self.stop:
                    self._show_lyric(line[1])
            except:
                pass

    def get_lyric(self):
        lyrics = read_file(self.path)
        tmp_lyric = lyrics
        lyrics = filter(lambda line: len(self.TIME_AXIS_REGEXP.findall(line))!=0, lyrics)
        if len(lyrics) == 0:
            return False, tmp_lyric
        lyrics = map(self._get_time_diff, lyrics)
        tmp_lyric = copy.deepcopy(lyrics[:-1])
        tmp_lyric.insert(0, (0, ''))
        lyrics = map(lambda x: (x[0][0]-x[1][0], x[0][1]), zip(lyrics, tmp_lyric))
        lyrics = map(lambda x: (x[0], self.DEL_TIME_AXIS_REGEXP.findall(x[1])[0]), lyrics)
        return True, lyrics

    def show_lyric(self):
        play_option, lyrics = self.get_lyric()
        if play_option == True:
            self.dynamic_lyric(lyrics)
        else:
            self.static_lyric(lyrics)

    def stop_show_lyric(self):
        self.stop = True

if __name__ == "__main__":
    # get_channel_list()
    # print requests.get(category_url+"public_tuijian_rege").json()
    # link = requests.get(music_url+"277161").json()['data']['songList'][0]['songLink']
    # pygame.mixer.Sound(link).play()
    channel_list = get_channel_list()
    channel_names = []
    channel_dict = {}
    all_music_info = []
    for channel in channel_list:
        channel_name = channel['channel_name']
        # print isinstance(channel_name,str)
        channel_id = channel['channel_id']
        channel_names.append(channel_name)
        channel_dict[channel_name] = channel_id
    print u"***************************************************"
    print u"* 1、输入“all”，随机播放所有歌曲"
    print u"* 2、输入“类别名称”，随机播放指定类别的歌曲"
    print u"* 3、输入“q”，退出程序"
    print u"* 歌曲类别列表："
    for id, i in enumerate(channel_names):
        if id % 5 == 0:
            if id != 0:
                print
            print "*    ", i,
        else:
            print i,
    print
    print u"***************************************************"
    n = 1
    while n:
        name = raw_input("请输入：".decode('utf8').encode('gbk')).decode("gbk").strip()
        name_list = []
        if name == 'all':
            name_list = channel_names
        elif name == 'q':
            break
        elif name in channel_names:
            name_list.append(name)
        else:
            print u"输入有误，请重新输入："
            continue

        while True:
            name = random.choice(name_list)
            music_list = get_music_list(channel_dict[name])
            m = random.choice(music_list)
            try:
                music_info = get_music_info(str(m['id']))
                if music_info:
                    # content = requests.get(music_info['songLink'])
                    num = str(random.randint(10000, 99999))
                    songName = num + "." + music_info['format']
                    lrcName = num + ".lrc"
                    urllib.urlretrieve(music_info['songLink'], songName)
                    urllib.urlretrieve(music_info['lrcLink'], lrcName)
                    if os.path.exists(songName):
                        music = mp3play.load(songName)
                        music.volume(10)
                        seconds = music_info['time']
                        name = music_info['songName']
                        artistName = music_info['artistName']
                        os.system('cls')
                        print u"正在播放：" + name + "_" + artistName + "  " + str(seconds / 60).zfill(2) + ":" + str(
                            seconds % 60).zfill(2)
                        music.play()
                        # print lrc_path
                        if os.path.exists(lrcName):
                            lyrics = Lyrics(lrcName)
                            t_lyric = threading.Thread(target=lyrics.show_lyric)
                            t_lyric.start()
                        else:
                            print u"加载歌词失败"
                        time.sleep(seconds)
                        music.stop()
                        os.system('cls')
                        if os.path.exists(lrcName):
                            os.remove(lrcName)
                        os.remove(songName)
            except:
                music.stop()
                lyrics.stop_show_lyric()
                if os.path.exists(lrcName):
                    os.remove(lrcName)
                if os.path.exists(songName):
                    os.remove(songName)
                continue
            finally:
                if os.path.exists(lrcName):
                    os.remove(lrcName)
                if os.path.exists(songName):
                    os.remove(songName)
                n = 0

    print u"退出程序。"


