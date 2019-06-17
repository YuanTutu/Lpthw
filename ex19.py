def cheese_and_crackers(cheese_count,boxes_of_crackers):#定义函数，起个名字，两个参数
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")#全部是打印，最后有个换行
#虽然函数是一开始定义的但是并不是一开始就打印，而是下面调用时候才会用到。

print("We can just give the function numbers directly:")#打印
cheese_and_crackers(20,30)#将20 30分别传入函数的两个参数中去


print("OR,we can use variables from our script:")#打印
amount_of_cheese = 10#定义变量
amount_of_crackers = 50#定义变量


cheese_and_crackers(amount_of_cheese,amount_of_crackers)#用变量传参达到和第九行同样的作用


print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)#传参时候进行数学计算

print("And we can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)#变量+数学计算的方式传递参数给函数
