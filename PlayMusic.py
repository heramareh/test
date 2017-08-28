#encoding=utf-8
import mp3play, os, sys, random, time, eyed3

PlayingMusic = ''
music = ''
seconds = 0

def get_all_musics(path):
    music_list = []
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith(".mp3") or file.endswith(".wma"):
                music_list.append(os.path.join(root, file))
    return music_list

def playMusic(music_name):
    global PlayingMusic, music, seconds
    try:
        if music_name != PlayingMusic:
            music = mp3play.load(music_name)
            music.volume(10)
            seconds = eyed3.load(music_name).info.time_secs
            if seconds > music.seconds():
                seconds = music.seconds()
            print "正在播放：".decode().encode('gbk') + os.path.split(music_name)[1] + "  " + str(seconds / 60).zfill(2) + ":" + str(seconds % 60).zfill(2)
        music.play()
        time.sleep(seconds)
        music.stop()
    except KeyboardInterrupt:
        print "退出".decode().encode('gbk')
        raise
    except:
        print "不支持的文件格式".decode().encode('gbk')
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
        print "目录/文件不存在".decode().encode('gbk')

if __name__ == "__main__":
    random_all(sys.argv[1])
