#encoding=utf-8
import traceback

import MySQLdb
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
music_info_file = "music_info.txt"

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

    def execute_sql(self, sql):
        u"""执行sql语句"""
        try:
            self.cursor.execute(sql)
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

def get_channel_list():
    channel_list = requests.get(channel_list_url).json()['channel_list']
    return channel_list

def get_music_list(channel_id):
    music_list = requests.get(music_list_url + channel_id).json()['list']
    return music_list

def get_music_info(music_id):
    global count
    try:
        content = requests.get(music_url + music_id, timeout = 10).json()
        music_info = content['data']['songList'][0]
        print music_info['songName']
        use_info = music_info
        # for i in ['songName', 'artistName', 'format', 'songLink', 'lrcLink', 'time']:
        #     use_info[i] = music_info[i]
        count += 1
        return use_info
    except:
        return None

def download_music(music_info, path):
    music_name = music_info['songName']
    author_name = music_info['artistName']
    format_name = music_info['format']
    music_link = music_info['songLink']
    lrc_link = music_info['lrcLink']
    file_name = os.path.join(path,music_name.strip()+"_"+author_name+"."+format_name)
    lrc_name = os.path.join(path,music_name.strip()+"_"+author_name+".lrc")
    if not os.path.exists(file_name):
        urllib.urlretrieve(music_link, file_name)
        urllib.urlretrieve(lrc_link, lrc_name)
    if os.path.exists(file_name):
        return True
    return False
if __name__ == "__main__":
    # get_channel_list()
    # print requests.get(category_url+"public_tuijian_rege").json()
    # link = requests.get(music_url+"277161").json()['data']['songList'][0]['songLink']
    # pygame.mixer.Sound(link).play()
    channel_list = get_channel_list()
    channel_names = []
    channel_dict = {}
    all_music_info = {}
    for channel in channel_list:
        channel_name = channel['channel_name']
        # print isinstance(channel_name,str)
        channel_id = channel['channel_id']
        channel_names.append(channel_name)
        channel_dict[channel_name] = channel_id
    dir_ = raw_input("请输入下载目录：".decode('utf8').encode('gbk')).decode("gbk")
    if not os.path.exists(dir_):
        print u"目录不存在"
        os.system("pause")
        raise
    print u"***************************************************"
    print u"* 1、输入“all”，下载所有类别的歌曲"
    print u"* 2、输入“类别名称”，下载指定类别的歌曲"
    print u"* 3、输入“s”，搜索指定歌曲下载"
    print u"* 4、输入“q”，退出程序"
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
    while True:
        try:
            name = raw_input("请输入(输入“q”退出)：".decode('utf8').encode('gbk')).decode("gbk")
            name_list = []
            if name == 'all':
                print u"下载所有歌曲"
                name_list = channel_names
            elif name == 'q':
                break
            elif name in channel_names:
                name_list.append(name)
            elif name == 's':
                mm = MysqlManage()
                while True:
                    music_name = raw_input("请输入歌曲名称(输入“q”返回上一级)：".decode('utf8').encode('gbk')).decode("gbk").encode('utf8')
                    if music_name == 'q':
                        break
                    mm.connect()
                    mm.get_cursor()
                    mm.execute_sql("select songId, songName, artistName, albumName, songLink, lrcLink, format from music_info where songName like '%" + music_name + "%' or artistName like '%" + music_name + "%' or albumName like '%" + music_name + "%';")
                    search_result = mm.get_content_all()
                    mm.close()
                    if search_result:
                        print u"搜索结果（搜索到的歌曲）："
                        for i in ["songId", "songName", "artistName", "albumName"]:
                            print str(i).ljust(15, ' '),
                        print
                        for search in search_result:
                            for i in search[:-3]:
                                try:
                                    print i[:10].ljust(15, ' '),
                                except:
                                    pass
                            print
                        print
                        while True:
                            song_id = raw_input("请输入要下载的歌曲id(输入“q”返回上一级)：".decode('utf8').encode('gbk')).strip()
                            if song_id == 'q':
                                break
                            for search in search_result:
                                if song_id == search[0]:
                                    print u"下载中..."
                                    if download_music({'songName': search[1], 'artistName':search[2], 'format': search[6], 'songLink': search[4], 'lrcLink': search[5]},dir_):
                                        print u"下载完成。"
                                    else:
                                        print u"无法下载。"
                                    break
                            else:
                                print u"输入有误请重新输入。"
                    else:
                        print u"未搜索到结果。"

                continue
            else:
                print u"输入有误，请重新输入："
                continue
            # print name
            # print name_list
            for name in name_list:
                print u"下载【" + name + "】类别的所有歌曲"
                music_list = get_music_list(channel_dict[name])
                print u"共"+str(len(music_list))+"首歌"
                is_download = raw_input("是否下载（y/n）：".decode('utf8').encode('gbk'))
                if is_download.lower().strip() == 'y':
                    pass
                else:
                    continue
                path = os.path.join(dir_, name)
                # print path
                if not os.path.exists(path):
                    os.mkdir(path)
                print u"下载中..."
                for music in music_list:
                    try:
                        music_info = get_music_info(str(music['id']))
                        download_music(music_info, path)
                    except:
                        continue
                print u"下载完成。"
        except:
            print u"输入有误，请重新输入："
            print traceback.format_exc()
    print u"退出程序。"
    os.system("pause")

