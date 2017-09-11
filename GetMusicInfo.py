#encoding=utf-8

import MySQLdb
import requests
import copy
import re
import traceback
import os, sys, time
reload(sys)
sys.setdefaultencoding("utf8")

channel_list_url = "http://fm.baidu.com/dev/api/?tn=channellist"
music_list_url = "http://fm.baidu.com/dev/api/?tn=playlist&format=json&id="
music_url = "http://music.baidu.com/data/music/fmlink?type=mp3&rate=320&songIds="
create_table = """CREATE TABLE `music_info` (
  `queryId` VARCHAR(100) DEFAULT NULL,
  `songId` VARCHAR(100) NOT NULL,
  `songName` VARCHAR(100) NOT NULL,
  `artistId` VARCHAR(100) DEFAULT NULL,
  `artistName` VARCHAR(100) DEFAULT NULL,
  `albumId` VARCHAR(100) DEFAULT NULL,
  `albumName` VARCHAR(100) DEFAULT NULL,
  `songPicSmall` VARCHAR(500) DEFAULT NULL,
  `songPicBig` VARCHAR(500) DEFAULT NULL,
  `songPicRadio` VARCHAR(500) DEFAULT NULL,
  `songLink` VARCHAR(500) DEFAULT NULL,
  `lrcLink` VARCHAR(500) DEFAULT NULL,
  `format` VARCHAR(100) DEFAULT NULL,
  `time` VARCHAR(100) DEFAULT NULL,
  `rate` VARCHAR(100) DEFAULT NULL,
  `size` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`songId`)
) ENGINE=INNODB DEFAULT CHARSET=utf8"""
# 本地数据库信息
sid = "localhost"
db_host = "127.0.0.1"
db_port = 3306
db_user = "root"
db_pass = "gloryroad"
db_db = "music"
db_charset = "utf8"

class MysqlManage(object):
    u"""Mysql数据库操作类"""
    def __init__(self):
        self.section = sid
        self.host = db_host
        self.port = db_port
        self.username = db_user
        self.password = db_pass
        self.db = db_db
        self.charset = db_charset
        self.conn = None
        self.cursor = None

    def connect(self):
        u"""连接数据库"""
        try:
            self.conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                user = self.username,
                passwd = self.password,
                db = self.db,
                charset = self.charset)
        except Exception, e:
            assert 1 == 2 , u"连接数据库：" + self.db + "失败：" + str(e)

    def get_cursor(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def execute_sql(self, sql, **args):
        u"""执行sql语句"""
        try:
            self.cursor.execute(sql, args)
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def executemany_sql(self, sql, datas):
        u"""执行sql语句"""
        try:
            self.cursor.executemany(sql, datas)
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content(self):
        u"""获取查询结果"""
        try:
            res = self.cursor.fetchone()
            return res
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content_all(self):
        u"""获取所有查询结果"""
        try:
            resSet = self.cursor.fetchall()
            return resSet
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content_by_line(self, lines):
        u"""获取指定条数的数据"""
        try:
            resTuple = self.cursor.fetchmany(lines)
            return resTuple
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            self.close()

    def commit(self):
        u"""提交事务"""
        try:
            self.conn.commit()
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def close(self):
        u"""断开连接"""
        try:
            if None == self.cursor:
                pass
            else:
                self.cursor.close()
                self.conn.close()
        except MySQLdb.Error, e:
            raise Exception(u"断开连接失败：" + str(e))

def get_music_list(channel_id):
    music_list = requests.get(music_list_url + channel_id).json()['list']
    return music_list

def get_music_info(music_id):
    try:
        content = requests.get(music_url + music_id).json()
        return content['data']['songList'][0]
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

def get_channel_list():
    channel_list = requests.get(channel_list_url).json()['channel_list']
    return channel_list

if __name__ == "__main__":
    music_dir = "music"
    lrc_dir = "lrc"
    music_info_file = "music_info.txt"
    if not os.path.exists(music_dir):
        os.mkdir(music_dir)
    if not os.path.exists(lrc_dir):
        os.mkdir(lrc_dir)
    lyrics = ''
    all_music_info = []
    count = 1
    mm = MysqlManage()
    mm.connect()
    mm.get_cursor()
    mm.execute_sql("desc music_info;")
    keys = [x[0] for x in mm.get_content_all()]
    mm.get_cursor()
    mm.execute_sql("SELECT songId FROM music_info;")
    all_music_info = [x[0] for x in mm.get_content_all()]
    channel_list = ['']
    # channel_list = get_channel_list()
    channels_id = []
    for channel in channel_list:
        num = 1
        while num <= 100:
            print num
            content = []
            try:
                for m in get_music_list(channel['channel_id'] if channel else ''):
                    try:
                        if str(m['id']) not in all_music_info:
                            music_info = get_music_info(str(m['id']))
                            if music_info:
                                all_music_info.append(str(m['id']))
                                content.append(tuple([music_info[key] if music_info.has_key(key) and music_info[key] else "" for key in keys]))
                                print count,
                                try:
                                    print music_info['songName'] + '_' + music_info['artistName']
                                except:
                                    pass
                                count += 1
                    except:
                        print traceback.format_exc()
                        continue
            except:
                print traceback.format_exc()
                continue
            if len(content):
                num = 1
                s = ','.join(['%s'] * len(keys))
                mm.get_cursor()
                mm.executemany_sql("insert into music_info values(" + s + ")", content)
                mm.commit()
            else:
                num += 1
    mm.close()
