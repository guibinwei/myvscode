import pyttsx3
# 创建对象
engine = pyttsx3.init()
# 获取当前语音速率
rate = engine.getProperty('rate')
print(f'语音速率：{rate}')
# 设置新的语音速率
engine.setProperty('rate', 140)
# 获取当前语音音量
volume = engine.getProperty('volume')
print(f'语音音量：{volume}')
# 设置新的语音音量，音量最小为 0，最大为 1
engine.setProperty('volume', 1.0)
# 获取当前语音声音的详细信息
voices = engine.getProperty('voices')
print(f'语音声音详细信息：{voices}')
# 设置当前语音声音为女性，当前声音不能读中文
engine.setProperty('voice', voices[1].id)
# 设置当前语音声音为男性，当前声音可以读中文
#这个似乎是女的声音
engine.setProperty('voice', voices[0].id)
# 获取当前语音声音
voice = engine.getProperty('voice')
print(f'语音声音：{voice}')
# 语音文本
path = 'test.txt'  #或者直接导入一个文本文件
words = """行路难，行路难，多歧路，今安在？
长风破浪会有时，直挂云帆济沧海。"""
# 将语音文本说出来
engine.say(words)
engine.runAndWait()
engine.stop()