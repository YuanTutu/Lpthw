#from sys import argv

#script,filename = argv
#filename = argv#测试只有一个参数测试失败
#txt = open(filename)
filename = input("please input the file name:\n")
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
