#encoding=utf-8
import copy
import re
import threading
import traceback
from pygame import mixer

import mp3play, os, sys, random, time, eyed3
reload(sys)
sys.setdefaultencoding("utf8")

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
    dir = raw_input("请输入歌曲目录：".decode('utf-8').encode('gbk'))
    try:
        random_all(dir)
    except:
        print traceback.format_exc()
        os.system("pause")

