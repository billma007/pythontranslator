# pythontranslator

## 如何使用/How to use

```cmd
git clone https://github.com/billma007/pythontranslator.git
cd pythontranslator
pip install -r requirements.txt
py translate-MSDOS1.0.0.py
```

**注意：pyttsx3一定要是2.71版本的，否则在输出中文时会报错!**

## 原理/principle

### 1.朗读设置

使用`transsettings.txt`来保存用户对朗读的偏好设置

```py
# speaking_open:判断用户是否打开了语音输出功能
speaking_open=False
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
def changedata():
        global speaking_open
        with open("transsettings.txt","w",encoding="utf-8") as settings:
            if speaking_open==False:
                settings.write("SPEAKING=TRUE")
                speaking_open=True
                settings.close()
                return
            else :
                settings.write("SPEAKING=FALSE")
                speaking_open=False
                settings.close()
                return
```

但是这样会出现一个问题，就是目录下没有transsettings.txt时，open()函数在r模式中会报错。所以，需要一个容错机制。

如果使用`try...except`，还是无法创建。所以需要一个函数来专门创建并写入设置。

```py
def setting_if_exist():
    filename="transsettings.txt"
    if not os.path.exists(filename):
        return False
    else :
        return True
```

### 2.多行输入

```py
string = ""
while "-qqq" not in string :
    string_through=input()
    if "-qqq" not in string:
        string+=(string_through+'\n')
```

太啰嗦了，简洁一点

```py
string = ""
while True :
    string_through=input()
    if "-qqq" in string:
        break
    else:
        string+=(string_through+'\n')
```

~~还是很啰嗦~~清爽了不少。

### 3.剪贴板操作

剪贴板操作使用`pyperclip`进行支撑。

```py
pyperclip.copy(translate_result) #将结果复制到剪贴板
string=pyperclip.paste() #将剪贴板的内容拷贝到string中
```

看起来很简单，但是实际操作中发现pyperclip.paste()或者用户输入要是是空的会报错。

```py
if "-paste" in string:
    if pyperclip.paste()=="":
        print("剪切板为空...")
        continue
    string=pyperclip.paste()
if string == "":
    print("请输入文字")
```

### 4.控制台颜色变化

如果控制台里面一片白茫茫的输入输出，你是否会眼花？使用`colorama`第三方库，让控制台变得五颜六色。

```py
from colorama import init,Fore #导入模块
init(autoreset=True) # 更改某句颜色后，输出完该句，自动还原变成白色
...
print(Fore+COLOR+"str")
```

COLOR换成颜色的英文大写。

```py
print(Fore.BLUE+"结果/RESULT:")
print(Fore.YELLOW+translate_result)
print(Fore.BLUE+"结果已经复制到剪贴板/Result has been copied!")
```

### 5.朗读音频

朗读翻译结果使用第三方库pyttsx3来支持。但是注意，安装的pyttsx3版本一定要是2.72版本的。在requirements.txt里面已经指定了pyttsx3的版本，但如果你先前已经安装了更高版本的pyttsx3，请卸载并安装2.71版本的pyttsx3.

```cmd
~>pip uninstall pyttsx3
Found existing installation: pyttsx3 2.90
Uninstalling pyttsx3-2.90:
  Would remove:
    ~\python\python38\lib\site-packages\pyttsx3-2.90.dist-info\*
    ~\python\python38\lib\site-packages\pyttsx3\*
Proceed (Y/n)? Y
  Successfully uninstalled pyttsx3-2.90

~>pip install pyttsx3==2.71
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting pyttsx3==2.71
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/2f/ca/019a5d782f355bc2040ac45bd9612995652934dc16e48873d3fb2e367547/pyttsx3-2.71-py3-none-any.whl (39 kB)
Requirement already satisfied: pypiwin32 in ~\python\python38\lib\site-packages (from pyttsx3==2.71) (223)
Requirement already satisfied: pywin32>=223 in ~\python\python38\lib\site-packages (from pypiwin32->pyttsx3==2.71) (303)
Installing collected packages: pyttsx3
Successfully installed pyttsx3-2.71
```

pyttsx3需要调动三个函数：

```py
pt = pyttsx3.init() #初始化
pt.say(translate_result) #将要说的话添加到缓冲区（注:到这里还不能发出声音）
pt.runAndWait() #把话说出来
```

### 4.核心代码

核心代码使用大名鼎鼎的requests进行驱动。

```py
url = "http://fanyi.youdao.com/translate"
r = requests.get(url,params=data)
result = r.json()
translate_result = result['translateResult'][0][0]["tgt"]
```

## 更新日志/Update Log

- 2022/3/9 MS-DOS1.0.0版本发布，同时GUI1.0版本开始筹划并初步完成。
- 2022/3/4 Basic2.2完成 增加色彩功能
- 2022/3/1 顺利完成Basic2.0，增加了语音设置和剪贴板读取功能
- 2022/2/15 元宵节，突如其来的疫情让我们~~被迫~~上网课，便在空余时间开始开发语音输出功能(当天便写完了Basic1.1)
- 2022/2/8 农历大年初八，增加了语音输出的功能，但是要上学了，便没有提交代码
- 2022/1/31 农历春节，写完了MS-DOS1.0版本的前身Basic1.0
- 2022/1/21 开始放寒假，学习requests爬虫知识并开始筹划

## 版本关系

特别声明：MS-DOS和GUI版本是**平等**的！没有高下之分！~~就像Microsoft Visual Studio和Microsoft Visual Studio Code的关系一样~~

## 关于作者/About

江苏省苏州市的一个普通高中牲，一个~~因为玩电脑被学校处分~~在省赛就被刷下来的信息学奥林匹克竞赛选手，热爱编程，但不喜欢前端。

欢迎通过以下联系方式与我探讨信息竞赛、博客搭建、学术讨论以及扯皮：

- QQ:36937975
- Twitter:@billma6688
- Facebook/Instagram:billma007
- CodeForces/USACO/AtCoder:billma007(不常用/not use them usually)
- Email:maboning237103015@163.com

## 推广：个人博客/Blog

[欢迎来到我的博客/Welcome Here!](https://billma.top)

## LICENSE

[MIT LICENSE](LICENSE)
