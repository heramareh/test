#encoding=utf-8

import urllib
import mp3play
import requests
import copy
import re
import threading
import traceback
import os, sys, random, time, eyed3
reload(sys)
sys.setdefaultencoding("utf8")

music_list_url = "http://fm.baidu.com/dev/api/?tn=playlist&format=json&id="
music_url = "http://music.baidu.com/data/music/fmlink?type=mp3&rate=320&songIds="

def get_music_list(channel_id):
    music_list = requests.get(music_list_url + channel_id).json()['list']
    return music_list

def get_music_info(music_id):
    try:
        content = requests.get(music_url + music_id).json()
        if content.has_key('data') and content['data']:
            music_info = content['data']['songList'][0]
            use_info = {}
            for i in ['songName', 'artistName', 'format', 'songLink', 'lrcLink', 'time']:
                use_info[i] = music_info[i]
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
                else:
                    break
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
    music_dir = "music"
    lrc_dir = "lrc"
    if not os.path.exists(music_dir):
        os.mkdir(music_dir)
    if not os.path.exists(lrc_dir):
        os.mkdir(lrc_dir)
    while True:
        try:
            for m in get_music_list(''):
                try:
                    music_info = get_music_info(str(m['id']))
                    if music_info:
                        seconds = music_info['time']
                        name = music_info['songName']
                        artistName = music_info['artistName']
                        music_name = os.path.join(music_dir, name + "_" + artistName + "." + music_info['format'])
                        music_lrc = os.path.join(lrc_dir, name + "_" + artistName + ".lrc")
                        if not os.path.exists(music_name):
                            urllib.urlretrieve(music_info['songLink'], music_name)
                            urllib.urlretrieve(music_info['lrcLink'], music_lrc)
                        music = mp3play.load(music_name)
                        music.volume(10)
                        os.system('cls')
                        print u"正在播放：" + name + "_" + artistName + "  " + str(seconds / 60).zfill(2) + ":" + str(seconds % 60).zfill(2)
                        music.play()
                        # print lrc_path
                        if os.path.exists(music_lrc):
                            lyrics = Lyrics(music_lrc)
                            t_lyric = threading.Thread(target=lyrics.show_lyric)
                            t_lyric.start()
                        else:
                            print u"加载歌词失败"
                        time.sleep(seconds)
                        music.stop()
                        os.system('cls')
                except:
                    music.stop()
                    lyrics.stop_show_lyric()
                    if os.path.exists(music_lrc):
                        os.remove(music_lrc)
                    if os.path.exists(music_name):
                        os.remove(music_name)
                    continue
                finally:
                    if os.path.exists(music_lrc):
                        os.remove(music_lrc)
                    if os.path.exists(music_name):
                        os.remove(music_name)
        except:
            music.stop()
            lyrics.stop_show_lyric()
            if os.path.exists(music_lrc):
                os.remove(music_lrc)
            if os.path.exists(music_name):
                os.remove(music_name)
            break
        finally:
            if os.path.exists(music_lrc):
                os.remove(music_lrc)
            if os.path.exists(music_name):
                os.remove(music_name)
            print u"退出程序。"
