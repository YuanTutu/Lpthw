from sys import argv

script, input_file = argv#解包，传参

def print_all(f):#定义函数
    print(f.read())#f执行read（），读取文件并进行打印

def rewind(f):#定义函数重置指针到文件开头
    f.seek(0)#f执行seek函数，读写位置移动到文件开头

def print_a_line(line_count,f):#定义函数，给参数命名
    print(line_count,f.readline(),end="")#f执行readline只读取一行文本然后和line_count一起打印
#end=""能够取消一个空行
current_file = open(input_file)#open开变量input然后赋值给current_file

print("First let's print the whole file:\n")#第一行输出

print_all(current_file)#调用函数print_all打印输出，参数为current_file

print("Now let's rewind,kind of like a tape.")#第二行输出

rewind(current_file)

print("Let's print three lines:")#最后输出

current_line = 1#整数1赋值给变量current_line
print_a_line(current_line,current_file)
#变更行号，打印第二行，打印第一行之后指针在第二行开头
current_line += 1#current_file+1赋值给变量current_line
print_a_line(current_line,current_file)

current_line += 1#current_file+1赋值给变量current_line
print_a_line(current_line,current_file)
