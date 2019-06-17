types_of_people = 10 #设置人员类型数量
x = f"There are {types_of_people} types of people." #x为一个新的变量，在该变量中嵌入types_of_people

binary="binary" #设置binary变量
do_not = "don't" #设置do_not变量
y = f"Those who know {binary} and those who {do_not}." #y设置方式同x

print(x)#打印x
print(y)#打印y

print(f"I said:{x}")#打印 我说+x的内容
print(f"I also said:'{y}'")#打印 我也说+y的内容

hilarious = "False"#设置是否幽默？？？？？
joke_evaluation = "Isn't that joke so funnuy?! {}"#笑话评估？

print(joke_evaluation.format(hilarious))#打印上面的评估内容，同时内部嵌入hilarious
#print(f"{joke_evaluation}+{hilarious}")#测试直接f的方式格式化，但是这时候joke_evaluation后面的{}会打印出来
w = "This is the left side of ..."#简单定义变量
e = "a string with a right side."#简单定义变量+1

print(w + e)#简单变量拼接，实际为字符串拼接
