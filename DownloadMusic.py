#encoding=utf-8
import traceback
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
def get_channel_list():
    channel_list = requests.get(channel_list_url).json()['channel_list']
    return channel_list

def get_music_list(channel_id):
    music_list = requests.get(music_list_url + channel_id).json()['list']
    return music_list

def get_music_info(music_id):
    global count
    try:
        content = requests.get(music_url + music_id, timeout = 1).json()
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
    dir_ = raw_input("请输入下载目录：".decode('utf8').encode('gbk'))
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
            name = raw_input("请输入：".decode('utf8').encode('gbk')).decode("gbk")
            name_list = []
            if name == 'all':
                print u"下载所有歌曲"
                name_list = channel_names
            elif name == 'q':
                break
            elif name in channel_names:
                name_list.append(name)
            elif name == 's':
                print u"数据加载中，请稍等..."
                start_time = time.time()
                if not os.path.exists(music_info_file):
                    with open(music_info_file, 'w') as fp:
                        print len(channel_names)
                        for channel_name in channel_names:
                            music_list = get_music_list(channel_dict[channel_name])
                            print len(music_list)
                            for music in music_list:
                                music_info = get_music_info(str(music['id']))
                                if music_info and not all_music_info.has_key(music_info['songName']+'_'+music_info['artistName']):
                                    all_music_info[music_info['songName']+'_'+music_info['artistName']] = music_info
                                    fp.write(music_info['songName']+'_'+music_info['artistName']+'||'+str(music_info)+'\n')
                        # with open(music_info_file, 'w') as fp:
                        #     fp.writelines([k+'||'+v+'\n' for k,v in all_music_info.items()])
                        print time.time() - start_time
                        print count
                with open(music_info_file) as fp:
                    contents = fp.readlines()
                for content in contents:
                    k,v = content.strip().split("||")
                    all_music_info[k] = eval(v)
                while True:
                    music_name = raw_input("请输入歌曲名称(输入“q”返回上一级)：".decode('utf8').encode('gbk')).decode("gbk")
                    if music_name == 'q':
                        break
                    search_result = []
                    for music_info in all_music_info.keys():
                        if music_name in music_info:
                            search_result.append(music_info)
                    for search in search_result:
                        print u"搜索结果（搜索到的歌曲）："
                        print search['songName'],
                    print
                    print
                    while True:
                        song_name = raw_input("请输入要下载的歌曲名称(输入“q”返回上一级)：".decode('utf8').encode('gbk')).decode("gbk")
                        if song_name == 'q':
                            break
                        for search in search_result:
                            if song_name == search['songName']:
                                print u"下载中..."
                                if download_music(search,dir_):
                                    print u"下载完成。"
                                else:
                                    print u"无法下载。"
                                break
                        else:
                            print u"输入有误请重新输入。"

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

