from sys import argv
# read the WYSS sextion for how to run this
#源代码
script,first,second,third = argv
#修改测试 下述均为错误
#script,first=input(),second=input(),third=input() = argv

#script = input("input script:\n")
#first = input("input first:\n")
#second = input("input second:\n")
#third = input("input third:\n")

#print("The script is called:"script)


print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
#错误理解题意，实际是input和argv无法同时用？暂时没有确定但是不知道如何写在一起
print("Your height is:")
height = input()
print("Your weight is:")
weight = input()
animal = input("What is your first variable?")
print(f"So your first variable is {animal}.")
