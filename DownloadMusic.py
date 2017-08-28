#encoding=utf-8
import traceback

import requests
import urllib
import os,sys
reload(sys)
sys.setdefaultencoding("utf8")

channel_list_url = "http://fm.baidu.com/dev/api/?tn=channellist"
music_list_url = "http://fm.baidu.com/dev/api/?tn=playlist&format=json&id="
music_url = "http://music.baidu.com/data/music/fmlink?type=mp3&rate=320&songIds="

def get_channel_list():
    channel_list = requests.get(channel_list_url).json()['channel_list']
    return channel_list

def get_music_list(channel_id):
    music_list = requests.get(music_list_url + channel_id).json()['list']
    return music_list

def get_music_info(music_id):
    music_info = requests.get(music_url + music_id).json()['data']['songList'][0]
    return music_info

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
if __name__ == "__main__":
    # get_channel_list()
    # print requests.get(category_url+"public_tuijian_rege").json()
    # link = requests.get(music_url+"277161").json()['data']['songList'][0]['songLink']
    # pygame.mixer.Sound(link).play()
    try:
        dir_ = raw_input("请输入下载目录：".decode('utf8').encode('gbk'))
        if not os.path.exists(dir_):
            print u"新建目录", dir_
            os.makedirs(dir_)
    except:
        print u"输入内容有误"
        os.system("pause")
        raise
    channel_list = get_channel_list()
    channel_names = []
    channel_dict = {}
    for channel in channel_list:
        channel_name = channel['channel_name']
        # print isinstance(channel_name,str)
        channel_id = channel['channel_id']
        channel_names.append(channel_name)
        channel_dict[channel_name] = channel_id
    print u"***************************************************"
    print u"* 1、输入all，下载所有类别的歌曲"
    print u"* 2、输入类别名称，下载指定类别的歌曲"
    print u"* 3、输入q，退出程序"
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
            name = raw_input("请输入：".decode('utf8').encode('gbk'))
            name_list = []
            if name == 'all':
                print u"下载所有歌曲"
                name_list = channel_names
            elif name == 'q':
                break
            elif name.decode("gbk") in channel_names:
                name_list.append(name.decode("gbk"))
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

