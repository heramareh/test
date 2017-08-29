#encoding=utf-8
import ctypes
import inspect
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

PlayingMusic = ''
music = ''
seconds = 0

def get_all_musics(path):
    music_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".mp3") or file.endswith(".wma"):
                music_list.append(os.path.join(root, file))
    return music_list

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

def playMusic(music_name):
    global PlayingMusic, music, seconds
    try:
        if music_name != PlayingMusic:
            music = mp3play.load(music_name)
            music.volume(10)
            seconds = eyed3.load(music_name).info.time_secs
            if seconds > music.seconds():
                seconds = music.seconds()
            name = os.path.split(music_name)[1]
            print u"正在播放：" + name.decode('gbk') + "  " + str(seconds / 60).zfill(2) + ":" + str(seconds % 60).zfill(2)
        music.play()
        lrc_path = os.path.splitext(music_name)[0].decode('gbk')+u'.lrc'
        # print lrc_path
        if os.path.exists(lrc_path):
            lyrics = Lyrics(lrc_path)
            t_lyric = threading.Thread(target=lyrics.show_lyric)
            t_lyric.start()
        else:
            print u"加载歌词失败"
        time.sleep(seconds)
        music.stop()
    except KeyboardInterrupt:
        print u"退出"
        os.system("pause")
        raise
    except:
        print u"不支持的文件格式"
        print traceback.format_exc()
        os.system("pause")
        raise

def random_all(name):
    global PlayingMusic
    if os.path.exists(name):
        if os.path.isdir(name):
            music_list = get_all_musics(name)
        else:
            music_list = [name]
        while True:
                try:
                    music_name = random.choice(music_list)
                    playMusic(music_name)
                    PlayingMusic = music_name
                except:
                    break
    else:
        print u"目录/文件不存在"


if __name__ == "__main__":
    while True:
        try:
            for music in get_music_list(''):
                music_info = get_music_info(str(music['id']))
                if music_info:
                    # content = requests.get(music_info['songLink'])
                    num = str(random.randint(10000,99999))
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
                        print u"正在播放：" + name + "_" + artistName + "  " + str(seconds / 60).zfill(2) + ":" + str(seconds % 60).zfill(2)
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
                        time.sleep(5)
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
            break
        finally:
            if os.path.exists(lrcName):
                os.remove(lrcName)
            if os.path.exists(songName):
                os.remove(songName)
            print u"退出程序。"

