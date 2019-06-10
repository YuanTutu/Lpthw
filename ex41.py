import random #生成一个0-1的随机浮点数
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []#创建列表
#phrases短语
PHRASES = {#创建字典
    "class %%%(%%%):":#创建一个class类叫做%%%，继承自%%%
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":#__init__接收self和***为参数
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self,@@@)":#class里面有一个叫***的函数，接收self和@@@为参数
        "class %%% has-a function *** that takes self and @@@ params.",#function函数
    "*** = %%%()":#***设置为%%%（）的实例
        "Set *** to an instance of class %%%.",#instances实例
    "***.***(@@@)":#从***中找到***函数，并使用self和@@@参数调用他
        "From *** get the *** function,call it with params self,@@@.",
    "***.*** = '***' ":#从***找到***属性，将其设置为***
        "From *** get the *** attribute and set it to '***'."#attribute属性
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True#判断命令行参数是不是两个且第一个参数是english，再分别赋值
else:
    PHRASES_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))
#30行，先urlopen打开网址返回数据，再调用readlines，然后返回列表，所有元素带入变量word
#31行，在变量word上面strip移除每一行开始和结尾的空格返回新字符串，然后str转化成utf-8编码，之后WORDS上面append，把前面的str出来的结果添加到列表WORDS里面
def convert(snippet,phrases):#snippet片段。定义一个函数内部两个变量snippet和phrase
    class_names = [w.capitalize() for w in#创建列表class_names，在位置变量snippet上调用count()函数统计%%%出现的次数，返回值是整数
                random.sample(WORDS,snippet.count("%%%"))]#然后random.sample()，参数为WORDS和count返回的整数。从列表WORDS中随机获取指定长度的片段并随机排列返回列表，把列表内的所有元素带入变量w中。w上调用capitalize函数把字符串第一个字母变成大写，其他字母小写
    other_names = random.sample(WORDS,snippet.count("***"))#创建列表other_names,snippet调用count统计***出现次数再调用random.sample函数
    results = []#创建空列表results
    params_names = []#创建空列表param_names

    for i in range(0,snippet.count("@@@")):#在位置变量snippet上调用count统计@@@出现次数，调用range创建一个整数序列，把序列内的每一个元素带入变量中
        params_count = random.randint(1,3)#调用random.randint()生成一个1~3的整数，赋值给params_count
        params_names.append(', '.join(#调用random.sample函数参数为WORDS和上面一行的结果，从列表WORDS中随机获取指定长度的片段并随机排列,返回列表
            random.sample(WORDS,params_count)))#然后调用join()将列表中的元素用，连接生成新的字符串，再把结果append添加到param_names中

    for sentence in snippet,phrases:#变量snippet和phrases每一个元素代入到变量sentence中
        result = sentence[:]#把变量sentence的复制结果给变量result。[:]列表内的冒号前后可以添加参数a,b表示复制列表的开始与结束位置
#[:]列表切片
        #fake class names
        for word in class_names:#将列表class_names other_names params_names内部所有元素分别带入word中
            result = result.replace("%%%",word,1)#分别将旧的字符串%%%***@@@替换成新的字符串变量word
#替换不超过一次，再分别赋值给result。
        #fake other names
        for  word in other_names:
            result = result.replace("***",word,1)#str.replace(old,new[,max])

        #fake parameter lists
        for word in params_names:
            result = result.replace("@@@",word,1)

        results.append(result)#空列表result调用append把对象添加到results中，最后返回的是results，注意s，并不是同一个列表

    return results


#keep going until they hit CTRL-D
try:
    while True:#布尔值为真的时候
        snippets = list(PHRASES.keys())#字典PHRASES上面调用keys()，以列表形式返回所有的键,并赋值给变量snippets
        random.shuffle(snippets)#在边路snippets上random.shuffle()，将所有元素随机排列

        for snippet in snippets:#snippets每一个元素代入snippet中
            phrase = PHRASES[snippet]#取出字典PHRASES中对象snippet并将其赋值给phrase
            question,answer = convert(snippet,phrase)#调用convert()，位置参数是question和answer
            if PHRASES_FIRST:#如果PHRASES_FIRST是真
                question,answer =answer,question#就把question和answer调换位置

            print(question)#打印

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:#如果try部分引发EOFError异常就打印bye
    print("\nBye")

#所有的函数定义由此进行说明
#标注行数
#24-len(sys.argv)命令行参数个数，去掉len是命令行参数列表
#30-urlopen是urllib模块里面一个方法函数，通过网址url来获取数据.readlines读取所有行并返回列表，可以由for in处理的列表
#31-strip()移除字符串头尾指定的字符，默认是空格或者换行符，或者字符序列#str()函数将对象转化为适合人阅读的形式
#35-caoitalize将字符串中的第一个字母变成大写，其他字母小写
#36-random.sample()从指定的序列中随机获取指定长度的片段并随机排列
#37-count函数用于统计字符串里面某个字符出现的次数，可选参数为在字符串搜索的开始与结束为止。返回结果是子字符串出现的次数
#42-random.randint用于生成一个指定范围内的证书，第一个参数是下限，第二个参数是上限
#43-join()函数用于将序列中的元素以指定的字符连接生成一个新的字符串。返回通过指定字符连接序列中元素生成后的新字符串
#51-replace()函数把字符串中的old替换成new，如果指定第三个参数max则替换不超过max次。返回是替换完成的新字符串
#67-try...except...语法检测try语句块中的错误，从而让except语句捕获异常信息并进行处理。如果不想在异常发生结束时结束程序，只需要在try里面捕获它
#69-key()返回一个字典的所有键
#70-shuffle()将序列的所有元素随机排序。这个函数不能直接访问，需要导入random模块，然后通过random静态对象调用该方法
