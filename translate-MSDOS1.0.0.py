# -*- coding:utf-8 -*-
import requests
import pyperclip #剪贴板操作
import os
# 注意：pyttsx3一定要是2.72版本，高于2.72版本一定会出错！
import pyttsx3 # 语音输出 
import webbrowser # 打开浏览器
from colorama import init,Fore # 更改警示颜色
init(autoreset=True) # 更改该句颜色后自动变成白色
# speaking_open:判断用户是否打开了语音输出功能
speaking_open=False

# 判断settings.txt是否存在
def setting_if_exist():
    filename="transsettings.txt"
    if not os.path.exists(filename):
        return False
    else :
        return True

# 输出 MIT LICENSE
def mitlicense():
    print(Fore.BLUE+'''
Copyright (C) 2021-2022  BillMa
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
''')
# 导入transsettings.txt中用户保存的speaking_open数据，并在transsettings.txt没有数据的时候进行数据初始化
def writingdata():
    global speaking_open
    if setting_if_exist():
        with open("transsettings.txt","r",encoding="utf-8") as settings_read:
            s=settings_read.read()
            settings_read.close()
        if s=="SPEAKING=TRUE":
            speaking_open=True
            return
        elif s=="SPEAKING=FALSE":
            speaking_open=False
            return
        else :
            with open("transsettings.txt","w",encoding="utf-8") as settings:
                speaking_open=False
                settings.write("SPEAKING=FALSE")
                settings.close()
    else:
        with open("transsettings.txt","w",encoding="utf-8") as settings:
                settings.write("SPEAKING=FALSE")
                speaking_open=False
                settings.close()
                return
# 在用户输入-c即主动要求修改语音输出配置时进行修改
def changedata():
        global speaking_open
        with open("transsettings.txt","w",encoding="utf-8") as settings:
            if speaking_open==False:
                settings.write("SPEAKING=TRUE")
                speaking_open=True
                settings.close()
                print(Fore.RED+"语音播报已开启/Voice broadcast is turned on")
                return
            else :
                settings.write("SPEAKING=FALSE")
                speaking_open=False
                settings.close()
                print(Fore.RED+"语音播报已关闭/Voice broadcast is turned off")
                return
# 输出作者联系方式
def contactau():
    print(Fore.BLUE+"""
QQ:36937975
Email: maboning237103015@163.com
GitHub/Gitee: billma007
Website:https://billma.top
""")

# 开始欢迎界面和如何使用
def help_about_CHINESE():
    print(Fore.BLUE+'''欢迎使用马哥中英文翻译机(1.0.0交互式界面版本）！
本软件由 BillMa编写，BillMa版权所有，本项目未经允许禁止商用
本项目已经开源，开源地址：https://github.com/billma007/pythontranslator 或者在下面输入\"-git\"到达
本项目使用MIT LICENSE协议，使用该项目的任何部分时请遵守该协议。输入\"-mit\"查看该协议完整内容。
该版本为内测版本，请及时更新，最新release版本会及时发布在GiHub上
----------------------------------------------------------------------------------------------''')
    print(Fore.GREEN+'''输入参数：
1.正常输入则会得到正常翻译
2. -c:更改语音设置（开启/关闭语音播报，默认关闭）
3. -git:查看项目地址
4. -mit 查看 MIT LICENSE相关内容
5. -contact 联系作者
6. -official 前往官方网站(网站暂未完全开发，暂时无法访问）
7. -help 或者 -about 本程序的帮助和关于界面
8, -cls:清除当前页面
9. -paste (或者按下鼠标右键)将现在你剪贴板的内容粘贴至终端
0. 同时按下Crrl+C结束程序。
a. -m :多行输入
可以开始愉快的翻译了！
''')
def help_about_ENGLISH():
    print(Fore.BLUE+"""Welcome to Chinese-English translator (interactive interface version)!
This software is written by billma, and the copyright of billma is reserved. The commercial use of this project is prohibited without permission
The project has been open source. Open source address: https://github.com/billma007/pythontranslator Or enter "-git" below to arrive
This project uses MIT license agreement. Please abide by this agreement when using any part of the project. Enter "-mit" to view the full content of the agreement.
This version is an internal test version. Please update it in time. The latest release version will be released on gihub in time.
----------------------------------------------------------------------------------------------""")
    print(Fore.GREEN+"""Input parameters:
1. Normal input will get normal translation
2. -c: change voice settings
3. -git: view project address
4. -mit :view MIT license related content
5. -contact :contact the author
6. -official :go to the official website (the website is not fully developed and cannot be accessed temporarily)
7. -help or -about the help and about interface of this program
8, -cls: clear current page
0. Press crrl + C at the same time to end the program.
You can start a happy translation!""")
if __name__ =="__main__":
    writingdata()
    help_about_CHINESE()
    help_about_ENGLISH()
    while True:
        print(Fore.CYAN+"\n请输入一段要翻译的文字：/Please enter what you want to translate:")
        string = str(input())
        if string == "":
            print(Fore.RED+"请输入文字/Please enter something...")
        elif (string[0]=='-' and ("-paste" not in string) and ("-m" not in string))==True:
            if string=="-c":
                changedata()
            elif string=="-git":
                webbrowser.open_new('https://github.com/billma007/pythontranslator')
            elif string=="-mit":
                mitlicense()
            elif string=="-contact":
                contactau()
            elif string=="-official":
                webbrowser.open_new('https://billma.top')
            elif string=="-help" or string=="-about":
                help_about_ENGLISH()
                help_about_CHINESE()
            elif string=="-cls":
                os.system("cls")
            else:
                print(Fore.RED+"Error:入参错误/Entry error.")
        else:
            if "-paste" in string:
                if pyperclip.paste()=="":
                    print(Fore.RED+"剪切板为空...")
                    continue
                string=pyperclip.paste()
            if "-m" in string:
                print(Fore.YELLOW+"请输入多行字符，输入-qqq结束")
                string = ""
                while "-qqq" not in string :
                    string_through=input()
                    if "-qqq" not in string:
                        string+=(string_through+'\n')
            data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i':string
            }
            url = "http://fanyi.youdao.com/translate"
            r = requests.get(url,params=data)
            result = r.json()
            translate_result = result['translateResult'][0][0]["tgt"]
            pyperclip.copy(translate_result)# 复制到剪贴板
            print(Fore.BLUE+"结果/RESULT:")
            print(Fore.YELLOW+translate_result)
            print(Fore.BLUE+"结果已经复制到剪贴板/Result has been copied!")
            if speaking_open==True:
                    pt = pyttsx3.init()
                    pt.say(translate_result)
                    pt.runAndWait()