from sys import argv#从sys库里导入argv模块

script,filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that,hit CTRL-C(^C).")
print("If you do want that,hit RETURN.")

input("?")#其实只是一个没有意义的输入用于开始下面的的运行

print("Opening the file...")
target = open(filename,'w')#open函数，写入模式

print("Truncating the file.Goodeye!")
target.truncate()#清空打开的文件

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")#输入内容，共三行，定义三个变量直接输入
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#下属三行需要进行替换，使用一个target.write()
"""
target.write(line1)#写入操作开始，将三个变量写入文件
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
#下面一行在\\n转义字符位置有问题
#target.write(f"{line1}\\n{line2}\\n{line3}")
#下面的是自己写的

#target.write(f"""{line1}
#{line2}
#{line3}
#""")

#下面一行是知乎大神写的
target.write(line1+'\n'+line2+'\n'+line3+'\n')
print("And finally,we close it.")
target.close()#关闭变量文件
