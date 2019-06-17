from sys import argv#引用argv

script,filename = argv#确定argv有两个参数，第一个参数为脚本名称本身，第二个为手动输入的测试txt文件名

txt = open(filename)#定义变量txt，打开上面的文件名的对应文件并将打开后的内容赋值给txt变量

print(f"Here's your file {filename}:")#格式化filename字符串然后输出
print(txt.read())#使用read打开txt并进行打印

print("Type the filename again:")
file_again = input(">")
#开始重复上述过程
txt_again = open(file_again)

print(txt_again.read())
#巩固练习7，加close
txt.close()
txt_again.close()
