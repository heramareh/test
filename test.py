#encoding=utf-8

import requests

content = requests.get("http://yinyueshiting.baidu.com/data2/music/e26fda35fa09c06340a237859a76443e/542059395/277161118800128.mp3?xcode=2880a1f4ff562bb7f4316fffb8ff8771")
print content.json()
