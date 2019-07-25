import ctypes
import random

music_list = ["白狐"
    "笨小孩",
    "此生不换",
    "单身情歌",
    "火苗",
    "看透爱情看透你",
    "看月亮爬上来",
    "来生缘",
    "郎的诱惑",
    "天空之城",
    "我和草原有个约定",
    "真的爱你",
    "醉美天下"
]

music_name = random.choice(music_list)

print("正在播放 %s" % music_name)

ctypes.windll.winmm.mciSendStringW(r"open C:\Users\dengjun\Music\Music\%s.mp3 alias s" % music_name, None, 0, None)
ctypes.windll.winmm.mciSendStringW(r"play s repeat", None, 0, None)

input("\n按回车键退出......")