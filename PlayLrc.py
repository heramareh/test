#encoding=utf-8
import re
import os
import time
import copy
import threading

import mp3play
import pygame
import sys
from pygame import mixer
import itertools

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
        print line

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
        while mixer.music.get_busy() == True:
            time.sleep(5)

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

def play(mp3_path, lrc_path):
    mixer.init()
    track = mp3play.load(mp3_path)
    track.play(100)
    if os.path.exists(lrc_path):
        lyrics = Lyrics(lrc_path)
        t_lyric = threading.Thread(target=lyrics.show_lyric)
        t_lyric.start()
        t_lyric.join()
    else:
        print u"not exists"

def __main__():
    play_list = [['G:\音乐\大约在冬季 - 王杰.mp3','G:\音乐\丁当-不是你的错.lrc'], ['G:\音乐\当你老了 - 赵照.mp3','G:\音乐\刀郎-守候在凌晨二点的伤心Show bar,lrc'], ['G:\音乐\断桥残雪 许嵩.mp3','G:\音乐\多亮-小情歌 (中国好声音).lrc']]
    play_list = itertools.cycle(play_list)
    play(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    __main__()